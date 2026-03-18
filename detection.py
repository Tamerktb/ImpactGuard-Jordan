import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder, StandardScaler
import shap  # ← new
import joblib

def detect_fraud():
    df = pd.read_csv('transactions.csv')
    
    # More features (real banks use 20+)
    le_type = LabelEncoder()
    le_merch = LabelEncoder()
    df['type_enc'] = le_type.fit_transform(df['type'])
    df['merchant_enc'] = le_merch.fit_transform(df['merchant'])
    
    X = df[['amount_JOD', 'type_enc', 'merchant_enc', 'hour']]  # ← added hour
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    model = IsolationForest(contamination=0.05, random_state=42, n_estimators=200)
    df['fraud_score'] = (model.fit_predict(X_scaled) == -1).astype(int)
    
    # SHAP explanations (banks LOVE this)
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_scaled)
    df['shap_amount'] = shap_values[:, 0]  # example
    
    # Save model for "production" feel
    joblib.dump(model, 'fraud_model.joblib')
    
    # Proper metrics (precision + recall)
    caught = ((df['fraud_score'] == 1) & (df['is_fraud'] == 1)).sum()
    precision = caught / df['fraud_score'].sum() if df['fraud_score'].sum() > 0 else 0
    recall = caught / df['is_fraud'].sum() if df['is_fraud'].sum() > 0 else 0
    
    print(f"Precision: {precision:.1%} | Recall: {recall:.1%}")
    
    df.to_csv('transactions_with_predictions.csv', index=False)
    return df
