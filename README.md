# 🏦 Credit Scoring Prediction App

A full machine learning application built with Python and Streamlit to predict an individual's creditworthiness based on financial and behavioral features.

---

## 📌 Project Overview

This app uses a trained **Random Forest Classifier** to determine whether an applicant is **creditworthy** or not, based on multiple input parameters like income, debt, credit history, etc. The application is designed to be simple, interactive, and easy to deploy.

---

## 📁 Project Structure

Credit_Scoring_App/
├── app/
│ └── app.py # Streamlit frontend
├── data/
│ └── credit_score.csv # Dataset (2000 rows)
├── models/
│ └── credit_model.pkl # Trained ML model
├── train_model.py # Model training script
├── requirements.txt # Project dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## 📊 Features Used for Prediction

- **Income** — Annual income in INR
- **Debt** — Current total debt
- **Payment_History** — Score representing historical payment reliability (0–1)
- **Late_Payments** — Number of late payments
- **Credit_Utilization** — Ratio of credit used to total credit limit (0–1)
- **Credit_Inquiries** — Recent credit inquiries (last 6 months)
- **Credit_History_Years** — Total years of credit history

---

## ⚙️ How It Works

1. `train_model.py` loads and trains a Random Forest classifier.
2. The trained model is saved to `models/credit_model.pkl`.
3. `app.py` is a Streamlit-based UI that allows users to enter input features.
4. The app loads the model, makes a prediction, and shows the result.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/credit-scoring-app.git
cd credit-scoring-app
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Train the Model
bash
Copy
Edit
python train_model.py
4. Run the Streamlit App
bash
Copy
Edit
streamlit run app/app.py
✅ Output Example
Input	Prediction
Income = ₹50,000	Creditworthy ✅
Late Payments = 5	Not Creditworthy ❌

🧠 Future Improvements
Add confusion matrix & performance metrics

Integrate with database to log user predictions

Add login authentication and user history

Deploy via Streamlit Cloud or Render

📌 Requirements
Python 3.10+

Streamlit

scikit-learn

pandas

numpy

