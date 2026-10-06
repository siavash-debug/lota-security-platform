# Platform Security Principles

The **LOTA Security Platform** adheres to ten non-negotiable security principles across all product architectures and code implementations:

---

## 1. Core Principles

1. **Read-Only by Default**: Repository inspection, metadata collection, static analysis, and vulnerability correlation must not alter target repositories, deployments, or external environments.
2. **No Blind Code Execution**: Source code, build scripts, Dockerfiles, setup scripts, and downloaded artifacts must never execute on the control plane or developer workstations.
3. **Sandbox-First Execution**: Any build simulation or dynamic telemetry observation must execute solely inside disposable, isolated worker containers or microVMs.
4. **Approval-Gated High-Risk Actions**: Any action modifying infrastructure, access, secrets, network rules, policies, or production configurations requires explicit, authenticated human approval.
5. **Evidence-First Findings**: Every finding must contain verifiable, immutable evidence—including file paths, line ranges, AST nodes, configuration keys, API responses, scanner outputs, or artifact hashes.
6. **Immutable Asset Identity**: All analysis results must be anchored to an immutable reference: a Git commit SHA, container image digest, artifact SHA-256 hash, or SBOM digest.
7. **Least Privilege**: Every connector, worker process, service account, API token, and integration must possess only the minimum permissions necessary for its discrete function.
8. **Default-Deny Networking**: Sandboxes and analysis workers must have zero outbound network access unless specific, verified destinations are explicitly authorized.
9. **Zero Secrets in Logs**: Structured logs, error traces, and reporting payloads must sanitize and redact credentials, tokens, and authorization headers.
10. **Comprehensive Auditability**: Every critical platform operation (asset ingestion, scan initiation, scanner execution, policy evaluation, exception approval, remediation execution, rollback) must generate an immutable, tamper-evident audit log event.
