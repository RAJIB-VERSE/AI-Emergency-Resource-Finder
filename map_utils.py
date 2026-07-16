"""
map_utils.py — Map & Overpass API Utilities

Handles querying OpenStreetMap via the Overpass API for emergency services,
and generates interactive Folium maps with color-coded markers.
"""

import html
import time
from typing import Optional

import folium
import requests

from utils import (
    OVERPASS_API_URL,
    DEFAULT_SEARCH_RADIUS,
    SERVICE_ICONS,
    SERVICE_LABELS,
    haversine_distance,
)


# ─────────────────────────────────────────────
# Overpass API Query Templates
# ─────────────────────────────────────────────

# Maps service types to their Overpass QL tag queries
OVERPASS_QUERIES: dict[str, list[str]] = {
    "hospital": [
        'node["amenity"="hospital"](around:{radius},{lat},{lon});',
        'way["amenity"="hospital"](around:{radius},{lat},{lon});',
    ],
    "police": [
        'node["amenity"="police"](around:{radius},{lat},{lon});',
        'way["amenity"="police"](around:{radius},{lat},{lon});',
    ],
    "fire_station": [
        'node["amenity"="fire_station"](around:{radius},{lat},{lon});',
        'way["amenity"="fire_station"](around:{radius},{lat},{lon});',
    ],
    "blood_bank": [
        'node["healthcare"="blood_donation"](around:{radius},{lat},{lon});',
        'node["amenity"="blood_bank"](around:{radius},{lat},{lon});',
        'node["healthcare:speciality"="haematology"](around:{radius},{lat},{lon});',
    ],
    "pharmacy": [
        'node["amenity"="pharmacy"](around:{radius},{lat},{lon});',
        'way["amenity"="pharmacy"](around:{radius},{lat},{lon});',
    ],
    "shelter": [
        'node["amenity"="shelter"](around:{radius},{lat},{lon});',
        'node["amenity"="community_centre"](around:{radius},{lat},{lon});',
        'node["emergency"="assembly_point"](around:{radius},{lat},{lon});',
        'way["amenity"="shelter"](around:{radius},{lat},{lon});',
    ],
}

# Color mapping for map markers
MARKER_COLORS: dict[str, str] = {
    "hospital": "red",
    "police": "blue",
    "fire_station": "orange",
    "blood_bank": "darkred",
    "pharmacy": "green",
    "shelter": "purple",
}

# Folium icon names for markers
MARKER_ICONS: dict[str, str] = {
    "hospital": "plus-sign",
    "police": "star",
    "fire_station": "fire",
    "blood_bank": "tint",
    "pharmacy": "medkit",
    "shelter": "home",
}


# ─────────────────────────────────────────────
# Overpass API Functions
# ─────────────────────────────────────────────

def query_overpass(
    lat: float,
    lon: float,
    service_type: str,
    radius: int = DEFAULT_SEARCH_RADIUS,
) -> list[dict]:
    """
    Query the Overpass API for a specific amenity type near given coordinates.

    Args:
        lat: Latitude of the search center.
        lon: Longitude of the search center.
        service_type: Type of service (e.g., 'hospital', 'police').
        radius: Search radius in meters.

    Returns:
        List of dictionaries with service details (name, lat, lon, address, etc.).
    """
    if service_type not in OVERPASS_QUERIES:
        return []

    # Build the Overpass QL query
    query_parts = []
    for template in OVERPASS_QUERIES[service_type]:
        query_parts.append(
            template.format(radius=radius, lat=lat, lon=lon)
        )

    overpass_query = f"""
    [out:json][timeout:25];
    (
        {''.join(query_parts)}
    );
    out center body;
    """

    try:
        response = requests.post(
            OVERPASS_API_URL,
            data={"data": overpass_query},
            timeout=30,
            headers={"User-Agent": "AIEmergencyResourceFinder/1.0"},
        )
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.Timeout:
        print(f"Overpass API timeout for {service_type}")
        return []
    except requests.exceptions.RequestException as e:
        print(f"Overpass API error for {service_type}: {e}")
        return []
    except ValueError:
        print(f"Invalid JSON response for {service_type}")
        return []

    # Parse the results
    results: list[dict] = []
    seen_names: set[str] = set()

    for element in data.get("elements", []):
        tags = element.get("tags", {})
        name = tags.get("name", "").strip()

        # Get coordinates — nodes have lat/lon directly, ways have center
        elem_lat = element.get("lat") or element.get("center", {}).get("lat")
        elem_lon = element.get("lon") or element.get("center", {}).get("lon")

        if not elem_lat or not elem_lon:
            continue

        # Skip duplicates by name (or by coordinates if unnamed)
        dedup_key = name if name else f"{elem_lat:.5f},{elem_lon:.5f}"
        if dedup_key in seen_names:
            continue
        seen_names.add(dedup_key)

        # Build address from tags
        address_parts = []
        for key in ["addr:street", "addr:housenumber", "addr:city", "addr:postcode"]:
            if key in tags:
                address_parts.append(tags[key])
        address = ", ".join(address_parts) if address_parts else tags.get("address", "")

        # Calculate distance from search center
        distance = haversine_distance(lat, lon, elem_lat, elem_lon)

        # Build OpenStreetMap link
        osm_link = f"https://www.openstreetmap.org/{element['type']}/{element['id']}"

        results.append({
            "name": name or f"Unnamed {SERVICE_LABELS.get(service_type, service_type)}",
            "lat": elem_lat,
            "lon": elem_lon,
            "distance": distance,
            "address": address,
            "osm_link": osm_link,
            "service_type": service_type,
            "phone": tags.get("phone", tags.get("contact:phone", "")),
        })

    # Sort by distance
    results.sort(key=lambda x: x["distance"])
    return results


def search_nearby_services(
    lat: float,
    lon: float,
    radius: int = DEFAULT_SEARCH_RADIUS,
    service_types: Optional[list[str]] = None,
) -> dict[str, list[dict]]:
    """
    Search for all emergency service types near the given coordinates.

    Args:
        lat: Latitude of the search center.
        lon: Longitude of the search center.
        radius: Search radius in meters.
        service_types: Optional list of service types to search. Defaults to all.

    Returns:
        Dictionary mapping service type to list of results.
    """
    if service_types is None:
        service_types = list(OVERPASS_QUERIES.keys())

    all_results: dict[str, list[dict]] = {}

    for service_type in service_types:
        results = query_overpass(lat, lon, service_type, radius)
        all_results[service_type] = results
        # Small delay between queries to be respectful to the API
        time.sleep(0.3)

    return all_results


# ─────────────────────────────────────────────
# Folium Map Generation
# ─────────────────────────────────────────────

def create_emergency_map(
    lat: float,
    lon: float,
    services: dict[str, list[dict]],
    zoom_start: int = 13,
) -> folium.Map:
    """
    Create an interactive Folium map with color-coded emergency service markers.

    Args:
        lat: Center latitude (user's location).
        lon: Center longitude (user's location).
        services: Dictionary of service results from search_nearby_services.
        zoom_start: Initial zoom level.

    Returns:
        folium.Map object with all markers added.
    """
    # Create base map with dark tiles
    emergency_map = folium.Map(
        location=[lat, lon],
        zoom_start=zoom_start,
        tiles="CartoDB dark_matter",
        attr="© OpenStreetMap contributors © CARTO",
    )

    # Add user location marker
    folium.Marker(
        location=[lat, lon],
        popup=folium.Popup(
            "<b>📍 Your Location</b>",
            max_width=200,
        ),
        icon=folium.Icon(
            color="white",
            icon="user",
            prefix="glyphicon",
        ),
    ).add_to(emergency_map)

    # Add a circle showing the search radius
    folium.Circle(
        location=[lat, lon],
        radius=DEFAULT_SEARCH_RADIUS,
        color="#FF4B4B",
        fill=True,
        fill_opacity=0.05,
        opacity=0.3,
        weight=1,
    ).add_to(emergency_map)

    # Add markers for each service
    for service_type, results in services.items():
        color = MARKER_COLORS.get(service_type, "gray")
        icon_name = MARKER_ICONS.get(service_type, "info-sign")
        emoji = SERVICE_ICONS.get(service_type, "📍")
        label = SERVICE_LABELS.get(service_type, service_type)

        for place in results[:10]:  # Limit to 10 markers per type
            safe_name = html.escape(place['name'])
            safe_addr = html.escape(place['address']) if place['address'] else ""
            safe_phone = html.escape(place['phone']) if place['phone'] else ""
            
            popup_html = f"""
            <div style="font-family: Inter, sans-serif; min-width: 180px;">
                <b style="font-size: 13px;">{emoji} {safe_name}</b><br>
                <span style="color: #666; font-size: 11px;">{label}</span><br>
                <span style="font-size: 11px;">📏 {place['distance']} km away</span><br>
                {'<span style="font-size: 11px;">📍 ' + safe_addr + '</span><br>' if safe_addr else ''}
                {'<span style="font-size: 11px;">📞 ' + safe_phone + '</span><br>' if safe_phone else ''}
                <a href="{place['osm_link']}" target="_blank" style="font-size: 11px; color: #FF6B35;">
                    🔗 View on OSM
                </a>
            </div>
            """

            folium.Marker(
                location=[place["lat"], place["lon"]],
                popup=folium.Popup(popup_html, max_width=250),
                tooltip=f"{emoji} {place['name']} ({place['distance']} km)",
                icon=folium.Icon(
                    color=color,
                    icon=icon_name,
                    prefix="glyphicon",
                ),
            ).add_to(emergency_map)

    # Add a legend
    legend_html = _build_legend_html()
    emergency_map.get_root().html.add_child(folium.Element(legend_html))

    return emergency_map


def _build_legend_html() -> str:
    """
    Build HTML for the map legend overlay.

    Returns:
        HTML string for the legend.
    """
    legend_items = [
        ("🏥 Hospital", "#D63E2A"),
        ("🚔 Police", "#38AADD"),
        ("🚒 Fire Station", "#F69730"),
        ("🩸 Blood Bank", "#A23336"),
        ("💊 Pharmacy", "#72AF26"),
        ("🏠 Shelter", "#D252B9"),
    ]

    items_html = ""
    for label, color in legend_items:
        items_html += f"""
            <div style="margin: 3px 0; font-size: 12px;">
                <span style="display: inline-block; width: 12px; height: 12px;
                       background: {color}; border-radius: 50%; margin-right: 6px;
                       vertical-align: middle;"></span>
                {label}
            </div>
        """

    return f"""
    <div style="
        position: fixed;
        bottom: 30px;
        right: 30px;
        z-index: 1000;
        background: rgba(14, 17, 23, 0.92);
        border: 1px solid rgba(255, 75, 75, 0.25);
        border-radius: 10px;
        padding: 10px 14px;
        font-family: Inter, sans-serif;
        color: #FAFAFA;
        backdrop-filter: blur(8px);
    ">
        <div style="font-weight: 700; font-size: 12px; margin-bottom: 6px;
                    border-bottom: 1px solid rgba(255,75,75,0.2); padding-bottom: 4px;">
            🗺️ Map Legend
        </div>
        {items_html}
    </div>
    """
