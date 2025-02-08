# Use official Python image as base
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files
COPY iforest iforest
# Copy model.pkl to the appropriate directory inside the container
COPY iforest/model.pkl /app/model.pkl
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for FastAPI
EXPOSE 8000

# Command to run the API
CMD ["uvicorn", "iforest.api:app", "--host", "0.0.0.0", "--port", "8000"]

