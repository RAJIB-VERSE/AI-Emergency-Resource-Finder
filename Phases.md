# 📅 Phases – AI Emergency Resource Finder

## Phase 1: Foundation & Core Infrastructure
**Goal**: Get the app skeleton running with basic UI and geocoding.

### Tasks
1. Create project structure (all files and folders)
2. Set up `requirements.txt` with all dependencies
3. Build `utils.py` — geocoding, distance calculations, emergency data constants
4. Build basic `app.py` — Streamlit page config, custom CSS, landing page header
5. Add city input and emergency type selector
6. Verify: `streamlit run app.py` launches without errors

### Deliverables
- Running Streamlit app with landing page
- City → coordinates conversion working
- Emergency type dropdown functional

---

## Phase 2: Map & Location Services
**Goal**: Fetch nearby emergency services and display on an interactive map.

### Tasks
1. Build `map_utils.py` — Overpass API queries for all 6 service types
2. Implement service search with distance calculation and sorting
3. Create Folium map with color-coded markers and popups
4. Display results in styled cards (name, distance, address, OSM link)
5. Integrate map into `app.py`

### Deliverables
- Overpass API integration working
- Interactive Folium map with markers
- Results displayed as cards below map

---

## Phase 3: AI Assistant & First Aid
**Goal**: Add AI-powered emergency guidance and first-aid tips.

### Tasks
1. Build `ai_helper.py` — HuggingFace Inference API integration
2. Implement keyword-based fallback classifier
3. Build `first_aid.py` — comprehensive first-aid tips database
4. Add AI chat interface in sidebar
5. Display first-aid tips based on emergency type
6. Add medical disclaimer

### Deliverables
- AI assistant classifies emergencies and provides guidance
- First-aid tips display contextually
- Medical disclaimer shown

---

## Phase 4: Polish & Documentation
**Goal**: Final UI polish, emergency numbers, footer, and documentation.

### Tasks
1. Add emergency numbers section
2. Add footer with social links
3. Polish all CSS (animations, hover effects, transitions)
4. Generate assets (logo, banner) 
5. Write comprehensive `README.md`
6. Create `LICENSE` file
7. Create `.gitignore`
8. Create `Memory.md` with development progress
9. Final testing — all features working end-to-end

### Deliverables
- Complete, polished application
- All documentation files
- Ready for deployment

---

## Phase Summary

| Phase | Focus | Estimated Effort |
|---|---|---|
| Phase 1 | Foundation & UI | Core setup |
| Phase 2 | Maps & Services | API integration |
| Phase 3 | AI & First Aid | Intelligence layer |
| Phase 4 | Polish & Docs | Production quality |

## Dependencies

```
Phase 1 → Phase 2 (needs geocoding)
Phase 1 → Phase 3 (needs UI skeleton)  
Phase 2 + Phase 3 → Phase 4 (needs all features)
```
