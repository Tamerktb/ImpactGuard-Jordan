import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_data():
    n = 5000
    dates = [datetime(2024, 1, 1) + timedelta(days=i % 365) for i in range(n)]
    
    # Normal transactions
    amounts = np.random.lognormal(5, 1, n)
    types = np.random.choice(['online', 'pos', 'atm'], n)
    merchants = np.random.choice(['Amazon', 'Carrefour', 'Zain', 'Aman Bank', 'Other'], n)
    is_fraud = np.random.choice([0, 1], n, p=[0.95, 0.05])
    
    # 🔥 REALISTIC FRAUD: make fraud cases have MUCH higher amounts (outliers)
    amounts = np.where(is_fraud == 1, amounts * np.random.uniform(8, 15), amounts)
    
    df = pd.DataFrame({
        'date': dates,
        'amount_JOD': amounts,
        'type': types,
        'merchant': merchants,
        'is_fraud': is_fraud
    })
    df.to_csv('transactions.csv', index=False)
    print("✅ Generated 5,000 truly fresh transactions with realistic fraud outliers")

if __name__ == "__main__":
    generate_data()