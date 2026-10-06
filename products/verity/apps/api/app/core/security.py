"""Security and header processing utilities for LOTA Security Verity API."""

from __future__ import annotations

from typing import Any
from fastapi import Request
from lota_common.ids import generate_request_id


def extract_request_id(request: Request) -> str:
    """Extract incoming X-Request-ID or generate a new tracking ID."""
    req_id = request.headers.get("X-Request-ID")
    if req_id and len(req_id) <= 128:
        return req_id
    return generate_request_id()


def get_current_user_placeholder(request: Request) -> dict[str, Any]:
    """Placeholder identity extractor for initial scaffolding mode.

    NOTE: In production, this verifies OIDC Bearer tokens and extracts claims.
    """
    return {
        "user_id": "usr_dev_scaffold",
        "role": "analyst",
        "tenant_id": "tenant_default",
    }
