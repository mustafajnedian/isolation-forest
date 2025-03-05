import pandas as pd
import pickle
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
from iforest.config import MODEL_PATH  # Use the same path as in model.py

# Define dataset path
DATA_PATH = "~/unsw-nb15/UNSW_NB15_training-set.csv"  # Update if needed

# Load the dataset
df = pd.read_csv(DATA_PATH)

# Encode categorical features (convert text to numbers)
for col in df.select_dtypes(include=["object"]).columns:
    df[col] = LabelEncoder().fit_transform(df[col])

# Drop unnecessary columns (e.g., attack labels)
X_train = df.drop(columns=["attack_cat", "label"], errors="ignore")

# Fill missing values (if any)
X_train = X_train.fillna(X_train.median())

# Train Isolation Forest model
model = IsolationForest(n_estimators=100, contamination="auto", random_state=42)
model.fit(X_train)

# Save trained model
with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)

print(f"Model trained and saved as {MODEL_PATH}")

