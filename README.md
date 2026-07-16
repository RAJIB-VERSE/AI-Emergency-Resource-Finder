# 🚨 AI Emergency Resource Finder

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-7EBC6F?style=for-the-badge&logo=openstreetmap&logoColor=white)](https://openstreetmap.org)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

> **Find the nearest emergency services in seconds.** An AI-powered application that helps users quickly locate hospitals, blood banks, police stations, fire stations, pharmacies, and emergency shelters based on their location — with intelligent emergency guidance and first-aid tips.

🚀 **Live Demo:** [first-aid-ai-locator.streamlit.app](https://first-aid-ai-locator.streamlit.app)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🗺️ **Interactive Map** | Color-coded Folium map with emergency service markers |
| 🤖 **Generative AI** | Free-text emergency guidance via Qwen/Phi-3/Gemma HF models |
| 🏥 **6 Service Types** | Hospitals, Blood Banks, Police, Fire, Pharmacies, Shelters |
| 🌐 **Multi-Language** | Instantly translate the UI between English, Hindi, and Bengali |
| 📥 **CSV Export** | Download your local emergency search results instantly |
| ⛑️ **First Aid Tips** | Context-sensitive first-aid instructions for each emergency |
| 📞 **1-Tap Dialing** | `tel:` links on emergency numbers for instant mobile dialing |
| 📋 **Copy Address** | One-click clipboard button for all service addresses |
| 🌓 **Dark/Light Mode** | Premium UI with Font Awesome icons and live theme toggling |
| 🆓 **100% Free Core** | No API keys required for mapping — uses OpenStreetMap |

---

## 🏗️ Architecture

```
User Input (City + Emergency Type)
  → Geopy geocodes city to (lat, lon)
  → Overpass API queries nearby services
  → Results sorted by distance
  → Folium renders interactive map
  → AI classifies emergency from free text
  → First-aid tips displayed contextually
  → Streamlit renders everything
```

### Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Maps | Folium + streamlit-folium |
| Map Data | Overpass API (OpenStreetMap) |
| Geocoding | Geopy (Nominatim) |
| AI | HuggingFace Inference API + Local Fallback |
| Deployment | Hugging Face Spaces |

---

## 📁 Project Structure

```
AI-Emergency-Resource-Finder/
├── app.py                  # Main Streamlit application
├── ai_helper.py            # AI emergency classifier & recommendations
├── map_utils.py            # Overpass API queries & Folium map
├── utils.py                # Geocoding, distance calc, CSS, constants
├── first_aid.py            # First-aid knowledge base
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── LICENSE                 # MIT License
├── .gitignore              # Git ignore rules
├── PRD.md                  # Product Requirements Document
├── Architecture.md         # System architecture
├── Rules.md                # Development rules
├── Phases.md               # Development phases
├── Design.md               # UI/UX design system
├── Memory.md               # Development context tracker
├── assets/                 # Static assets
│   ├── logo.png            # App logo
│   └── banner.png          # Hero banner
└── screenshots/            # App screenshots
```

---

## 🚀 Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/AI-Emergency-Resource-Finder.git
   cd AI-Emergency-Resource-Finder
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux/Mac
   venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   - The app will open at `http://localhost:8501`

### Optional: HuggingFace API Token

For enhanced AI classification, set a HuggingFace API token:
```bash
export HF_API_TOKEN="<YOUR_HUGGINGFACE_TOKEN>"    # Linux/Mac
set HF_API_TOKEN=<YOUR_HUGGINGFACE_TOKEN>         # Windows
```
> The app works fully without a token — it falls back to local keyword matching.

---

## 📸 Screenshots

> Screenshots will be added after deployment.

| Landing Page | Map View | AI Assistant |
|---|---|---|
| *Coming soon* | *Coming soon* | *Coming soon* |

---

## 🔮 Future Improvements

- [ ] Real-time ambulance tracking integration
- [ ] Browser geolocation (GPS) support
- [ ] Multi-language support (Hindi, Tamil, Telugu, etc.)
- [ ] Push notifications for disaster alerts
- [ ] SQLite database for caching frequent searches
- [ ] User accounts & saved locations
- [ ] Voice input for emergency descriptions
- [ ] Integration with Google Maps directions
- [ ] Offline mode with cached data
- [ ] PWA (Progressive Web App) support

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m "Add your feature"`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [OpenStreetMap](https://www.openstreetmap.org) — Free map data
- [Overpass API](https://overpass-api.de) — OSM data queries
- [Streamlit](https://streamlit.io) — Web app framework
- [Folium](https://python-visualization.github.io/folium/) — Interactive maps
- [HuggingFace](https://huggingface.co) — AI model inference
- [Geopy](https://geopy.readthedocs.io) — Geocoding

---

<p align="center">
  Made with ❤️ by <strong>AI Emergency Team</strong><br>
  <sub>🚨 In a real emergency, always call your local emergency number first.</sub>
</p>
