# Docker Compose Local Development Environment

This directory houses configuration templates and environment variables for running the **LOTA Security Platform** local development stack.

> [!WARNING]
> **DEVELOPMENT ONLY NOTICE**:  
> The Docker Compose setup in this repository is strictly for local developer scaffolding, integration testing, and architectural verification. It is **never** intended for staging or production deployment.  
> All credentials defined in `*.env.example` files are hardcoded placeholders for local isolated testing. In production, utilize external KMS/Vault secrets, managed PostgreSQL, enterprise object storage, and Kubernetes with mTLS.

---

## 1. Directory Structure

```text
compose/
├── README.md                  # This file
├── dev.env.example            # Master development environment template
└── services/                  # Individual service configuration templates
    ├── postgres.env.example   # PostgreSQL development configuration
    ├── redis.env.example      # Redis development configuration
    ├── minio.env.example      # MinIO object storage configuration
    └── opa.env.example        # Open Policy Agent development configuration
```

---

## 2. Usage Instructions

To launch the local development stack:

1. Copy the master environment file:
   ```bash
   cp compose/dev.env.example compose/dev.env
   ```
2. Start the services using Docker Compose:
   ```bash
   docker compose up -d
   ```
3. To view logs:
   ```bash
   docker compose logs -f
   ```
4. To shut down and remove local volumes:
   ```bash
   docker compose down -v
   ```

---

## 3. Network & Security Isolation

- All published ports are bound to `127.0.0.1` (localhost) to avoid unintentional network exposure on local LANs.
- Services communicate over an internal, unrouted Docker bridge network named `lota_dev_network`.
- Ephemeral containers run as non-root users where supported by base images.
