# 🧠 Memory — AI Emergency Resource Finder

> This file tracks development progress and context for AI assistants.
> Updated as features are completed.

## Last Updated
2026-07-17

## Project Status
✅ **Complete — v2.0 Ready**

## Version History

### v2.0 — Enhanced Release
- Upgraded AI to generative models (Qwen 2.5 3B / Phi-3 / Gemma 2B) via HF Inference API
- Added Font Awesome 6 icons throughout UI
- Added Dark/Light mode toggle with session state persistence
- Added multi-language support (English / Hindi / Bengali) via translations.py
- Added copy-to-clipboard button on service cards (JavaScript clipboard API)
- Added emergency dial links (tel: scheme) on number cards and service cards
- Added CSV export of search results via pandas
- Added python-dotenv for .env file support
- Added AI generative response box with model badge
- Updated CSS with parameterized dark/light color variables

### v1.0 — Initial Release
- Full Streamlit app with Overpass API, Folium maps, keyword AI classifier
- First-aid tips, emergency numbers, CPR guide
- Custom dark-mode CSS with gradient accents

## Completed Modules

### utils.py
- Geocoding (Geopy/Nominatim), haversine distance
- Emergency type constants with Font Awesome icon mappings
- Emergency numbers with dial links
- Custom CSS function with dark_mode parameter (dark/light themes)
- HTML card renderers with copy-to-clipboard and tel: dial buttons
- Font Awesome 6 CDN injection

### map_utils.py
- Overpass API integration for 6 service types
- Result parsing with deduplication and distance sorting
- Folium map with CartoDB dark_matter tiles, color-coded markers, popups, tooltips, legend

### ai_helper.py
- HuggingFace Inference API: zero-shot classification (facebook/bart-large-mnli)
- HuggingFace Inference API: generative guidance (Qwen 2.5 → Phi-3 → Gemma 2B failover)
- Local keyword-based fallback classifier
- Unified classify_emergency() with auto-fallback
- generate_ai_guidance() for free-text emergency recommendations
- Curated static recommendations for all 9 emergency types
- python-dotenv integration for HF_API_TOKEN

### first_aid.py
- First-aid knowledge base for 9 emergency types
- Steps, do's, don'ts, call_when for each type
- CPR quick guide

### translations.py (NEW in v2.0)
- ~50 translated string keys
- 3 languages: English (en), Hindi (hi), Bengali (bn)
- t(key, lang) lookup function
- Covers all UI labels, section headers, button text, emergency types, service labels

### app.py
- Dark/Light mode toggle in sidebar with st.session_state
- Language selector (English / Hindi / Bengali)
- AI assistant with both classification + generative response
- Hero section with Font Awesome icons
- Emergency type selector (translated)
- City geocoding + Folium map display
- 3-column result cards with copy/dial buttons
- CSV export via st.download_button + pandas
- First-aid tips section
- Footer with FA GitHub/LinkedIn icons

## Architecture
```
app.py → imports → utils.py (geocoding, CSS, constants)
                 → map_utils.py (Overpass API, Folium)
                 → ai_helper.py (HF generative + classifier + keyword)
                 → first_aid.py (first-aid knowledge base)
                 → translations.py (multi-language strings)
```

## Environment Variables
- `HF_API_TOKEN` (optional) — HuggingFace API token for generative AI and better classification
- Template at `.env.example`

## Key Decisions (v2.0)
1. Generative models via HF Inference API (not local torch) — keeps deployment lightweight
2. Model failover chain: Qwen 2.5 → Phi-3 → Gemma 2B → keyword fallback
3. Font Awesome via CDN (not local) — always up to date
4. Dark/light mode via CSS variables — single function, parameterized
5. Translations as simple dict lookup — no heavy i18n library
6. CSV export with pandas — user can download all found services
