# 📊 Customer Retention Intelligence Platform

An end-to-end Machine Learning project that predicts customer churn using classification algorithms. The project includes data preprocessing, model training, experiment tracking with MLflow, and deployment through a Streamlit web application.

---

## 📌 Business Problem

Customer churn is one of the major challenges faced by telecom companies. Acquiring new customers is significantly more expensive than retaining existing ones. Identifying customers who are likely to leave enables businesses to take proactive retention measures.

This project predicts whether a customer is likely to churn based on demographic information, account details, and subscribed services, enabling businesses to make informed customer retention decisions.

---

## 🎯 Project Objectives

- Perform exploratory data analysis on telecom customer data.
- Preprocess and transform data for machine learning.
- Train and compare multiple classification models.
- Optimize model performance using hyperparameter tuning.
- Track experiments using MLflow.
- Save the trained model for deployment.
- Build an interactive Streamlit application for real-time churn prediction.

---

## 📂 Dataset

**Dataset:** Telco Customer Churn Dataset

The dataset contains customer demographic information, account details, subscribed services, billing information, and churn status.

**Target Variable**

- Churn
  - Yes
  - No

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- MLflow
- Joblib
- Streamlit
- Git & GitHub

---

## ⚙️ Project Workflow

```text
Business Understanding
        ↓
Exploratory Data Analysis
        ↓
Data Preprocessing
        ↓
Feature Engineering
        ↓
Model Training
        ↓
Model Comparison
        ↓
Hyperparameter Tuning
        ↓
Model Saving
        ↓
MLflow Experiment Tracking
        ↓
Streamlit Deployment
```

---

## 🤖 Machine Learning Models

The following machine learning models were trained and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- XGBoost Classifier

---

## 🏆 Best Model Performance

After comparing multiple models, **Logistic Regression** provided the best balance between performance and generalization.

| Metric | Score |
|---------|-------|
| Accuracy | **80.55%** |
| Precision | **65.72%** |
| Recall | **55.88%** |
| F1 Score | **60.40%** |
| ROC-AUC | **84.20%** |

---

## 📋 Features Used

The model uses the following customer attributes:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges

---

## 🚀 Streamlit Application

The web application allows users to:

- Enter customer information.
- Predict whether a customer is likely to churn.
- View churn probability.
- Receive an easy-to-understand prediction result instantly.

---

## 📸 Application Preview

### Home Page

> *(Add screenshot here)*

```markdown
![Home Page](images/home_page.png)
```

### Prediction Result

> *(Add screenshot here)*

```markdown
![Prediction Result](images/prediction_result.png)
```

---

## 📁 Project Structure

```text
Customer-Retention-Intelligence-Platform/
│
├── app/
│   └── app.py
│
├── artifacts/
│   ├── final_model.pkl
│   ├── preprocessor.pkl
│   └── data_split.pkl
│
├── data/
│
├── notebook/
│
├── images/
│   ├── home_page.png
│   └── prediction_result.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚡ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/Customer-Retention-Intelligence-Platform.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run app/app.py
```

---

## 🔮 Future Improvements

- Deploy the application on Streamlit Cloud.
- Add SHAP explainability for model predictions.
- Develop a REST API using FastAPI.
- Implement automated model retraining using MLOps pipelines.
- Integrate real-time prediction with cloud deployment.

---

## 👩‍💻 Author

**Satya Kiran**

Aspiring Data Scientist | Machine Learning Enthusiast

- GitHub: *(Add your GitHub profile link)*
- LinkedIn: *(Add your LinkedIn profile link)*

---

## ⭐ If you found this project helpful, consider giving it a star!