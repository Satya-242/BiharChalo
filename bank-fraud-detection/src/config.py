# src/config.py

# ✅ Hardcoded base directory (your system)
BASE_DIR = r"C:\Users\sinha\OneDrive\Documents\Projects\Bihar Hackathon\bank-fraud-detection"

# 📂 Directory Paths
RAW_DATA_DIR = fr"{BASE_DIR}\data\raw"
PROCESSED_DATA_DIR = fr"{BASE_DIR}\data\processed"
MODELS_DIR = fr"{BASE_DIR}\models"
REPORTS_DIR = fr"{BASE_DIR}\reports"

# 📄 Raw Data Files
TRANSACTIONS_FILE = fr"{RAW_DATA_DIR}\transactions.csv"
BANK_STATEMENTS_FILE = fr"{RAW_DATA_DIR}\bank_statements.csv"
MY_TRANSACTIONS_FILE = fr"{RAW_DATA_DIR}\MyTransaction.csv"

# 📄 Processed Data Files
CLEANED_TRANSACTIONS = fr"{PROCESSED_DATA_DIR}\cleaned_transactions.csv"
CLEANED_BANK_STATEMENTS = fr"{PROCESSED_DATA_DIR}\cleaned_bank_statements.csv"
CLEANED_PERSONAL_TXNS = fr"{PROCESSED_DATA_DIR}\cleaned_personal_txns.csv"
FINAL_DATASET = fr"{PROCESSED_DATA_DIR}\final_dataset.csv"

# 📄 Output Files
FRAUD_REPORT = fr"{REPORTS_DIR}\fraud_report.csv"
MODEL_FILE = fr"{MODELS_DIR}\fraud_model.pkl"
