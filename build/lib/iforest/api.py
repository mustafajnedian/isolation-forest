from fastapi import FastAPI, UploadFile, File
import pandas as pd
import io
from .model import detect_anomalies

def create_app():
    """Create FastAPI app."""
    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"message": "Isolation Forest API is running"}

    @app.post("/detect/")
    async def detect(file: UploadFile = File(...)):
        df = pd.read_csv(io.StringIO((await file.read()).decode("utf-8")))
        print(df.dtypes)
        print(df.head())
        anomalies = detect_anomalies(df)
        #return anomalies.to_dict(orient="records")
        return anomalies

    return app

app = create_app()  # Ensure the app instance is created

