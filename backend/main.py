from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
import shutil
from pathlib import Path

load_dotenv()

app = FastAPI(
    title="Chaos Engine V3 API",
    description="Universal Multi-Agent AI Code & Video Analysis System",
    version="3.5.0"
)

# Create temp directory for video uploads
UPLOAD_DIR = Path("temp_uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

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
    return {"message": "Chaos Engine V3 Universal Backend Online 🚀"}

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
    domain: str = "game"  # "game", "software", "learning", "support"

class BugVisualizationRequest(BaseModel):
    bug_description: str
    bug_type: str  # "crash", "glitch", "performance", "logic"
    api_key: str | None = None

# Domain Configuration System
DOMAIN_CONFIG = {
    "game": {
        "title": "Game QA Mode",
        "agents": {
            "griefer": {"name": "Griefer", "icon": "💥", "role": "Exploit Hunter"},
            "speedrunner": {"name": "Speedrunner", "icon": "⚡", "role": "Performance Optimizer"},
            "auditor": {"name": "Auditor", "icon": "🔍", "role": "Code Quality Expert"}
        },
        "prompt_template": """You are the "Chaos Engine V3" in GAME QA MODE - an elite autonomous game testing system with three specialized AI agents.

**YOUR MISSION:** Perform deep analysis of this game code using advanced reasoning. Auto-detect the programming language and adapt your analysis accordingly.

**CODE TO ANALYZE:**
```
{code}
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

**IMPORTANT:** Use deep reasoning to understand the game's state machine and logic flow. Think through edge cases systematically."""
    },
    "software": {
        "title": "Software/Web App Mode",
        "agents": {
            "griefer": {"name": "Security Agent", "icon": "🛡️", "role": "Security Auditor"},
            "speedrunner": {"name": "Performance Agent", "icon": "🚀", "role": "Performance Analyst"},
            "auditor": {"name": "Architecture Agent", "icon": "🏗️", "role": "Design Reviewer"}
        },
        "prompt_template": """You are the "Chaos Engine V3" in SOFTWARE/WEB APP MODE - an elite autonomous software quality system with three specialized AI agents.

**YOUR MISSION:** Perform comprehensive analysis of this software/web application code using advanced reasoning.

**CODE TO ANALYZE:**
```
{code}
```

**ANALYSIS FRAMEWORK:**

1. **SECURITY AGENT** (Security Auditor):
   - Find SQL injection, XSS, CSRF, authentication bypass vulnerabilities
   - Identify insecure data handling, weak encryption, exposed secrets
   - Check for OWASP Top 10 vulnerabilities
   - Rate severity: CRITICAL/HIGH/MEDIUM/LOW
   - Provide exploitation scenarios

2. **PERFORMANCE AGENT** (Performance Analyst):
   - Detect N+1 query problems, memory leaks, inefficient algorithms
   - Identify slow API endpoints, blocking operations, resource bottlenecks
   - Find opportunities for caching, lazy loading, pagination
   - Suggest optimization strategies

3. **ARCHITECTURE AGENT** (Design Reviewer):
   - Evaluate SOLID principles, design patterns, separation of concerns
   - Check for tight coupling, code duplication, circular dependencies
   - Assess scalability, maintainability, testability
   - Provide architectural recommendations

**IMPORTANT:** Focus on production-ready code quality, security best practices, and enterprise-grade architecture."""
    },
    "learning": {
        "title": "Learning/Education Mode",
        "agents": {
            "griefer": {"name": "Concept Analyzer", "icon": "🎓", "role": "Learning Analyst"},
            "speedrunner": {"name": "Bug Injector", "icon": "🧪", "role": "Exercise Creator"},
            "auditor": {"name": "Mentor Agent", "icon": "👨‍🏫", "role": "Teaching Assistant"}
        },
        "prompt_template": """You are the "Chaos Engine V3" in LEARNING/EDUCATION MODE - an intelligent tutoring system with three specialized AI agents.

**YOUR MISSION:** Analyze this student code to provide educational insights and create learning opportunities.

**CODE TO ANALYZE:**
```
{code}
```

**ANALYSIS FRAMEWORK:**

1. **CONCEPT ANALYZER** (Learning Analyst):
   - Identify programming concepts demonstrated (loops, recursion, OOP, etc.)
   - Assess understanding level: BEGINNER/INTERMEDIATE/ADVANCED
   - Find conceptual gaps or misunderstandings
   - Highlight what the student did well

2. **BUG INJECTOR** (Exercise Creator):
   - Suggest intentional bugs to create learning exercises
   - Propose "fix this code" challenges at appropriate difficulty
   - Design debugging scenarios that reinforce concepts
   - Create progressive difficulty levels

3. **MENTOR AGENT** (Teaching Assistant):
   - Provide step-by-step explanations of how the code works
   - Suggest improvements with educational rationale
   - Offer alternative approaches with pros/cons
   - Give encouragement and constructive feedback

**IMPORTANT:** Be encouraging, educational, and focus on building understanding rather than just finding errors."""
    },
    "support": {
        "title": "Customer Support Mode",
        "agents": {
            "griefer": {"name": "Bug Reproducer", "icon": "🔬", "role": "Issue Investigator"},
            "speedrunner": {"name": "Root Cause Analyzer", "icon": "🎯", "role": "Diagnostic Expert"},
            "auditor": {"name": "Solution Agent", "icon": "💡", "role": "Fix Recommender"}
        },
        "prompt_template": """You are the "Chaos Engine V3" in CUSTOMER SUPPORT MODE - an autonomous bug reproduction and diagnostic system.

**YOUR MISSION:** Analyze this code in the context of a customer-reported issue. Help reproduce, diagnose, and solve the problem.

**CODE TO ANALYZE:**
```
{code}
```

**ANALYSIS FRAMEWORK:**

1. **BUG REPRODUCER** (Issue Investigator):
   - Attempt to reproduce the reported issue from the code
   - Identify conditions that trigger the bug
   - Create step-by-step reproduction instructions
   - Rate reproducibility: ALWAYS/SOMETIMES/RARE/CANNOT_REPRODUCE

2. **ROOT CAUSE ANALYZER** (Diagnostic Expert):
   - Trace the bug to specific code sections and line numbers
   - Explain WHY the bug occurs (root cause, not just symptoms)
   - Identify related issues that might have the same root cause
   - Assess impact on users

3. **SOLUTION AGENT** (Fix Recommender):
   - Provide concrete fix recommendations with code examples
   - Suggest workarounds for immediate relief
   - Recommend preventive measures to avoid similar issues
   - Estimate fix complexity: TRIVIAL/SIMPLE/MODERATE/COMPLEX

**IMPORTANT:** Focus on practical, actionable solutions that can be communicated to both technical and non-technical stakeholders."""
    }
}

def get_domain_config(domain: str):
    """Get configuration for the specified domain"""
    return DOMAIN_CONFIG.get(domain, DOMAIN_CONFIG["game"])

@app.post("/analyze")
async def analyze_code(submission: CodeSubmission):
    api_key = submission.api_key or os.getenv("GEMINI_API_KEY")
    domain_config = get_domain_config(submission.domain)
    
    print(f"[DEBUG] API Key status: {bool(api_key) and api_key != 'your_key_here'}")
    print(f"[DEBUG] Domain: {submission.domain} - {domain_config['title']}")
    
    if api_key and api_key != "your_key_here":
        try:
            print(f"[DEBUG] Attempting Gemini 3 API call for {domain_config['title']}...")
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
            
            # Use domain-specific prompt
            prompt = domain_config['prompt_template'].format(code=submission.code)

            # Use Gemini 3 Pro for complex analysis with extended thinking
            # Falls back to Gemini 3 Flash if Pro unavailable
            # Prioritize Gemini 3 models for the Hackathon Challenge
            models_to_try = [
                ("models/gemini-3-pro-preview", 32000, "Gemini 3 Pro (Next-Gen Reasoning)"),
                ("models/gemini-3-flash-preview", 16000, "Gemini 3 Flash (Fast Analysis)"),
                ("models/gemini-2.0-pro-exp-02-05", 32000, "Gemini 2.0 Pro (Experimental)"),
                ("models/gemini-1.5-pro-latest", 8000, "Gemini 1.5 Pro (Legacy)")
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
                        "domain": submission.domain,
                        "agents": agents_result,
                        "raw_analysis": result,
                        "logs": [
                            f"🚀 Connected to {model_label}...",
                            f"🧠 [UNIVERSAL REASONING] Analyzing {submission.domain} logic...",
                            f"🤖 [{domain_config['agents']['griefer']['name']}] {domain_config['agents']['griefer']['role']} sequence active...",
                            f"🤖 [{domain_config['agents']['speedrunner']['name']}] {domain_config['agents']['speedrunner']['role']} analysis running...",
                            f"🤖 [{domain_config['agents']['auditor']['name']}] {domain_config['agents']['auditor']['role']} evaluation complete...",
                            f"✅ {domain_config['title']} ANALYSIS COMPLETE"
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
                    "⚠️ Tried: Gemini 2.0 Pro → Flash → 1.5 Pro",
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

    # Demo mode - Domain Aware
    print(f"[DEBUG] Running in DEMO mode for domain: {submission.domain}")
    time.sleep(1.5)
    
    demo_data = {
        "game": {
            "griefer": "Potential buffer overflow in input handling [Severity: CRITICAL] (Demo)",
            "speedrunner": "O(N^2) complexity detected in particle simulation (Demo)",
            "auditor": "Class 'PhysicsEngine' is too large (God Object pattern) [Quality: D] (Demo)"
        },
        "software": {
            "griefer": "SQL Injection vulnerability in login query [Severity: CRITICAL] (Demo)",
            "speedrunner": "Blocking I/O detected on the main event loop (Demo)",
            "auditor": "Missing CSRF protection on mutation endpoints [Quality: F] (Demo)"
        },
        "learning": {
            "griefer": "Missing base case in recursive function 'calculate' [Severity: HIGH] (Demo)",
            "speedrunner": "Redundant loop detected - could use list comprehension (Demo)",
            "auditor": "Variable naming 'a', 'b', 'c' should be more descriptive [Quality: B-] (Demo)"
        },
        "support": {
            "griefer": "Reproduced: Discount is applied to shipping instead of subtotal [Severity: HIGH] (Demo)",
            "speedrunner": "Race condition in state update during high-load checkout (Demo)",
            "auditor": "Error handling swallows the exception at line 42 [Quality: C] (Demo)"
        }
    }
    
    current_demo = demo_data.get(submission.domain, demo_data["game"])
    
    return {
        "status": "complete",
        "mode": "DEMO_MOCK",
        "domain": submission.domain,
        "agents": current_demo,
        "logs": [
            "⚠️ API KEY MISSING - RUNNING IN DOMAIN DEMO MODE",
            f"[DEMO] Analyzing as {domain_config['title']}...",
            f"[DEMO] Simulating {domain_config['agents']['griefer']['name']}...",
            f"[DEMO] Simulating {domain_config['agents']['speedrunner']['name']}...",
            "✅ DEMO ANALYSIS COMPLETE"
        ]
    }

@app.post("/generate-bug-visual")
async def generate_bug_visual(request: BugVisualizationRequest):
    """Generate a visual representation of the bug using Imagen 4"""
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


@app.post("/analyze-video")
async def analyze_video(
    video: UploadFile = File(...),
    code: str = Form(...),
    domain: str = Form("support"),
    api_key: str = Form(None)
):
    """Analyze a bug video in correlation with source code using Gemini 3 Multimodal reasoning"""
    key = api_key or os.getenv("GEMINI_API_KEY")
    if not key or key == "your_key_here":
        # Simulate demo video analysis
        time.sleep(3)
        return {
            "status": "complete",
            "mode": "DEMO_VIDEO_MOCK",
            "agents": {
                "griefer": "WATCHED: At 0:02 mark, the UI flickered red. This correlates with the unhandled exception in the logic [Severity: HIGH] (Demo)",
                "speedrunner": "WATCHED: The frame rate dropped to 12fps during the particle burst (Demo)",
                "auditor": "WATCHED: Fix the race condition identified at the timestamp 0:05 (Demo)"
            },
            "logs": [
                "🎥 PROCESSING MULTIMODAL VIDEO INPUT...",
                "🧠 CORRELATING VISUAL FRAMES WITH SOURCE CODE...",
                "✅ VIDEO ANALYSIS COMPLETE (MOCKED)"
            ]
        }

    try:
        # Save video locally
        local_path = UPLOAD_DIR / video.filename
        with local_path.open("wb") as buffer:
            shutil.copyfileobj(video.file, buffer)

        client = genai.Client(api_key=key)
        
        # 1. Upload file to Gemini API
        print(f"[VIDEO] Uploading {video.filename} to Gemini...")
        uploaded_file = client.files.upload(path=str(local_path))
        
        # 2. Wait for processing
        while uploaded_file.state == "PROCESSING":
            print(".", end="", flush=True)
            time.sleep(2)
            uploaded_file = client.files.get(name=uploaded_file.name)
        
        if uploaded_file.state == "FAILED":
            raise Exception("Video processing failed on Gemini servers")

        # 3. Analyze with Gemini 3 Pro (Thinking Mode)
        prompt = f"""You are the "Multimodal Chaos Engine". I have provided a video recording of a bug and the corresponding source code.

**CODE:**
```
{code}
```

**YOUR TASK:**
1. Watch the video carefully.
2. Identify the EXACT moment the bug occurs (provide timestamps).
3. Correlate the visual evidence with the source code.
4. Tell me which part of the code is responsible for what we see in the video.

Return your analysis in the standard Chaos Engine JSON format for 3 agents (Griefer, Speedrunner, Auditor). In the findings, focus on the "Watched" evidence from the video."""

        response_schema = {
            "type": "object",
            "properties": {
                "griefer": {"type": "object", "properties": {"finding": {"type": "string"}}, "required": ["finding"]},
                "speedrunner": {"type": "object", "properties": {"finding": {"type": "string"}}, "required": ["finding"]},
                "auditor": {"type": "object", "properties": {"finding": {"type": "string"}}, "required": ["finding"]}
            },
            "required": ["griefer", "speedrunner", "auditor"]
        }

        print("[VIDEO] Generating Multimodal reasoning...")
        response = client.models.generate_content(
            model="models/gemini-3-pro-preview",
            contents=[uploaded_file, prompt],
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=response_schema,
                thinking_config=types.ThinkingConfig(thinking_budget=16000)
            )
        )

        result = response.parsed
        
        # Cleanup
        os.remove(local_path)

        return {
            "status": "complete",
            "mode": "REAL_MULTIMODAL_GEMINI_3",
            "agents": {
                "griefer": result.griefer.finding,
                "speedrunner": result.speedrunner.finding,
                "auditor": result.auditor.finding
            },
            "logs": [
                "🎥 MULTIMODAL PIPELINE ACTIVE",
                f"📂 {video.filename} uploaded and processed",
                "🧠 [VIDEO REASONING] Correlating frames with code symbols...",
                "✅ MULTIMODAL CONTEXTUAL ANALYSIS COMPLETE"
            ]
        }

    except Exception as e:
        print(f"[VIDEO ERROR] {e}")
        return {"status": "error", "message": str(e)}

@app.get("/domains")
async def get_domains():
    """Return available domains and their configurations"""
    return {
        "domains": {
            domain_key: {
                "title": config["title"],
                "agents": config["agents"]
            }
            for domain_key, config in DOMAIN_CONFIG.items()
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
