import requests
import random

URL = "http://127.0.0.1:8000/predict"

def test_my_api():
    # 1. Create a list of 30 random numbers 
    # (Matching the 30 columns: Time, V1-V28, Amount)
    random_data = [random.uniform(-1, 1) for _ in range(30)]
    
    # 2. Package it in the 'features' key that main.py expects
    payload = {
        "features": random_data
    }

    print(f"📡 Sending 30 features to: {URL}")
    
    try:
        response = requests.post(URL, json=payload)
        
        if response.status_code == 200:
            print("✅ SUCCESS!")
            print("API Response:", response.json())
        else:
            print(f"❌ Failed with Status {response.status_code}")
            print("Details:", response.text)
            
    except Exception as e:
        print(f"❌ Connection Error: {e}")

if __name__ == "__main__":
    test_my_api()