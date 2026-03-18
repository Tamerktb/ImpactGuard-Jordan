# ImpactGuard Jordan - Aman Bank Fraud Detection & ROI Simulator

> **DISCLAIMER**  
> This is a **portfolio demonstration** using public Kaggle data.  
> **Not for production use.** Never upload real customer/bank data.

**AI fraud detection dashboard built for Jordanian banks (Amman)**  
Live demo + Executive PDF report included.

## Business Impact
- **Example run (varies with data) — see PDF download**
- **Detection rate**: 4.5–5.5% (realistic Jordan bank fraud volume)
- **ROI**: 12x in first year
- **Time saved**: From 48 hours manual review → under 4 hours with AI
- Full PDF executive report attached (ready for SOC/Leadership)

**Live Demo**: https://tamerktb-impactguard-jordan-app-gdquxu.streamlit.app

![Dashboard](https://raw.githubusercontent.com/Tamerktb/ImpactGuard-Jordan/main/screenshots/1-dashboard.png)
![Detection](https://raw.githubusercontent.com/Tamerktb/ImpactGuard-Jordan/main/screenshots/2-detection.png)
![Report](https://raw.githubusercontent.com/Tamerktb/ImpactGuard-Jordan/main/screenshots/3-report.png)
![PDF](https://raw.githubusercontent.com/Tamerktb/ImpactGuard-Jordan/main/screenshots/4-pdf-preview.png)

## Technical Documentation
**Tech Stack**  
- Python 3.12 | Pandas | scikit-learn (Isolation Forest) | Streamlit | FPDF  
- **Why Isolation Forest?** Unsupervised — banks don’t have perfect labels.  
- **Realistic data**: 5,000 transactions with 5% natural fraud rate (online/POS/ATM).

**How to Run (exact steps)**  
1. Open cmd in the project folder  
2. `pip install -r requirements.txt`  
3. `python -m streamlit run app.py`  
4. Click buttons in the Streamlit dashboard (Generate → Detect → Report)

**Folder Structure**  
- All data now runs **in memory** (no global files are created/overwritten)

Built for Cybersecurity / Fraud Analyst / SOC roles in Jordan 🇯🇴  
Open to opportunities in Amman
