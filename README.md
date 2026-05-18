# Loan Approval Prediction using Machine Learning

## Project Overview
This project predicts whether a loan application will be approved or rejected based on applicant financial and personal information.

The main objective of this project is to automate the loan approval process using machine learning algorithms and help financial institutions make faster decisions.

---

## Dataset
Dataset Source: Kaggle

The dataset contains applicant details such as:

- Income
- Loan Amount
- CIBIL Score
- Education
- Self Employment Status
- Residential Assets Value
- Commercial Assets Value
- Luxury Assets Value
- Bank Asset Value
- Loan Status (Target Variable)

---

## Problem Statement
Banks receive a large number of loan applications every day. Manually verifying each application can be time-consuming.

This project builds a machine learning classification model to predict whether a loan application will be approved or rejected.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

## Project Workflow

### 1. Data Collection
- Imported dataset from Kaggle

### 2. Data Cleaning
- Removed unnecessary columns
- Handled extra spaces in column names
- Checked missing values
- Checked duplicate records

### 3. Exploratory Data Analysis (EDA)
Performed visualizations using:

### Count Plot
![Loan Status](images/Loan%20Status.png)

### Histogram
![Income distribution](images/Incoms%20distribution.png)

### Box Plot
![CIBIL Score](images/Cibil%20Score.png)

### Correlation Heatmap
![Correlations](images/Heatmap.png)

### 4. Data Preprocessing
- Applied Label Encoding
- Feature selection
- Train-test split
- Feature scaling for Logistic Regression

### 5. Model Building
Trained multiple machine learning models:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

### 6. Model Evaluation
Evaluated models using:
- Accuracy Score
- Classification Report
- Confusion Matrix
 ![Confusion Matrix](images/Confusion%20Matrix.png)

### 7. Feature Importance
Identified the most important factors affecting loan approval.

- important features
 ![Important Features](images/Important%20Features.png)
---

## Model Performance

| Model | Accuracy |
|--------|------------|
| Logistic Regression | 79% |
| Decision Tree | 97% |
| Random Forest | 97% |

---

## Key Insights
- Applicants with higher CIBIL scores had better chances of loan approval.
- Income plays an important role in loan approval decisions.
- Loan amount and asset values also impact approval results.
- Random Forest performed best among all models.

---

## Conclusion
This project shows how machine learning can improve loan approval prediction and reduce manual effort in the banking sector.

---

## Future Improvements
- Hyperparameter tuning
- Model deployment using Streamlit
- Use larger datasets
- Improve model accuracy

---

## Author
**Bunty Saini**