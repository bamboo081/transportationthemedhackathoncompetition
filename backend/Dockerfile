# backend/Dockerfile
FROM python:3.10.11-slim

# Install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code & data
COPY backend/ backend/
COPY data/ data/
COPY scenarios/ scenarios/

# Expose the FastAPI port
EXPOSE 8000

# Start the API
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]
