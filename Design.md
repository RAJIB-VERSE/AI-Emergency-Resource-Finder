# 🎨 Design – AI Emergency Resource Finder

## 1. Design Philosophy

- **Emergency-First**: Red/orange accents convey urgency without causing panic
- **Dark Mode Default**: Reduces eye strain, looks premium, modern feel
- **Card-Based Layout**: Clean information hierarchy
- **Accessible**: High contrast, readable fonts, clear iconography

## 2. Color Palette

### Primary Colors
| Token | Hex | Usage |
|---|---|---|
| `--bg-primary` | `#0E1117` | Main background (Streamlit dark) |
| `--bg-secondary` | `#1A1D23` | Card backgrounds |
| `--bg-tertiary` | `#262730` | Elevated surfaces |
| `--accent-primary` | `#FF4B4B` | Emergency red — CTAs, alerts |
| `--accent-secondary` | `#FF6B35` | Orange — warnings, fire |
| `--accent-gradient` | `linear-gradient(135deg, #FF4B4B, #FF6B35)` | Gradient buttons |

### Text Colors
| Token | Hex | Usage |
|---|---|---|
| `--text-primary` | `#FAFAFA` | Headings, primary text |
| `--text-secondary` | `#B0B8C1` | Body text, descriptions |
| `--text-muted` | `#6B7280` | Captions, footnotes |

### Marker Colors (Map)
| Service | Color | Folium Color |
|---|---|---|
| Hospital | Red | `red` |
| Police | Blue | `blue` |
| Fire Station | Orange | `orange` |
| Blood Bank | Dark Red | `darkred` |
| Pharmacy | Green | `green` |
| Shelter | Purple | `purple` |

### Status Colors
| Status | Hex | Usage |
|---|---|---|
| Success | `#10B981` | Found results |
| Warning | `#F59E0B` | Slow response, limited results |
| Error | `#EF4444` | API failure, no results |
| Info | `#3B82F6` | Tips, guidance |

## 3. Typography

### Font Stack
```css
/* Primary Font — clean, modern, highly readable */
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

### Type Scale
| Element | Size | Weight | Usage |
|---|---|---|---|
| Hero Title | 2.5rem | 800 | Landing page title |
| Section Title | 1.5rem | 700 | Section headings |
| Card Title | 1.1rem | 600 | Card headings |
| Body | 1rem | 400 | Regular text |
| Caption | 0.85rem | 400 | Subtitles, meta |
| Badge | 0.75rem | 600 | Tags, labels |

## 4. Component Design

### Cards
```
┌──────────────────────────┐
│  🏥 Icon + Title        │  ← Bold, accent color
│  ─────────────────────  │
│  📍 Address text         │  ← Muted text
│  📏 Distance: 2.3 km    │  ← Secondary text
│  🔗 View on Map         │  ← Accent link
└──────────────────────────┘
```
- Background: `--bg-secondary`
- Border: 1px solid rgba(255, 75, 75, 0.2)
- Border-radius: 12px
- Padding: 1.2rem
- Hover: subtle glow effect

### Buttons
- Primary: Gradient background (`--accent-gradient`)
- Border-radius: 8px
- Padding: 0.6rem 1.5rem
- Hover: brightness(1.1) + slight scale(1.02)
- Transition: all 0.3s ease

### Sidebar
- Used for: AI Assistant, Emergency Numbers
- Background: default Streamlit sidebar dark

### Map Container
- Full width within main column
- Border-radius: 12px
- Height: 500px
- Box-shadow: 0 4px 20px rgba(0,0,0,0.3)

## 5. Iconography (Emoji-Based)

| Element | Emoji | Usage |
|---|---|---|
| Hospital | 🏥 | Hospital markers/cards |
| Police | 🚔 | Police station markers |
| Fire | 🚒 | Fire station markers |
| Blood Bank | 🩸 | Blood bank markers |
| Pharmacy | 💊 | Pharmacy markers |
| Shelter | 🏠 | Shelter markers |
| Emergency | 🚨 | Alerts, warnings |
| Location | 📍 | Location input |
| AI | 🤖 | AI assistant |
| First Aid | ⛑️ | First aid section |
| Phone | 📞 | Emergency numbers |
| Search | 🔍 | Search actions |
| Heart | ❤️ | Heart attack |
| Snake | 🐍 | Snake bite |
| Fire | 🔥 | Fire emergency |
| Flood | 🌊 | Flood |
| Earthquake | 🌍 | Earthquake |

## 6. Layout Structure

```
┌─────────────────────────────────────────────┐
│              🚨 HERO SECTION                │
│     AI Emergency Resource Finder             │
│   Find nearest emergency services            │
└─────────────────────────────────────────────┘
┌──────────┐  ┌──────────────────────────────┐
│ SIDEBAR  │  │      MAIN CONTENT            │
│          │  │  ┌────────────────────────┐   │
│ 🤖 AI   │  │  │ Emergency Type Select  │   │
│ Assist   │  │  └────────────────────────┘   │
│          │  │  ┌────────────────────────┐   │
│ 📞 Emerg │  │  │ 📍 Location Input     │   │
│ Numbers  │  │  └────────────────────────┘   │
│          │  │  ┌────────────────────────┐   │
│ ⛑️ First │  │  │ 🗺️ Interactive Map    │   │
│ Aid Tips │  │  └────────────────────────┘   │
│          │  │  ┌──┐ ┌──┐ ┌──┐             │
│          │  │  │C1│ │C2│ │C3│  Results    │
│          │  │  └──┘ └──┘ └──┘             │
└──────────┘  └──────────────────────────────┘
┌─────────────────────────────────────────────┐
│              📎 FOOTER                       │
│     GitHub | LinkedIn | Made by Name         │
└─────────────────────────────────────────────┘
```

## 7. Animations & Transitions

- **Page Load**: Fade-in animation on hero section (CSS keyframe)
- **Cards**: Hover → translateY(-2px) + box-shadow increase
- **Buttons**: Hover → brightness + slight scale
- **Map**: Smooth zoom transitions (Folium default)
- **Spinners**: Streamlit native spinner during API calls
- **Status Messages**: Streamlit toast/success/error with auto-dismiss

## 8. Responsive Considerations

- Streamlit handles most responsiveness
- Cards use `st.columns()` — 3 columns on desktop, stack on mobile
- Map: full-width, fixed height
- Sidebar: collapsible on mobile (Streamlit default)
