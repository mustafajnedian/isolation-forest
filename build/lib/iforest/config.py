import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

MODEL_PATH = os.getenv("MODEL_PATH")
LOG_LEVEL = os.getenv("LOG_LEVEL")

if not MODEL_PATH:
    raise ValueError("MODEL_PATH is not set. Please define it in the environment variables or .env file.")
