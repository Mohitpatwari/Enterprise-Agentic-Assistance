FROM python:3.11-slim-bookworm

# Patch OS-level CVEs, then install system deps
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    gcc g++ libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Create a non-root user for Hugging Face security requirements
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# Copy requirements and install to user space
COPY --chown=user:user requirements-prod.txt .
RUN pip install --no-cache-dir --prefer-binary --user -r requirements-prod.txt

# Copy the app package
COPY --chown=user:user app/ ./app/

# Hugging Face Spaces require port 7860
EXPOSE 7860

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]