import streamlit as st
import pickle
import numpy as np

# Load model (correct path)
model = pickle.load(open("models/credit_model.pkl", "rb"))

st.title("Credit Scoring Prediction App")

# Input fields based on actual dataset
income = st.number_input("Annual Income", min_value=10000, max_value=1000000, step=1000)
debt = st.number_input("Total Debt", min_value=0.0, step=100.0)
payment_history = st.slider("Payment History Score (0=Bad, 1=Perfect)", 0.0, 1.0, 0.8, 0.01)
late_payments = st.slider("Number of Late Payments", 0, 20, 2)
credit_util = st.slider("Credit Utilization Ratio", 0.0, 1.0, 0.3, 0.01)
inquiries = st.slider("Credit Inquiries in Last 6 Months", 0, 10, 1)
credit_history_years = st.slider("Credit History Length (Years)", 1, 30, 5)

# Form input vector
input_data = np.array([[income, debt, payment_history, late_payments, credit_util, inquiries, credit_history_years]])

# Predict
if st.button("Predict Creditworthiness"):
    pred = model.predict(input_data)
    st.success("The applicant is Creditworthy ✅" if pred[0] == 1 else "The applicant is NOT Creditworthy ❌")
