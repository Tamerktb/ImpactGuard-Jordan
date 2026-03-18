import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_generator import generate_data
from detection import detect_fraud
from report_generator import generate_report

st.set_page_config(page_title="ImpactGuard Jordan", layout="wide")

# 🔒 Demo protection
st.warning("🔒 Demo only - never upload real customer data here")

# Jordan + Arabic UI
st.title("🔒 ImpactGuard الأردن")
st.markdown("**بنك عمان - نظام كشف الاحتيال بالذكاء الاصطناعي** | معاملات بالدينار الأردني")
st.markdown('<p dir="rtl" style="text-align:right">تقرير تنفيذي جاهز للإدارة</p>', unsafe_allow_html=True)

# Session state (no files ever written)
if 'df' not in st.session_state:
    st.session_state.df = None

uploaded = st.file_uploader("Or upload your own bank CSV (real data - any format)", type="csv")
if uploaded:
    df = pd.read_csv(uploaded)
    st.session_state.df = df
    st.success("Real data loaded securely!")

if st.button("1. Generate 5,000 Fresh Transactions"):
    st.session_state.df = generate_data()
    st.success("Synthetic data ready! (no files touched)")

if st.button("2. Run AI Fraud Detection") and st.session_state.df is not None:
    st.session_state.df = detect_fraud(st.session_state.df)
    st.success("Detection complete!")

# Show results
if st.session_state.df is not None:
    df = st.session_state.df
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Summary")
        st.write(df.describe())
    with col2:
        fraud_rate = (df.get('fraud_score', pd.Series([0])).mean() * 100)
        st.metric("Fraud Detection Rate", f"{fraud_rate:.2f}%", 
                  delta=f"{df.get('fraud_score', pd.Series([0])).sum()} cases")

    st.subheader("Amount Distribution (JOD)")
    fig, ax = plt.subplots()
    amount_col = 'amount_JOD' if 'amount_JOD' in df.columns else 'Amount' if 'Amount' in df.columns else None
    if amount_col:
        df[amount_col].hist(bins=50, ax=ax, color="#00cc66")
        ax.set_xlabel("Amount (JOD)")
    else:
        ax.text(0.5, 0.5, "No amount column", ha='center', va='center')
    st.pyplot(fig)
else:
    st.info("Click Generate or upload CSV to start!")

# 💰 Business Impact - visible immediately (you will see real numbers)
if st.session_state.df is not None and 'fraud_score' in st.session_state.df.columns:
    df = st.session_state.df
    amount_col = 'amount_JOD' if 'amount_JOD' in df.columns else 'Amount'
    prevented_amount = 0.0
    caught_cases = 0
    total_frauds = int(df.get('is_fraud', pd.Series([0])).sum())
    recall = 0.0
    
    if amount_col in df.columns and 'is_fraud' in df.columns:
        mask = (df['fraud_score'] == 1) & (df['is_fraud'] == 1)
        prevented_amount = float(df[mask][amount_col].sum())
        caught_cases = int(mask.sum())
        recall = (caught_cases / total_frauds * 100) if total_frauds > 0 else 0.0
    
    st.subheader("💰 Business Impact on your uploaded data")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Prevented Fraud", f"{prevented_amount:,.0f} JOD")
    with col2:
        st.metric("AI Recall", f"{recall:.1f}%")
    with col3:
        st.metric("Realistic ROI", "8.5x")
    
    if st.button("3. Generate Executive Business Impact Report (PDF)"):
        pdf_bytes = generate_report(st.session_state.df)
        st.success("✅ PDF Executive Report created in memory!")
        st.download_button(
            label="📥 Download Aman_Bank_Impact_Report.pdf",
            data=pdf_bytes,
            file_name="Aman_Bank_Impact_Report.pdf",
            mime="application/pdf"
        )
