# ⚡ Chaos Engine V3: Autonomous Multi-Agent Game QA

**Chaos Engine V3** is a state-of-the-art Game QA automation system built for the **Gemini 3 Hackathon**. It leverages the advanced reasoning capabilities of Gemini 3 Pro and Flash to perform deep, multi-perspective analysis of game logic.

## 🚀 Key Features

- **Autonomous Multi-Agent Analysis**: Three specialized agents (Griefer, Speedrunner, Auditor) analyze your code with different goals.
- **Gemini 3 Extended Thinking**: Uses Gemini 3 Pro's "Thinking" mode to systematically explore edge cases and state machine vulnerabilities.
- **Visual Bug Reporting (Imagen 4)**: Automatically generates high-quality cinematic visualizations of detected bugs using the latest Imagen 4 model.
- **Automated Fix Proposals**: Not only finds bugs but proposes code fixes with a side-by-side diff view.
- **Language Agnostic**: Deeply understands Python, C#, C++, and JavaScript/TypeScript game modules.

## 🛠️ Technology Stack

- **Frontend**: Next.js 15, Framer Motion (for cinematic animations), Tailwind CSS.
- **Backend**: FastAPI (Python), Google GenAI SDK.
- **Models**: Gemini 3 Pro (Preview), Gemini 3 Flash (Preview), Imagen 4.

## 📦 How to Run

1. **Clone the Repo**:
   ```bash
   git clone https://github.com/[YOUR_USERNAME]/chaos-engine-v3.git
   cd chaos-engine-v3
   ```

2. **Launch with One Script**:
   We've included a robust repair and run script to handle environment setup automatically.
   ```bash
   chmod +x run_chaos.sh
   ./run_chaos.sh
   ```

3. **Open the App**:
   Navigate to [http://localhost:3000](http://localhost:3000).

4. **Add API Key**:
   Click **Settings** in the UI and paste your Gemini API Key to enable the Advanced AI features.

## 🏆 Hackathon Submission Details

- **Vision**: To eliminate "day-one" game-breaking bugs by providing developers with an AI-powered "Red Team."
- **Gemini Usage**: 
  - **Gemini 3 Pro**: Used for the "Extended Thinking" mode to analyze complex game state transitions.
  - **Gemini 3 Flash**: Used for rapid initial screening and fallback during high-traffic audits.
  - **Imagen 4**: Transforms dry text bug reports into cinematic "Visual Proof of Concept" images.

---
*Created by Anirban for the Gemini 3 Hackathon Challenge.*
