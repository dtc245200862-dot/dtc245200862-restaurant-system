FROM python:3.12-alpine

# Cài đặt thư viện hệ thống cần thiết cho PostgreSQL client
RUN apk add --no-cache libpq

WORKDIR /app

# Tạo non-root user (Hardening: non-root container)
RUN addgroup -g 1001 appgroup && \
    adduser -u 1001 -G appgroup -s /bin/sh -D appuser

COPY requirements.txt .
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps

COPY . .
RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
