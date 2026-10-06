# LOTA Security Verity - API Contract

> **Authoritative Specification Reference**: Section 16 ("API Requirements") of [`source-of-truth.md`](file:///docs/products/verity/source-of-truth.md).

---

## 1. General Principles

- **Base URL**: `/v1`
- **Transport**: HTTPS (TLS 1.3 mandatory in production)
- **Content-Type**: `application/json`
- **Mandatory Headers**:
  - `Authorization`: `Bearer <OIDC_TOKEN>`
  - `X-Request-ID`: Client-provided or gateway-assigned UUIDv7/prefixed string (`req_...`)
  - `Idempotency-Key`: Required on state-changing requests (`POST`, `PUT`, `DELETE`)
- **Audit Mandate**: All mutating operations generate an immutable audit log record.

---

## 2. API Endpoints

### 2.1 System Health & Diagnostics

#### `GET /health`
Returns service operational health.
- **Response**: `200 OK`
  ```json
  {
    "status": "ok",
    "service": "verity-api",
    "environment": "development"
  }
  ```

#### `GET /ready`
Returns service readiness.
- **Response**: `200 OK`
  ```json
  {
    "ready": true,
    "checks": {
      "database": "connected",
      "redis": "connected"
    }
  }
  ```

#### `GET /v1/version`
Returns semantic version and build metadata.
- **Response**: `200 OK`
  ```json
  {
    "app_name": "LOTA Security Verity",
    "version": "0.1.0",
    "build": "development-scaffold",
    "revision": "initial-commit"
  }
  ```

---

### 2.2 Core Product Endpoints

#### `POST /v1/assets/git`
Registers a Git repository asset and resolves its immutable commit SHA.
- **Request Body**:
  ```json
  {
    "repository_url": "https://github.com/example/project",
    "ref": "main",
    "analysis_profile": "standard-static",
    "owner_team": "security-engineering"
  }
  ```
- **Response**: `201 Created` (in initial scaffold: `501 Not Implemented`)
  ```json
  {
    "asset_id": "asset_01H...",
    "resolved_commit_sha": "abc1234567890abcdef...",
    "status": "snapshot_resolved"
  }
  ```

#### `POST /v1/scans`
Initiates a new posture assessment scan on a registered asset.
- **Request Body**:
  ```json
  {
    "asset_id": "asset_01H...",
    "analysis_level": "L1_STATIC",
    "policy_bundle_version": "latest-approved"
  }
  ```
- **Response**: `202 Accepted` (in initial scaffold: `501 Not Implemented`)
  ```json
  {
    "scan_id": "scan_01H...",
    "asset_id": "asset_01H...",
    "status": "QUEUED",
    "created_at": "2026-10-05T00:00:00Z"
  }
  ```

#### `GET /v1/scans/{scan_id}`
Retrieves current scan progress, status, and summary metrics.
- **Response**: `200 OK` (in initial scaffold: `501 Not Implemented`)
  ```json
  {
    "scan_id": "scan_01H...",
    "asset_id": "asset_01H...",
    "status": "SUCCEEDED",
    "analysis_level": "L1_STATIC",
    "started_at": "2026-10-05T00:00:00Z",
    "ended_at": "2026-10-05T00:05:00Z"
  }
  ```

#### `GET /v1/findings`
Lists security posture findings with optional filtering.
- **Query Parameters**: `asset_id`, `scan_id`, `severity`, `status`
- **Response**: `200 OK` (in initial scaffold: `501 Not Implemented`)
  ```json
  {
    "items": [],
    "total": 0
  }
  ```

#### `POST /v1/exceptions`
Submits a temporary policy exception request.
- **Request Body**:
  ```json
  {
    "control_id": "CONTAINER-PRIV-001",
    "asset_scope": "asset_01H...",
    "justification": "Legacy component undergoing migration.",
    "compensating_controls": ["Network isolation", "No host mounts"],
    "expires_at": "2026-11-05T00:00:00Z"
  }
  ```
- **Response**: `201 Created` (in initial scaffold: `501 Not Implemented`)

#### `POST /v1/remediations/{remediation_id}/approve`
Records human authorization to execute a proposed remediation action.
- **Request Body**:
  ```json
  {
    "reason": "Change reviewed and approved for sprint maintenance window."
  }
  ```
- **Response**: `200 OK` (in initial scaffold: `501 Not Implemented`)
