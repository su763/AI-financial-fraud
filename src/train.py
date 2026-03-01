import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os

def train_model():
    # 1. Load Data - Using forward slash for Windows/Mac compatibility
    try:
        data = pd.read_csv('data/creditcard.csv') 
        print("✅ Data loaded successfully!")
    except FileNotFoundError:
        print("❌ Error: Could not find 'data/creditcard.csv'. Check your folder structure.")
        return

    # 2. Check and Set Target Column
    # Most fraud datasets use 'Class'. If yours is different, change it here.
    target_column = 'Class' 
    
    if target_column not in data.columns:
        print(f"❌ Error: Column '{target_column}' not found. Available columns: {data.columns.tolist()[:5]}...")
        return

    # 3. Split Features and Target
    X = data.drop(target_column, axis=1)
    y = data[target_column]

    # 4. Preprocessing
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 5. Train XGBoost
    print("🚀 Training the model... this might take a minute.")
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    # We add scale_pos_weight because fraud data is usually 99% safe, 1% fraud
    model = XGBClassifier(n_estimators=100, max_depth=5, learning_rate=0.1, scale_pos_weight=99)
    model.fit(X_train, y_train)

    # 6. Save model and scaler
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/fraud_model.pkl')
    joblib.dump(scaler, 'models/scaler.pkl')
    
    print("🔥 Success! Model and Scaler saved in the 'models/' folder.")

if __name__ == "__main__":
    train_model()