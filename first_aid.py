"""
first_aid.py — First Aid Knowledge Base

Contains structured first-aid instructions for various emergency types.
Each entry includes step-by-step instructions, do's, don'ts, and
when to call emergency services.
"""


# ─────────────────────────────────────────────
# First Aid Tips Database
# ─────────────────────────────────────────────

FIRST_AID_TIPS: dict[str, dict] = {
    "Heart Attack": {
        "title": "❤️‍🩹 Heart Attack / Cardiac Emergency",
        "steps": [
            "Call emergency services (112) immediately",
            "Have the person sit upright in a comfortable position",
            "Give them an aspirin (325mg) to chew if not allergic",
            "Loosen tight clothing around the chest and neck",
            "Monitor breathing and consciousness continuously",
            "If person becomes unresponsive, begin CPR",
        ],
        "do": [
            "Stay calm and reassure the patient",
            "Keep them still — avoid any physical exertion",
            "Note the time symptoms started",
            "Be ready with CPR if needed",
        ],
        "dont": [
            "Don't let them walk or move unnecessarily",
            "Don't give water if they are unconscious",
            "Don't ignore mild chest discomfort — act fast",
            "Don't delay calling emergency services",
        ],
        "call_when": "Chest pain lasting more than 5 minutes, difficulty breathing, loss of consciousness",
    },
    "Road Accident": {
        "title": "🚗💥 Road Accident / Trauma",
        "steps": [
            "Ensure the scene is safe before approaching",
            "Call emergency services (112) and police (100)",
            "Check if the victim is breathing and conscious",
            "Control any visible bleeding with direct pressure",
            "Immobilize the neck/spine — do NOT move the victim",
            "Cover the victim to prevent shock (keep warm)",
        ],
        "do": [
            "Use hazard lights and warning triangles",
            "Apply pressure with a clean cloth on wounds",
            "Keep the victim warm with a blanket",
            "Talk to them to keep them conscious",
        ],
        "dont": [
            "Don't move the victim unless there's immediate danger (fire, explosion)",
            "Don't remove a helmet from a motorcyclist",
            "Don't give food or water to the injured person",
            "Don't try to straighten broken limbs",
        ],
        "call_when": "Any road accident with injuries, unconsciousness, or trapped victims",
    },
    "Fire": {
        "title": "🔥 Fire / Burn Emergency",
        "steps": [
            "Evacuate immediately — use stairs, NOT elevators",
            "Call fire services (101)",
            "If clothes catch fire: Stop, Drop, and Roll",
            "For minor burns: cool with running water for 10-20 minutes",
            "Cover burns loosely with a sterile bandage",
            "Do NOT apply ice, butter, or toothpaste to burns",
        ],
        "do": [
            "Stay low to avoid smoke (crawl if needed)",
            "Cover mouth with a damp cloth",
            "Close doors behind you to slow fire spread",
            "Meet at a pre-designated assembly point",
        ],
        "dont": [
            "Don't re-enter a burning building",
            "Don't use elevators during a fire",
            "Don't open doors that are hot to touch",
            "Don't apply ice or grease to burn wounds",
        ],
        "call_when": "Any fire, regardless of size — smoke inhalation or burns of any degree",
    },
    "Flood": {
        "title": "🌊 Flood / Water Disaster",
        "steps": [
            "Move to higher ground immediately",
            "Call disaster management (1078) or emergency (112)",
            "Turn off gas and electrical connections",
            "Avoid walking through moving water",
            "Store important documents in waterproof bags",
            "Stay tuned to weather warnings and radio",
        ],
        "do": [
            "Stock clean drinking water and dry food",
            "Keep a battery-operated flashlight and radio",
            "Help elderly and disabled neighbors evacuate",
            "Follow official evacuation routes",
        ],
        "dont": [
            "Don't walk or drive through floodwaters",
            "Don't touch electrical equipment while standing in water",
            "Don't drink floodwater — it may be contaminated",
            "Don't return home until authorities declare it safe",
        ],
        "call_when": "Rising water levels, trapped by water, structural damage",
    },
    "Earthquake": {
        "title": "🌍 Earthquake / Seismic Emergency",
        "steps": [
            "DROP to the ground, take COVER under furniture, HOLD ON",
            "Stay away from windows, mirrors, and heavy objects",
            "If indoors: stay inside until shaking stops",
            "If outdoors: move to an open area away from buildings",
            "After shaking stops: check for injuries and damage",
            "Be prepared for aftershocks",
        ],
        "do": [
            "Keep an earthquake emergency kit ready",
            "Know your building's evacuation routes",
            "Check gas and water lines after shaking stops",
            "Help trapped neighbors and call for rescue",
        ],
        "dont": [
            "Don't run outside during shaking",
            "Don't stand near windows or glass doors",
            "Don't use elevators after an earthquake",
            "Don't light candles or matches (gas leak risk)",
        ],
        "call_when": "Building damage, people trapped, injuries, or gas leaks detected",
    },
    "Pregnancy": {
        "title": "🤰 Pregnancy / Childbirth Emergency",
        "steps": [
            "Call emergency services (102) for an ambulance",
            "Have the person lie on their left side",
            "Time the contractions (frequency and duration)",
            "Keep them calm and breathing steadily",
            "Prepare clean towels and warm water",
            "Do NOT attempt delivery unless trained and no help available",
        ],
        "do": [
            "Keep the mother comfortable and reassured",
            "Gather medical records, ID, and hospital bag",
            "Keep the area clean if delivery is imminent",
            "Support breathing exercises",
        ],
        "dont": [
            "Don't give medication without medical guidance",
            "Don't panic — calmness helps the mother",
            "Don't delay going to the hospital if water breaks",
            "Don't let untrained people attempt delivery",
        ],
        "call_when": "Heavy bleeding, severe abdominal pain, contractions less than 5 minutes apart, water breaking",
    },
    "Snake Bite": {
        "title": "🐍 Snake Bite / Venomous Animal",
        "steps": [
            "Call emergency services (112) immediately",
            "Keep the person calm and still",
            "Immobilize the bitten limb below heart level",
            "Remove rings, watches, tight clothing near the bite",
            "Clean the wound gently with soap and water",
            "Get to the hospital ASAP — antivenom may be needed",
        ],
        "do": [
            "Note the time of the bite",
            "Try to remember the snake's appearance",
            "Mark the edge of swelling with a pen and time",
            "Keep the victim lying down and still",
        ],
        "dont": [
            "Don't suck the venom out",
            "Don't cut the wound",
            "Don't apply a tourniquet or ice",
            "Don't give the person alcohol or caffeine",
        ],
        "call_when": "Any snake bite — even if the snake looks non-venomous, seek medical attention",
    },
    "Blood Requirement": {
        "title": "🩸 Blood Requirement / Donation",
        "steps": [
            "Identify the patient's blood group",
            "Contact the nearest blood bank",
            "Check hospital blood bank availability",
            "Reach out to voluntary blood donors",
            "Ensure the donor is healthy and eligible",
            "Carry valid ID documents for donation",
        ],
        "do": [
            "Verify blood group compatibility",
            "Contact multiple blood banks simultaneously",
            "Ask family, friends, and social media for donors",
            "Keep emergency blood bank numbers saved",
        ],
        "dont": [
            "Don't accept blood from unverified sources",
            "Don't delay — blood requirements are time-critical",
            "Don't donate if you have recent infections or medications",
            "Don't forget to check for proper screening at blood banks",
        ],
        "call_when": "Severe bleeding, surgery requirement, anemia, accident injuries",
    },
    "Medical Emergency": {
        "title": "🚑 General Medical Emergency",
        "steps": [
            "Call emergency services (112 / 102)",
            "Assess: Is the person conscious and breathing?",
            "If not breathing: begin CPR (30 compressions, 2 breaths)",
            "Place unconscious but breathing person in recovery position",
            "Control any bleeding with direct pressure",
            "Do NOT give food, water, or medication to unconscious person",
        ],
        "do": [
            "Stay calm and provide reassurance",
            "Note the time and sequence of symptoms",
            "Clear the area for paramedics",
            "Have medical history/medications ready if known",
        ],
        "dont": [
            "Don't move someone with a suspected spinal injury",
            "Don't remove embedded objects from wounds",
            "Don't administer medication you're unsure about",
            "Don't leave an unconscious person alone",
        ],
        "call_when": "Unconsciousness, difficulty breathing, severe bleeding, chest pain, seizures, severe allergic reaction",
    },
}


# ─────────────────────────────────────────────
# CPR Quick Guide (Always Available)
# ─────────────────────────────────────────────

CPR_GUIDE: dict[str, list[str]] = {
    "title": "🫀 CPR Quick Guide (Hands-Only)",
    "steps": [
        "1️⃣ Check for responsiveness — tap and shout 'Are you okay?'",
        "2️⃣ Call 112 (or have someone call)",
        "3️⃣ Place the person on their back on a firm surface",
        "4️⃣ Place the heel of one hand on the center of the chest",
        "5️⃣ Place your other hand on top, interlace fingers",
        "6️⃣ Push hard and fast — at least 2 inches deep, 100-120 compressions/min",
        "7️⃣ Continue until help arrives or the person starts breathing",
    ],
    "remember": [
        "Push hard, push fast — don't worry about breaking ribs",
        "Minimize interruptions in compressions",
        "If trained: give 2 rescue breaths after every 30 compressions",
        "Use an AED (defibrillator) if available — follow the voice prompts",
    ],
}


def get_first_aid_tips(emergency_type: str) -> dict:
    """
    Retrieve first-aid tips for the given emergency type.

    Args:
        emergency_type: The type of emergency (must match keys in FIRST_AID_TIPS).

    Returns:
        Dict with 'title', 'steps', 'do', 'dont', and 'call_when'.
        Falls back to Medical Emergency if type not found.
    """
    return FIRST_AID_TIPS.get(
        emergency_type,
        FIRST_AID_TIPS["Medical Emergency"],
    )


def get_cpr_guide() -> dict:
    """
    Get the CPR quick reference guide.

    Returns:
        Dict with 'title', 'steps', and 'remember'.
    """
    return CPR_GUIDE
