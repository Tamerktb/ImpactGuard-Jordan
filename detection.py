"""
ImpactGuard Jordan - AI Fraud Detection Engine
Uses Isolation Forest (unsupervised) — exactly what Jordan banks use.
"""

import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder, StandardScaler   # ← ADD StandardScaler
import numpy as np


def detect_fraud():
    df = pd.read_csv('transactions.csv')
    
    # Encode categoricals (unchanged)
    le_type = LabelEncoder()
    le_merch = LabelEncoder()
    df['type_enc'] = le_type.fit_transform(df['type'])
    df['merchant_enc'] = le_merch.fit_transform(df['merchant'])
    
    # ←←← THIS IS THE IMPORTANT PART ←←←
    X = df[['amount_JOD', 'type_enc', 'merchant_enc']]
    
    # NEW: Scale all features to same range
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Fixed parameters = reproducible results
    contamination = 0.05                     # exactly 5% like real banks
    model = IsolationForest(
        contamination=contamination, 
        random_state=42,                     # ← fixed seed
        n_estimators=100,                    # optional but nice
        max_samples='auto'
    )
    
    df['fraud_score'] = (model.fit_predict(X_scaled) == -1).astype(int)
    
    # Save + metrics (exactly as before)
    df.to_csv('transactions_with_predictions.csv', index=False)
    
    true_frauds = df['is_fraud'].sum()
    ai_cases = df['fraud_score'].sum()
    caught = (df['is_fraud'] & df['fraud_score']).sum()
    recall = (caught / true_frauds * 100) if true_frauds > 0 else 0
    
    print(f"✅ Fraud detection complete!")
    print(f"   AI flagged: {ai_cases} cases ({ai_cases/len(df)*100:.2f}%)")
    print(f"   True frauds: {true_frauds} | Recall: {recall:.1f}%")
    return df


if __name__ == "__main__":
    detect_fraud()
