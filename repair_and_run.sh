#!/bin/bash

# Stop on any error
set -e

echo "=========================================="
echo "🔧 AUTO-REPAIR & START SCRIPT"
echo "=========================================="
echo "I detected your system repositories are down."
echo "I will install the tools directly to your user folder"
echo "to bypass the need for 'sudo' or 'apt'."
echo "=========================================="

# 1. Install Node.js using NVM (Bypassing apt)
# --------------------------------------------
echo ""
echo "[1/4] Checking Node.js..."

# Check if NVM is already installed
export NVM_DIR="$HOME/.nvm"
if [ -s "$NVM_DIR/nvm.sh" ]; then
    . "$NVM_DIR/nvm.sh"
else
    echo "   -> Installing NVM (Node Version Manager)..."
    wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
fi

# Install latest Node.js LTS if not present
if ! command -v node &> /dev/null; then
    echo "   -> Installing Node.js (this downloads about 50MB)..."
    nvm install --lts
    nvm use --lts
else
    echo "   -> Node.js is ready: $(node -v)"
fi


# 2. Fix Python Virtual Environment (Bypassing apt)
# -------------------------------------------------
echo ""
echo "[2/4] Setting up Python Environment..."

# Since python3-venv is broken on your OS, we use 'virtualenv' via pip
# This works even if the system venv module is missing.
echo "   -> Installing isolated 'virtualenv' tool..."
python3 -m pip install --user virtualenv --quiet

# Add local bin to PATH just in case
export PATH="$HOME/.local/bin:$PATH"

echo "   -> Creating fresh virtual environment..."
cd backend
rm -rf venv
# Use the module directly to avoid path issues
python3 -m virtualenv venv


# 3. Install Dependencies
# -----------------------
echo ""
echo "[3/4] Installing App Dependencies..."

echo "   -> Backend Libraries..."
./venv/bin/pip install -r requirements.txt --quiet --no-warn-script-location

cd ../frontend
echo "   -> Frontend Libraries (this takes 1-2 mins)..."
npm install --silent


# 4. Start Servers
# ----------------
echo ""
echo "[4/4] 🚀 STARTING SERVERS..."
echo "------------------------------------------"

# Use a trap to kill both servers when you press Ctrl+C
trap 'kill $(jobs -p)' EXIT

# Start Backend
cd ../backend
./venv/bin/python main.py &
echo "✅ Backend Live: http://localhost:8000"

# Start Frontend
cd ../frontend
npm run dev &
echo "✅ Frontend Live: http://localhost:3000"

echo "------------------------------------------"
echo "WAIT! It performs a first-time build now."
echo "When you see 'Ready in Xms', open your browser."
echo "------------------------------------------"

wait
