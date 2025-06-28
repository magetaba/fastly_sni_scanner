#!/bin/bash

APP_NAME="fastly_sni_scanner.py"
VENV_DIR="venv"

if [ ! -d "$VENV_DIR" ]; then
    echo "🔧 Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

source "$VENV_DIR/bin/activate"

echo "📦 Installing dependencies..."
pip install --upgrade pip >/dev/null
pip install requests dnspython >/dev/null

echo "🚀 Running $APP_NAME..."
python "$APP_NAME"
