#!/bin/bash

# ==========================================
# 🚀 ULTRA-START SCRIPT FOR CHAOS ENGINE
# ==========================================

echo "🔧 Starting repair and launch process..."

# 1. FORCE LOAD NVM (To get 'node' and 'npm')
# ------------------------------------------
export NVM_DIR="$HOME/.nvm"
if [ -s "$NVM_DIR/nvm.sh" ]; then
    echo "Found NVM, loading..."
    source "$NVM_DIR/nvm.sh"
fi

if ! command -v npm &> /dev/null; then
    echo "❌ ERROR: npm is still missing. Trying to find it..."
    # Search for nvm in common spots
    [ -s "/usr/share/nvm/init.sh" ] && source "/usr/share/nvm/init.sh"
fi

# 2. FIX PYTHON VENV (Using virtualenv)
# ------------------------------------------
echo "Checking Python tools..."
python3 -m pip install --user virtualenv --quiet 2>/dev/null
export PATH="$HOME/.local/bin:$PATH"

# 3. SET UP BACKEND
# ------------------------------------------
echo "Setting up Backend..."
cd backend
rm -rf venv
python3 -m virtualenv venv
./venv/bin/pip install -r requirements.txt --quiet
cd ..

# 4. SET UP FRONTEND
# ------------------------------------------
echo "Setting up Frontend..."
cd frontend
if [ ! -d "node_modules" ]; then
    npm install --quiet
fi
cd ..

# 5. KILL OLD SERVERS
# ------------------------------------------
echo "Cleaning up ports..."
fuser -k 3000/tcp > /dev/null 2>&1
fuser -k 8000/tcp > /dev/null 2>&1

# 6. LAUNCH
# ------------------------------------------
echo ""
echo "=========================================="
echo "✅ SETUP COMPLETE! Launching now..."
echo "=========================================="

cd backend
./venv/bin/python main.py &
BACKEND_PID=$!

cd ../frontend
npm run dev &
FRONTEND_PID=$!

echo "Frontend starting at: http://localhost:3000"
echo "Backend starting at: http://localhost:8000"
echo "=========================================="
echo "Wait about 30 seconds, then open Chrome to http://localhost:3000"
echo "Press Ctrl+C to stop both servers."

# Keep running and handle cleanup
trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait
