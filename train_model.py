import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
df = pd.read_csv('data\Credit_Score_1.csv')
df.columns = df.columns.str.strip()

# Display available columns
print("Available columns:", df.columns.tolist())

# Check for required target column
if 'Creditworthy' not in df.columns:
    raise KeyError("The column 'Creditworthy' is missing from the dataset.")

# Convert target label to numeric (if it's in string format)
if df['Creditworthy'].dtype == 'object':
    df['Creditworthy'] = df['Creditworthy'].map({'Good': 1, 'Bad': 0})

# Features and target
X = df.drop("Creditworthy", axis=1)
y = df["Creditworthy"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save model
os.makedirs("models", exist_ok=True)
with open("models/credit_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model training complete and saved to models/credit_model.pkl")
