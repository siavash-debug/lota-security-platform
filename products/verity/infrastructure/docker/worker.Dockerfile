# ==============================================================================
# LOTA Security Verity - Scan Worker Dockerfile
# Production Hardened Worker Scaffold
# NOTE: In production, pin exact SHA-256 digest: python:3.12-slim@sha256:...
# NOTE: Release images must attach CycloneDX SBOM and SLSA Cosign signature.
# ==============================================================================

FROM python:3.12-slim AS builder

WORKDIR /build

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    rm -rf /var/lib/apt/lists/*

COPY shared/python/ /build/shared/python/
COPY products/verity/apps/worker/ /build/products/verity/apps/worker/

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir /build/shared/python && \
    pip install --no-cache-dir /build/products/verity/apps/worker

FROM python:3.12-slim AS runtime

RUN groupadd -g 10001 lota && \
    useradd -u 10001 -g lota -m -s /bin/false lotauser

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY products/verity/apps/worker/worker /app/worker

# Security: Worker operates under strict non-root user
USER 10001:10001

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

CMD ["python", "-m", "worker.main"]
