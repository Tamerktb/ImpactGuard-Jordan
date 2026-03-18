import pandas as pd
import numpy as np

def generate_data():
    np.random.seed(42)   # ← added for same results every time
    n = 5000
    data = {
        'amount_JOD': np.random.lognormal(mean=5, sigma=1.5, size=n) * 0.71,
        'type': np.random.choice(['online', 'POS', 'ATM', 'mobile_money'], n),
        'merchant': np.random.choice([
            'Zain', 'Orange', 'Umniah', 'Carrefour Jordan', 'Amazon.ae', 
            'Jordan Post', 'Citi Bank ATM', 'Hawala Transfer', 'Local Shop'
        ], n),
        'hour': np.random.randint(0, 24, n),
        'is_fraud': np.random.choice([0, 1], n, p=[0.95, 0.05])
    }
    df = pd.DataFrame(data)
    print("✅ Generated 5,000 realistic Jordan transactions")
    return df
