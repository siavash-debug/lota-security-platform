# Local Development Guide

This guide describes how to configure, develop, and test components within the **LOTA Security Platform** monorepo.

---

## 1. Prerequisites

Before developing locally, ensure you have installed:
- Python 3.12+
- Node.js 20+ LTS
- Docker Engine 24+ and Docker Compose V2
- GNU Make

---

## 2. Environment Setup

1. Copy the root environment templates:
   ```bash
   cp .env.example .env
   cp compose/dev.env.example compose/dev.env
   ```
2. Run the bootstrap script:
   ```bash
   make bootstrap
   ```

---

## 3. Running Services

Start the development backing services (PostgreSQL, Redis, MinIO, OPA, and Verity API):
```bash
make up
```

Verify service status:
```bash
curl http://localhost:8000/health
```

Stop services:
```bash
make down
```

---

## 4. Quality Checks

Always run quality and hygiene checks prior to committing:
```bash
make lint
make test
make policy-test
make contracts-validate
```
