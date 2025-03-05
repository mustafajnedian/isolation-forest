import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

#MODEL_PATH = os.getenv("MODEL_PATH", "model.pkl")  # Default to local file if env var is missing
#MODEL_PATH = "/app/model.pkl"
MODEL_PATH = "./iforest/model.pkl"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

