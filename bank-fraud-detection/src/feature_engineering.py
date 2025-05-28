# src/feature_engineering.py

import pandas as pd
import numpy as np

def add_features(df):
    """
    Add engineered features to cleaned transactions dataframe.
    Returns a new DataFrame with additional columns.
    """

    # 🕒 Time-based features
    df['hour'] = df['Timestamp'].dt.hour
    df['day_of_week'] = df['Timestamp'].dt.dayofweek
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
    df['time_of_day'] = pd.cut(
        df['hour'],
        bins=[0, 6, 12, 18, 24],
        labels=['Night', 'Morning', 'Afternoon', 'Evening'],
        right=False
    )

    # 💸 Transaction-based features
    df['is_large_amount'] = (df['Amount (INR)'] > 10000).astype(int)
    df['same_bank_transfer'] = (df['sender_bank'] == df['receiver_bank']).astype(int)

    # ⏱️ Time gap with previous transaction (sender-wise)
    df.sort_values(['Sender UPI ID', 'Timestamp'], inplace=True)
    df['prev_txn_time'] = df.groupby('Sender UPI ID')['Timestamp'].shift(1)
    df['time_gap_seconds'] = (df['Timestamp'] - df['prev_txn_time']).dt.total_seconds()
    df['time_gap_seconds'] = df['time_gap_seconds'].fillna(999999)

    # 🔁 Receiver repeat count
    df['receiver_repeat_count'] = df.groupby(['Sender UPI ID', 'Receiver UPI ID']).cumcount()

    # 📊 Sender's rolling average transaction amount (last 5 transactions)
    df['avg_txn_amt_sender'] = (
        df.groupby('Sender UPI ID')['Amount (INR)']
        .rolling(window=5, min_periods=1)
        .mean()
        .reset_index(level=0, drop=True)
    )

    # 🧼 Handle missing values
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)

    df['time_of_day'] = df['time_of_day'].cat.add_categories(['Unknown']).fillna('Unknown')

    return df
