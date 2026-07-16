"""
utils.py — Core Utilities for AI Emergency Resource Finder

Provides geocoding, distance calculations, emergency data constants,
custom CSS (dark/light mode), Font Awesome icons, and HTML card renderers
with copy-to-clipboard and emergency dial links.
"""

import math
from typing import Optional
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable


# ─────────────────────────────────────────────
# Constants
# ─────────────────────────────────────────────

APP_NAME: str = "AI Emergency Resource Finder"
APP_SUBTITLE: str = "Find the nearest emergency services in seconds."
APP_VERSION: str = "2.0.0"
AUTHOR_NAME: str = "Rajib"
GITHUB_URL: str = "https://github.com/RAJIB-VERSE"
LINKEDIN_URL: str = "https://www.linkedin.com/in/rajib-chatterjee-bb5963369"

# Default search radius in meters
DEFAULT_SEARCH_RADIUS: int = 5000
MAX_SEARCH_RADIUS: int = 10000

# Overpass API endpoint
OVERPASS_API_URL: str = "https://overpass-api.de/api/interpreter"

# Nominatim user agent
NOMINATIM_USER_AGENT: str = "AIEmergencyResourceFinder/2.0"


# ─────────────────────────────────────────────
# Emergency Types
# ─────────────────────────────────────────────

EMERGENCY_TYPES: dict[str, dict[str, str]] = {
    "Road Accident": {
        "icon": "🚗💥",
        "fa_icon": "fa-car-burst",
        "description": "Vehicle collision or road accident",
        "services": "hospital,police",
        "color": "#EF4444",
    },
    "Heart Attack": {
        "icon": "❤️‍🩹",
        "fa_icon": "fa-heart-pulse",
        "description": "Chest pain, cardiac arrest, or heart-related emergency",
        "services": "hospital",
        "color": "#DC2626",
    },
    "Fire": {
        "icon": "🔥",
        "fa_icon": "fa-fire",
        "description": "Building fire, wildfire, or fire-related emergency",
        "services": "fire_station,hospital",
        "color": "#F97316",
    },
    "Flood": {
        "icon": "🌊",
        "fa_icon": "fa-water",
        "description": "Flooding, water damage, or water rescue needed",
        "services": "shelter,police",
        "color": "#3B82F6",
    },
    "Earthquake": {
        "icon": "🌍💔",
        "fa_icon": "fa-house-crack",
        "description": "Earthquake, structural collapse, or seismic emergency",
        "services": "shelter,hospital",
        "color": "#8B5CF6",
    },
    "Pregnancy": {
        "icon": "🤰",
        "fa_icon": "fa-baby",
        "description": "Pregnancy complication, labor, or delivery emergency",
        "services": "hospital",
        "color": "#EC4899",
    },
    "Snake Bite": {
        "icon": "🐍",
        "fa_icon": "fa-spaghetti-monster-flying",
        "description": "Venomous snake bite or animal attack",
        "services": "hospital",
        "color": "#10B981",
    },
    "Blood Requirement": {
        "icon": "🩸",
        "fa_icon": "fa-droplet",
        "description": "Urgent blood donation or transfusion needed",
        "services": "blood_bank,hospital",
        "color": "#B91C1C",
    },
    "Medical Emergency": {
        "icon": "🚑",
        "fa_icon": "fa-truck-medical",
        "description": "General medical emergency requiring immediate attention",
        "services": "hospital,pharmacy",
        "color": "#06B6D4",
    },
}


# ─────────────────────────────────────────────
# Emergency Contact Numbers (India)
# ─────────────────────────────────────────────

EMERGENCY_NUMBERS: dict[str, dict[str, str]] = {
    "Police": {"number": "100", "icon": "🚔", "fa_icon": "fa-shield-halved"},
    "Fire": {"number": "101", "icon": "🚒", "fa_icon": "fa-fire-extinguisher"},
    "Ambulance": {"number": "102", "icon": "🚑", "fa_icon": "fa-truck-medical"},
    "Emergency (Universal)": {"number": "112", "icon": "🆘", "fa_icon": "fa-phone-volume"},
    "Women Helpline": {"number": "1091", "icon": "👩", "fa_icon": "fa-person-dress"},
    "Child Helpline": {"number": "1098", "icon": "👶", "fa_icon": "fa-child"},
    "Disaster Management": {"number": "1078", "icon": "🌪️", "fa_icon": "fa-tornado"},
}


# ─────────────────────────────────────────────
# Service Icons
# ─────────────────────────────────────────────

SERVICE_ICONS: dict[str, str] = {
    "hospital": "🏥",
    "police": "🚔",
    "fire_station": "🚒",
    "blood_bank": "🩸",
    "pharmacy": "💊",
    "shelter": "🏠",
}

SERVICE_FA_ICONS: dict[str, str] = {
    "hospital": "fa-hospital",
    "police": "fa-shield-halved",
    "fire_station": "fa-fire-extinguisher",
    "blood_bank": "fa-droplet",
    "pharmacy": "fa-pills",
    "shelter": "fa-house-chimney",
}

SERVICE_LABELS: dict[str, str] = {
    "hospital": "Hospitals",
    "police": "Police Stations",
    "fire_station": "Fire Stations",
    "blood_bank": "Blood Banks",
    "pharmacy": "Pharmacies",
    "shelter": "Shelters",
}


# ─────────────────────────────────────────────
# Geocoding Functions
# ─────────────────────────────────────────────

def geocode_city(city: str) -> Optional[tuple[float, float, str]]:
    """
    Convert a city name to geographic coordinates using Nominatim.

    Args:
        city: Name of the city to geocode.

    Returns:
        Tuple of (latitude, longitude, display_name) or None if geocoding fails.
    """
    try:
        geolocator = Nominatim(user_agent=NOMINATIM_USER_AGENT, timeout=10)
        location = geolocator.geocode(city)
        if location:
            return (location.latitude, location.longitude, location.address)
        return None
    except (GeocoderTimedOut, GeocoderUnavailable) as e:
        print(f"Geocoding error for '{city}': {e}")
        return None
    except Exception as e:
        print(f"Unexpected geocoding error for '{city}': {e}")
        return None


# ─────────────────────────────────────────────
# Distance Calculation
# ─────────────────────────────────────────────

def haversine_distance(
    lat1: float, lon1: float, lat2: float, lon2: float
) -> float:
    """
    Calculate the great-circle distance between two points on Earth
    using the Haversine formula.

    Args:
        lat1: Latitude of point 1 (degrees).
        lon1: Longitude of point 1 (degrees).
        lat2: Latitude of point 2 (degrees).
        lon2: Longitude of point 2 (degrees).

    Returns:
        Distance in kilometers.
    """
    R = 6371.0  # Earth's radius in kilometers

    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return round(R * c, 2)


# ─────────────────────────────────────────────
# Custom CSS — Dark Mode (default)
# ─────────────────────────────────────────────

def get_emergency_css(dark_mode: bool = True) -> str:
    """
    Returns custom CSS for the emergency-themed UI.
    Supports both dark and light mode.

    Args:
        dark_mode: If True, returns dark theme. If False, returns light theme.

    Returns:
        CSS string to inject via st.markdown.
    """
    # Theme-specific variables
    if dark_mode:
        bg_primary = "#0E1117"
        bg_card = "#1A1D23"
        bg_card_end = "#1E2128"
        bg_hover = "#22252D"
        text_primary = "#FAFAFA"
        text_secondary = "#B0B8C1"
        text_muted = "#6B7280"
        border_subtle = "rgba(255, 75, 75, 0.15)"
        border_hover = "rgba(255, 75, 75, 0.4)"
        card_shadow = "rgba(0, 0, 0, 0.3)"
        ai_border = "rgba(59, 130, 246, 0.25)"
        firstaid_border = "rgba(16, 185, 129, 0.2)"
    else:
        bg_primary = "#F8FAFC"
        bg_card = "#FFFFFF"
        bg_card_end = "#F1F5F9"
        bg_hover = "#E2E8F0"
        text_primary = "#0F172A"
        text_secondary = "#475569"
        text_muted = "#94A3B8"
        border_subtle = "rgba(255, 75, 75, 0.2)"
        border_hover = "rgba(255, 75, 75, 0.5)"
        card_shadow = "rgba(0, 0, 0, 0.08)"
        ai_border = "rgba(59, 130, 246, 0.3)"
        firstaid_border = "rgba(16, 185, 129, 0.3)"

    return f"""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        /* ── Import Google Font ── */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

        /* ── Global Styles ── */
        .stApp {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }}

        /* ── Hero Section ── */
        .hero-container {{
            text-align: center;
            padding: 2rem 1rem 1.5rem 1rem;
            margin-bottom: 1.5rem;
            background: linear-gradient(135deg, rgba(255, 75, 75, 0.08) 0%, rgba(255, 107, 53, 0.08) 50%, rgba(139, 92, 246, 0.08) 100%);
            border-radius: 16px;
            border: 1px solid {border_subtle};
            animation: fadeInDown 0.8s ease-out;
        }}

        .hero-title {{
            font-size: 2.6rem;
            font-weight: 800;
            background: linear-gradient(135deg, #FF4B4B, #FF6B35, #FF4B4B);
            background-size: 200% 200%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: gradientShift 4s ease infinite;
            margin-bottom: 0.3rem;
            line-height: 1.2;
        }}

        .hero-subtitle {{
            font-size: 1.15rem;
            color: {text_secondary};
            font-weight: 400;
            margin-bottom: 0.5rem;
        }}

        .hero-icons {{
            font-size: 1.8rem;
            letter-spacing: 0.5rem;
            margin-top: 0.5rem;
        }}

        /* ── Animations ── */
        @keyframes fadeInDown {{
            from {{ opacity: 0; transform: translateY(-20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        @keyframes fadeInUp {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        @keyframes gradientShift {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}

        @keyframes pulseGlow {{
            0%, 100% {{ box-shadow: 0 0 5px rgba(255, 75, 75, 0.3); }}
            50% {{ box-shadow: 0 0 20px rgba(255, 75, 75, 0.5); }}
        }}

        /* ── Service Cards ── */
        .service-card {{
            background: linear-gradient(145deg, {bg_card}, {bg_card_end});
            border: 1px solid {border_subtle};
            border-radius: 12px;
            padding: 1.2rem;
            margin-bottom: 0.8rem;
            transition: all 0.3s ease;
            animation: fadeInUp 0.5s ease-out;
        }}

        .service-card:hover {{
            transform: translateY(-3px);
            border-color: {border_hover};
            box-shadow: 0 8px 25px {card_shadow};
        }}

        .service-card h4 {{
            margin: 0 0 0.5rem 0;
            font-size: 1.05rem;
            font-weight: 600;
            color: {text_primary};
        }}

        .service-card p {{
            margin: 0.2rem 0;
            font-size: 0.88rem;
            color: {text_secondary};
        }}

        .service-card .distance-badge {{
            display: inline-block;
            background: linear-gradient(135deg, #FF4B4B, #FF6B35);
            color: white;
            padding: 0.2rem 0.6rem;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
            margin-top: 0.4rem;
        }}

        .service-card a {{
            color: #FF6B35;
            text-decoration: none;
            font-weight: 500;
            font-size: 0.85rem;
        }}

        .service-card a:hover {{
            color: #FF4B4B;
            text-decoration: underline;
        }}

        .service-card .card-actions {{
            display: flex;
            gap: 0.6rem;
            margin-top: 0.6rem;
            flex-wrap: wrap;
            align-items: center;
        }}

        .service-card .btn-copy, .service-card .btn-dial {{
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
            padding: 0.25rem 0.6rem;
            border-radius: 6px;
            font-size: 0.78rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s ease;
            border: none;
            text-decoration: none;
        }}

        .service-card .btn-copy {{
            background: rgba(59, 130, 246, 0.12);
            color: #60A5FA;
        }}

        .service-card .btn-copy:hover {{
            background: rgba(59, 130, 246, 0.25);
        }}

        .service-card .btn-dial {{
            background: rgba(16, 185, 129, 0.12);
            color: #34D399;
        }}

        .service-card .btn-dial:hover {{
            background: rgba(16, 185, 129, 0.25);
        }}

        /* ── Section Headers ── */
        .section-header {{
            font-size: 1.4rem;
            font-weight: 700;
            color: {text_primary};
            margin: 1.5rem 0 1rem 0;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid rgba(255, 75, 75, 0.3);
        }}

        /* ── Emergency Number Cards ── */
        .emergency-number-card {{
            background: linear-gradient(145deg, {bg_card}, {bg_card_end});
            border: 1px solid rgba(255, 75, 75, 0.12);
            border-radius: 10px;
            padding: 0.7rem 1rem;
            margin-bottom: 0.5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: all 0.2s ease;
        }}

        .emergency-number-card:hover {{
            border-color: rgba(255, 75, 75, 0.35);
            background: linear-gradient(145deg, {bg_card_end}, {bg_hover});
        }}

        .emergency-number-card .number {{
            font-size: 1.15rem;
            font-weight: 700;
            color: #FF4B4B;
            letter-spacing: 1px;
        }}

        .emergency-number-card .number a {{
            color: #FF4B4B;
            text-decoration: none;
        }}

        .emergency-number-card .number a:hover {{
            text-decoration: underline;
        }}

        .emergency-number-card .label {{
            font-size: 0.88rem;
            color: {text_secondary};
        }}

        .emergency-number-card .fa-icon {{
            color: #FF6B35;
            margin-right: 0.4rem;
            width: 18px;
            text-align: center;
        }}

        /* ── AI Chat ── */
        .ai-response-box {{
            background: linear-gradient(145deg, {bg_card}, {bg_card_end});
            border: 1px solid {ai_border};
            border-radius: 12px;
            padding: 1.2rem;
            margin-top: 0.8rem;
            animation: fadeInUp 0.4s ease-out;
        }}

        .ai-response-box h4 {{
            color: #60A5FA;
            margin: 0 0 0.6rem 0;
            font-size: 1rem;
        }}

        .ai-response-box p, .ai-response-box li {{
            color: {text_secondary};
            font-size: 0.9rem;
            line-height: 1.6;
        }}

        .ai-generative-box {{
            background: linear-gradient(145deg, {bg_card}, {bg_card_end});
            border: 1px solid rgba(139, 92, 246, 0.25);
            border-radius: 12px;
            padding: 1.2rem;
            margin-top: 0.8rem;
            animation: fadeInUp 0.5s ease-out;
        }}

        .ai-generative-box h4 {{
            color: #A78BFA;
            margin: 0 0 0.6rem 0;
            font-size: 1rem;
        }}

        .ai-generative-box .model-badge {{
            display: inline-block;
            background: rgba(139, 92, 246, 0.15);
            color: #A78BFA;
            padding: 0.15rem 0.5rem;
            border-radius: 12px;
            font-size: 0.7rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }}

        .ai-generative-box p {{
            color: {text_secondary};
            font-size: 0.9rem;
            line-height: 1.7;
            white-space: pre-wrap;
        }}

        .disclaimer-box {{
            background: rgba(245, 158, 11, 0.08);
            border: 1px solid rgba(245, 158, 11, 0.25);
            border-radius: 8px;
            padding: 0.8rem 1rem;
            margin-top: 0.8rem;
            font-size: 0.82rem;
            color: #FBBF24;
        }}

        /* ── First Aid Tips ── */
        .first-aid-card {{
            background: linear-gradient(145deg, {bg_card}, {bg_card_end});
            border: 1px solid {firstaid_border};
            border-radius: 12px;
            padding: 1.2rem;
            margin-bottom: 0.8rem;
        }}

        .first-aid-card h4 {{
            color: #34D399;
            margin: 0 0 0.6rem 0;
        }}

        .first-aid-card ol, .first-aid-card ul {{
            color: {text_secondary};
            font-size: 0.9rem;
            padding-left: 1.2rem;
        }}

        .first-aid-card li {{
            margin-bottom: 0.3rem;
            line-height: 1.5;
        }}

        /* ── Map Container ── */
        .map-container {{
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 20px {card_shadow};
            margin: 1rem 0;
            border: 1px solid {border_subtle};
        }}

        /* ── Footer ── */
        .footer {{
            text-align: center;
            padding: 2rem 1rem;
            margin-top: 3rem;
            border-top: 1px solid {border_subtle};
            color: {text_muted};
            font-size: 0.88rem;
        }}

        .footer a {{
            color: #FF6B35;
            text-decoration: none;
            margin: 0 0.8rem;
            font-weight: 500;
            transition: color 0.2s ease;
        }}

        .footer a:hover {{
            color: #FF4B4B;
        }}

        /* ── Streamlit Overrides ── */
        /* Hide default Streamlit menu and header for production */
        #MainMenu {{visibility: hidden;}}
        header {{visibility: hidden;}}

        .stSelectbox label, .stTextInput label {{
            font-weight: 600 !important;
            font-size: 0.95rem !important;
        }}

        div[data-testid="stMetric"] {{
            background: linear-gradient(145deg, {bg_card}, {bg_card_end});
            border: 1px solid rgba(255, 75, 75, 0.12);
            border-radius: 10px;
            padding: 1rem;
        }}

        /* ── Gradient Button ── */
        .stButton > button {{
            background: linear-gradient(135deg, #FF4B4B, #FF6B35) !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 0.6rem 1.5rem !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
            transition: all 0.3s ease !important;
            width: 100%;
        }}

        .stButton > button:hover {{
            filter: brightness(1.1) !important;
            transform: scale(1.02);
            box-shadow: 0 4px 15px rgba(255, 75, 75, 0.4) !important;
        }}

        /* ── Sidebar Styling ── */
        section[data-testid="stSidebar"] {{
            border-right: 1px solid rgba(255, 75, 75, 0.1);
        }}

        section[data-testid="stSidebar"] .stMarkdown h2 {{
            font-size: 1.2rem;
            color: {text_primary};
            border-bottom: 2px solid rgba(255, 75, 75, 0.3);
            padding-bottom: 0.4rem;
        }}

        /* ── Stats Badge Row ── */
        .stats-row {{
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            flex-wrap: wrap;
            margin: 1rem 0;
        }}

        .stat-badge {{
            background: linear-gradient(145deg, {bg_card}, {bg_card_end});
            border: 1px solid {border_subtle};
            border-radius: 10px;
            padding: 0.6rem 1.2rem;
            text-align: center;
            min-width: 100px;
        }}

        .stat-badge .stat-number {{
            font-size: 1.4rem;
            font-weight: 700;
            color: #FF4B4B;
        }}

        .stat-badge .stat-label {{
            font-size: 0.75rem;
            color: {text_muted};
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        /* ── Pulse animation ── */
        .pulse {{
            animation: pulseGlow 2s ease-in-out infinite;
            display: inline-block;
        }}

        /* ── Font Awesome enhancements ── */
        .fa-icon-service {{
            margin-right: 0.4rem;
            font-size: 0.9rem;
        }}
    </style>
    """


# ─────────────────────────────────────────────
# HTML Renderers
# ─────────────────────────────────────────────

def render_service_card(
    name: str,
    distance: float,
    address: str,
    osm_link: str,
    icon: str,
    phone: str = "",
    lang: str = "en",
) -> str:
    """
    Generate HTML for a service result card with copy button and dial link.

    Args:
        name: Name of the service/place.
        distance: Distance from user location in km.
        address: Address or location description.
        osm_link: Link to OpenStreetMap.
        icon: Emoji icon for the service type.
        phone: Phone number (optional).
        lang: Language code for labels.

    Returns:
        HTML string for the card.
    """
    from translations import t

    addr_display = address if address else t("address_not_available", lang)
    addr_safe = address.replace("'", "\\'").replace('"', "&quot;") if address else ""

    # Copy address button (JavaScript clipboard API)
    copy_btn = ""
    if address:
        copy_btn = f"""
        <button class="btn-copy" onclick="navigator.clipboard.writeText('{addr_safe}').then(()=>this.innerHTML='✅ Copied!')">
            <i class="fa-regular fa-copy"></i> {t("copy_address", lang)}
        </button>
        """

    # Emergency dial link (tel: scheme for mobile)
    dial_btn = ""
    if phone:
        phone_clean = phone.replace(" ", "").replace("-", "")
        dial_btn = f"""
        <a class="btn-dial" href="tel:{phone_clean}">
            <i class="fa-solid fa-phone"></i> {t("call", lang)}
        </a>
        """

    return f"""
    <div class="service-card">
        <h4>{icon} {name}</h4>
        <p><i class="fa-solid fa-location-dot fa-icon-service"></i> {addr_display}</p>
        <span class="distance-badge"><i class="fa-solid fa-ruler"></i> {distance} {t("km_away", lang)}</span>
        <div class="card-actions">
            <a href="{osm_link}" target="_blank">{t("view_on_osm", lang)}</a>
            {copy_btn}
            {dial_btn}
        </div>
    </div>
    """


def render_emergency_number(
    label: str, number: str, icon: str, fa_icon: str = ""
) -> str:
    """
    Generate HTML for an emergency number card with dial link.

    Args:
        label: Name of the emergency service.
        number: Phone number.
        icon: Emoji icon.
        fa_icon: Font Awesome icon class (optional).

    Returns:
        HTML string for the emergency number card.
    """
    fa_html = f'<i class="fa-solid {fa_icon} fa-icon"></i> ' if fa_icon else ""

    return f"""
    <div class="emergency-number-card">
        <span class="label">{fa_html}{icon} {label}</span>
        <span class="number"><a href="tel:{number}">{number}</a></span>
    </div>
    """
