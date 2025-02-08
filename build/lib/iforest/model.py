import pickle
import pandas as pd
from sklearn.ensemble import IsolationForest
from .config import MODEL_PATH

def load_model():
    """Load the Isolation Forest model from file."""
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

def detect_anomalies(df: pd.DataFrame):
    """Detect anomalies using the Isolation Forest model."""
    model = load_model()
    df["Anomaly"] = model.predict(df) == -1
    return df[df["Anomaly"]]
