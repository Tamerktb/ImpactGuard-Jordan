import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_jordan_data():
    # Load real fraud data
    df = pd.read_csv('creditcard.csv')
    df = df.sample(5000, random_state=42)  # keep demo size
    
    # Jordanify it
    df.rename(columns={'Amount': 'amount_JOD'}, inplace=True)
    df['amount_JOD'] = df['amount_JOD'] * 0.71  # rough EUR→JOD conversion
    
    # Add Jordan-specific columns
    types = np.random.choice(['online', 'POS', 'ATM', 'mobile_money'], len(df))
    merchants = np.random.choice([
        'Zain', 'Orange', 'Umniah', 'Carrefour Jordan', 'Amazon.ae', 
        'Jordan Post', 'Citi Bank ATM', 'Hawala Transfer', 'Local Shop'
    ], len(df))
    hours = np.random.randint(0, 24, len(df))
    
    df['type'] = types
    df['merchant'] = merchants
    df['hour'] = hours
    df['is_fraud'] = df['Class']  # real labels
    
    df.to_csv('transactions.csv', index=False)
    print("✅ Generated 5,000 REAL fraud transactions (Kaggle) with Jordan flavor")
    
if __name__ == "__main__":
    generate_jordan_data()
