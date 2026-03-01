from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI(title="Suhayl's Fraud Detection System")

# Global variables
model = None
scaler = None

# This runs when the server starts
@app.on_event("startup")
def load_assets():
    global model, scaler
    try:
        model = joblib.load('models/fraud_model.pkl')
        scaler = joblib.load('models/scaler.pkl')
        print("✅ Models loaded successfully!")
    except Exception as e:
        print(f"❌ Error loading models: {e}")

class Transaction(BaseModel):
    features: list[float]

# --- THE FIX: This adds the Home Page ---
@app.get("/")
async def home():
    return {
        "status": "Online",
        "project": "AI Financial Fraud Detection",
        "developer": "Suhayl",
        "usage": "Go to /docs to test the API"
    }

@app.post("/predict")
async def predict_fraud(data: Transaction):
    try:
        input_array = np.array(data.features).reshape(1, -1)
        scaled_data = scaler.transform(input_array)
        prediction = model.predict(scaled_data)
        probability = model.predict_proba(scaled_data)[0][1]
        
        return {
            "is_fraud": int(prediction[0]),
            "fraud_probability": round(float(probability), 4),
            "verdict": "🚨 FRAUD DETECTED" if prediction[0] == 1 else "✅ SECURE TRANSACTION"
        }
    except Exception as e:
        return {"error": str(e)}