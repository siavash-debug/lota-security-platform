"""Unit tests for Verity API health, readiness, version, and placeholder endpoints."""

from __future__ import annotations

import sys
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint() -> None:
    """Verify GET /health returns 200 OK with status and service."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "verity-api"
    assert "environment" in data


def test_readiness_endpoint() -> None:
    """Verify GET /ready returns 200 OK with ready boolean."""
    response = client.get("/ready")
    assert response.status_code == 200
    data = response.json()
    assert data["ready"] is True
    assert "checks" in data


def test_version_endpoint() -> None:
    """Verify GET /v1/version returns 200 OK with app name and version."""
    response = client.get("/v1/version")
    assert response.status_code == 200
    data = response.json()
    assert data["app_name"] == "LOTA Security Verity"
    assert data["version"] == "0.1.0"
    assert "build" in data
    assert "revision" in data


def test_placeholder_endpoints_return_501() -> None:
    """Verify placeholder endpoints return HTTP 501 Not Implemented."""
    # POST /v1/assets/git
    res = client.post(
        "/v1/assets/git",
        json={
            "repository_url": "https://github.com/example/repo",
            "ref": "main",
            "analysis_profile": "standard-static",
            "owner_team": "security-engineering",
        },
    )
    assert res.status_code == 501
    assert res.json()["error_code"] == "NOT_IMPLEMENTED"

    # POST /v1/scans
    res = client.post(
        "/v1/scans",
        json={"asset_id": "asset_01H12345678901234567890123", "analysis_level": "L1_STATIC"},
    )
    assert res.status_code == 501
    assert res.json()["error_code"] == "NOT_IMPLEMENTED"

    # GET /v1/scans/{scan_id}
    res = client.get("/v1/scans/scan_01H12345678901234567890123")
    assert res.status_code == 501

    # GET /v1/findings
    res = client.get("/v1/findings")
    assert res.status_code == 501

    # POST /v1/exceptions
    res = client.post(
        "/v1/exceptions",
        json={
            "control_id": "CONTAINER-PRIV-001",
            "asset_scope": "asset_01H12345678901234567890123",
            "justification": "Test justification",
        },
    )
    assert res.status_code == 501

    # POST /v1/remediations/{id}/approve
    res = client.post(
        "/v1/remediations/rem_01H12345678901234567890123/approve",
        json={"reason": "Approved for testing"},
    )
    assert res.status_code == 501


if __name__ == "__main__":
    test_health_endpoint()
    test_readiness_endpoint()
    test_version_endpoint()
    test_placeholder_endpoints_return_501()
    print("All Verity API tests completed successfully.")
