import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi import FastAPI
import joblib
import numpy as np
from database.db import get_connection

print("THIS IS MY MAIN FILE RUNNING 🚀")

app = FastAPI()

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "xgb_model.pkl")
model = joblib.load(MODEL_PATH)

THRESHOLD = 0.4

@app.get("/")
def home():
    return {"message": "Fraud Detection API Running 🚀"}

# @app.post("/predict")
# def predict(data: dict):
#     return {"status": "predict API working"}
@app.post("/predict")
def predict(data: dict):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # ✅ Insert transaction
        cursor.execute("""
            INSERT INTO transactions 
            (Time, Amount, Class, user_id, location, device_type, transaction_time)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            data["Time"],
            data["Amount"],
            data.get("Class", 0),
            data["user_id"],
            data["location"],
            data["device_type"],
            data["transaction_time"]
        ))

        transaction_id = cursor.lastrowid

        # ✅ Prepare features
        feature_keys = ["Time"] + [f"V{i}" for i in range(1, 29)] + ["Amount", "user_id"]

        features = [data[k] for k in feature_keys]

        import numpy as np
        features = np.array(features).reshape(1, -1)

        # ✅ Predict
        prob = model.predict_proba(features)[0][1]
        prediction = 1 if prob > 0.4 else 0

        # ✅ Store prediction
        cursor.execute("""
            INSERT INTO predictions 
            (transaction_id, fraud_probability, predicted_label)
            VALUES (%s, %s, %s)
        """, (transaction_id, float(prob), int(prediction)))

        conn.commit()
        conn.close()

        return {
            "transaction_id": transaction_id,
            "fraud_probability": float(prob),
            "prediction": int(prediction)
        }

    except Exception as e:
        return {"error": str(e)}