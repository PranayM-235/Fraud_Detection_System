import streamlit as st
import requests

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="💳",
    layout="centered"
)

# -----------------------------------
# TITLE
# -----------------------------------
st.title("💳 Credit Card Fraud Detection System")

st.markdown("""
This application predicts whether a credit card transaction is **Fraudulent** or **Normal**
using a Machine Learning model deployed with FastAPI.
""")

# -----------------------------------
# SIDEBAR
# -----------------------------------
st.sidebar.header("📘 How to Use")

st.sidebar.markdown("""
### Instructions
1. Enter transaction details
2. Click **Predict Fraud**
3. View prediction result

### Tips
- Large unusual values may indicate fraud
- Negative V-values can sometimes represent suspicious behavior
""")

# -----------------------------------
# DEFAULT VALUES
# -----------------------------------
default_values = {
    "time": 10000,
    "amount": 100.0,
    "v1": 0.0,
    "v2": 0.0,
    "v3": 0.0,
    "v4": 0.0
}

fraud_values = {
    "time": 120000,
    "amount": 5000.0,
    "v1": -5.0,
    "v2": 5.5,
    "v3": -4.2,
    "v4": 4.8
}

# -----------------------------------
# SESSION STATE
# -----------------------------------
if "input_data" not in st.session_state:
    st.session_state.input_data = default_values

# -----------------------------------
# EXAMPLE BUTTONS
# -----------------------------------
st.subheader("📌 Load Example Data")

col1, col2 = st.columns(2)

with col1:
    if st.button("🟢 Load Normal Example"):
        st.session_state.input_data = default_values

with col2:
    if st.button("🔴 Load Fraud Example"):
        st.session_state.input_data = fraud_values

# -----------------------------------
# INPUT FIELDS
# -----------------------------------
st.subheader("📝 Transaction Details")

time = st.number_input(
    "Transaction Time",
    value=st.session_state.input_data["time"]
)

amount = st.number_input(
    "Transaction Amount",
    value=st.session_state.input_data["amount"]
)

v1 = st.number_input(
    "V1",
    value=st.session_state.input_data["v1"]
)

v2 = st.number_input(
    "V2",
    value=st.session_state.input_data["v2"]
)

v3 = st.number_input(
    "V3",
    value=st.session_state.input_data["v3"]
)

v4 = st.number_input(
    "V4",
    value=st.session_state.input_data["v4"]
)

# -----------------------------------
# PREDICT BUTTON
# -----------------------------------
if st.button("🚀 Predict Fraud"):

    payload = {
        "Time": time,
        "V1": v1,
        "V2": v2,
        "V3": v3,
        "V4": v4,
        "V5": 0,
        "V6": 0,
        "V7": 0,
        "V8": 0,
        "V9": 0,
        "V10": 0,
        "V11": 0,
        "V12": 0,
        "V13": 0,
        "V14": 0,
        "V15": 0,
        "V16": 0,
        "V17": 0,
        "V18": 0,
        "V19": 0,
        "V20": 0,
        "V21": 0,
        "V22": 0,
        "V23": 0,
        "V24": 0,
        "V25": 0,
        "V26": 0,
        "V27": 0,
        "V28": 0,
        "Amount": amount,
        "user_id": 101,
        "location": "Unknown",
        "device_type": "Mobile",
        "transaction_time": "2024-05-01 12:00:00"
    }

    # YOUR RENDER API URL
    url = "https://fraud-detection-system-r6n1.onrender.com/predict"

try:

    with st.spinner("Analyzing transaction..."):

           response = requests.post(url, json=payload)

    st.write("Status Code:", response.status_code)

    result = response.json()

    st.write("📦 API Response:", result)

    if "prediction" in result:

        prediction = result["prediction"]
        fraud_prob = result["fraud_probability"]

        st.subheader("📊 Prediction Result")

    if prediction == 1:
        st.error("🚨 Fraudulent Transaction Detected")
    else:
        st.success("✅ Normal Transaction")

    st.metric(
        label="Fraud Probability",
        value=f"{fraud_prob:.6f}"
    )
    
    st.error("Prediction key not found in API response")

except Exception as e:
 st.error(f"Error: {e}")

# -----------------------------------
# FOOTER
# -----------------------------------
st.markdown("---")
st.caption("Built using FastAPI, Streamlit, Machine Learning, and Render.")