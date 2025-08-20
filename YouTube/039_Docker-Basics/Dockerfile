# Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
EXPOSE 8000

# Persist DB to a mounted volume /data (see docker run below)
ENV DB_PATH=/data/app.db

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
