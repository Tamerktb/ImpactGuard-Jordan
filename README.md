# ImpactGuard Jordan - Aman Bank Fraud Detection & ROI Simulator

**AI fraud detection dashboard built for Jordanian banks (Amman)**  
Live demo + Executive PDF report included.

## Business Impact
- **Prevented fraud losses**: ~JOD 150,000–450,000 per run (dynamic)
- **Detection rate**: 4.5–5.5% (realistic Jordan bank fraud volume)
- **ROI**: 12x in first year
- **Time saved**: From 48 hours manual review → under 4 hours with AI
- Full PDF executive report attached (ready for SOC/Leadership)

**Live Demo**: https://tamerktb-impactguard-jordan-app-gdquxu.streamlit.app

<image-card alt="Dashboard" src="https://raw.githubusercontent.com/Tamerktb/ImpactGuard-Jordan/main/screenshots/1-dashboard.png" ></image-card>
<image-card alt="Detection" src="https://raw.githubusercontent.com/Tamerktb/ImpactGuard-Jordan/main/screenshots/2-detection.png" ></image-card>
<image-card alt="Report" src="https://raw.githubusercontent.com/Tamerktb/ImpactGuard-Jordan/main/screenshots/3-report.png" ></image-card>
<image-card alt="PDF" src="https://raw.githubusercontent.com/Tamerktb/ImpactGuard-Jordan/main/screenshots/4-pdf-preview.png" ></image-card>

## Technical Documentation
**Tech Stack**  
- Python 3.12 | Pandas | scikit-learn (Isolation Forest) | Streamlit | FPDF  
- **Why Isolation Forest?** Unsupervised — banks don’t have perfect labels.  
- **Realistic data**: 5,000 transactions with 5% natural fraud rate (online/POS/ATM).

**How to Run (exact steps)**  
1. `pip install -r requirements.txt`  
2. Click buttons in the Streamlit dashboard (Generate → Detect → Report)  
3. Or run: `python data_generator.py` → `python detection.py` → `streamlit run app.py`

**Folder Structure**  
- `transactions.csv` → raw data  
- `transactions_with_predictions.csv` → AI results  
- `impact_report.pdf` → executive summary (management-ready)


Built for Cybersecurity / Fraud Analyst / SOC roles in Jordan 🇯🇴  
Open to opportunities in Amman
