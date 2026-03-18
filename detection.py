import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder, StandardScaler
import shap

def detect_fraud(df):
    # Auto-fix for raw Kaggle creditcard.csv
    if 'type' not in df.columns:
        if len(df) > 5000:
            df = df.sample(5000, random_state=42).copy()
        if 'Amount' in df.columns:
            df.rename(columns={'Amount': 'amount_JOD'}, inplace=True)
            df['amount_JOD'] = df['amount_JOD'] * 0.71
        df['type'] = np.random.choice(['online', 'POS', 'ATM', 'mobile_money'], len(df))
        df['merchant'] = np.random.choice([
            'Zain', 'Orange', 'Umniah', 'Carrefour Jordan', 'Amazon.ae', 
            'Jordan Post', 'Citi Bank ATM', 'Hawala Transfer', 'Local Shop'
        ], len(df))
        df['hour'] = np.random.randint(0, 24, len(df))
        df['is_fraud'] = df.get('Class', 0)

    le_type = LabelEncoder()
    le_merch = LabelEncoder()
    df['type_enc'] = le_type.fit_transform(df['type'])
    df['merchant_enc'] = le_merch.fit_transform(df['merchant'])
    
    X = df[['amount_JOD', 'type_enc', 'merchant_enc', 'hour']]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    model = IsolationForest(contamination=0.05, random_state=42, n_estimators=200)
    df['fraud_score'] = (model.fit_predict(X_scaled) == -1).astype(int)
    
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_scaled)
    df['shap_amount'] = shap_values[:, 0]
    
    return df
