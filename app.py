import streamlit as st
import pickle
import numpy as np

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="🏦",
    layout="wide"
)

# -----------------------------
# Load Model
# -----------------------------
model = pickle.load(open("Loan_model.pkl", "rb"))
# If your file name is loan_model.pkl, replace the above line with:
# model = pickle.load(open("loan_model.pkl", "rb"))

# -----------------------------
# Title
# -----------------------------
st.title("🏦 Loan Approval Prediction System")
st.write("Enter the applicant details below to predict loan approval.")

# -----------------------------
# Input Fields
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    no_of_dependents = st.number_input(
        "Number of Dependents",
        min_value=0,
        step=1
    )

    education = st.selectbox(
        "Education",
        ["Graduate", "Not Graduate"]
    )

    self_employed = st.selectbox(
        "Self Employed",
        ["No", "Yes"]
    )

    income_annum = st.number_input(
        "Annual Income",
        min_value=0
    )

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0
    )

with col2:
    loan_term = st.number_input(
        "Loan Term",
        min_value=1
    )

    cibil_score = st.number_input(
        "CIBIL Score",
        min_value=300,
        max_value=900
    )

    residential_assets_value = st.number_input(
        "Residential Assets Value",
        min_value=0
    )

    commercial_assets_value = st.number_input(
        "Commercial Assets Value",
        min_value=0
    )

    luxury_assets_value = st.number_input(
        "Luxury Assets Value",
        min_value=0
    )

    bank_asset_value = st.number_input(
        "Bank Asset Value",
        min_value=0
    )

# -----------------------------
# Encoding
# -----------------------------
education = 0 if education == "Graduate" else 1
self_employed = 1 if self_employed == "Yes" else 0

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Loan Status"):

    data = np.array([[
        no_of_dependents,
        education,
        self_employed,
        income_annum,
        loan_amount,
        loan_term,
        cibil_score,
        residential_assets_value,
        commercial_assets_value,
        luxury_assets_value,
        bank_asset_value
    ]])

    prediction = model.predict(data)

    st.subheader("Prediction Result")

    # Change this if your model uses opposite labels
    if prediction[0] == 0:
        st.success("✅ Loan Approved")
        st.balloons()
    else:
        st.error("❌ Loan Rejected")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("About")
st.sidebar.info(
    """
    This application predicts whether a loan is likely to be approved
    based on applicant information using a Machine Learning model.

    Developed with:
    - Python
    - Streamlit
    - Scikit-learn
    """
)