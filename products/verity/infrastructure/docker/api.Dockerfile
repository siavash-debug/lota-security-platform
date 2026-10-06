# ==============================================================================
# LOTA Security Verity - API Gateway Dockerfile
# Production Hardened Scaffold
# NOTE: In production, pin exact SHA-256 digest: python:3.12-slim@sha256:...
# NOTE: Release images must attach CycloneDX SBOM and SLSA Cosign signature.
# ==============================================================================

FROM python:3.12-slim AS builder

WORKDIR /build

# Install build dependencies safely without curl | bash
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    rm -rf /var/lib/apt/lists/*

# Install shared library and application requirements
COPY shared/python/ /build/shared/python/
COPY products/verity/apps/api/ /build/products/verity/apps/api/

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir /build/shared/python && \
    pip install --no-cache-dir /build/products/verity/apps/api

# Final runtime image
FROM python:3.12-slim AS runtime

# Security: Create non-root user and group
RUN groupadd -g 10001 lota && \
    useradd -u 10001 -g lota -m -s /bin/false lotauser

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn
COPY products/verity/apps/api/app /app/app

# Security: Drop privileges to non-root user
USER 10001:10001

EXPOSE 8000

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
