import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Customer Retention Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Load Trained Model
# -----------------------------
from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "artifacts" / "final_model.pkl"

print("Model Path:", MODEL_PATH)
print("Exists:", MODEL_PATH.exists())

model = joblib.load(MODEL_PATH)

# -----------------------------
# Title
# -----------------------------
st.title("📊 Customer Retention Intelligence Platform")

st.write(
    "Predict whether a telecom customer is likely to churn based on customer information."
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("About")

st.sidebar.info(
    """
    Customer Retention Intelligence Platform

    This application predicts whether a telecom customer is likely to churn using a trained Machine Learning model.
    """
)

# -----------------------------
# Input Form
# -----------------------------
col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    senior = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        max_value=100,
        value=12
    )

    phone = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple = st.selectbox(
        "Multiple Lines",
        ["No", "Yes", "No phone service"]
    )

    internet = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )

with col2:

    device_protection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )

    contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    paperless = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    payment = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=500.0
    )

# -----------------------------
# Predict Button
# -----------------------------
if st.button("Predict Churn"):

    # Binary Mapping
    binary_mapping = {
        "gender": {"Male": 1, "Female": 0},
        "Partner": {"Yes": 1, "No": 0},
        "Dependents": {"Yes": 1, "No": 0},
        "PhoneService": {"Yes": 1, "No": 0},
        "PaperlessBilling": {"Yes": 1, "No": 0}
    }

    # Create DataFrame
    new_customer = pd.DataFrame({
        "gender": [gender],
        "SeniorCitizen": [senior],
        "Partner": [partner],
        "Dependents": [dependents],
        "tenure": [tenure],
        "PhoneService": [phone],
        "MultipleLines": [multiple],
        "InternetService": [internet],
        "OnlineSecurity": [online_security],
        "OnlineBackup": [online_backup],
        "DeviceProtection": [device_protection],
        "TechSupport": [tech_support],
        "StreamingTV": [streaming_tv],
        "StreamingMovies": [streaming_movies],
        "Contract": [contract],
        "PaperlessBilling": [paperless],
        "PaymentMethod": [payment],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges]
    })

    # Apply Binary Mapping
    for column, mapping in binary_mapping.items():
        new_customer[column] = new_customer[column].map(mapping)

    # Prediction
    prediction = model.predict(new_customer)[0]
    probability = model.predict_proba(new_customer)[0][1]

    # Display Result
    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Customer is likely to Churn.")
    else:
        st.success("✅ Customer is not likely to Churn.")

    st.metric(
        label="Churn Probability",
        value=f"{probability:.2%}"
    )

    st.markdown("---")
    st.caption(
    "Developed by Satya Kiran | Customer Retention Intelligence Platform"
)