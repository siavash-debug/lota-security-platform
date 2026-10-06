#!/usr/bin/env bash
# ==============================================================================
# LOTA Security Platform - Bootstrap Script
# Defensive local development bootstrap script.
# ==============================================================================
set -euo pipefail

echo "=========================================================="
echo "  LOTA Security Platform: Local Environment Bootstrap     "
echo "=========================================================="

echo "[1/4] Checking system prerequisites..."
command -v python3 >/dev/null 2>&1 || command -v python >/dev/null 2>&1 || {
    echo "ERROR: Python 3.12+ is required but neither python3 nor python was found." >&2
    exit 1
}

command -v git >/dev/null 2>&1 || {
    echo "ERROR: Git is required but not found." >&2
    exit 1
}

echo "Prerequisites verified: Python and Git are available."

echo "[2/4] Initializing local environment configuration..."
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo "Created .env from .env.example"
    else
        echo "WARNING: .env.example not found."
    fi
else
    echo ".env already exists, preserving existing configuration."
fi

if [ ! -f "compose/dev.env" ]; then
    if [ -f "compose/dev.env.example" ]; then
        cp compose/dev.env.example compose/dev.env
        echo "Created compose/dev.env from compose/dev.env.example"
    fi
fi

echo "[3/4] Validating repository structure..."
REQUIRED_DIRS=(
    "docs/products/verity"
    "products/verity/apps/api"
    "products/verity/apps/worker"
    "products/verity/apps/console"
    "products/verity/policy"
    "products/verity/contracts"
    "shared/python/lota_common"
)

for dir in "${REQUIRED_DIRS[@]}"; do
    if [ ! -d "$dir" ]; then
        echo "ERROR: Required directory '$dir' is missing." >&2
        exit 1
    fi
done
echo "Core repository directories verified."

echo "[4/4] Python environment check..."
PYTHON_CMD="python"
if command -v python3 >/dev/null 2>&1; then
    PYTHON_CMD="python3"
fi

$PYTHON_CMD -c "
import sys
if sys.version_info < (3, 10):
    print(f'WARNING: Recommended Python version is 3.12+. Detected {sys.version}')
else:
    print(f'Python environment verified: {sys.version.split()[0]}')
"

echo "=========================================================="
echo "  Bootstrap completed successfully. Safe to proceed.     "
echo "=========================================================="
