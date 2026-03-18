import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_generator import generate_data
from detection import detect_fraud
from report_generator import generate_report

st.set_page_config(page_title="ImpactGuard Jordan", layout="wide")

# 🔒 Live demo protection
st.warning("🔒 Demo only - never upload real customer data here")

# Jordan + Arabic UI (exactly as requested)
st.title("🔒 ImpactGuard الأردن")
st.markdown("**بنك عمان - نظام كشف الاحتيال بالذكاء الاصطناعي** | معاملات بالدينار الأردني")
st.markdown('<p dir="rtl" style="text-align:right">تقرير تنفيذي جاهز للإدارة</p>', unsafe_allow_html=True)

# BIGGEST FIX: Session state + temp/in-memory only (no global files ever)
if 'df' not in st.session_state:
    st.session_state.df = None

uploaded = st.file_uploader("Or upload your own bank CSV (real data - any format)", type="csv")
if uploaded:
    df = pd.read_csv(uploaded)
    st.session_state.df = df          # ← in memory, no file overwrite!
    st.success("Real data loaded securely!")

# All buttons now work on st.session_state.df
if st.button("1. Generate 5,000 Fresh Transactions"):
    st.session_state.df = generate_data()
    st.success("Synthetic data ready! (no files touched)")

if st.button("2. Run AI Fraud Detection") and st.session_state.df is not None:
    st.session_state.df = detect_fraud(st.session_state.df)
    st.success("Detection complete! (Model now scaled & reproducible)")

# Show results
if st.session_state.df is not None:
    df = st.session_state.df
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Summary")
        st.write(df.describe())
    with col2:
        fraud_rate = (df['fraud_score'].mean() * 100) if 'fraud_score' in df.columns else 0
        st.metric("Fraud Detection Rate", f"{fraud_rate:.2f}%", 
                  delta=f"{df.get('fraud_score', pd.Series([0])).sum()} cases")

    st.subheader("Amount Distribution (JOD)")
    fig, ax = plt.subplots()
    if 'amount_JOD' in df.columns:
        df['amount_JOD'].hist(bins=50, ax=ax, color="#00cc66")
    st.pyplot(fig)
else:
    st.warning("Click Generate or upload CSV to start!")

if st.button("3. Generate Executive Business Impact Report (PDF)") and st.session_state.df is not None and 'fraud_score' in st.session_state.df.columns:
    pdf_bytes = generate_report(st.session_state.df)
    st.success("PDF Executive Report created (in memory)!")
    st.download_button(
        label="Download Aman_Bank_Impact_Report.pdf",
        data=pdf_bytes,
        file_name="Aman_Bank_Impact_Report.pdf",
        mime="application/pdf"
    )
