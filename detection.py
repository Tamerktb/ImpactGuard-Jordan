"""
ImpactGuard Jordan - AI Fraud Detection Engine
Uses Isolation Forest (unsupervised) — exactly what Jordan banks use because they rarely have perfect labeled data.
"""
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
import numpy as np

def detect_fraud():
    df = pd.read_csv('transactions.csv')
    le_type = LabelEncoder()
    le_merch = LabelEncoder()
    df['type_enc'] = le_type.fit_transform(df['type'])
    df['merchant_enc'] = le_merch.fit_transform(df['merchant'])
    
    X = df[['amount_JOD', 'type_enc', 'merchant_enc']]
    
    # Realistic varying rate (4.5%–5.5%) like real Aman Bank SOC
    contamination = 0.05 + np.random.uniform(-0.005, 0.005)
    model = IsolationForest(contamination=contamination, random_state=None)
    
    df['fraud_score'] = (model.fit_predict(X) == -1).astype(int)
    
    df.to_csv('transactions_with_predictions.csv', index=False)
    
    # Performance metrics (great for technical interview)
    true_frauds = df['is_fraud'].sum()
    ai_cases = df['fraud_score'].sum()
    caught = (df['is_fraud'] & df['fraud_score']).sum()
    recall = (caught / true_frauds * 100) if true_frauds > 0 else 0
    
    print(f"✅ Fraud detection complete!")
    print(f"   AI flagged: {ai_cases} cases ({(ai_cases/len(df)*100):.2f}%)")
    print(f"   True frauds: {true_frauds} | Recall: {recall:.1f}%")
    return df

if __name__ == "__main__":
    detect_fraud()