
# Loan Approval Prediction App

This project is a machine learning application built using Python and Streamlit for predicting loan approval status based on various applicant features. The prediction model uses XGBoost and Random Forest along with standard data preprocessing. The app allows users to input applicant details and provides a prediction of whether the loan is approved or rejected.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technology Stack](#technology-stack)
4. [Setup and Installation](#setup-and-installation)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [License](#license)

---

## Project Overview

This application predicts the approval status of a loan application based on input features such as income, loan amount, CIBIL score, and other relevant details. The model was trained on a historical dataset of loan applications, and it classifies the approval status into two categories:
- **Approved** ✅
- **Rejected** ❌

### Key Features:
- **CIBIL Score Classification**: Classifies the CIBIL score into categories like "Low", "Fair", "Good", and "Excellent".
- **Debt-to-Income Ratio**: The loan amount to annual income ratio is calculated and used in prediction.
- **Interactive User Input**: Users can input applicant details via a simple and interactive form.
- **Real-time Prediction**: Once the user inputs the details, the app immediately predicts whether the loan would be approved or rejected.

---

## Features

- **Applicant Information Input**:
    - No. of dependents
    - Applicant's income
    - Loan amount
    - Loan term (months)
    - CIBIL score
    - Education (Graduate/Not Graduate)
    - Self-employed status
    - Asset values (residential, commercial, luxury, and bank)
  
- **CIBIL Score Classification**: Automatically classifies the CIBIL score into one of the categories ("Low", "Fair", "Good", "Excellent").
  
- **Debt-to-Income Ratio**: Computes the debt-to-income ratio as `loan_amount / annual_income`, which is used for loan approval prediction.

- **Machine Learning Model**: 
    - Uses XGBoost and Random Forest to predict loan approval.
    - Data scaling and preprocessing with `StandardScaler` to ensure model readiness.

---

## Technology Stack

- **Frontend**: Streamlit for interactive web app creation.
- **Backend**: Python (for data processing, prediction, and model inference).
- **Machine Learning**: XGBoost and Random Forest for predictive modeling.
- **Data Preprocessing**: StandardScaler for scaling the features.
- **Serialization**: Joblib to load and save the trained models and preprocessing pipeline.

---

## Setup and Installation

### Prerequisites

1. Python 3.7 or higher.
2. Install required libraries. You can do this by running the following command:

```bash
pip install -r requirements.txt
```

### Steps to Run

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Dverma2001/Loan-Approval-Prediction.git
cd Loan-Approval-Prediction
```

2. Install the dependencies (make sure you have Python 3.7 or later):

```bash
pip install -r requirements.txt
```

3. Once all dependencies are installed, run the Streamlit app:

```bash
streamlit run app/dashboard.py
```

4. The application will be accessible at `http://localhost:8501` in your browser.

---

## Usage

1. **Input Details**: 
   - Once the app loads, input the applicant's details in the form.
   - The form will allow you to input the number of dependents, income, loan amount, term, CIBIL score, and other details.
   
2. **Prediction**:
   - After filling out the form, click the **Predict Loan Status** button.
   - The app will display whether the loan is **Approved** or **Rejected**, along with a classification of the CIBIL score and other input details for review.

3. **Debt-to-Income Ratio**: The app calculates the debt-to-income ratio and uses it for the prediction.

---

## Project Structure

```
Loan-Approval-Prediction/
│
├── app/
│   └── dashboard.py              # Main Streamlit app renamed to dashboard.py
│
├── data/
│   ├── raw/
│   │   └── loan_approval_dataset.csv   # Raw loan approval dataset
│   └── processed/
│       └── loan_data_processed.csv     # Processed loan data
│
├── models/
│   ├── xgb_model.pkl              # Trained XGBoost model
│   ├── rf_model.pkl               # Trained Random Forest model
│
├── notebooks/
│   ├── 01_EDA.ipynb              # Exploratory Data Analysis
│   ├── 02_Preprocessing.ipynb    # Data Preprocessing
│   ├── 03_Modeling.ipynb         # Model Training (XGBoost and Random Forest)
│   ├── 04_Model_Evaluation.ipynb # Model Evaluation (Accuracy, ROC, etc.)
│   └── 05_Model_Explanability.ipynb # SHAP for model explainability
│
├── outputs/
│   ├── figures/                  # Folder for storing output figures and plots
│   └── evaluation_report.txt     # Evaluation report (model performance)
│
├── scripts/
│   ├── evaluate.py               # Script for evaluating models
│   ├── preprocess.py             # Script for preprocessing the data
│   ├── train_model.py            # Script for training models
│   └── utils.py                  # Utility functions (e.g., feature engineering)
│
├── requirements.txt              # Required libraries for the project
└── README.md                     # Project overview and instructions
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

