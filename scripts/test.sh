#!/usr/bin/env bash
# ==============================================================================
# LOTA Security Platform - Test Execution Script
# Executes unit and contract tests safely.
# ==============================================================================
set -euo pipefail

echo "=========================================================="
echo "  LOTA Security Platform: Test Suite Execution            "
echo "=========================================================="

PYTHON_CMD="python"
if command -v python3 >/dev/null 2>&1; then
    PYTHON_CMD="python3"
fi

# Set PYTHONPATH to include shared/python and api app
export PYTHONPATH="${PYTHONPATH:-}:shared/python:products/verity/apps/api"

echo "[1/2] Running Shared Library (lota_common) Tests..."
$PYTHON_CMD -c "
import sys
from lota_common.ids import generate_id, validate_id
from lota_common.redaction import redact_sensitive_data, redact_string
from lota_common.audit import AuditEvent, create_audit_event
from lota_common.errors import PlatformError, ValidationError, NotFoundError

# Test ID generation
aid = generate_id('asset')
assert aid.startswith('asset_'), f'Invalid asset id {aid}'
assert validate_id(aid, 'asset') is True
assert validate_id('invalid_id', 'asset') is False

# Test redaction
test_dict = {'api_key': 'secret123456', 'safe_field': 'hello', 'password': 'pass'}
redacted = redact_sensitive_data(test_dict)
assert redacted['api_key'] == '[REDACTED]'
assert redacted['safe_field'] == 'hello'
assert redacted['password'] == '[REDACTED]'

raw_text = 'User authorization: Bearer eyJhbGciOiJIUzI1Ni...'
redacted_text = redact_string(raw_text)
assert '[REDACTED]' in redacted_text

# Test audit event
evt = create_audit_event(
    action='asset.create',
    actor={'user_id': 'usr_01', 'role': 'admin'},
    target={'asset_id': aid},
    status='SUCCESS'
)
assert evt.action == 'asset.create'
assert evt.event_id.startswith('evt_')

# Test errors
err = ValidationError('Invalid input parameter')
assert err.error_code == 'VALIDATION_ERROR'

print('lota_common unit tests passed successfully.')
"

echo "[2/2] Running Verity API Health & Contract Unit Tests..."
$PYTHON_CMD -c "
import sys
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Health endpoint
resp = client.get('/health')
assert resp.status_code == 200, f'Expected 200, got {resp.status_code}'
data = resp.json()
assert data['status'] == 'ok'
assert data['service'] == 'verity-api'
assert 'environment' in data

# Readiness endpoint
resp = client.get('/ready')
assert resp.status_code == 200, f'Expected 200, got {resp.status_code}'
data = resp.json()
assert data['ready'] is True

# Version endpoint
resp = client.get('/v1/version')
assert resp.status_code == 200
data = resp.json()
assert data['app_name'] == 'LOTA Security Verity'
assert 'version' in data

# Placeholder endpoints (must return 501 Not Implemented)
resp = client.post('/v1/assets/git', json={
    'repository_url': 'https://github.com/example/repo',
    'ref': 'main',
    'analysis_profile': 'standard-static',
    'owner_team': 'security'
})
assert resp.status_code == 501, f'Expected 501, got {resp.status_code}: {resp.text}'

resp = client.post('/v1/scans', json={'asset_id': 'asset_01H12345678901234567890123', 'analysis_level': 'L1_STATIC'})
assert resp.status_code == 501

resp = client.get('/v1/scans/scan_01H12345678901234567890123')
assert resp.status_code == 501

resp = client.get('/v1/findings')
assert resp.status_code == 501

resp = client.post('/v1/exceptions', json={'control_id': 'CTRL-01', 'asset_scope': 'asset_01H12345678901234567890123', 'justification': 'test'})
assert resp.status_code == 501

resp = client.post('/v1/remediations/rem_01H12345678901234567890123/approve', json={'reason': 'approved for testing'})
assert resp.status_code == 501

print('Verity API unit and placeholder tests passed successfully.')
"

echo "=========================================================="
echo "  All tests passed successfully.                          "
echo "=========================================================="
