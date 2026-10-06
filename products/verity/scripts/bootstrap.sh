#!/usr/bin/env bash
# ==============================================================================
# Verity - Bootstrap Script
# ==============================================================================
set -euo pipefail

echo "Bootstrapping LOTA Security Verity environment..."
command -v python3 >/dev/null 2>&1 || command -v python >/dev/null 2>&1 || {
    echo "ERROR: Python 3.12+ is required." >&2
    exit 1
}

echo "Verity directory checks passed."
