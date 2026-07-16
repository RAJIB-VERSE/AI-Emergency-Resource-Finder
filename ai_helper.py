"""
ai_helper.py — AI Emergency Assistant

Provides emergency classification and AI-generated guidance using
HuggingFace Inference API (generative models: Qwen 2.5, Phi-3, Gemma 2B)
with a local keyword-based fallback for offline/free-tier usage.
"""

import os
import time
from typing import Optional

import requests

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv is optional


# ─────────────────────────────────────────────
# Constants
# ─────────────────────────────────────────────

MEDICAL_DISCLAIMER: str = (
    "⚠️ **Disclaimer**: This AI assistant provides general guidance only. "
    "It is NOT a substitute for professional medical advice, diagnosis, or treatment. "
    "In case of a medical emergency, **call your local emergency number (112) immediately**."
)

# HuggingFace Inference API — Generative Models (priority order)
GENERATIVE_MODELS: list[dict[str, str]] = [
    {
        "name": "Qwen 2.5 3B Instruct",
        "url": "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-3B-Instruct",
    },
    {
        "name": "Microsoft Phi-3 Mini",
        "url": "https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct",
    },
    {
        "name": "Google Gemma 2B",
        "url": "https://api-inference.huggingface.co/models/google/gemma-2b-it",
    },
]

# Zero-shot classification model (fallback for classification)
HF_ZEROSHOT_URL: str = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"

# Emergency categories for classification
EMERGENCY_LABELS: list[str] = [
    "heart attack or cardiac emergency",
    "road accident or vehicle collision",
    "fire or burn emergency",
    "flood or water disaster",
    "earthquake or structural collapse",
    "pregnancy or childbirth emergency",
    "snake bite or animal attack",
    "blood requirement or bleeding",
    "general medical emergency",
    "breathing difficulty or choking",
    "poisoning or drug overdose",
]

# Map AI labels back to our emergency types
LABEL_TO_EMERGENCY: dict[str, str] = {
    "heart attack or cardiac emergency": "Heart Attack",
    "road accident or vehicle collision": "Road Accident",
    "fire or burn emergency": "Fire",
    "flood or water disaster": "Flood",
    "earthquake or structural collapse": "Earthquake",
    "pregnancy or childbirth emergency": "Pregnancy",
    "snake bite or animal attack": "Snake Bite",
    "blood requirement or bleeding": "Blood Requirement",
    "general medical emergency": "Medical Emergency",
    "breathing difficulty or choking": "Medical Emergency",
    "poisoning or drug overdose": "Medical Emergency",
}


# ─────────────────────────────────────────────
# HuggingFace Auth Helper
# ─────────────────────────────────────────────

def _get_hf_headers() -> dict[str, str]:
    """Get authorization headers for HuggingFace API."""
    hf_token = os.environ.get("HF_API_TOKEN", "")
    headers: dict[str, str] = {"Content-Type": "application/json"}
    if hf_token:
        headers["Authorization"] = f"Bearer {hf_token}"
    return headers


# ─────────────────────────────────────────────
# Keyword-Based Fallback Classifier
# ─────────────────────────────────────────────

KEYWORD_MAP: dict[str, list[str]] = {
    "Heart Attack": [
        "chest pain", "heart", "cardiac", "heart attack", "heartbeat",
        "palpitation", "angina", "cardiac arrest", "chest tightness",
        "left arm pain", "jaw pain", "sweating profusely",
    ],
    "Road Accident": [
        "accident", "crash", "collision", "hit", "run over", "injured on road",
    ],
    "Fire": [
        "fire", "burn", "flame", "smoke", "burning", "blaze", "arson",
        "caught fire", "explosion", "gas leak",
    ],
    "Flood": [
        "flood", "drowning", "dam", "submerged",
        "waterlogging", "heavy rain", "inundation",
    ],
    "Earthquake": [
        "earthquake", "tremor", "quake", "collapse", "building fell",
        "shaking", "seismic", "rubble", "structure collapse",
    ],
    "Pregnancy": [
        "pregnant", "pregnancy", "labor", "contractions",
        "baby coming", "water broke", "maternity", "prenatal",
    ],
    "Snake Bite": [
        "snake", "bite", "venom", "cobra", "viper", "scorpion",
        "animal attack", "dog bite", "rabies",
    ],
    "Blood Requirement": [
        "blood", "transfusion", "blood bank", "donation", "bleeding",
        "hemorrhage", "blood loss", "blood group", "blood type",
    ],
    "Medical Emergency": [
        "sick", "pain", "emergency", "hospital", "doctor", "medicine",
        "unconscious", "fainted", "fever", "breathing", "choking",
        "poison", "overdose", "seizure", "stroke", "diabetic",
        "allergy", "anaphylaxis", "asthma",
    ],
}


def classify_emergency_local(text: str) -> dict:
    """
    Classify emergency type using keyword matching (offline fallback).

    Args:
        text: User's emergency description.

    Returns:
        Dict with 'emergency_type', 'confidence', and 'method'.
    """
    import re
    text_lower = text.lower().strip()
    scores: dict[str, int] = {}

    for emergency_type, keywords in KEYWORD_MAP.items():
        score = 0
        for keyword in keywords:
            # Use word boundaries so "rain" doesn't match inside "brain"
            if re.search(r'\b' + re.escape(keyword) + r'\b', text_lower):
                score += len(keyword.split())
        if score > 0:
            scores[emergency_type] = score

    if not scores:
        return {
            "emergency_type": "Medical Emergency",
            "confidence": 0.3,
            "method": "keyword_fallback",
            "all_scores": {},
        }

    best_type = max(scores, key=scores.get)  # type: ignore[arg-type]
    max_score = scores[best_type]
    total_score = sum(scores.values())
    confidence = round(min(max_score / max(total_score, 1), 1.0), 2)

    return {
        "emergency_type": best_type,
        "confidence": confidence,
        "method": "keyword_matching",
        "all_scores": scores,
    }


# ─────────────────────────────────────────────
# HuggingFace Zero-Shot Classification
# ─────────────────────────────────────────────

def classify_emergency_hf(text: str) -> Optional[dict]:
    """
    Classify emergency type using HuggingFace zero-shot classification.

    Args:
        text: User's emergency description.

    Returns:
        Dict with classification results, or None if API fails.
    """
    headers = _get_hf_headers()
    payload = {
        "inputs": text,
        "parameters": {
            "candidate_labels": EMERGENCY_LABELS,
            "multi_label": False,
        },
    }

    try:
        response = requests.post(
            HF_ZEROSHOT_URL, json=payload, headers=headers, timeout=15,
        )

        if response.status_code == 503:
            time.sleep(3)
            response = requests.post(
                HF_ZEROSHOT_URL, json=payload, headers=headers, timeout=20,
            )

        response.raise_for_status()
        result = response.json()

        if "labels" in result and "scores" in result:
            best_label = result["labels"][0]
            best_score = result["scores"][0]
            emergency_type = LABEL_TO_EMERGENCY.get(best_label, "Medical Emergency")
            return {
                "emergency_type": emergency_type,
                "confidence": round(best_score, 3),
                "method": "huggingface_zeroshot",
                "raw_label": best_label,
            }
        return None

    except (requests.exceptions.RequestException, ValueError, KeyError) as e:
        print(f"HF zero-shot error: {e}")
        return None


# ─────────────────────────────────────────────
# Unified Classifier
# ─────────────────────────────────────────────

def classify_emergency(text: str) -> dict:
    """
    Classify emergency type — tries HuggingFace API first, falls back to keywords.

    Args:
        text: User's emergency description.

    Returns:
        Dict with 'emergency_type', 'confidence', and 'method'.
    """
    if not text or not text.strip():
        return {
            "emergency_type": "Medical Emergency",
            "confidence": 0.0,
            "method": "default",
        }

    # Try HuggingFace API first
    hf_result = classify_emergency_hf(text)
    if hf_result and hf_result.get("confidence", 0) > 0.3:
        return hf_result

    # Fallback to local keyword matching
    return classify_emergency_local(text)


# ─────────────────────────────────────────────
# Generative AI Guidance (NEW)
# ─────────────────────────────────────────────

def _build_emergency_prompt(user_text: str, emergency_type: str) -> str:
    """
    Build a structured prompt for the generative model.

    Args:
        user_text: The user's original emergency description.
        emergency_type: The classified emergency type.

    Returns:
        Formatted prompt string.
    """
    return f"""You are an emergency first-aid assistant. A user has described the following situation:

"{user_text}"

This has been identified as a **{emergency_type}** emergency.

Please provide:
1. **Emergency Assessment**: Briefly confirm what type of emergency this is.
2. **Immediate Actions** (3-5 steps): What should be done RIGHT NOW, in order of priority.
3. **Which Service to Visit**: Recommend the most appropriate emergency service (hospital, police, fire station, etc.).
4. **Warning Signs**: What symptoms mean the situation is getting worse.

Keep your response concise, clear, and actionable. Use simple language. This is a life-or-death situation — be direct.

IMPORTANT: You are NOT a doctor. Always recommend calling emergency services (112) first."""


def generate_ai_guidance(
    user_text: str, emergency_type: str
) -> Optional[dict[str, str]]:
    """
    Generate free-text emergency guidance using a generative HF model.

    Tries models in priority order: Qwen 2.5 → Phi-3 → Gemma 2B.
    Returns None if all models fail (caller should use static recommendations).

    Args:
        user_text: The user's emergency description.
        emergency_type: The classified emergency type.

    Returns:
        Dict with 'guidance' (text) and 'model' (name), or None.
    """
    headers = _get_hf_headers()
    prompt = _build_emergency_prompt(user_text, emergency_type)

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 400,
            "temperature": 0.3,
            "top_p": 0.9,
            "do_sample": True,
            "return_full_text": False,
        },
    }

    for model in GENERATIVE_MODELS:
        try:
            response = requests.post(
                model["url"],
                json=payload,
                headers=headers,
                timeout=30,
            )

            # If model is loading, wait and retry once
            if response.status_code == 503:
                time.sleep(5)
                response = requests.post(
                    model["url"],
                    json=payload,
                    headers=headers,
                    timeout=30,
                )

            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    generated_text = result[0].get("generated_text", "").strip()
                    if generated_text and len(generated_text) > 50:
                        return {
                            "guidance": generated_text,
                            "model": model["name"],
                        }

        except (requests.exceptions.RequestException, ValueError, KeyError) as e:
            print(f"Generative model {model['name']} error: {e}")
            continue

    return None


# ─────────────────────────────────────────────
# AI Recommendations (Static Fallback)
# ─────────────────────────────────────────────

RECOMMENDATIONS: dict[str, dict] = {
    "Heart Attack": {
        "immediate_actions": [
            "Call emergency services (112 / 102) immediately",
            "Have the person sit down and rest in a comfortable position",
            "If available, give them an aspirin (325mg) to chew slowly",
            "Loosen any tight clothing around chest and neck",
            "Be prepared to perform CPR if the person becomes unresponsive",
            "Do NOT let the person walk or exert themselves",
        ],
        "resources": ["Hospital", "Ambulance"],
        "urgency": "CRITICAL",
    },
    "Road Accident": {
        "immediate_actions": [
            "Call emergency services (112) and police (100) immediately",
            "Do NOT move the injured person unless there is immediate danger",
            "Check for breathing and consciousness",
            "Apply pressure to any visible bleeding wounds",
            "Keep the person warm with a blanket or clothing",
            "Direct traffic away from the accident scene if safe",
        ],
        "resources": ["Hospital", "Police", "Ambulance"],
        "urgency": "CRITICAL",
    },
    "Fire": {
        "immediate_actions": [
            "Call fire services (101) immediately",
            "Evacuate the building — use stairs, NOT elevators",
            "Stay low to the ground to avoid smoke inhalation",
            "Cover nose and mouth with a damp cloth",
            "If clothes catch fire: Stop, Drop, and Roll",
            "Do NOT re-enter a burning building",
        ],
        "resources": ["Fire Station", "Hospital"],
        "urgency": "CRITICAL",
    },
    "Flood": {
        "immediate_actions": [
            "Move to higher ground immediately",
            "Avoid walking or driving through floodwaters",
            "Call disaster management helpline (1078)",
            "Turn off electrical appliances and gas connections",
            "Stay away from power lines and electrical wires",
            "Keep emergency supplies and documents in waterproof bags",
        ],
        "resources": ["Shelter", "Police"],
        "urgency": "HIGH",
    },
    "Earthquake": {
        "immediate_actions": [
            "DROP, COVER, and HOLD ON",
            "Get under a sturdy desk or table",
            "Stay away from windows, mirrors, and heavy furniture",
            "If outdoors, move to an open area away from buildings",
            "After shaking stops, evacuate and check for injuries",
            "Be prepared for aftershocks",
        ],
        "resources": ["Shelter", "Hospital"],
        "urgency": "CRITICAL",
    },
    "Pregnancy": {
        "immediate_actions": [
            "Call emergency services (102) for an ambulance",
            "Keep the person comfortable and lying on their left side",
            "Time the contractions if in labor",
            "Do NOT give any medication without medical advice",
            "Keep the person calm and reassured",
            "Prepare for hospital — gather ID, medical records",
        ],
        "resources": ["Hospital", "Ambulance"],
        "urgency": "HIGH",
    },
    "Snake Bite": {
        "immediate_actions": [
            "Call emergency services (112) immediately",
            "Keep the person calm and still — movement spreads venom",
            "Immobilize the bitten limb below heart level",
            "Remove any rings, watches, or tight clothing near the bite",
            "Do NOT suck the venom, cut the wound, or apply a tourniquet",
            "Try to remember the snake's appearance for identification",
        ],
        "resources": ["Hospital"],
        "urgency": "CRITICAL",
    },
    "Blood Requirement": {
        "immediate_actions": [
            "Contact the nearest blood bank immediately",
            "Know the patient's blood group before requesting",
            "Check hospital blood bank availability first",
            "Reach out to voluntary blood donation organizations",
            "Ask family and friends for compatible blood donors",
            "Carry a valid ID for blood donation/collection",
        ],
        "resources": ["Blood Bank", "Hospital"],
        "urgency": "HIGH",
    },
    "Medical Emergency": {
        "immediate_actions": [
            "Call emergency services (112 / 102) immediately",
            "Assess the situation — check for breathing and consciousness",
            "Do NOT move the person if spinal injury is suspected",
            "Provide basic first aid if trained",
            "Keep the person warm and comfortable",
            "Note the time of onset of symptoms for medical staff",
        ],
        "resources": ["Hospital", "Pharmacy", "Ambulance"],
        "urgency": "HIGH",
    },
}


def get_ai_recommendations(emergency_type: str) -> dict:
    """
    Get curated recommendations for a specific emergency type.

    Args:
        emergency_type: The classified emergency type.

    Returns:
        Dict with 'immediate_actions', 'resources', and 'urgency'.
    """
    return RECOMMENDATIONS.get(
        emergency_type,
        RECOMMENDATIONS["Medical Emergency"],
    )
