#!/bin/bash

set -e

PROJECT_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"

cd "$PROJECT_ROOT"

# Activate virtual environment
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
else
    echo "❌ Virtual environment not found."
    exit 1
fi

echo ""
echo "=========================================="
echo " AKYDev Sprint 002"
echo " Project Intelligence Engine"
echo "=========================================="

echo ""
echo "[1/5] Installing AKYDev..."
python -m pip install -e .

echo ""
echo "[2/5] Running Project Analyzer..."
akydev analyze ~/Documents/AKY_AI/RAPO

echo ""
echo "[3/5] Checking Git..."
git status --short

echo ""
echo "[4/5] Sprint verification complete."

echo ""
echo "=========================================="
echo " Sprint 002 Finished Successfully"
echo "=========================================="