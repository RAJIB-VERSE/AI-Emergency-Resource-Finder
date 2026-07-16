# 📏 Rules – AI Emergency Resource Finder

## 1. Library Rules

### ✅ ALLOWED Libraries
| Library | Version | Purpose |
|---|---|---|
| streamlit | >=1.28.0 | UI framework |
| folium | >=0.15.0 | Interactive maps |
| streamlit-folium | >=0.17.0 | Folium ↔ Streamlit bridge |
| geopy | >=2.4.0 | Geocoding |
| requests | >=2.31.0 | HTTP requests to Overpass API |
| huggingface-hub | >=0.19.0 | HF Inference API |
| transformers | >=4.36.0 | Local AI pipeline (optional) |
| math (stdlib) | — | Distance calculations |
| json (stdlib) | — | JSON parsing |

### ❌ FORBIDDEN Libraries
- Google Maps API (requires payment)
- Mapbox (requires API key)
- Any paid API service
- Flask/Django (using Streamlit instead)
- Pandas (unnecessary complexity for this project)
- NumPy (unnecessary for this project)

## 2. Code Rules

### Python Style
- Follow PEP 8
- Use type hints on all function signatures
- Write docstrings for all functions (Google style)
- Maximum function length: 40 lines
- Maximum file length: 300 lines
- Use f-strings for string formatting

### Error Handling
- Wrap ALL API calls in try/except blocks
- Never expose raw error messages to users
- Show user-friendly error messages with st.error()
- Log errors with context for debugging
- Provide fallback behavior when APIs fail

### Naming Conventions
- Functions: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Classes: `PascalCase` (if any)
- Files: `snake_case.py`

## 3. AI Rules

### What AI SHOULD Do
- Classify emergency type from free text
- Provide first-aid recommendations
- Suggest which emergency service to contact
- Always show medical disclaimer

### What AI SHOULD NOT Do
- Provide medical diagnoses
- Recommend specific medications or dosages
- Replace professional medical advice
- Store or process personal health data
- Make claims about response times

### Disclaimer (MUST be shown)
> ⚠️ **Disclaimer**: This AI assistant provides general guidance only. It is NOT a substitute for professional medical advice, diagnosis, or treatment. In case of a medical emergency, call your local emergency number immediately.

## 4. API Rules

### Overpass API
- Maximum search radius: 10,000 meters (10 km)
- Default search radius: 5,000 meters (5 km)
- Timeout: 25 seconds per query
- Retry: 1 retry with exponential backoff
- User-Agent: "AIEmergencyResourceFinder/1.0"

### Geopy Nominatim
- User-Agent: "AIEmergencyResourceFinder/1.0"
- Timeout: 10 seconds
- One request at a time (rate limit compliance)

### HuggingFace Inference API
- Use free tier (no API key required for public models)
- Fallback to local keyword matching if API fails
- Timeout: 15 seconds

## 5. Security Rules

- No API keys hardcoded in source code
- No user data stored or logged
- No personal health information persisted
- All external links open in new tabs
- Input sanitization on city names

## 6. UI Rules

- Dark mode as default theme
- All interactive elements must have loading states
- Error states must be user-friendly
- Emojis used for visual clarity, not decoration overload
- Maps must be responsive
- Cards must have consistent styling
- Maximum 3 columns in any row
