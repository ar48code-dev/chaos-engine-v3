#!/bin/bash

# Ensure we can use Node from NVM
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

echo "=========================================="
echo "🚀 CHAOS ENGINE LAUNCHER"
echo "=========================================="

# Kill ports
fuser -k 3000/tcp > /dev/null 2>&1
fuser -k 8000/tcp > /dev/null 2>&1

# Start Backend
echo "Starting Backend..."
cd backend
if [ ! -d "venv" ]; then
    echo "Recreating venv..."
    python3 -m virtualenv venv
    ./venv/bin/pip install -r requirements.txt
fi
./venv/bin/python main.py &
BACKEND_PID=$!
echo "✅ Backend (PID: $BACKEND_PID)"

# Start Frontend
cd ../frontend
echo "Starting Frontend..."
if [ ! -d "node_modules" ]; then
    echo "Installing frontend dependencies (first time only)..."
    npm install --legacy-peer-deps
fi
npm run dev &
FRONTEND_PID=$!
echo "✅ Frontend (PID: $FRONTEND_PID)"

echo "------------------------------------------"
echo "Both servers are running!"
echo "Open: http://localhost:3000"
echo "------------------------------------------"
echo "Press Ctrl+C to stop."

trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait
