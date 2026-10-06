"""Health, diagnostics, and safe placeholder endpoints for Verity API Gateway."""

from __future__ import annotations

from typing import Any
from fastapi import APIRouter, Query, Request, status
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.core.security import extract_request_id
from app.domain import (
    ExceptionCreateRequest,
    GitAssetCreateRequest,
    HealthResponse,
    NotImplementedResponse,
    ReadyResponse,
    RemediationApproveRequest,
    ScanCreateRequest,
    VersionResponse,
)

router = APIRouter()


@router.get("/health", response_model=HealthResponse, tags=["Diagnostics"])
async def get_health() -> HealthResponse:
    """Operational health check endpoint."""
    return HealthResponse(
        status="ok",
        service=settings.service_name,
        environment=settings.environment,
    )


@router.get("/ready", response_model=ReadyResponse, tags=["Diagnostics"])
async def get_ready() -> ReadyResponse:
    """Service readiness probe endpoint."""
    return ReadyResponse(
        ready=True,
        checks={
            "database": "placeholder_ready",
            "redis": "placeholder_ready",
            "opa": "placeholder_ready",
        },
    )


@router.get("/v1/version", response_model=VersionResponse, tags=["Diagnostics"])
async def get_version() -> VersionResponse:
    """Returns application name, semantic version, and build info."""
    return VersionResponse(
        app_name=settings.app_name,
        version=settings.version,
        build=settings.build,
        revision=settings.revision,
    )


@router.post(
    "/v1/assets/git",
    response_model=NotImplementedResponse,
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
    tags=["Assets"],
)
async def create_git_asset(
    payload: GitAssetCreateRequest,
    request: Request,
) -> JSONResponse:
    """Safe placeholder: validates input schema and returns 501 Not Implemented."""
    req_id = extract_request_id(request)
    body = NotImplementedResponse(
        error_code="NOT_IMPLEMENTED",
        message="Asset ingestion pipeline has not been implemented in this scaffold release.",
        service=settings.service_name,
        request_id=req_id,
        details={"validated_ref": payload.ref, "validated_owner": payload.owner_team},
    )
    return JSONResponse(status_code=status.HTTP_501_NOT_IMPLEMENTED, content=body.model_dump())


@router.post(
    "/v1/scans",
    response_model=NotImplementedResponse,
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
    tags=["Scans"],
)
async def create_scan(
    payload: ScanCreateRequest,
    request: Request,
) -> JSONResponse:
    """Safe placeholder: validates scan input and returns 501 Not Implemented."""
    req_id = extract_request_id(request)
    body = NotImplementedResponse(
        error_code="NOT_IMPLEMENTED",
        message="Scan execution engine has not been implemented in this scaffold release.",
        service=settings.service_name,
        request_id=req_id,
        details={"validated_asset_id": payload.asset_id},
    )
    return JSONResponse(status_code=status.HTTP_501_NOT_IMPLEMENTED, content=body.model_dump())


@router.get(
    "/v1/scans/{scan_id}",
    response_model=NotImplementedResponse,
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
    tags=["Scans"],
)
async def get_scan_status(
    scan_id: str,
    request: Request,
) -> JSONResponse:
    """Safe placeholder: returns 501 Not Implemented."""
    req_id = extract_request_id(request)
    body = NotImplementedResponse(
        error_code="NOT_IMPLEMENTED",
        message="Scan status lookup has not been implemented in this scaffold release.",
        service=settings.service_name,
        request_id=req_id,
        details={"scan_id": scan_id},
    )
    return JSONResponse(status_code=status.HTTP_501_NOT_IMPLEMENTED, content=body.model_dump())


@router.get(
    "/v1/findings",
    response_model=NotImplementedResponse,
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
    tags=["Findings"],
)
async def get_findings(
    request: Request,
    asset_id: str | None = Query(default=None),
    severity: str | None = Query(default=None),
) -> JSONResponse:
    """Safe placeholder: returns 501 Not Implemented."""
    req_id = extract_request_id(request)
    body = NotImplementedResponse(
        error_code="NOT_IMPLEMENTED",
        message="Findings query service has not been implemented in this scaffold release.",
        service=settings.service_name,
        request_id=req_id,
        details={"asset_id": asset_id, "severity": severity},
    )
    return JSONResponse(status_code=status.HTTP_501_NOT_IMPLEMENTED, content=body.model_dump())


@router.post(
    "/v1/exceptions",
    response_model=NotImplementedResponse,
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
    tags=["Exceptions"],
)
async def request_exception(
    payload: ExceptionCreateRequest,
    request: Request,
) -> JSONResponse:
    """Safe placeholder: returns 501 Not Implemented."""
    req_id = extract_request_id(request)
    body = NotImplementedResponse(
        error_code="NOT_IMPLEMENTED",
        message="Policy exception workflow has not been implemented in this scaffold release.",
        service=settings.service_name,
        request_id=req_id,
        details={"control_id": payload.control_id, "asset_scope": payload.asset_scope},
    )
    return JSONResponse(status_code=status.HTTP_501_NOT_IMPLEMENTED, content=body.model_dump())


@router.post(
    "/v1/remediations/{remediation_id}/approve",
    response_model=NotImplementedResponse,
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
    tags=["Remediation"],
)
async def approve_remediation(
    remediation_id: str,
    payload: RemediationApproveRequest,
    request: Request,
) -> JSONResponse:
    """Safe placeholder: returns 501 Not Implemented."""
    req_id = extract_request_id(request)
    body = NotImplementedResponse(
        error_code="NOT_IMPLEMENTED",
        message="Remediation approval gate has not been implemented in this scaffold release.",
        service=settings.service_name,
        request_id=req_id,
        details={"remediation_id": remediation_id},
    )
    return JSONResponse(status_code=status.HTTP_501_NOT_IMPLEMENTED, content=body.model_dump())
