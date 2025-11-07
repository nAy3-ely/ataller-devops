# Dockerfile

FROM python:3.10-slim

LABEL maintainer="Nayhely Valle"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY nayhely.py .

# Ejecutar la aplicación Flask cuando el contenedor arranque
CMD ["python", "nayhely.py"]
