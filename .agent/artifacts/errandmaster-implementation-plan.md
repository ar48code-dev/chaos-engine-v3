# ErrandMaster - Implementation Plan

## Project Overview
**ErrandMaster** is a Gemini 3-powered multimodal logistics optimizer that transforms messy inputs (photos, handwritten lists, voice memos, text) into ultra-optimized errand routes with time, money, and carbon savings.

## Tech Stack
- **Frontend**: React 18 + Vite (for fast dev experience)
- **Styling**: Tailwind CSS 3 with custom design system
- **AI Engine**: Google Gemini 3 SDK (`@google/generative-ai`)
- **Routing**: React Router DOM
- **State**: React Context API + Hooks
- **File Upload**: Native File API + drag-n-drop
- **Icons**: Lucide React
- **Deployment**: Vercel-ready

## Architecture

### 1. Multimodal Input Handler
- **Text Input**: Direct errand list entry
- **Image Upload**: Photos of receipts, handwritten lists, store names
- **Voice Support**: Speech-to-text integration
- **Drag & Drop**: Seamless file upload UX

### 2. Gemini 3 Integration Layer
```javascript
- Initialize Gemini 3 with API key from .env
- Use gemini-3-flash-preview for fast multimodal analysis
- Implement proper error handling and rate limiting
- Structured output parsing for JSON responses
```

### 3. Core Features

#### A. Multimodal Analysis Engine
- Upload images → Gemini 3 vision identifies stores, items, priorities
- Parse handwritten text from photos
- Extract structured data from receipts
- Voice memo transcription + intent analysis

#### B. Route Optimization Algorithm
- Calculate optimal path using traveling salesman approach
- Factor in: distance, store hours, traffic, user priorities
- Suggest intelligent bundling (nearby locations)
- Google Maps integration for real-time data

#### C. Smart Suggestions
- "Since you're at Target, the Post Office is next door—do both now"
- Store hours validation
- Traffic-aware timing
- Weather considerations

#### D. Analytics Dashboard
- Time saved (minutes)
- Money saved (USD)
- Carbon reduction (%)
- Route visualization

### 4. Response Schema (Strict JSON Output)
```json
{
  "summary": "One-sentence overview",
  "errands_detected": [
    {
      "location": "Target",
      "task": "Buy groceries",
      "priority": "high"
    }
  ],
  "optimized_route": [
    {
      "step": 1,
      "action": "Buy groceries",
      "location": "Target",
      "tip": "Store closes at 10 PM"
    }
  ],
  "stats": {
    "time_saved_mins": 25,
    "money_saved_usd": 12.50,
    "carbon_reduction": "15%"
  },
  "logic_trace": "Explanation of route choice"
}
```

## File Structure
```
errandmaster/
├── .env.example                 # API key template
├── .env                         # Real API key (gitignored)
├── .gitignore
├── package.json
├── vite.config.js
├── tailwind.config.js
├── postcss.config.js
├── index.html
├── README.md
└── src/
    ├── main.jsx                 # App entry
    ├── App.jsx                  # Main component
    ├── index.css                # Tailwind + custom styles
    ├── config/
    │   └── gemini.js            # Gemini 3 SDK setup
    ├── components/
    │   ├── InputPanel.jsx       # Multimodal input UI
    │   ├── ImageUpload.jsx      # Drag-n-drop upload
    │   ├── TextInput.jsx        # Text errand entry
    │   ├── RouteDisplay.jsx     # Optimized route visualization
    │   ├── StatsCard.jsx        # Savings metrics
    │   ├── ErrandCard.jsx       # Individual errand display
    │   └── LoadingState.jsx     # AI processing state
    ├── services/
    │   ├── geminiService.js     # Gemini 3 API calls
    │   └── routeOptimizer.js    # Optimization logic
    ├── utils/
    │   ├── jsonParser.js        # Safe JSON extraction
    │   └── validators.js        # Input validation
    └── hooks/
        ├── useErrandAnalysis.js # Main AI hook
        └── useImageUpload.js    # Upload handling
```

## Implementation Phases

### Phase 1: Project Setup ✓
- Initialize Vite + React project
- Install dependencies (Gemini SDK, Tailwind, Lucide)
- Configure Tailwind with premium design tokens
- Set up environment variables

### Phase 2: Design System ✓
- Create gradient-based color palette
- Define typography (Inter font)
- Build reusable UI components
- Implement glassmorphism effects
- Add micro-animations

### Phase 3: Gemini 3 Integration ✓
- Configure Gemini SDK with API key validation
- Implement multimodal prompt engineering
- Add error handling and retries
- Create structured output parser
- Test with real API calls

### Phase 4: Core Features ✓
- Build multimodal input panel
- Implement image upload + preview
- Create text input with smart parsing
- Add route optimization logic
- Build results visualization

### Phase 5: Polish & Optimization ✓
- Add loading states and animations
- Implement error boundaries
- Optimize performance
- Add responsive design
- Create demo mode for testing

### Phase 6: Testing & Deployment ✓
- Test with various input types
- Validate JSON parsing
- Check API error handling
- Deploy to Vercel
- Create demo video

## Gemini 3 Prompt Engineering

### System Prompt (Master Prompt)
```
ROLE: ErrandMaster AI Logistics Agent
You are an advanced logistics orchestrator powered by Gemini 3. Transform messy, multimodal inputs into ultra-optimized errand routes.

CAPABILITIES:
1. Multimodal Analysis: Identify stores, items, priorities from images
2. Spatial Reasoning: Calculate efficient paths
3. Agentic Action: Suggest intelligent bundling
4. Google Search Grounding: Real-time store hours/traffic

RESPONSE FORMAT (Strict JSON):
{
  "summary": "...",
  "errands_detected": [...],
  "optimized_route": [...],
  "stats": {...},
  "logic_trace": "..."
}

RULES:
- Professional, high-energy tone
- Flag impossible errands (closed stores)
- Date context: February 7, 2026
- No general advice, only specific solutions
```

### User Prompt Template
```
Analyze this errand input and create an optimized route:

[IMAGE: uploaded photo if present]

User's text: "{user_input}"

Provide:
1. Detected errands with locations and priorities
2. Optimal route with step-by-step actions
3. Time/money/carbon savings estimates
4. Brief logic explanation

Return ONLY valid JSON matching the schema.
```

## Design Specifications

### Color Palette (Modern & Vibrant)
- **Primary**: `hsl(262, 83%, 58%)` - Electric purple
- **Accent**: `hsl(142, 76%, 36%)` - Success green
- **Background**: `hsl(240, 10%, 3.9%)` - Deep dark
- **Card**: `hsl(240, 4%, 9%)` - Subtle elevation
- **Text**: `hsl(0, 0%, 98%)` - High contrast white

### Typography
- **Font**: Inter (Google Fonts)
- **Headings**: 700 weight
- **Body**: 400 weight
- **Code**: JetBrains Mono

### UI Components
1. **Hero Section**: Gradient background, animated title
2. **Input Panel**: Glassmorphic card with tabs (Text/Upload)
3. **Route Display**: Step-by-step cards with icons
4. **Stats Dashboard**: Animated counters for savings
5. **Loading State**: Pulsing gradient animation

## Security & Best Practices
- ✅ API key in `.env` (never committed)
- ✅ Input sanitization for XSS prevention
- ✅ Rate limiting for API calls
- ✅ Error boundaries for graceful failures
- ✅ CORS handling for production
- ✅ Image size validation (max 4MB)

## Testing Strategy
1. **Text Input**: "Buy milk at Target, return package at UPS, get gas"
2. **Image Input**: Photo of handwritten shopping list
3. **Mixed Input**: Text + receipt photo
4. **Edge Cases**: Closed stores, invalid locations, empty input
5. **API Errors**: Invalid key, rate limit, network failure

## Success Metrics
- ✅ Gemini 3 API working with real key
- ✅ Multimodal inputs processed correctly
- ✅ JSON output parsed 100% of the time
- ✅ Route optimization provides measurable savings
- ✅ UI feels premium and responsive
- ✅ No placeholder data or mocked responses

## Deployment Checklist
- [ ] Environment variables configured on Vercel
- [ ] Build passes without errors
- [ ] API key validation working
- [ ] SEO meta tags added
- [ ] README with setup instructions
- [ ] Demo video recorded
- [ ] Hackathon submission form completed

## Unique Selling Points (For Hackathon Pitch)
1. **True Multimodal**: Images, text, voice all processed seamlessly
2. **Real-World Impact**: Saves time, money, and reduces carbon
3. **Agentic Intelligence**: Proactive suggestions, not just routing
4. **Production-Ready**: Real API, error handling, beautiful UI
5. **2026-Ready**: Uses cutting-edge Gemini 3 capabilities

---

**Next Steps**: Generate all files and test with real Gemini 3 API key.
