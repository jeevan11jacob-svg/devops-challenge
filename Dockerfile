# Stage 1: Build dependencies
FROM python:3.14-slim AS builder

WORKDIR /app

COPY requirements-prod.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements-prod.txt


# Stage 2: Production runtime
FROM python:3.14-slim

WORKDIR /app

COPY --from=builder /install /usr/local
COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
