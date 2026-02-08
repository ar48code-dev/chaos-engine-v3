# ⚡ Chaos Engine V3
### Autonomous Multi-Agent Game QA System

> **Designed for the Gemini 3 Hackathon Challenge**
> *Turning dry code analysis into a cinematic, multi-agent adventure.*

---

Traditional static analysis tools find syntax errors. Human testers find functional bugs. **Chaos Engine V3** bridges the gap by using Gemini 3's advanced reasoning to understand *logic and intent*. It doesn't just check if your code runs; it checks if your system can be broken, exploited, or optimized across multiple domains.

## 🤖 Universal Multi-Agent Domains
We deploy specialized AI personality "Red Teams" tailored to your specific project needs:

1. **🎮 Game QA**: Exploit hunters and performance optimizers for AAA or indie game logic.
2. **💻 Software/Web**: Security auditors and architecture reviewers for enterprise-grade applications.
3. **🎓 Learning/Education**: Mentors and concept analyzers to help developers grow and learn.
4. **🎧 Customer Support**: Bug reproducers and diagnostic experts to solve user issues in record time.

## 🧬 Powered by Gemini 3 & Imagen 4
*   **Gemini 3 Pro/Flash (Thinking Mode)**: We leverage the latest `thinking_budget` features to allow the agents to simulate complex logic transitions in their heads before reaching a conclusion.
*   **Imagen 4 (Universal Bug Reporting)**: Chaos Engine transforms abstract technical failures into **Cinematic Visual Proofs**. Whether it's a game glitch or a security breach, Imagen 4 visualizes the impact for stakeholders.

## 🚀 Key Features
*   **Universal Domain Switching**: One platform for Game, Software, Learning, and Support analysis.
*   **Auto-Language Detection**: Supports Python, JavaScript, TypeScript, C#, C++, and Java.
*   **Deep Reasoning Logs**: Watch the "Live Logs" to see the agents think through edge cases in real-time.
*   **Automated Fix Proposals**: View side-by-side code diffs showing exactly how to resolve vulnerabilities.
*   **Premium Cyberpunk UI**: A futuristic, high-performance interface that responds dynamically to your selected domain.

## 📦 How to Run (Quick Start)

### **Option 1: One-Command Launch (Recommended)**
```bash
git clone https://github.com/ar48code-dev/chaos-engine-v3.git
cd chaos-engine-v3
chmod +x start.sh
./start.sh
```

**⏳ Wait 30-60 seconds** for setup to complete, then **open your browser** to:
```
http://localhost:3000
```

The script will:
- ✅ Auto-install Python dependencies
- ✅ Auto-install Node.js dependencies  
- ✅ Launch both backend (port 8000) and frontend (port 3000)
- ✅ Keep running until you press `Ctrl+C`

### **Option 2: Manual Setup**
If the auto-script doesn't work on your system:

**Backend:**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

**Frontend (in a new terminal):**
```bash
cd frontend
npm install
npm run dev
```

Then open: **http://localhost:3000**

---

## 🔑 Getting Your API Key
1. Click the **⚙️ Settings** button in the top-right
2. Click **"🔑 Get Key from AI Studio"** (opens Google AI Studio)
3. Generate a free API key
4. Paste it into the settings modal
5. Now you can run **Real Gemini 3 Analysis** instead of Demo Mode!

## 🛠️ Tech Stack
- **Frontend**: Next.js 15, Tailwind CSS, Framer Motion, Lucide React.
- **Backend**: FastAPI, Google GenAI SDK 1.0+, Pydantic V2.
- **AI Models**: Gemini 3 Pro (Preview), Gemini 3 Flash, Imagen 4.

---
*Developed by Anirban with ❤️ for the Gemini 3 Hackathon.*
