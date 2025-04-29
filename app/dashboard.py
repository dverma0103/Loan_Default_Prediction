#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and scaler
model = joblib.load(r"C:\Users\Deepak Verma\OneDrive\Documents\Loan_Default_Prediction\models\xgb_model.pkl")
scaler = joblib.load(r"C:\Users\Deepak Verma\OneDrive\Documents\Loan_Default_Prediction\models\preprocessing_pipeline.pkl")

# Set page config
st.set_page_config(page_title="🏦 Loan Approval Predictor", layout="centered")
st.title("🏦 Loan Approval Prediction App")

# Function to classify CIBIL score
def cibil_class(cibil_score):
    if 300 <= cibil_score < 600:
        return "Low"
    elif 601 <= cibil_score < 699:
        return "Fair"
    elif 700 <= cibil_score < 799:
        return "Good"
    else:
        return "Excellent"

# Prediction function
def predict(data):
    data_scaled = scaler.transform([data])
    pred = model.predict(data_scaled)
    return "✅ Approved" if pred[0] == 1 else "❌ Rejected"

# Interactive Form
with st.form("prediction_form"):
    st.subheader("Enter Applicant Details")

    col1, col2 = st.columns(2)
    with col1:
        no_of_dependents = st.number_input("👨‍👩‍👧‍👦 No. of Dependents", min_value=0)
        income = st.number_input("💰 Applicant Income (in Lakhs)", min_value=0)
        annual_income = income * 100000  # Convert to absolute value in currency
        loan_amount = st.number_input("💸 Loan Amount (in Lakhs)", min_value=0)
        
        # Debt-to-Income Ratio Calculation
        debt_to_income_ratio = loan_amount / annual_income if annual_income > 0 else 0
        
        cibil = st.slider("📊 CIBIL Score", 300, 900, 650)  # Default value set to 650
        
        # Classify the CIBIL score
        cibil_classification = cibil_class(cibil)
        st.write(f"📈 CIBIL Score Classification: **{cibil_classification}**")
        
        education = st.selectbox("🎓 Education", ["Graduate", "Not Graduate"])

    with col2:
        term = st.number_input("📅 Loan Term (months)", min_value=0)
        self_employed = st.selectbox("👔 Self Employed", ["Yes", "No"])
        asset_value = st.number_input("🏦 Total Assets in Lakhs", min_value=0)

    submitted = st.form_submit_button("🔍 Predict Loan Status")

if submitted:
    # Encode categorical data
    education_val = 1 if education == "Graduate" else 0
    self_employed_val = 1 if self_employed == "Yes" else 0

    # Update user_input with debt_to_income_ratio
    user_input = [
        no_of_dependents,
        education_val,
        self_employed_val,
        income,
        loan_amount,
        term,
        cibil,
        asset_value,
        debt_to_income_ratio  # Added the new feature
    ]

    prediction = predict(user_input)

    st.markdown("### 📋 Prediction Result")
    st.success(f"Loan Status: {prediction}")

    with st.expander("🔎 Review Input Details"):
        input_df = pd.DataFrame({
            "No of Dependents": [no_of_dependents],
            "Education": [education],
            "Self Employed": [self_employed],
            "Income (Lakhs)": [income],
            "Loan Amount (Lakhs)": [loan_amount],
            "Loan Term (Months)": [term],
            "CIBIL Score": [cibil],
            "Total Assets in Lakhs": [asset_value],
            "Debt to Income Ratio": [debt_to_income_ratio],  # Displaying the debt-to-income ratio
        })
        st.dataframe(input_df)
