# 📋 PRD – AI Emergency Resource Finder

## 1. Product Overview

**AI Emergency Resource Finder** is a Streamlit-based web application that helps users quickly locate nearby emergency services (hospitals, blood banks, police stations, fire stations, pharmacies, and emergency shelters) based on their current location or a manually entered city. It also provides an AI-powered assistant for emergency guidance, first-aid tips, and emergency contact numbers.

## 2. Problem Statement

During emergencies, people often panic and waste critical time searching for the nearest hospital, police station, or other emergency services. Existing map applications require multiple steps and don't provide contextual emergency guidance. This app provides a one-stop solution that combines location-based service discovery with AI-powered emergency advice.

## 3. Target Users

| User Segment | Use Case |
|---|---|
| General Public | Find nearest hospital, police, fire station during emergencies |
| Travelers | Locate emergency services in unfamiliar cities |
| Caregivers | Quick access to first-aid tips and AI guidance |
| Students / Portfolio Viewers | Evaluate as a technical project |

## 4. Goals

- **Speed**: Users should find emergency services within 5 seconds of entering location
- **Accuracy**: Display real, verified locations from OpenStreetMap data
- **AI Guidance**: Provide contextual emergency recommendations
- **Accessibility**: Work on any device with a modern browser
- **Portfolio Quality**: Professional UI, clean code, comprehensive documentation

## 5. Feature Requirements

### 5.1 Landing Page (P0)
- Branded title with emergency theme
- Subtitle: "Find the nearest emergency services in seconds."
- Modern dark-mode UI with icons and gradient accents
- Responsive layout

### 5.2 Emergency Type Selector (P0)
- Dropdown with emergency categories:
  - Road Accident, Heart Attack, Fire, Flood, Earthquake, Pregnancy, Snake Bite, Blood Requirement, Medical Emergency

### 5.3 Location Input (P0)
- City name text input with geocoding via Geopy
- Fallback to manual city entry

### 5.4 Nearby Services Search (P0)
- Query OpenStreetMap Overpass API for:
  - Hospitals, Blood Banks, Police Stations, Fire Stations, Pharmacies, Shelters
- Display results with: Name, Distance, Address, OpenStreetMap Link

### 5.5 Interactive Map (P0)
- Folium map with color-coded markers
- Marker categories: Hospital (red), Police (blue), Fire (orange), Blood Bank (darkred), Pharmacy (green), Shelter (purple)
- Popup info on each marker

### 5.6 AI Assistant (P1)
- Text input for emergency description
- AI identifies emergency type, recommends actions, suggests resources
- Medical disclaimer displayed

### 5.7 Emergency Numbers (P1)
- Display key emergency numbers (Police, Fire, Ambulance, Women Helpline, Child Helpline)

### 5.8 First Aid Tips (P1)
- Context-sensitive first-aid guidance based on selected emergency type

### 5.9 Footer (P2)
- GitHub link, LinkedIn link, author credit

## 6. Non-Functional Requirements

- **Performance**: Page load < 3s, API queries < 5s
- **Error Handling**: Graceful degradation if APIs are unavailable
- **Code Quality**: Type hints, docstrings, modular architecture
- **Deployment**: Compatible with Hugging Face Spaces (Streamlit SDK)

## 7. Out of Scope (v1)

- User authentication
- Real-time ambulance tracking
- Push notifications
- Database persistence (SQLite deferred to v2)
- Browser geolocation (requires HTTPS, deferred)

## 8. Success Metrics

- App runs locally with `streamlit run app.py` without errors
- All 6 service types discoverable on map
- AI assistant provides relevant guidance
- Deployable to Hugging Face Spaces
