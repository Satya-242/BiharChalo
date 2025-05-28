# src/preprocessing.py

import pandas as pd
import numpy as np
import os

def clean_transactions(file_path):
    """Clean transactions.csv file (UPI transfers)"""
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    
    # Clean and convert data types
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
    df['Amount (INR)'] = pd.to_numeric(df['Amount (INR)'], errors='coerce')

    # Drop invalid rows
    df = df.dropna(subset=['Transaction ID', 'Sender UPI ID', 'Receiver UPI ID', 'Amount (INR)'])

    # Assign mock banks
    banks = ['example_hdfc', 'example_sbi', 'example_axis', 'example_icic_bank']
    df['sender_bank'] = np.random.choice(banks, size=len(df))
    df['receiver_bank'] = df['sender_bank'].apply(lambda x: np.random.choice([b for b in banks if b != x]))

    return df


def clean_bank_statements(file_path):
    """Clean bank_statements.csv (ATM, card transactions)"""
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()

    df['transactionTimestamp'] = pd.to_datetime(df['transactionTimestamp'], errors='coerce')
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

    df = df.dropna(subset=['txnId', 'amount'])
    return df


def clean_personal_txns(file_path):
    """Clean MyTransaction.csv (personal expense tracking)"""
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip().str.lower()

    df.rename(columns={
        'refno': 'ref_no',
        'withdrawal': 'withdrawal',
        'deposit': 'deposit',
        'balance': 'balance'
    }, inplace=True)

    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['withdrawal'] = pd.to_numeric(df['withdrawal'], errors='coerce')
    df['deposit'] = pd.to_numeric(df['deposit'], errors='coerce')
    df['balance'] = pd.to_numeric(df['balance'], errors='coerce')

    return df
