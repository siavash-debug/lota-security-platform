#!/usr/bin/env bash
# ==============================================================================
# Verity - Linting Script
# ==============================================================================
set -euo pipefail

PYTHON_CMD="python"
if command -v python3 >/dev/null 2>&1; then
    PYTHON_CMD="python3"
fi

echo "Linting Verity applications..."
$PYTHON_CMD -m compileall -q products/verity/apps/api products/verity/apps/worker
echo "Verity compilation lint passed."
