# 🛡️ Real-Time Financial Fraud Detection API

## 📌 Project Overview
A production-ready Machine Learning REST API built to detect fraudulent credit card transactions in real-time. This project bridges the gap between Data Science and Software Engineering by taking a trained XGBoost model and deploying it as a scalable web service.

## 🚀 Business Impact
Financial fraud costs billions annually. Traditional batch-processing is too slow. This API allows a financial institution to send transaction data instantly and receive a "Fraud/Safe" verdict in milliseconds, preventing the transaction before it clears.

## 🛠️ Tech Stack
* **Machine Learning:** Scikit-Learn, XGBoost, Pandas, NumPy
* **Backend & API:** FastAPI, Uvicorn, Pydantic
* **Development:** Python 3.10+, VS Code

## 🧠 Machine Learning Architecture
* **Algorithm:** `XGBClassifier`
* **Challenge Solved:** Handled severe class imbalance (fraud is <1% of data) by utilizing XGBoost's `scale_pos_weight` parameter to heavily penalize false negatives.
* **Pipeline:** Raw Data $\rightarrow$ StandardScaler $\rightarrow$ XGBoost Model $\rightarrow$ FastAPI Endpoint.

## 💻 How to Run Locally
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Train the model: `python src/train.py`
4. Start the server: `python -m uvicorn src.main:app --reload`
5. Test the API at `http://127.0.0.1:8000/docs`