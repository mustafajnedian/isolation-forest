import pickle
import pandas as pd
from sklearn.ensemble import IsolationForest

from .config import MODEL_PATH  # Import model path from config.py

# Load the trained model
def load_model():
    """Loads the Isolation Forest model from the specified path."""
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    return model

# Detect anomalies in incoming data
def detect_anomalies(data: pd.DataFrame):
    """Runs anomaly detection on input data using Isolation Forest and returns only detected anomalies."""
    model = load_model()  # Load model

    # Drop non-feature columns if they exist
    non_feature_cols = ["attack_cat", "label"]
    data = data.drop(columns=[col for col in non_feature_cols if col in data.columns], errors="ignore")

    # Ensure all categorical columns are encoded
    categorical_cols = data.select_dtypes(include=["object"]).columns
    data = pd.get_dummies(data, columns=categorical_cols)  # One-hot encoding

    # Align features with training data
    expected_features = model.feature_names_in_  # Features used during training
    for col in expected_features:
        if col not in data.columns:
            data[col] = 0  # Add missing features as 0

    data = data[expected_features]  # Ensure order matches

    predictions = model.predict(data)  # Predict anomalies

    # Convert -1 (anomaly) and 1 (normal) into human-readable format
    data["anomaly"] = ["anomaly" if pred == -1 else "normal" for pred in predictions]

    # Filter only anomalies (ensure it's a DataFrame before converting)
    anomalies = data[data["anomaly"] == "anomaly"]

    if not anomalies.empty:  # Avoid returning empty list issues
        # Select meaningful columns (Adjust based on relevance)
        selected_columns = ["proto", "sbytes", "dbytes", "rate", "sload", "dload", "smean", "dmean", "anomaly"]
        anomalies = anomalies[selected_columns]
        return anomalies.to_dict(orient="records")  # Convert DataFrame to a list of dicts
    else:
        return []  # Return an empty list if no anomalies are found

