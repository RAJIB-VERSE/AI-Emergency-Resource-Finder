# 🏗️ Architecture – AI Emergency Resource Finder

## 1. System Architecture

```
┌──────────────────────────────────────────────────────┐
│                   STREAMLIT FRONTEND                  │
│  ┌─────────┐ ┌───────────┐ ┌──────────┐ ┌─────────┐ │
│  │ Landing  │ │ Emergency │ │ Location │ │   Map   │ │
│  │  Page    │ │ Selector  │ │  Input   │ │  View   │ │
│  └─────────┘ └───────────┘ └──────────┘ └─────────┘ │
│  ┌─────────┐ ┌───────────┐ ┌──────────┐ ┌─────────┐ │
│  │   AI    │ │ Emergency │ │ First Aid│ │ Results │ │
│  │ Assist  │ │ Numbers   │ │  Tips    │ │  Cards  │ │
│  └────┬────┘ └───────────┘ └──────────┘ └─────────┘ │
└───────┼──────────────────────────────────────────────┘
        │
┌───────┴──────────────────────────────────────────────┐
│                   PYTHON BACKEND                      │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌─────────┐ │
│  │ ai_helper│ │map_utils  │ │  utils   │ │first_aid│ │
│  │   .py    │ │   .py     │ │   .py    │ │   .py   │ │
│  └────┬─────┘ └────┬──────┘ └────┬─────┘ └─────────┘ │
└───────┼────────────┼────────────┼───────────────────┘
        │            │            │
┌───────┴────┐ ┌─────┴──────┐ ┌──┴──────────┐
│ HuggingFace│ │  Overpass  │ │   Geopy     │
│ Inference  │ │    API     │ │ (Nominatim) │
│    API     │ │(OSM Data)  │ │             │
└────────────┘ └────────────┘ └─────────────┘
```

## 2. Data Flow

```
User Input (City/Emergency) 
  → Geopy geocodes city → (lat, lon)
  → Overpass API queries nearby services
  → Results processed (distance, sorting)
  → Folium renders map with markers
  → AI Assistant processes emergency text
  → Streamlit renders everything
```

## 3. File & Folder Structure

```
AI-Emergency-Resource-Finder/
├── app.py                 # Main Streamlit application entry point
├── ai_helper.py           # AI assistant (HF Inference API / local pipeline)
├── map_utils.py           # Folium map generation, Overpass API queries
├── utils.py               # Geocoding, distance calculations, emergency data
├── first_aid.py           # First aid tips database and retrieval
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── LICENSE                # MIT License
├── .gitignore             # Git ignore rules
├── PRD.md                 # Product Requirements Document
├── Architecture.md        # This file
├── Rules.md               # Development rules & constraints
├── Phases.md              # Development phases
├── Design.md              # UI/UX design system
├── Memory.md              # AI development context tracker
├── assets/                # Static assets
│   ├── logo.png           # App logo (generated)
│   └── banner.png         # Hero banner (generated)
└── screenshots/           # App screenshots for README
```

## 4. Technology Stack

| Layer | Technology | Purpose |
|---|---|---|
| Frontend | Streamlit | UI framework |
| Styling | Custom CSS in Streamlit | Dark mode, gradients, cards |
| Maps | Folium + streamlit-folium | Interactive map rendering |
| Map Data | Overpass API (OpenStreetMap) | Emergency service locations |
| Geocoding | Geopy (Nominatim) | City → coordinates |
| AI | HuggingFace Inference API | Emergency text analysis |
| AI Fallback | Local keyword matching | Offline emergency detection |
| Deployment | Hugging Face Spaces | Streamlit SDK hosting |

## 5. API Integrations

### Overpass API
- **Endpoint**: `https://overpass-api.de/api/interpreter`
- **Method**: POST with Overpass QL queries
- **Rate Limit**: Respectful usage, 1 query at a time
- **Data**: Returns JSON with nodes/ways matching amenity types

### Geopy Nominatim
- **Service**: OpenStreetMap Nominatim
- **Method**: Geocode city name → (latitude, longitude)
- **User-Agent**: Required (app name)

### HuggingFace Inference API
- **Model**: `facebook/bart-large-mnli` (zero-shot classification)
- **Fallback**: Local keyword-based emergency detection
- **Purpose**: Classify emergency type from free-text input

## 6. Key Design Decisions

1. **No Database (v1)**: All data is fetched live from APIs — keeps deployment simple
2. **Keyword Fallback for AI**: If HF API is unavailable, use local keyword matching
3. **Overpass API over Google Maps**: 100% free, no API key required
4. **Folium over Plotly**: Better OSM integration, lighter weight
5. **Streamlit over Flask**: Faster development, built-in widgets, HF Spaces compatible
