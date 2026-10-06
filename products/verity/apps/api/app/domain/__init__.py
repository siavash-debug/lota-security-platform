"""Domain Pydantic models for Verity API request and response contracts."""

from __future__ import annotations

from typing import Any
from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class HealthResponse(BaseModel):
    """Payload for GET /health."""

    status: str = "ok"
    service: str = "verity-api"
    environment: str

    model_config = ConfigDict(extra="forbid")


class ReadyResponse(BaseModel):
    """Payload for GET /ready."""

    ready: bool = True
    checks: dict[str, str] = Field(default_factory=dict)

    model_config = ConfigDict(extra="forbid")


class VersionResponse(BaseModel):
    """Payload for GET /v1/version."""

    app_name: str
    version: str
    build: str
    revision: str

    model_config = ConfigDict(extra="forbid")


class GitAssetCreateRequest(BaseModel):
    """Payload for POST /v1/assets/git."""

    repository_url: HttpUrl
    ref: str = Field(min_length=1, max_length=128, default="main")
    analysis_profile: str = Field(default="standard-static")
    owner_team: str = Field(min_length=1, max_length=128)

    model_config = ConfigDict(extra="forbid")


class ScanCreateRequest(BaseModel):
    """Payload for POST /v1/scans."""

    asset_id: str = Field(pattern=r"^asset_[0-9a-zA-Z]+$")
    analysis_level: str = Field(default="L1_STATIC")
    policy_bundle_version: str = Field(default="latest-approved")

    model_config = ConfigDict(extra="forbid")


class ExceptionCreateRequest(BaseModel):
    """Payload for POST /v1/exceptions."""

    control_id: str = Field(min_length=1, max_length=64)
    asset_scope: str = Field(min_length=1, max_length=128)
    justification: str = Field(min_length=1, max_length=1000)
    compensating_controls: list[str] = Field(default_factory=list)
    expires_at: str | None = None

    model_config = ConfigDict(extra="forbid")


class RemediationApproveRequest(BaseModel):
    """Payload for POST /v1/remediations/{remediation_id}/approve."""

    reason: str = Field(min_length=1, max_length=500)

    model_config = ConfigDict(extra="forbid")


class NotImplementedResponse(BaseModel):
    """Structured response for scaffolded placeholder endpoints."""

    error_code: str = "NOT_IMPLEMENTED"
    message: str
    service: str = "verity-api"
    request_id: str | None = None
    details: dict[str, Any] = Field(default_factory=dict)

    model_config = ConfigDict(extra="forbid")
