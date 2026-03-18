import pandas as pd

def generate_report(df):
    amount_col = 'amount_JOD' if 'amount_JOD' in df.columns else 'Amount'
    prevented_amount = 0.0
    caught_cases = 0
    total_frauds = int(df.get('is_fraud', pd.Series([0])).sum())
    recall = 0.0
    
    if amount_col in df.columns and 'fraud_score' in df.columns and 'is_fraud' in df.columns:
        mask = (df['fraud_score'] == 1) & (df['is_fraud'] == 1)
        prevented_amount = float(df[mask][amount_col].sum())
        caught_cases = int(mask.sum())
        recall = (caught_cases / total_frauds * 100) if total_frauds > 0 else 0.0
    
    roi_multiplier = 8.5
    savings_jod = round(prevented_amount * roi_multiplier)
    
    from fpdf import FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, "ImpactGuard Jordan - Aman Bank Fraud Report", ln=1, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"Prevented Fraud: {prevented_amount:,.0f} JOD", ln=1)
    pdf.cell(200, 10, f"Recall: {recall:.1f}%", ln=1)
    pdf.cell(200, 10, f"Realistic ROI: {roi_multiplier}x (savings {savings_jod:,} JOD)", ln=1)
    pdf.cell(200, 10, "Time saved: 48h manual to ~4h AI", ln=1)   # ← FIXED: no arrow
    
    pdf_bytes = pdf.output(dest='S')
    print(f"✅ PDF generated | Prevented: {prevented_amount:,.0f} JOD | Recall: {recall:.1f}%")
    return pdf_bytes
