"""
analytics_helper.py — Analytics Dashboard Utilities

Handles loading, updating, and summarizing search analytics for the dashboard.
Data is stored locally in JSON format.
"""

import os
import json

ANALYTICS_FILE = os.path.join(os.path.dirname(__file__), "data", "analytics.json")

def load_analytics() -> dict:
    """Load analytics data from JSON file."""
    if not os.path.exists(ANALYTICS_FILE):
        return {
            "total_searches": 0,
            "hospitals_found": 0,
            "blood_banks_found": 0,
            "total_distance": 0.0,
            "distance_count": 0,
            "search_history": [],
            "emergency_types": {}
        }
    try:
        with open(ANALYTICS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading analytics: {e}")
        return {
            "total_searches": 0,
            "hospitals_found": 0,
            "blood_banks_found": 0,
            "total_distance": 0.0,
            "distance_count": 0,
            "search_history": [],
            "emergency_types": {}
        }

def save_analytics(data: dict):
    """Save analytics data to JSON file."""
    os.makedirs(os.path.dirname(ANALYTICS_FILE), exist_ok=True)
    try:
        with open(ANALYTICS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving analytics: {e}")

def update_analytics(city: str, emergency_type: str, hospitals_count: int, blood_banks_count: int, avg_distance: float):
    """Update analytics with a new search result."""
    data = load_analytics()
    
    data["total_searches"] += 1
    data["hospitals_found"] += hospitals_count
    data["blood_banks_found"] += blood_banks_count
    
    if avg_distance > 0:
        data["total_distance"] += avg_distance
        data["distance_count"] += 1
        
    # Update search history (keep last 10)
    if city not in data["search_history"]:
        data["search_history"].insert(0, city)
        data["search_history"] = data["search_history"][:10]
        
    # Update emergency types count
    if emergency_type in data["emergency_types"]:
        data["emergency_types"][emergency_type] += 1
    else:
        data["emergency_types"][emergency_type] = 1
        
    save_analytics(data)

def get_analytics_summary() -> dict:
    """Get summarized analytics for the dashboard."""
    data = load_analytics()
    
    avg_dist = 0.0
    if data["distance_count"] > 0:
        avg_dist = round(data["total_distance"] / data["distance_count"], 1)
        
    most_common_type = "None"
    if data["emergency_types"]:
        most_common_type = max(data["emergency_types"], key=data["emergency_types"].get)
        
    return {
        "total_searches": data["total_searches"],
        "hospitals_found": data["hospitals_found"],
        "blood_banks_found": data["blood_banks_found"],
        "average_distance": avg_dist,
        "search_history": data["search_history"],
        "most_common_emergency": most_common_type,
    }
