import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_generator import generate_data
from detection import detect_fraud
from report_generator import generate_report

st.set_page_config(page_title="ImpactGuard Jordan", layout="wide")
st.title("ImpactGuard - Jordan")
st.markdown("**Aman Bank Fraud Detection & Impact Dashboard** | JOD transactions protected with AI")

# ←←← NEW: Step protection + Real data upload ←←←
if 'step' not in st.session_state:
    st.session_state.step = 0

# Pro feature banks love
uploaded = st.file_uploader("📤 Or upload your own bank CSV (real data - any format)", type="csv")
if uploaded:
    df_upload = pd.read_csv(uploaded)
    df_upload.to_csv('transactions.csv', index=False)
    st.success("✅ Real bank data uploaded! You can now run detection.")
    st.session_state.step = 1

# Step-protected buttons
if st.button("1. Generate 5,000 Fresh Transactions"):
    generate_data()
    st.session_state.step = 1
    st.success("✅ Synthetic data ready!")

if st.button("2. Run AI Fraud Detection") and st.session_state.step >= 1:
    detect_fraud()
    st.session_state.step = 2
    st.success("✅ Detection complete! (Model now scaled & reproducible)")

# Show results only after detection
try:
    df = pd.read_csv('transactions_with_predictions.csv')
except:
    st.warning("👆 Click the buttons above first (or upload real CSV)")
    st.stop()

col1, col2 = st.columns(2)
with col1:
    st.subheader("Summary")
    st.write(df.describe())
with col2:
    fraud_rate = (df['fraud_score'].mean() * 100)
    st.metric("Fraud Detection Rate", f"{fraud_rate:.2f}%", delta=f"{df['fraud_score'].sum()} cases")

st.subheader("Amount Distribution (JOD)")
fig, ax = plt.subplots()
df['amount_JOD'].hist(bins=50, ax=ax, color="#00cc66")
st.pyplot(fig)

if st.button("3. Generate Executive Business Impact Report (PDF)") and st.session_state.step >= 2:
    generate_report()
    st.success("✅ PDF Executive Report created!")
    
    with open("impact_report.pdf", "rb") as f:
        st.download_button(
            label="Download Aman_Bank_Impact_Report.pdf",
            data=f,
            file_name="Aman_Bank_Impact_Report.pdf",
            mime="application/pdf"
        )
