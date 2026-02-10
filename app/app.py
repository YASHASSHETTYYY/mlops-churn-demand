import streamlit as st
import joblib
import numpy as np

st.title("MLOps: Churn Prediction & Demand Forecasting")

model_type = st.selectbox("Select Model", ["Churn", "Demand"])

if model_type == "Churn":
    model = joblib.load("models/churn_model.pkl")

    input_value = st.number_input("Enter numeric feature value (example)")

    if st.button("Predict Churn"):
        prediction = model.predict([[input_value]])
        st.write("Prediction:", prediction[0])

else:
    model = joblib.load("models/demand_model.pkl")

    day = st.number_input("Day")
    month = st.number_input("Month")
    year = st.number_input("Year")

    if st.button("Predict Sales"):
        prediction = model.predict([[day, month, year]])
        st.write("Predicted Sales:", prediction[0])
