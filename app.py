"""
app.py — AI Emergency Resource Finder v2.0

Main Streamlit application with:
- Dark/Light mode toggle
- Multi-language support (English/Hindi/Bengali)
- AI generative guidance (Qwen 2.5 / Phi-3 / Gemma 2B)
- Font Awesome icons
- Copy address & emergency dial links
- CSV export of search results
- Interactive Folium maps

Run with:  streamlit run app.py
"""

import streamlit as st
import pandas as pd
from streamlit_folium import st_folium

from utils import (
    APP_NAME,
    AUTHOR_NAME,
    GITHUB_URL,
    LINKEDIN_URL,
    EMERGENCY_TYPES,
    EMERGENCY_NUMBERS,
    SERVICE_ICONS,
    SERVICE_LABELS,
    get_emergency_css,
    geocode_city,
    render_service_card,
    render_emergency_number,
)
from map_utils import create_emergency_map, search_nearby_services
from ai_helper import (
    classify_emergency,
    get_ai_recommendations,
    generate_ai_guidance,
    MEDICAL_DISCLAIMER,
)
from first_aid import get_first_aid_tips, get_cpr_guide
from translations import t, get_lang_code, SUPPORTED_LANGUAGES


# ─────────────────────────────────────────────
# Page Configuration
# ─────────────────────────────────────────────

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize session state
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True
if "language" not in st.session_state:
    st.session_state.language = "English"

# Get current language code
lang = get_lang_code(st.session_state.language)

# Inject custom CSS (theme-aware)
st.markdown(get_emergency_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Sidebar — Settings, AI Assistant & Emergency Info
# ─────────────────────────────────────────────

with st.sidebar:
    # ── Settings ──
    st.markdown("## ⚙️ Settings")

    col_theme, col_lang = st.columns(2)
    with col_theme:
        dark_mode = st.toggle(
            t("dark_mode", lang),
            value=st.session_state.dark_mode,
            key="dark_toggle",
        )
        if dark_mode != st.session_state.dark_mode:
            st.session_state.dark_mode = dark_mode
            st.rerun()

    with col_lang:
        selected_lang = st.selectbox(
            t("language", lang),
            options=list(SUPPORTED_LANGUAGES.keys()),
            index=list(SUPPORTED_LANGUAGES.keys()).index(st.session_state.language),
            key="lang_select",
            label_visibility="collapsed",
        )
        if selected_lang != st.session_state.language:
            st.session_state.language = selected_lang
            st.rerun()

    st.markdown("---")

    # ── AI Assistant ──
    st.markdown(f"## {t('ai_assistant', lang)}")
    st.markdown(t("ai_assistant_desc", lang))

    user_query = st.text_area(
        t("describe_situation", lang),
        placeholder=t("ai_placeholder", lang),
        height=100,
        key="ai_input",
    )

    if st.button(t("get_ai_guidance", lang), key="ai_btn", use_container_width=True):
        if user_query.strip():
            with st.spinner(t("analyzing", lang)):
                result = classify_emergency(user_query)

            emergency_type = result["emergency_type"]
            confidence = result.get("confidence", 0)
            method = result.get("method", "unknown")

            recommendations = get_ai_recommendations(emergency_type)
            urgency = recommendations["urgency"]

            # Urgency badge
            urgency_colors = {"CRITICAL": "🔴", "HIGH": "🟠", "MEDIUM": "🟡"}
            urgency_icon = urgency_colors.get(urgency, "🟢")

            em_icon = EMERGENCY_TYPES.get(emergency_type, {}).get("icon", "🚑")
            em_name = t(emergency_type, lang)

            ai_html = f"""
            <div class="ai-response-box">
                <h4>{t('ai_analysis_result', lang)}</h4>
                <p><strong>{t('detected_emergency', lang)}:</strong> {em_icon} {em_name}</p>
                <p><strong>{t('urgency_level', lang)}:</strong> {urgency_icon} {urgency}</p>
                <p><strong>{t('confidence', lang)}:</strong> {confidence:.0%} ({method.replace('_', ' ').title()})</p>
                <hr style="border-color: rgba(59,130,246,0.15); margin: 0.6rem 0;">
                <h4>{t('immediate_actions', lang)}:</h4>
                <ol>
            """
            for action in recommendations["immediate_actions"]:
                ai_html += f"<li>{action}</li>"
            ai_html += "</ol>"
            ai_html += f"<p><strong>{t('recommended_resources', lang)}:</strong> "
            ai_html += ", ".join(recommendations["resources"])
            ai_html += "</p></div>"

            st.markdown(ai_html, unsafe_allow_html=True)

            # ── Generative AI Guidance ──
            with st.spinner(t("generating_guidance", lang)):
                gen_result = generate_ai_guidance(user_query, emergency_type)

            if gen_result:
                gen_html = f"""
                <div class="ai-generative-box">
                    <h4>{t('ai_guidance', lang)}</h4>
                    <span class="model-badge"><i class="fa-solid fa-microchip"></i> {gen_result['model']}</span>
                    <p>{gen_result['guidance']}</p>
                </div>
                """
                st.markdown(gen_html, unsafe_allow_html=True)

            # Medical Disclaimer
            st.markdown(
                f'<div class="disclaimer-box">{MEDICAL_DISCLAIMER}</div>',
                unsafe_allow_html=True,
            )
        else:
            st.warning(t("describe_warning", lang))

    st.markdown("---")

    # ── Emergency Numbers ──
    st.markdown(f"## {t('emergency_numbers', lang)}")

    for label, info in EMERGENCY_NUMBERS.items():
        st.markdown(
            render_emergency_number(
                label, info["number"], info["icon"], info.get("fa_icon", "")
            ),
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # ── CPR Quick Guide ──
    st.markdown(f"## {t('cpr_guide', lang)}")
    cpr = get_cpr_guide()
    for step in cpr["steps"]:
        st.markdown(f"- {step}")
    with st.expander(t("key_reminders", lang)):
        for tip in cpr["remember"]:
            st.markdown(f"- {tip}")


# ─────────────────────────────────────────────
# Main Content — Hero Section
# ─────────────────────────────────────────────

st.markdown(
    f"""
    <div class="hero-container">
        <div class="hero-icons">
            <i class="fa-solid fa-hospital"></i>
            <i class="fa-solid fa-shield-halved"></i>
            <i class="fa-solid fa-fire-extinguisher"></i>
            <i class="fa-solid fa-droplet"></i>
            <i class="fa-solid fa-pills"></i>
            <i class="fa-solid fa-house-chimney"></i>
        </div>
        <h1 class="hero-title">{t('app_title', lang)}</h1>
        <p class="hero-subtitle">{t('app_subtitle', lang)}</p>
        <p style="color: #6B7280; font-size: 0.85rem; margin: 0;">
            {t('powered_by', lang)}
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# ─────────────────────────────────────────────
# Emergency Type & Location Input
# ─────────────────────────────────────────────

col_type, col_city = st.columns([1, 1])

with col_type:
    emergency_options = list(EMERGENCY_TYPES.keys())
    selected_emergency = st.selectbox(
        t("select_emergency", lang),
        options=emergency_options,
        format_func=lambda x: f"{EMERGENCY_TYPES[x]['icon']}  {t(x, lang)}",
        index=8,  # Default to Medical Emergency
        key="emergency_type",
    )

with col_city:
    city_input = st.text_input(
        t("enter_city", lang),
        placeholder=t("city_placeholder", lang),
        key="city_input",
    )

# Search button
search_clicked = st.button(
    t("find_services", lang),
    key="search_btn",
    use_container_width=True,
)


# ─────────────────────────────────────────────
# Search & Display Results
# ─────────────────────────────────────────────

if search_clicked and city_input:
    with st.spinner(t("finding_location", lang)):
        location = geocode_city(city_input)

    if location is None:
        st.error(t("location_not_found", lang))
    else:
        lat, lon, display_name = location
        st.success(f"{t('location_found', lang)}: **{display_name}**")

        # Get recommended services for this emergency type
        emergency_info = EMERGENCY_TYPES.get(selected_emergency, {})
        recommended = emergency_info.get("services", "hospital").split(",")

        # Search for ALL services
        all_service_types = [
            "hospital", "police", "fire_station",
            "blood_bank", "pharmacy", "shelter",
        ]

        with st.spinner(t("searching_services", lang)):
            services = search_nearby_services(lat, lon, service_types=all_service_types)

        # Count total results
        total_found = sum(len(v) for v in services.values())

        # ── Stats Row ──
        st.markdown(
            f"""
            <div class="stats-row">
                <div class="stat-badge">
                    <div class="stat-number">{total_found}</div>
                    <div class="stat-label">{t('services_found', lang)}</div>
                </div>
                <div class="stat-badge">
                    <div class="stat-number">{len([s for s in services.values() if s])}</div>
                    <div class="stat-label">{t('categories', lang)}</div>
                </div>
                <div class="stat-badge">
                    <div class="stat-number">5 km</div>
                    <div class="stat-label">{t('search_radius', lang)}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # ── Interactive Map ──
        st.markdown(
            f'<div class="section-header">{t("interactive_map", lang)}</div>',
            unsafe_allow_html=True,
        )

        st.markdown('<div class="map-container">', unsafe_allow_html=True)
        emergency_map = create_emergency_map(lat, lon, services)
        st_folium(emergency_map, width=None, height=500, returned_objects=[])
        st.markdown('</div>', unsafe_allow_html=True)

        # ── Service Results ──
        st.markdown(
            f'<div class="section-header">{t("nearby_services", lang)}</div>',
            unsafe_allow_html=True,
        )

        # Show recommended services first
        for service_type in all_service_types:
            results = services.get(service_type, [])
            if not results:
                continue

            icon = SERVICE_ICONS.get(service_type, "📍")
            label_key = SERVICE_LABELS.get(service_type, service_type)
            label = t(label_key, lang)
            is_recommended = service_type in recommended

            badge = f" {t('recommended', lang)}" if is_recommended else ""

            with st.expander(
                f"{icon} {label} ({len(results)} {t('found', lang)}){badge}",
                expanded=is_recommended,
            ):
                # Display in columns of 3
                for i in range(0, min(len(results), 9), 3):
                    cols = st.columns(3)
                    for j, col in enumerate(cols):
                        idx = i + j
                        if idx < len(results):
                            place = results[idx]
                            with col:
                                st.markdown(
                                    render_service_card(
                                        name=place["name"],
                                        distance=place["distance"],
                                        address=place["address"],
                                        osm_link=place["osm_link"],
                                        icon=icon,
                                        phone=place.get("phone", ""),
                                        lang=lang,
                                    ),
                                    unsafe_allow_html=True,
                                )

        if total_found == 0:
            st.warning(t("no_services_found", lang))

        # ── CSV Export ──
        all_places: list[dict] = []
        for service_type, results in services.items():
            for place in results:
                all_places.append({
                    "Type": SERVICE_LABELS.get(service_type, service_type),
                    "Name": place["name"],
                    "Distance (km)": place["distance"],
                    "Address": place["address"],
                    "Phone": place.get("phone", ""),
                    "OpenStreetMap Link": place["osm_link"],
                })

        if all_places:
            df = pd.DataFrame(all_places)
            csv_data = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label=t("export_csv", lang),
                data=csv_data,
                file_name=f"emergency_services_{city_input.replace(' ', '_')}.csv",
                mime="text/csv",
                use_container_width=True,
            )

    # ── First Aid Tips ──
    st.markdown(
        f'<div class="section-header">{t("first_aid_tips", lang)}</div>',
        unsafe_allow_html=True,
    )

    tips = get_first_aid_tips(selected_emergency)

    tip_col1, tip_col2 = st.columns(2)

    with tip_col1:
        steps_html = f"""
        <div class="first-aid-card">
            <h4>{tips['title']}</h4>
            <p style="color: #9CA3AF; font-size: 0.85rem; margin-bottom: 0.6rem;">
                {t('first_aid_steps', lang)}
            </p>
            <ol>
        """
        for step in tips["steps"]:
            steps_html += f"<li>{step}</li>"
        steps_html += "</ol></div>"
        st.markdown(steps_html, unsafe_allow_html=True)

    with tip_col2:
        do_dont_html = """<div class="first-aid-card">"""
        do_dont_html += f"<h4>{t('dos', lang)}</h4><ul>"
        for item in tips["do"]:
            do_dont_html += f"<li>{item}</li>"
        do_dont_html += "</ul>"
        do_dont_html += f'<h4 style="color: #F87171;">{t("donts", lang)}</h4><ul>'
        for item in tips["dont"]:
            do_dont_html += f"<li>{item}</li>"
        do_dont_html += "</ul></div>"
        st.markdown(do_dont_html, unsafe_allow_html=True)

    st.info(f"{t('call_emergency_when', lang)} {tips['call_when']}")

elif search_clicked and not city_input:
    st.warning(t("enter_city_warning", lang))


# ─────────────────────────────────────────────
# Footer
# ─────────────────────────────────────────────

st.markdown("---")
st.markdown(
    f"""
    <div class="footer">
        <p>
            <a href="{GITHUB_URL}" target="_blank"><i class="fa-brands fa-github"></i> GitHub</a>
            <a href="{LINKEDIN_URL}" target="_blank"><i class="fa-brands fa-linkedin"></i> LinkedIn</a>
        </p>
        <p>{t('made_with', lang)} <strong>{AUTHOR_NAME}</strong></p>
        <p style="font-size: 0.75rem; color: #4B5563;">
            {APP_NAME} v2.0 • Powered by OpenStreetMap & HuggingFace
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
