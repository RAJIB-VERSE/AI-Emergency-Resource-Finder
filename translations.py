"""
translations.py — Multi-Language Support

Provides translation dictionaries for English, Hindi, and Bengali.
All user-facing strings are accessed through the t() function.
"""

from typing import Optional


# ─────────────────────────────────────────────
# Supported Languages
# ─────────────────────────────────────────────

SUPPORTED_LANGUAGES: dict[str, str] = {
    "English": "en",
    "हिन्दी (Hindi)": "hi",
    "বাংলা (Bengali)": "bn",
}

# ─────────────────────────────────────────────
# Translation Dictionary
# ─────────────────────────────────────────────

TRANSLATIONS: dict[str, dict[str, str]] = {

    # ── App Header ──
    "app_title": {
        "en": "🚨 AI Emergency Resource Finder",
        "hi": "🚨 AI आपातकालीन संसाधन खोजक",
        "bn": "🚨 AI জরুরি সম্পদ অনুসন্ধানকারী",
    },
    "app_subtitle": {
        "en": "Find the nearest emergency services in seconds.",
        "hi": "सेकंडों में निकटतम आपातकालीन सेवाएं खोजें।",
        "bn": "কয়েক সেকেন্ডে নিকটতম জরুরি পরিষেবা খুঁজুন।",
    },
    "powered_by": {
        "en": "Powered by OpenStreetMap • AI-Assisted • 100% Free",
        "hi": "OpenStreetMap द्वारा संचालित • AI-सहायता प्राप्त • 100% मुफ्त",
        "bn": "OpenStreetMap দ্বারা চালিত • AI-সহায়তা • ১০০% বিনামূল্যে",
    },

    # ── Sidebar ──
    "ai_assistant": {
        "en": "🤖 AI Emergency Assistant",
        "hi": "🤖 AI आपातकालीन सहायक",
        "bn": "🤖 AI জরুরি সহকারী",
    },
    "ai_assistant_desc": {
        "en": "Describe your emergency and get instant guidance.",
        "hi": "अपनी आपातकालीन स्थिति बताएं और तुरंत मार्गदर्शन पाएं।",
        "bn": "আপনার জরুরি অবস্থা বর্ণনা করুন এবং তাৎক্ষণিক নির্দেশনা পান।",
    },
    "describe_situation": {
        "en": "💬 Describe your situation:",
        "hi": "💬 अपनी स्थिति बताएं:",
        "bn": "💬 আপনার পরিস্থিতি বর্ণনা করুন:",
    },
    "ai_placeholder": {
        "en": "e.g., My father has chest pain and difficulty breathing...",
        "hi": "जैसे, मेरे पिता को सीने में दर्द और सांस लेने में कठिनाई हो रही है...",
        "bn": "যেমন, আমার বাবার বুকে ব্যথা এবং শ্বাস নিতে অসুবিধা হচ্ছে...",
    },
    "get_ai_guidance": {
        "en": "🔍 Get AI Guidance",
        "hi": "🔍 AI मार्गदर्शन पाएं",
        "bn": "🔍 AI নির্দেশনা পান",
    },
    "analyzing": {
        "en": "🧠 Analyzing your situation...",
        "hi": "🧠 आपकी स्थिति का विश्लेषण हो रहा है...",
        "bn": "🧠 আপনার পরিস্থিতি বিশ্লেষণ করা হচ্ছে...",
    },
    "generating_guidance": {
        "en": "🤖 Generating AI guidance...",
        "hi": "🤖 AI मार्गदर्शन तैयार हो रहा है...",
        "bn": "🤖 AI নির্দেশনা তৈরি হচ্ছে...",
    },
    "ai_analysis_result": {
        "en": "🧠 AI Analysis Result",
        "hi": "🧠 AI विश्लेषण परिणाम",
        "bn": "🧠 AI বিশ্লেষণ ফলাফল",
    },
    "detected_emergency": {
        "en": "Detected Emergency",
        "hi": "पहचानी गई आपातकालीन स्थिति",
        "bn": "চিহ্নিত জরুরি অবস্থা",
    },
    "urgency_level": {
        "en": "Urgency Level",
        "hi": "तात्कालिकता स्तर",
        "bn": "জরুরি মাত্রা",
    },
    "confidence": {
        "en": "Confidence",
        "hi": "विश्वास स्तर",
        "bn": "আত্মবিশ্বাস",
    },
    "immediate_actions": {
        "en": "⚡ Immediate Actions",
        "hi": "⚡ तत्काल कार्रवाई",
        "bn": "⚡ তাৎক্ষণিক পদক্ষেপ",
    },
    "recommended_resources": {
        "en": "🏢 Recommended Resources",
        "hi": "🏢 अनुशंसित संसाधन",
        "bn": "🏢 প্রস্তাবিত সম্পদ",
    },
    "ai_guidance": {
        "en": "🤖 AI-Generated Guidance",
        "hi": "🤖 AI-जनित मार्गदर्शन",
        "bn": "🤖 AI-উত্পাদিত নির্দেশনা",
    },
    "describe_warning": {
        "en": "⚠️ Please describe your emergency situation.",
        "hi": "⚠️ कृपया अपनी आपातकालीन स्थिति बताएं।",
        "bn": "⚠️ অনুগ্রহ করে আপনার জরুরি অবস্থা বর্ণনা করুন।",
    },

    # ── Emergency Numbers ──
    "emergency_numbers": {
        "en": "📞 Emergency Numbers",
        "hi": "📞 आपातकालीन नंबर",
        "bn": "📞 জরুরি নম্বর",
    },

    # ── CPR ──
    "cpr_guide": {
        "en": "🫀 CPR Quick Guide",
        "hi": "🫀 CPR त्वरित मार्गदर्शिका",
        "bn": "🫀 CPR দ্রুত গাইড",
    },
    "key_reminders": {
        "en": "💡 Key Reminders",
        "hi": "💡 मुख्य अनुस्मारक",
        "bn": "💡 মূল অনুস্মারক",
    },

    # ── Main Content ──
    "select_emergency": {
        "en": "🚨 Select Emergency Type",
        "hi": "🚨 आपातकालीन प्रकार चुनें",
        "bn": "🚨 জরুরি ধরন নির্বাচন করুন",
    },
    "enter_city": {
        "en": "📍 Enter City or Location",
        "hi": "📍 शहर या स्थान दर्ज करें",
        "bn": "📍 শহর বা অবস্থান লিখুন",
    },
    "city_placeholder": {
        "en": "e.g., Mumbai, Delhi, Bangalore...",
        "hi": "जैसे, मुंबई, दिल्ली, बैंगलोर...",
        "bn": "যেমন, মুম্বাই, দিল্লি, ব্যাঙ্গালোর...",
    },
    "find_services": {
        "en": "🔍  Find Emergency Services",
        "hi": "🔍  आपातकालीन सेवाएं खोजें",
        "bn": "🔍  জরুরি পরিষেবা খুঁজুন",
    },
    "finding_location": {
        "en": "📍 Finding your location...",
        "hi": "📍 आपका स्थान खोजा जा रहा है...",
        "bn": "📍 আপনার অবস্থান খোঁজা হচ্ছে...",
    },
    "location_not_found": {
        "en": "❌ Could not find that location. Please check the city name and try again.",
        "hi": "❌ वह स्थान नहीं मिला। कृपया शहर का नाम जांचें और पुनः प्रयास करें।",
        "bn": "❌ সেই অবস্থান পাওয়া যায়নি। অনুগ্রহ করে শহরের নাম পরীক্ষা করুন এবং আবার চেষ্টা করুন।",
    },
    "location_found": {
        "en": "📍 Location found",
        "hi": "📍 स्थान मिल गया",
        "bn": "📍 অবস্থান পাওয়া গেছে",
    },
    "searching_services": {
        "en": "🔍 Searching nearby emergency services...",
        "hi": "🔍 निकटतम आपातकालीन सेवाएं खोजी जा रही हैं...",
        "bn": "🔍 কাছাকাছি জরুরি পরিষেবা অনুসন্ধান করা হচ্ছে...",
    },
    "services_found": {
        "en": "Services Found",
        "hi": "सेवाएं मिलीं",
        "bn": "পরিষেবা পাওয়া গেছে",
    },
    "categories": {
        "en": "Categories",
        "hi": "श्रेणियां",
        "bn": "বিভাগ",
    },
    "search_radius": {
        "en": "Search Radius",
        "hi": "खोज दायरा",
        "bn": "অনুসন্ধান ব্যাসার্ধ",
    },
    "interactive_map": {
        "en": "🗺️ Interactive Emergency Map",
        "hi": "🗺️ इंटरैक्टिव आपातकालीन मानचित्र",
        "bn": "🗺️ ইন্টারেক্টিভ জরুরি মানচিত্র",
    },
    "nearby_services": {
        "en": "📋 Nearby Emergency Services",
        "hi": "📋 निकटतम आपातकालीन सेवाएं",
        "bn": "📋 কাছাকাছি জরুরি পরিষেবা",
    },
    "found": {
        "en": "found",
        "hi": "मिले",
        "bn": "পাওয়া গেছে",
    },
    "recommended": {
        "en": "⭐ Recommended",
        "hi": "⭐ अनुशंसित",
        "bn": "⭐ প্রস্তাবিত",
    },
    "no_services_found": {
        "en": "⚠️ No emergency services found in this area. Try a larger city or check the city name.",
        "hi": "⚠️ इस क्षेत्र में कोई आपातकालीन सेवा नहीं मिली। कोई बड़ा शहर आज़माएं।",
        "bn": "⚠️ এই এলাকায় কোনো জরুরি পরিষেবা পাওয়া যায়নি। একটি বড় শহর চেষ্টা করুন।",
    },
    "enter_city_warning": {
        "en": "⚠️ Please enter a city name to search for emergency services.",
        "hi": "⚠️ कृपया आपातकालीन सेवाओं की खोज के लिए एक शहर का नाम दर्ज करें।",
        "bn": "⚠️ অনুগ্রহ করে জরুরি পরিষেবা খুঁজতে একটি শহরের নাম লিখুন।",
    },

    # ── First Aid ──
    "first_aid_tips": {
        "en": "⛑️ First Aid Tips",
        "hi": "⛑️ प्राथमिक चिकित्सा सुझाव",
        "bn": "⛑️ প্রাথমিক চিকিৎসা টিপস",
    },
    "first_aid_steps": {
        "en": "Step-by-step first aid instructions:",
        "hi": "चरण-दर-चरण प्राथमिक चिकित्सा निर्देश:",
        "bn": "ধাপে ধাপে প্রাথমিক চিকিৎসা নির্দেশাবলী:",
    },
    "dos": {
        "en": "✅ Do's",
        "hi": "✅ करें",
        "bn": "✅ করুন",
    },
    "donts": {
        "en": "❌ Don'ts",
        "hi": "❌ न करें",
        "bn": "❌ করবেন না",
    },
    "call_emergency_when": {
        "en": "📞 **Call Emergency When:**",
        "hi": "📞 **आपातकाल कब कॉल करें:**",
        "bn": "📞 **কখন জরুরি কল করবেন:**",
    },

    # ── Export ──
    "export_csv": {
        "en": "📥 Export Results as CSV",
        "hi": "📥 परिणाम CSV में निर्यात करें",
        "bn": "📥 ফলাফল CSV হিসেবে রপ্তানি করুন",
    },

    # ── Theme ──
    "dark_mode": {
        "en": "🌙 Dark Mode",
        "hi": "🌙 डार्क मोड",
        "bn": "🌙 ডার্ক মোড",
    },
    "language": {
        "en": "🌐 Language",
        "hi": "🌐 भाषा",
        "bn": "🌐 ভাষা",
    },

    # ── Footer ──
    "made_with": {
        "en": "Made with ❤️ by",
        "hi": "❤️ द्वारा निर्मित",
        "bn": "❤️ দিয়ে তৈরি",
    },

    # ── Service Labels ──
    "Hospitals": {
        "en": "Hospitals",
        "hi": "अस्पताल",
        "bn": "হাসপাতাল",
    },
    "Police Stations": {
        "en": "Police Stations",
        "hi": "पुलिस स्टेशन",
        "bn": "পুলিশ স্টেশন",
    },
    "Fire Stations": {
        "en": "Fire Stations",
        "hi": "फायर स्टेशन",
        "bn": "ফায়ার স্টেশন",
    },
    "Blood Banks": {
        "en": "Blood Banks",
        "hi": "ब्लड बैंक",
        "bn": "ব্লাড ব্যাঙ্ক",
    },
    "Pharmacies": {
        "en": "Pharmacies",
        "hi": "फार्मेसी",
        "bn": "ফার্মেসি",
    },
    "Shelters": {
        "en": "Shelters",
        "hi": "आश्रय",
        "bn": "আশ্রয়",
    },

    # ── Emergency Types ──
    "Road Accident": {
        "en": "Road Accident",
        "hi": "सड़क दुर्घटना",
        "bn": "সড়ক দুর্ঘটনা",
    },
    "Heart Attack": {
        "en": "Heart Attack",
        "hi": "दिल का दौरा",
        "bn": "হার্ট অ্যাটাক",
    },
    "Fire": {
        "en": "Fire",
        "hi": "आग",
        "bn": "আগুন",
    },
    "Flood": {
        "en": "Flood",
        "hi": "बाढ़",
        "bn": "বন্যা",
    },
    "Earthquake": {
        "en": "Earthquake",
        "hi": "भूकंप",
        "bn": "ভূমিকম্প",
    },
    "Pregnancy": {
        "en": "Pregnancy",
        "hi": "गर्भावस्था",
        "bn": "গর্ভাবস্থা",
    },
    "Snake Bite": {
        "en": "Snake Bite",
        "hi": "सांप का काटना",
        "bn": "সাপের কামড়",
    },
    "Blood Requirement": {
        "en": "Blood Requirement",
        "hi": "रक्त आवश्यकता",
        "bn": "রক্তের প্রয়োজন",
    },
    "Medical Emergency": {
        "en": "Medical Emergency",
        "hi": "चिकित्सा आपातकाल",
        "bn": "চিকিৎসা জরুরি",
    },

    # ── Card labels ──
    "km_away": {
        "en": "km away",
        "hi": "किमी दूर",
        "bn": "কিমি দূরে",
    },
    "view_on_osm": {
        "en": "🔗 View on OpenStreetMap",
        "hi": "🔗 OpenStreetMap पर देखें",
        "bn": "🔗 OpenStreetMap-এ দেখুন",
    },
    "copy_address": {
        "en": "📋 Copy Address",
        "hi": "📋 पता कॉपी करें",
        "bn": "📋 ঠিকানা কপি করুন",
    },
    "address_not_available": {
        "en": "Address not available",
        "hi": "पता उपलब्ध नहीं",
        "bn": "ঠিকানা পাওয়া যায়নি",
    },
    "call": {
        "en": "📞 Call",
        "hi": "📞 कॉल करें",
        "bn": "📞 কল করুন",
    },
}


# ─────────────────────────────────────────────
# Translation Function
# ─────────────────────────────────────────────

def t(key: str, lang: str = "en") -> str:
    """
    Get a translated string by key and language code.

    Args:
        key: The translation key (must exist in TRANSLATIONS).
        lang: The language code ('en', 'hi', or 'bn').

    Returns:
        Translated string, or the English fallback if not found.
    """
    entry = TRANSLATIONS.get(key, {})
    # Try requested language, fall back to English, then return the key itself
    return entry.get(lang, entry.get("en", key))


def get_lang_code(lang_display: str) -> str:
    """
    Convert display language name to language code.

    Args:
        lang_display: Display name like 'English' or 'हिन्दी (Hindi)'.

    Returns:
        Language code ('en', 'hi', 'bn').
    """
    return SUPPORTED_LANGUAGES.get(lang_display, "en")
