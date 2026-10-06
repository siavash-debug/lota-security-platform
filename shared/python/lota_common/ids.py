"""Identifier generation and validation utilities for LOTA Security Platform."""

from __future__ import annotations

import re
import uuid

ID_PREFIX_MAP: dict[str, str] = {
    "asset": "asset_",
    "scan": "scan_",
    "finding": "finding_",
    "evidence": "evidence_",
    "exception": "exception_",
    "remediation": "rem_",
    "event": "evt_",
    "request": "req_",
    "correlation": "corr_",
    "user": "usr_",
}

_SAFE_ID_REGEX = re.compile(r"^[a-z]+_[0-9a-zA-Z]{16,64}$")


def generate_id(entity_type: str) -> str:
    """Generate a typed, prefixed unique identifier.

    Args:
        entity_type: The domain entity type (e.g. 'asset', 'scan', 'finding').

    Returns:
        A unique string formatted as '<prefix><hex_token>'.
    """
    prefix = ID_PREFIX_MAP.get(entity_type, f"{entity_type}_")
    # 24 characters of hex from uuid4 (12 random bytes)
    unique_suffix = uuid.uuid4().hex[:24]
    return f"{prefix}{unique_suffix}"


def generate_request_id() -> str:
    """Generate a standard request tracking identifier."""
    return generate_id("request")


def generate_correlation_id() -> str:
    """Generate a standard cross-service correlation identifier."""
    return generate_id("correlation")


def validate_id(identifier: str, expected_type: str | None = None) -> bool:
    """Validate that an identifier matches safe syntactic conventions.

    Args:
        identifier: The ID string to test.
        expected_type: Optional entity type to enforce prefix match.

    Returns:
        True if valid, False otherwise.
    """
    if not isinstance(identifier, str):
        return False
    if not _SAFE_ID_REGEX.match(identifier):
        return False
    if expected_type:
        expected_prefix = ID_PREFIX_MAP.get(expected_type, f"{expected_type}_")
        return identifier.startswith(expected_prefix)
    return True
