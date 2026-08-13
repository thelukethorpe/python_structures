#!/bin/bash
set -euo pipefail

VENV_DIR=".venv"
PY_MM="$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"

if [[ ! -d "$VENV_DIR" ]]; then
	echo "Creating virtual environment in $VENV_DIR..."
	if ! python3 -m venv "$VENV_DIR"; then
		echo
		echo "Failed to create virtual environment."
		echo "On Debian/Ubuntu, install venv support with one of:"
		echo "  sudo apt install python3-venv"
		echo "  sudo apt install python$PY_MM-venv"
		exit 1
	fi
fi

# Some Debian/Ubuntu setups can leave a venv without pip (for example, after a failed first create).
if ! "$VENV_DIR/bin/python" -m pip --version >/dev/null 2>&1; then
	echo "pip is missing in $VENV_DIR; recreating virtual environment..."
	rm -rf "$VENV_DIR"
	if ! python3 -m venv "$VENV_DIR"; then
		echo
		echo "Failed to recreate virtual environment."
		echo "On Debian/Ubuntu, install one of:"
		echo "  sudo apt install python3-venv"
		echo "  sudo apt install python$PY_MM-venv"
		exit 1
	fi

	if ! "$VENV_DIR/bin/python" -m pip --version >/dev/null 2>&1; then
		echo "pip still missing; attempting to bootstrap with ensurepip..."
		if ! "$VENV_DIR/bin/python" -m ensurepip --upgrade; then
			echo
			echo "Could not bootstrap pip inside $VENV_DIR."
			echo "Install prerequisites, then retry:"
			echo "  sudo apt install python3-venv python3-pip"
			echo "  sudo apt install python$PY_MM-venv python3-pip"
			exit 1
		fi
	fi
fi

echo "Installing package and dev dependencies into $VENV_DIR..."
"$VENV_DIR/bin/python" -m pip install --upgrade pip
"$VENV_DIR/bin/pip" install -e ".[dev]"

echo "Done. Activate with: source $VENV_DIR/bin/activate"
