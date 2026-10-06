#!/usr/bin/env bash
# ==============================================================================
# LOTA Security Platform - Linting Script
# Validates code style, schemas, and formatting defensively.
# ==============================================================================
set -euo pipefail

echo "=========================================================="
echo "  LOTA Security Platform: Linting & Code Hygiene Suite     "
echo "=========================================================="

PYTHON_CMD="python"
if command -v python3 >/dev/null 2>&1; then
    PYTHON_CMD="python3"
fi

echo "[1/3] Python Syntax & AST Compilation Check..."
$PYTHON_CMD -m compileall -q products/verity/apps/api products/verity/apps/worker shared/python
echo "Python compilation check passed."

echo "[2/3] Checking for forbidden secrets patterns in code files..."
$PYTHON_CMD -c "
import os, re, sys

forbidden_patterns = [
    re.compile(r'(?i)(AKIA[0-9A-Z]{16})'),
    re.compile(r'(?i)(-----BEGIN\s+PRIVATE\s+KEY-----)'),
    re.compile(r'(?i)(ghp_[0-9a-zA-Z]{36})'),
]

files_with_violations = []
for root, dirs, files in os.walk('.'):
    if any(skip in root for skip in ['.git', '.venv', 'node_modules', '__pycache__']):
        continue
    for file in files:
        if file.endswith(('.py', '.json', '.yaml', '.yml', '.rego', '.sh', '.md')):
            path = os.path.join(root, file)
            if 'lint.sh' in path or 'redaction.py' in path:
                continue
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    for pattern in forbidden_patterns:
                        if pattern.search(content):
                            files_with_violations.append(path)
                            break
            except Exception:
                pass

if files_with_violations:
    print('ERROR: Potential unmasked credential patterns found in:', files_with_violations)
    sys.exit(1)
print('Secret hygiene scan passed.')
"

echo "[3/3] Checking JSON syntax across all configuration and schema files..."
$PYTHON_CMD -c "
import json, os, sys

error_count = 0
for root, dirs, files in os.walk('.'):
    if any(skip in root for skip in ['.git', '.venv', 'node_modules', '__pycache__']):
        continue
    for file in files:
        if file.endswith('.json'):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    json.load(f)
            except Exception as e:
                print(f'JSON syntax error in {path}: {e}', file=sys.stderr)
                error_count += 1

if error_count > 0:
    print(f'Total JSON errors: {error_count}', file=sys.stderr)
    sys.exit(1)
print('All JSON files validated successfully.')
"

echo "=========================================================="
echo "  All lint checks completed successfully.                 "
echo "=========================================================="
