# Stage 1 - Build
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2 - Production
FROM python:3.11-slim

WORKDIR /app

# Create non-root user - security best practice
RUN addgroup --system appgroup && \
    adduser --system --ingroup appgroup appuser

# Copy dependencies from builder
COPY --from=builder /root/.local /home/appuser/.local

# Copy app code
COPY app.py .

# Set ownership
RUN chown -R appuser:appgroup /app

# Switch to non-root user
USER appuser

# Environment variables
ENV APP_VERSION=1.0.0
ENV APP_ENV=production
ENV PATH=/home/appuser/.local/bin:$PATH

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]