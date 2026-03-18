import pandas as pd
import numpy as np

def generate_data():  # renamed to match your import
    df = pd.read_csv('creditcard.csv')
    df = df.sample(5000, random_state=42)
    
    # Jordanify it (your local merchants already done ✅)
    df.rename(columns={'Amount': 'amount_JOD'}, inplace=True)
    df['amount_JOD'] = df['amount_JOD'] * 0.71
    
    types = np.random.choice(['online', 'POS', 'ATM', 'mobile_money'], len(df))
    merchants = np.random.choice([
        'Zain', 'Orange', 'Umniah', 'Carrefour Jordan', 'Amazon.ae', 
        'Jordan Post', 'Citi Bank ATM', 'Hawala Transfer', 'Local Shop'
    ], len(df))
    hours = np.random.randint(0, 24, len(df))
    
    df['type'] = types
    df['merchant'] = merchants
    df['hour'] = hours
    df['is_fraud'] = df['Class']
    
    print("Generated 5,000 REAL fraud transactions (Kaggle) with Jordan flavor")
    return df  # ← now returns df (no file write)
