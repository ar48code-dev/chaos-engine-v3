from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Chaos Engine V3 API",
    description="Autonomous Multi-Agent Game QA System Backend",
    version="3.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Chaos Engine V3 Backend Online 🚀"}

from pydantic import BaseModel
import time
import random
import os
from google import genai
from google.genai import types
import base64

class CodeSubmission(BaseModel):
    code: str
    api_key: str | None = None

class BugVisualizationRequest(BaseModel):
    bug_description: str
    bug_type: str  # "crash", "glitch", "performance", "logic"
    api_key: str | None = None

@app.post("/analyze")
async def analyze_code(submission: CodeSubmission):
    api_key = submission.api_key or os.getenv("GEMINI_API_KEY")
    
    print(f"[DEBUG] API Key status: {bool(api_key) and api_key != 'your_key_here'}")
    
    if api_key and api_key != "your_key_here":
        try:
            print("[DEBUG] Attempting Gemini 3 API call with advanced features...")
            client = genai.Client(api_key=api_key)
            
            # Define the response schema for structured output
            response_schema = {
                "type": "object",
                "properties": {
                    "griefer": {
                        "type": "object",
                        "properties": {
                            "finding": {"type": "string"},
                            "severity": {"type": "string", "enum": ["CRITICAL", "HIGH", "MEDIUM", "LOW"]},
                            "exploit_steps": {"type": "array", "items": {"type": "string"}}
                        },
                        "required": ["finding", "severity"]
                    },
                    "speedrunner": {
                        "type": "object",
                        "properties": {
                            "finding": {"type": "string"},
                            "optimization_potential": {"type": "string"},
                            "skip_sequence": {"type": "array", "items": {"type": "string"}}
                        },
                        "required": ["finding"]
                    },
                    "auditor": {
                        "type": "object",
                        "properties": {
                            "finding": {"type": "string"},
                            "code_quality_score": {"type": "string"},
                            "recommendations": {"type": "array", "items": {"type": "string"}}
                        },
                        "required": ["finding"]
                    }
                },
                "required": ["griefer", "speedrunner", "auditor"]
            }
            
            # Auto-detect programming language
            code_sample = submission.code[:200].lower()
            if 'class ' in code_sample and 'def ' in code_sample:
                detected_lang = "Python"
            elif 'public class' in code_sample or 'void ' in code_sample:
                detected_lang = "C# or Java"
            elif 'function' in code_sample or 'const ' in code_sample or 'let ' in code_sample:
                detected_lang = "JavaScript/TypeScript"
            elif '#include' in code_sample or 'int main' in code_sample:
                detected_lang = "C/C++"
            else:
                detected_lang = "Unknown (will auto-detect)"
            
            print(f"[DEBUG] Detected language: {detected_lang}")
            
            prompt = f"""You are the "Chaos Engine V3", an elite autonomous game QA system with three specialized AI agents.

**YOUR MISSION:** Perform deep analysis of this game code using advanced reasoning. Auto-detect the programming language and adapt your analysis accordingly.

**CODE TO ANALYZE:**
```
{submission.code}
```

**ANALYSIS FRAMEWORK:**

1. **GRIEFER AGENT** (Exploit Hunter):
   - Find crash vulnerabilities, input exploits, edge cases, buffer overflows
   - Identify ways to break game logic, physics, or memory safety
   - Rate severity: CRITICAL/HIGH/MEDIUM/LOW
   - Provide step-by-step exploit reproduction

2. **SPEEDRUNNER AGENT** (Performance Optimizer):
   - Identify skippable logic, physics exploits, sequence breaks
   - Find optimization opportunities (algorithmic, memory, rendering)
   - Suggest shortcuts or frame-perfect execution possibilities
   - Analyze performance bottlenecks

3. **AUDITOR AGENT** (Code Quality Expert):
   - Check for logic errors, missing error handling, null pointer risks
   - Evaluate code quality, maintainability, and best practices
   - Identify style violations and anti-patterns
   - Provide actionable recommendations

**IMPORTANT:** Use deep reasoning to understand the game's state machine and logic flow. Think through edge cases systematically. Adapt your analysis to the detected programming language's specific vulnerabilities (e.g., memory safety for C++, async issues for JavaScript, null reference for C#)."""

            # Use Gemini 3 Pro for complex analysis with extended thinking
            # Falls back to Gemini 3 Flash if Pro unavailable
            models_to_try = [
                ("models/gemini-3-pro-preview", 24000, "Gemini 3 Pro (Extended Reasoning)"),
                ("models/gemini-3-flash-preview", 12000, "Gemini 3 Flash (Fast Analysis)"),
                ("models/gemini-1.5-pro-latest", 8000, "Gemini 1.5 Pro (Fallback)"),
                ("models/gemini-1.5-flash-latest", 0, "Gemini 1.5 Flash (Basic)")
            ]
            
            last_error = None
            for model_name, thinking_budget, model_label in models_to_try:
                try:
                    print(f"[DEBUG] Trying {model_label}...")
                    
                    config_params = {
                        "response_mime_type": "application/json",
                        "response_schema": response_schema,
                        "temperature": 0.7
                    }
                    
                    # Add thinking config only for models that support it
                    if thinking_budget > 0:
                        config_params["thinking_config"] = types.ThinkingConfig(
                            thinking_budget=thinking_budget
                        )
                    
                    response = client.models.generate_content(
                        model=model_name,
                        contents=prompt,
                        config=types.GenerateContentConfig(**config_params)
                    )
                    
                    print(f"[DEBUG] SUCCESS with {model_label}")
                    
                    import json
                    result = json.loads(response.text)
                    
                    # Format for frontend
                    agents_result = {
                        "griefer": f"{result['griefer']['finding']} [Severity: {result['griefer'].get('severity', 'UNKNOWN')}]",
                        "speedrunner": result['speedrunner']['finding'],
                        "auditor": f"{result['auditor']['finding']} [Quality: {result['auditor'].get('code_quality_score', 'N/A')}]"
                    }
                    
                    return {
                        "status": "complete",
                        "mode": f"REAL_{model_label.split()[0].upper().replace('.', '_')}",
                        "model_used": model_label,
                        "agents": agents_result,
                        "raw_analysis": result,
                        "logs": [
                            f"🚀 Connected to {model_label}...",
                            "🧠 [DEEP THINKING] Analyzing game state machine..." if thinking_budget > 0 else "⚡ [FAST MODE] Analyzing code patterns...",
                            "🤖 [GRIEFER] Fuzzing input vectors with exploit chains...",
                            "🤖 [SPEEDRUNNER] Simulating frame-perfect execution paths...",
                            "🤖 [AUDITOR] Performing deep code quality analysis...",
                            f"✅ ANALYSIS COMPLETE ({model_label})"
                        ]
                    }
                    
                except Exception as e:
                    last_error = str(e)
                    print(f"[DEBUG] {model_label} failed: {last_error[:100]}")
                    continue  # Try next model
            
            # If all models failed
            print(f"[ERROR] All models failed. Last error: {last_error}")
            return {
                "status": "error",
                "mode": "API_ERROR",
                "agents": {
                    "griefer": f"All Gemini models failed. Last error: {last_error[:200]}",
                    "speedrunner": "Unable to analyze - API unavailable",
                    "auditor": "Try checking your API key or quota limits"
                },
                "logs": [
                    f"🔥 CRITICAL ERROR: {last_error[:150]}",
                    "⚠️ Tried: Gemini 3 Pro → 3 Flash → 1.5 Pro → 1.5 Flash",
                    "⚠️ Check https://ai.google.dev/gemini-api/docs/models",
                    "❌ All models unavailable"
                ]
            }
        except Exception as outer_e:
            print(f"[CRITICAL ERROR] UI-Level Failure: {outer_e}")
            return {
                "status": "error",
                "message": f"Global analysis failure: {str(outer_e)}",
                "logs": [f"🚨 FATAL: {str(outer_e)}"]
            }

    # Demo mode
    print("[DEBUG] Running in DEMO mode")
    time.sleep(1.5)
    return {
        "status": "complete",
        "mode": "DEMO_MOCK",
        "agents": {
            "griefer": "Found unhandled exception when health is negative [Severity: HIGH] (Demo)",
            "speedrunner": "Possible wall-clip in collision detection logic (Demo)",
            "auditor": "Function 'take_damage' lacks type hinting and docstrings [Quality: C+] (Demo)"
        },
        "logs": [
            "⚠️ API KEY MISSING - RUNNING IN DEMO MODE",
            "[DEMO] Simulating Griefer analysis...",
            "[DEMO] Simulating Speedrunner analysis...",
            "[DEMO] Simulating Auditor analysis...",
            "✅ DEMO ANALYSIS COMPLETE"
        ]
    }

@app.post("/generate-bug-visual")
async def generate_bug_visual(request: BugVisualizationRequest):
    """Generate a visual representation of the bug using Imagen 3"""
    api_key = request.api_key or os.getenv("GEMINI_API_KEY")
    
    if not api_key or api_key == "your_key_here":
        return {
            "status": "error",
            "message": "API key required for image generation"
        }
    
    try:
        print(f"[DEBUG] Generating bug visualization for: {request.bug_type}")
        client = genai.Client(api_key=api_key)
        
        # Map bug types to visual styles
        visual_styles = {
            "crash": "Dramatic explosion of red error particles, shattered glass effect, digital corruption, cyberpunk aesthetic",
            "glitch": "Glitching holographic interface, flickering neon colors, distorted reality, matrix-style artifacts",
            "performance": "Slow-motion freeze frame, clock symbols, loading bars stuck at 99%, time dilation visual",
            "logic": "Impossible geometry, M.C. Escher style paradox, broken causality, quantum superposition visual"
        }
        
        style = visual_styles.get(request.bug_type, "Abstract digital error visualization")
        
        prompt = f"""High-quality 3D rendered visualization of a game bug:

BUG: {request.bug_description}

VISUAL STYLE: {style}

REQUIREMENTS:
- Cinematic lighting with dramatic shadows
- Futuristic game engine aesthetic  
- Clear visual representation of the bug's impact
- Professional game development presentation quality
- Dark background with neon accents (cyan, magenta, orange)
- Include subtle UI elements showing error state
- 16:9 aspect ratio, suitable for technical presentation

Make it look like a professional bug report screenshot from a AAA game studio."""

        # Use Imagen 4 for generation (latest model)
        response = client.models.generate_images(
            model="imagen-4.0-generate-preview",
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio="16:9",
                safety_filter_level="block_only_high",
                person_generation="allow_adult"
            )
        )
        
        # Get the generated image
        if response.generated_images and len(response.generated_images) > 0:
            image_data = response.generated_images[0].image.image_bytes
            base64_image = base64.b64encode(image_data).decode('utf-8')
            
            return {
                "status": "success",
                "image": f"data:image/png;base64,{base64_image}",
                "prompt_used": prompt[:200] + "..."
            }
        else:
            raise Exception("No image generated")
            
    except Exception as e:
        print(f"[ERROR] Image generation failed: {e}")
        return {
            "status": "error",
            "message": str(e)
        }


@app.get("/health")
async def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
