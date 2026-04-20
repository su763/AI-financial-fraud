# AI Financial Fraud Detection System

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Real-time fraud detection for credit card transactions using ensemble ML methods**

</div>

---

## 📋 Overview

This system detects fraudulent credit card transactions in real-time using machine learning. It addresses the critical challenge of **severe class imbalance** where fraud represents less than 1% of all transactions — a common scenario in financial services that breaks traditional classifiers.

### Why This Matters

Financial fraud costs global businesses **$47+ billion annually**. Traditional rule-based systems generate excessive false positives, frustrating customers and increasing operational costs. This ML-driven approach reduces false positives while maintaining high fraud detection rates.

---

## 🎯 Key Features

| Feature | Description |
|---------|-------------|
| **XGBoost Classifier** | Handles imbalanced data with scale_pos_weight optimization |
| **Real-time API** | Sub-100ms predictions via FastAPI |
| **Class Imbalance Handling** | SMOTE + ensemble methods for <1% fraud rate |
| **Docker Deployment** | Production-ready containerization |
| **Explainability** | Feature importance for regulatory compliance |

---

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│  Transaction    │    │  FastAPI         │    │  XGBoost        │
│  Request (JSON) │───▶│  REST API        │───▶│  Model          │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │  Prediction      │
                       │  {fraud: bool,   │
                       │   confidence: %} │
                       └──────────────────┘
```

---

## 🛠️ Tech Stack

- **ML Framework:** Scikit-learn, XGBoost
- **Data Processing:** Pandas, NumPy
- **API Framework:** FastAPI, Uvicorn, Pydantic
- **Deployment:** Docker
- **Validation:** Cross-validation with stratified k-folds

---

## 📊 Model Performance

| Metric | Score | Why It Matters |
|--------|-------|----------------|
| **Precision** | Optimized | Minimizes false accusations |
| **Recall** | High | Catches actual fraud |
| **F1-Score** | Balanced | Trade-off for imbalanced data |
| **AUC-ROC** | >0.95 | Overall discrimination ability |

---

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.8+
pip
Docker (optional)
```

### Installation

```bash
# Clone repository
git clone https://github.com/su763/AI-financial-fraud.git
cd AI-financial-fraud

# Install dependencies
pip install -r requirements.txt
```

### Train Model

```bash
# Download dataset (Kaggle Credit Card Fraud Detection)
# Place at: data/creditcard.csv

# Train model
python src/train.py
```

### Run API Server

```bash
# Start server
python src/main.py

# API available at: http://localhost:8000
# Docs at: http://localhost:8000/docs
```

### Docker Deployment

```bash
# Build image
docker build -t fraud-detection:latest .

# Run container
docker run -p 8000:8000 fraud-detection:latest
```

---

## 📁 Project Structure

```
AI-financial-fraud/
├── src/
│   ├── main.py           # FastAPI application
│   ├── train.py          # Model training pipeline
│   ├── predict.py        # Inference logic
│   └── preprocess.py     # Feature engineering
├── data/
│   └── creditcard.csv    # Dataset (not included)
├── models/
│   └── fraud_model.pkl   # Trained model
├── Dockerfile            # Container config
├── requirements.txt      # Python dependencies
└── README.md
```

---

## 📈 Usage Examples

### API Request

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 99.99,
    "time_since_last_transaction": 3600,
    "feature_1": 1.2,
    "feature_2": -0.5
    ...
  }'
```

### Response

```json
{
  "is_fraud": false,
  "fraud_probability": 0.03,
  "risk_level": "LOW"
}
```

---

## 🔬 Methodology

### 1. Data Preprocessing
- **Scaling:** StandardScaler for numerical features
- **Handling Imbalance:** SMOTE (Synthetic Minority Oversampling)
- **Feature Engineering:** Time-based features, rolling statistics

### 2. Model Selection
- **XGBoost:** Chosen for handling imbalanced datasets
- **Class Weighting:** `scale_pos_weight` parameter tuned
- **Hyperparameters:** Optimized via GridSearchCV

### 3. Evaluation Strategy
- **Stratified K-Fold:** Maintains class distribution
- **Metrics:** Precision-Recall AUC (more informative than ROC for imbalanced data)
- **Threshold Tuning:** Business-cost optimized decision threshold

---

## 🎓 Key Learnings

1. **Class Imbalance:** Accuracy is misleading — use Precision-Recall curves
2. **Feature Scaling:** Critical for distance-based algorithms
3. **Threshold Selection:** Default 0.5 threshold rarely optimal for fraud
4. **Latency vs Accuracy:** Trade-off for real-time production systems

---

## 📝 Dataset

This project uses the **Credit Card Fraud Detection Dataset** (Kaggle):
- 284,807 transactions
- 492 fraud cases (0.172%)
- 28 PCA-transformed features + amount + time
- [Download here](https://www.kaggle.com/mlg-ulb/creditcardfraud)

---

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- [ ] Deep learning approaches (Autoencoders for anomaly detection)
- [ ] Real-time streaming with Kafka
- [ ] Model monitoring dashboard
- [ ] A/B testing framework

---

## 📄 License

MIT License — See [LICENSE](LICENSE) for details

---

## 👤 Author

**MD Suhayl Sekander**  
Data Scientist | Computer Science Student, Taylor's University

[![GitHub](https://img.shields.io/badge/GitHub-su763-black?style=flat&logo=github)](https://github.com/su763)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-MD%20Suhayl%20Sekander-blue?style=flat&logo=linkedin)](https://linkedin.com/in/su763)

---

<div align="center">

**If this project helped you, please ⭐ the repository!**

</div>
