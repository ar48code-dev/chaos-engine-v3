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
# Force legacy-peer-deps for stability
if [ ! -d "node_modules" ]; then
    echo "Installing frontend dependencies (this may take a minute)..."
    npm install --legacy-peer-deps --quiet
fi
cd ..

# 5. KILL OLD SERVERS
# ------------------------------------------
echo "Cleaning up ports..."
fuser -k 3000/tcp > /dev/null 2>&1
fuser -k 8000/tcp > /dev/null 2>&1
sleep 2

# 6. LAUNCH
# ------------------------------------------
echo ""
echo "=========================================="
echo "✅ SETUP COMPLETE! Launching now..."
echo "=========================================="

# Start Backend
cd backend
echo "🚀 Starting Backend on http://localhost:8000"
./venv/bin/python main.py > ../backend.log 2>&1 &
BACKEND_PID=$!

# Start Frontend
cd ../frontend
echo "🚀 Starting Frontend on http://localhost:3000"
# Use --ignore-scripts to skip potentially broken builds for faster startup
npm run dev -- --port 3000 > ../frontend.log 2>&1 &
FRONTEND_PID=$!

echo ""
echo "=========================================="
echo "⏳ WAITING FOR SERVERS TO INITIALIZE..."
echo "=========================================="

# Wait for frontend to be ready
ATTEMPTS=0
while ! curl -s http://localhost:3000 > /dev/null; do
    sleep 2
    ATTEMPTS=$((ATTEMPTS+1))
    echo -n "."
    if [ $ATTEMPTS -gt 30 ]; then
        echo -e "\n⚠️ Frontend taking a while to start. Please check http://localhost:3000 manually soon."
        break
    fi
done

echo -e "\n✨ EVERYTHING IS READY!"
echo "👉 OPEN THIS LINK: http://localhost:3000"
echo "=========================================="
echo "Press Ctrl+C to stop both servers."

# Keep running and handle cleanup
trap "echo 'Stopping servers...'; kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait
