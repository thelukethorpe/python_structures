#!/bin/bash
set -euo pipefail

VENV_DIR=".venv"

if [[ ! -x "$VENV_DIR/bin/pytest" ]]; then
	echo "Virtual environment not initialized. Run ./install.sh first."
	exit 1
fi

"$VENV_DIR/bin/pytest"
