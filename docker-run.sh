#docker run -d -p 8001:8000 -v "$(pwd)/iforest/model.pkl:/app/model.pkl" iforest-api
docker run -d -p 8002:8000 iforest-api

