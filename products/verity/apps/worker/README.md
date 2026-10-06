# LOTA Security Verity - Scan Worker Scaffold

This directory houses the execution runtime for **LOTA Security Verity** scan workers.

---

## 1. Intended Future Responsibilities

- **Job Ingestion**: Poll tasks from the Redis queue dispatch broker.
- **Repository Checkout**: Isolated clone of Git repositories at a pinned commit SHA using `--no-checkout` / disabled hooks.
- **Scanner Execution**: Run containerized scanning tools (Trivy, Semgrep, Gitleaks, Syft) against isolated workspaces.
- **Normalization**: Transform scanner JSON results into unified domain models.
- **Evidence Packaging**: Hash, encrypt, and upload evidence artifacts to object storage.

---

## 2. Security Boundaries & Invariants

- **Disposable Lifecycles**: Workers run as ephemeral processes destroyed upon task completion.
- **Non-Root Execution**: Runs strictly as an unprivileged user (`UID 10001`).
- **No Docker Socket**: Workers **never** mount or access `/var/run/docker.sock`.
- **Egress Deny by Default**: Network namespaces prohibit unapproved outbound network traffic.
- **Read-Only Root**: Container root filesystem is mounted read-only.
- **Zero Raw Secrets**: Credentials are redacted from all logs and output streams.

---

## 3. Scaffolding Mode Notice

In this initial commit, the worker:
- Starts safely and logs operational readiness.
- Does **not** poll or execute queue jobs.
- Does **not** invoke shell commands or external tools.
- Does **not** clone or download remote repositories.
