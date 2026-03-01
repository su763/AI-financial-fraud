import streamlit as st
import requests
import numpy as np

st.set_page_config(page_title="Fraud Guard AI", page_icon="🛡️")

st.title("🛡️ Fraud Guard: Real-Time Detection")
st.write("Adjust the transaction parameters to test the AI model.")

# Create sliders/inputs for the user
amount = st.number_input("Transaction Amount ($)", min_value=0.0, value=100.0)
time = st.number_input("Seconds since first transaction", min_value=0, value=3600)

# Simulate the other 28 features for the demo
if st.button("Analyze Transaction"):
    # Prepare 30 features (Time, Amount + 28 random for demo)
    dummy_v_features = list(np.random.randn(28))
    payload = {"features": [time, amount] + dummy_v_features}
    
    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        res = response.json()
        
        if res["is_fraud"] == 1:
            st.error(f"⚠️ {res['verdict']}")
            st.metric("Fraud Probability", f"{res['fraud_probability']*100}%")
        else:
            st.success(f"✅ {res['verdict']}")
            st.metric("Fraud Probability", f"{res['fraud_probability']*100}%")
            
    except Exception as e:
        st.error("Is the API server running? Could not connect.")