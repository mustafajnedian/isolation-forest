from fastapi import FastAPI, UploadFile, File
import pandas as pd
import io
from .model import detect_anomalies

def create_app():
    """Create FastAPI app."""
    app = FastAPI()

    @app.post("/detect/")
    async def detect(file: UploadFile = File(...)):
        df = pd.read_csv(io.StringIO(await file.read().decode()))
        anomalies = detect_anomalies(df)
        return anomalies.to_dict(orient="records")  # Return JSON

    return app
