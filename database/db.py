import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="#Pranay235",   # 🔴 change this
        database="fraud_detection"
    )
    return conn