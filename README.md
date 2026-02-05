# ⚡ Chaos Engine V3
### Autonomous Multi-Agent Game QA System

> **Designed for the Gemini 3 Hackathon Challenge**
> *Turning dry code analysis into a cinematic, multi-agent adventure.*

---

## 🌟 The Vision
Traditional static analysis tools find syntax errors. Human testers find gameplay bugs. **Chaos Engine V3** bridge the gap by using Gemini 3's advanced reasoning to understand *gameplay logic*. It doesn't just check if your code runs; it checks if your game can be broken, exploited, or optimized.

## 🤖 The Multi-Agent "Red Team"
We deploy three specialized AI personalities to "attack" your code from different angles:

1. **💥 The Griefer**: An elite exploit-hunter. Its only goal is to find crash vulnerabilities, input-injection loops, and ways to break your game engine's state machine. 
2. **⚡ The Speedrunner**: A performance perfectionist. It looks for sequence breaks, wall-clips in your logic, and algorithmic bottlenecks to ensure frame-perfect gameplay.
3. **🔍 The Auditor**: A AAA standards expert. It monitors code health, maintainability, and architectural best practices to ensure your project is ready for the global stage.

## 🧬 Powered by Gemini 3 & Imagen 4
*   **Gemini 3 Pro (Thinking Mode)**: We leverage the `thinking_budget` feature to allow the agents to "simulate" game state transitions in their heads before reaching a conclusion.
*   **Gemini 3 Flash**: Provides lightning-fast initial triage and handles rapid-fire code audits.
*   **Imagen 4 (Visual Bug Reporting)**: A world-first feature. Chaos Engine transforms abstract text bugs (like "Floating point overflow") into **Cinematic Visual Proofs**. It generates high-quality 3D-style visualizations of the bug's impact, allowing artists and designers to understand technical failures instantly.

## 🚀 Key Features
*   **Auto-Language Detection**: Supports Python, C#, C++, JavaScript, TypeScript, and Java.
*   **Interactive Control Center**: Load examples, run real-time audits, and monitor "Live Logs."
*   **Automated Fix Proposals**: View side-by-side code diffs showing exactly how to fix the detected vulnerabilities.
*   **Hackathon-Ready UI**: A premium, futuristic cyberpunk aesthetic designed to WOW at first glance.

## 📦 How to Run (Quick Start)

The project is designed to be "Zero-Config" using our autonomous repair script.

1. **Clone the Project**:
   ```bash
   git clone https://github.com/ar48code-dev/chaos-engine-v3.git
   cd chaos-engine-v3
   ```

2. **One-Command Setup & Launch**:
   Run our "Super Script" which automatically handles Python virtual environments, Node.js dependencies, and server synchronization:
   ```bash
   chmod +x start.sh
   ./start.sh
   ```

3. **Access the Engine**:
   - **Frontend**: [http://localhost:3000](http://localhost:3000)
   - **API Status**: [http://localhost:8000/health](http://localhost:8000/health)

4. **Enable Real AI**:
   The app starts in **Demo Mode**. To use real Gemini 3 analysis, click the **Settings** icon in the UI and paste your [Google AI Studio API Key](https://aistudio.google.com/app/apikey).

## 🛠️ Tech Stack
- **Frontend**: Next.js 15, Tailwind CSS, Framer Motion, Lucide React.
- **Backend**: FastAPI, Google GenAI SDK 1.0+, Pydantic V2.
- **AI Models**: Gemini 3 Pro (Preview), Gemini 3 Flash, Imagen 4.

---
*Developed by Anirban with ❤️ for the Gemini 3 Hackathon.*
