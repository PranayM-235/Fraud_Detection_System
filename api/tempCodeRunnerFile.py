import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi import FastAPI
import joblib
import numpy as np

print("THIS IS MY MAIN FILE RUNNING 🚀")

app = FastAPI()

# -----------------------------------
# LOAD MODEL
# -----------------------------------
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "xgb_model.pkl"
)

model = joblib.load(MODEL_PATH)

THRESHOLD = 0.4

# -----------------------------------
# HOME ROUTE
# -----------------------------------
@app.get("/")
def home():
    return {
        "message": "Fraud Detection API Running 🚀"
    }

# -----------------------------------
# PREDICT ROUTE
# -----------------------------------
@app.post("/predict")
def predict(data: dict):

    try:

        # Feature order
        feature_keys = (
            ["Time"] +
            [f"V{i}" for i in range(1, 29)] +
            ["Amount", "user_id"]
        )

        # Prepare features
        features = [data[k] for k in feature_keys]

        features = np.array(features).reshape(1, -1)

        # Prediction probability
        prob = model.predict_proba(features)[0][1]

        # Threshold prediction
        prediction = 1 if prob > THRESHOLD else 0

        # Return result
        return {
            "transaction_id": 1,
            "fraud_probability": float(prob),
            "prediction": int(prediction)
        }

    except Exception as e:

        return {
            "error": str(e)
        }