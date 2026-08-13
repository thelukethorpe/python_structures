#!/bin/bash
set -euo pipefail

VENV_DIR=".venv"

if [[ ! -x "$VENV_DIR/bin/ruff" || ! -x "$VENV_DIR/bin/mypy" ]]; then
	echo "Virtual environment not initialized. Run ./install.sh first."
	exit 1
fi

RUFF="$VENV_DIR/bin/ruff"
MYPY="$VENV_DIR/bin/mypy"

echo "Fixing style..."
"$RUFF" check --fix .
"$RUFF" format .

echo "Type checking..."
"$MYPY" src
