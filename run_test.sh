#!/usr/bin/env bash
set -euo pipefail

uv run python -m unittest discover -s todo_api -t . -p "*_test.py" -v
