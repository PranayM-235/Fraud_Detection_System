# 💳 Credit Card Fraud Detection System

## 📌 Overview
This project is an end-to-end **Credit Card Fraud Detection System** built using Machine Learning and deployed with a real-time API and interactive dashboard.

The system detects fraudulent transactions using advanced ML models and provides insights through a Power BI dashboard for monitoring fraud trends, user behavior, and high-risk activities.

---

## 🚀 Features

- 🔍 Fraud detection using Machine Learning models (XGBoost & Random Forest)
- ⚡ Real-time prediction using FastAPI
- 🗄️ Database integration to store transactions and predictions
- 📊 Interactive Power BI dashboard for fraud analysis
- 📈 Handles highly imbalanced dataset with optimized evaluation metrics

---

## 🧠 Tech Stack

- **Programming Language:** Python  
- **Machine Learning:** Scikit-learn, XGBoost  
- **API Framework:** FastAPI  
- **Database:** MySQL  
- **Visualization:** Power BI  
- **Libraries:** Pandas, NumPy, Joblib  

---

## 🏗️ Project Architecture

User Input → FastAPI → ML Model → Prediction → Database → Power BI Dashboard

---

## 📂 Project Structure

Fraud-Detection-System/
│
├── data/
│   └── creditcard_sample.csv
│
├── notebooks/
│   └── fraud_model.ipynb
│
├── models/
│   ├── xgboost_model.pkl
│   └── random_forest.pkl
│
├── api/
│   └── main.py
│
├── database/
│   └── db.py
│
├── dashboard/
│   └── fraud_dashboard.pbix
│
├── requirements.txt
├── README.md
└── .gitignore

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
git clone https://github.com/PranayM-235/Fraud-Detection-System.git
cd Fraud_Detection_ System

### 2️⃣ Install dependencies
pip install -r requirements.txt

### 3️⃣ Run FastAPI server
uvicorn api.main:app --reload

### 4️⃣ Open API Docs
http://127.0.0.1:8000/docs

---

## 🔮 API Usage

### Endpoint:
POST /predict

### Sample Input:
{
  "Time": 120000,
  "V1": -5.0,
  "V2": 5.5,
  "V3": -4.2,
  "V4": 4.8,
  "V5": 3.5,
  "V6": -2.5,
  "V7": 2.2,
  "V8": 1.8,
  "V9": -4.0,
  "V10": 3.0,
  "V11": -2.8,
  "V12": 2.5,
  "V13": 1.5,
  "V14": -3.5,
  "V15": 1.2,
  "V16": -1.0,
  "V17": 2.0,
  "V18": 1.5,
  "V19": -2.5,
  "V20": 1.0,
  "V21": 1.2,
  "V22": -1.5,
  "V23": 0.8,
  "V24": 1.0,
  "V25": -0.8,
  "V26": 1.2,
  "V27": 1.0,
  "V28": -0.7,
  "Amount": 5000,
  "user_id": 2003,
  "location": "Unknown",
  "device_type": "Tablet",
  "transaction_time": "2024-05-02 02:30:00"
}

### Sample Output:
{
  "transaction_id": 284813,
  "fraud_probability": 0.0003,
  "prediction": 0
}

---

## 📊 Dashboard

The Power BI dashboard provides:

- 📌 Total Transactions  
- 🚨 Fraud Count  
- 📉 Fraud Rate  
- 📊 Fraud Trend Over Time  
- 📱 Fraud by Device Type  
- 🌍 Fraud by Location  
- 🔎 Top Suspicious Transactions  


---

## 🧪 Model Performance

- ROC-AUC Score: ~0.97
- High precision and recall for fraud detection
- Optimized for imbalanced dataset

---

## 💡 Future Improvements

- Add real-time streaming (Kafka)
- Improve model with deep learning
- Add user authentication to API
- Deploy on cloud (AWS / Render)

---

## 👨‍💻 Author

Pranay S Masurkar

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!
