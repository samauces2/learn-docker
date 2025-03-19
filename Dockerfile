# Etapa 1: Construcción
FROM python:3.10 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 2: Imagen final optimizada
FROM python:3.10
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
