# src/fraud_model.py

import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
from src import config

def encode_categorical(df, categorical_cols):
    """Label encode categorical columns and append to features list"""
    features = []
    for col in categorical_cols:
        if df[col].dtype.name == 'category':
            df[col] = df[col].astype(str)
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        features.append(col)
    return df, features

def train_model():
    """Train Isolation Forest model and save it"""
    df = pd.read_csv(config.FINAL_DATASET)

    # Base numeric features
    features = [
        'Amount (INR)', 'hour', 'day_of_week', 'is_weekend', 'is_large_amount',
        'same_bank_transfer', 'time_gap_seconds', 'receiver_repeat_count', 'avg_txn_amt_sender'
    ]

    # Categorical columns to encode
    categorical = ['sender_bank', 'receiver_bank', 'time_of_day']
    df, encoded = encode_categorical(df, categorical)
    features += encoded

    # Train Isolation Forest
    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    model.fit(df[features])

    # Save model
    joblib.dump(model, config.MODEL_FILE)
    print("✅ Model trained and saved at:", config.MODEL_FILE)

def load_model():
    """Load trained model from disk"""
    return joblib.load(config.MODEL_FILE)

# ✅ Run the trainer if executed as a script/module
if __name__ == "__main__":
    train_model()
