# src/detector.py

import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from src import config

def encode_categorical(df, categorical_cols):
    """Label encode categorical columns"""
    for col in categorical_cols:
        df[col] = df[col].astype(str)
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
    return df

def detect_fraud():
    """Load final dataset and model, predict frauds, and export report"""
    print("🚨 Loading data and model...")
    
    df = pd.read_csv(config.FINAL_DATASET)
    model = joblib.load(config.MODEL_FILE)

    # Ensure categorical columns are encoded
    categorical = ['sender_bank', 'receiver_bank', 'time_of_day']
    df = encode_categorical(df, categorical)

    features = [
        'Amount (INR)', 'hour', 'day_of_week', 'is_weekend', 'is_large_amount',
        'same_bank_transfer', 'time_gap_seconds', 'receiver_repeat_count', 'avg_txn_amt_sender',
        'sender_bank', 'receiver_bank', 'time_of_day'
    ]

    # Predict
    df['is_fraud'] = model.predict(df[features])
    df['is_fraud'] = df['is_fraud'].map({1: 0, -1: 1})  # 1 = fraud, 0 = normal

    # Save fraud report
    fraud_df = df[df['is_fraud'] == 1]
    fraud_df.to_csv(config.FRAUD_REPORT, index=False)

    print(f"✅ Detected {len(fraud_df)} suspicious transactions.")
    print(f"📝 Saved to: {config.FRAUD_REPORT}")


if __name__ == "__main__":
    detect_fraud()
