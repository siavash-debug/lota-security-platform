# Platform Identity & Access Management

This subsystem manages authentication, authorization, and tenant identity across the **LOTA Security Platform**.

---

## 1. Capabilities

- **OIDC / SAML Federation**: Centralized authentication against enterprise IdPs (Okta, Keycloak, Entra ID).
- **MFA Enforcement**: Mandatory Multi-Factor Authentication for privileged roles (Remediation Approvers, Platform Admins).
- **Role-Based Access Control (RBAC)**: Fine-grained permissions matrix mapped to standard roles (`Viewer`, `Analyst`, `AssetOwner`, `SecurityApprover`, `PlatformAdmin`).
- **Short-Lived Tokens**: JWT access tokens limited to 15-minute expirations with refresh token rotation.
