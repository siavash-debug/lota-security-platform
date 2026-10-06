#!/usr/bin/env bash
# ==============================================================================
# Verity - Test Script
# ==============================================================================
set -euo pipefail

PYTHON_CMD="python"
if command -v python3 >/dev/null 2>&1; then
    PYTHON_CMD="python3"
fi

export PYTHONPATH="${PYTHONPATH:-}:shared/python:products/verity/apps/api"
echo "Running Verity API unit tests..."
$PYTHON_CMD products/verity/apps/api/tests/test_health.py
