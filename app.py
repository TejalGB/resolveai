"""
ResolveAI — Interactive Support Assistant for SAP SuccessFactors Learning.
Provides real-time troubleshooting, source citations, and ServiceNow ticket resolutions.
"""
import os
import streamlit as st
import requests

# Synchronize Streamlit Community Cloud secrets to os.environ
try:
    for key, val in st.secrets.items():
        if isinstance(val, str) and key not in os.environ:
            os.environ[key] = val
except Exception:
    pass


# ============================================================
# RESOLVEAI INFERENCE ENGINE (HYBRID / STANDALONE)
# ============================================================

def query_resolveai(question: str) -> dict:
    """
    Query ResolveAI via configured REST API, or seamlessly execute
    direct in-process RAG pipeline (ideal for Hugging Face Spaces & standalone operation).
    """
    api_url = os.getenv("RESOLVEAI_API_URL", "").strip()

    # Try external/local API if configured
    if api_url:
        try:
            response = requests.post(
                f"{api_url.rstrip('/')}/ask",
                json={"question": question},
                timeout=120
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.ConnectionError:
            # Fall back to direct in-process RAG execution if API is offline
            pass
        except Exception:
            pass

    # Direct in-process execution (Hugging Face Spaces & standalone mode)
    from src.rag.pipeline import answer_question
    return answer_question(question)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="ResolveAI | SAP LMS Support",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# SESSION STATE & THEME MANAGEMENT
# ============================================================

if "conversations" not in st.session_state:
    st.session_state.conversations = {"Session 1": []}

if "active_session" not in st.session_state:
    st.session_state.active_session = "Session 1"

if "theme_mode" not in st.session_state:
    st.session_state.theme_mode = "light"

st.session_state.messages = st.session_state.conversations.get(
    st.session_state.active_session, []
)

is_dark = st.session_state.theme_mode == "dark"


# ============================================================
# ADAPTIVE ENTERPRISE STYLING (LIGHT & DARK THEMES)
# ============================================================

if is_dark:
    theme_specific_css = """
    /* Obsidian Dark Theme */
    [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background-color: #0F172A !important;
        color: #F8FAFC !important;
    }

    [data-testid="stSidebar"] {
        background-color: #1E293B !important;
        border-right: 1px solid #334155 !important;
    }

    [data-testid="stHeader"] {
        background-color: rgba(15, 23, 42, 0.95) !important;
    }

    .welcome-card {
        background: linear-gradient(135deg, rgba(30, 58, 138, 0.35) 0%, rgba(15, 23, 42, 0.85) 100%) !important;
        border: 1px solid rgba(59, 130, 246, 0.35) !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4) !important;
    }

    .welcome-label {
        color: #60A5FA !important;
    }

    .welcome-title {
        color: #F8FAFC !important;
    }

    .welcome-subtitle {
        color: #94A3B8 !important;
    }

    .feature-pill {
        background: #1E293B !important;
        border: 1px solid #334155 !important;
        color: #93C5FD !important;
    }

    .section-title {
        color: #F8FAFC !important;
    }

    .section-subtitle {
        color: #94A3B8 !important;
    }

    /* Sidebar in Dark Mode */
    .sidebar-brand {
        color: #F8FAFC !important;
    }

    .sidebar-desc {
        color: #94A3B8 !important;
    }

    .sidebar-nav-item {
        background: rgba(37, 99, 235, 0.25) !important;
        color: #60A5FA !important;
        border-left: 3px solid #3B82F6 !important;
    }

    .sidebar-help-box {
        background: #1E293B !important;
        border: 1px solid #334155 !important;
        color: #94A3B8 !important;
    }

    .source-box {
        background-color: #1E293B !important;
        border: 1px solid #334155 !important;
        border-left: 3px solid #3B82F6 !important;
    }

    .source-box b {
        color: #F8FAFC !important;
    }

    .chat-caption {
        color: #64748B !important;
    }

    /* Bottom chat container fix in Dark Mode - elevated and visible */
    [data-testid="stBottom"], [data-testid="stBottom"] > div {
        background-color: transparent !important;
        background: transparent !important;
    }

    [data-testid="stBottom"] {
        padding-bottom: 22px !important;
        padding-top: 8px !important;
    }

    div[data-testid="stChatInput"] {
        background-color: #1E293B !important;
        border: 1.5px solid #475569 !important;
        border-radius: 14px !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.45) !important;
    }

    div[data-testid="stChatInput"]:focus-within {
        border-color: #60A5FA !important;
        box-shadow: 0 0 0 3px rgba(96, 165, 250, 0.25), 0 4px 20px rgba(0, 0, 0, 0.5) !important;
    }

    div[data-testid="stChatInput"] textarea {
        background-color: transparent !important;
        color: #F8FAFC !important;
        border: none !important;
    }

    /* Sidebar action buttons in Dark Mode */
    section[data-testid="stSidebar"] div[data-testid="stColumn"] div[data-testid="stButton"] > button,
    section[data-testid="stSidebar"] [data-testid="stButton"] button {
        background-color: #1E293B !important;
        border: 1px solid #334155 !important;
        color: #F8FAFC !important;
    }

    section[data-testid="stSidebar"] [data-testid="stButton"] button:hover {
        border-color: #60A5FA !important;
        background-color: #243248 !important;
        color: #FFFFFF !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stToggle"] label,
    section[data-testid="stSidebar"] div[data-testid="stToggle"] label p,
    section[data-testid="stSidebar"] div[data-testid="stToggle"] label span {
        color: #F8FAFC !important;
        font-size: 13.5px !important;
        font-weight: 500 !important;
    }
    """
else:
    theme_specific_css = """
    /* Crisp Light Theme */
    [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
    }

    [data-testid="stSidebar"] {
        background-color: #F8FAFC !important;
        border-right: 1px solid #E2E8F0 !important;
    }

    [data-testid="stHeader"] {
        background-color: rgba(255, 255, 255, 0.95) !important;
    }

    .welcome-card {
        background: linear-gradient(135deg, #F0F7FF 0%, #E8F2FE 100%) !important;
        border: 1px solid #D6E4F6 !important;
        box-shadow: 0 2px 8px rgba(37, 99, 235, 0.04) !important;
    }

    .welcome-label {
        color: #2563EB !important;
    }

    .welcome-title {
        color: #0F172A !important;
    }

    .welcome-subtitle {
        color: #475569 !important;
    }

    .feature-pill {
        background: #FFFFFF !important;
        border: 1px solid #DBEAFE !important;
        color: #1E40AF !important;
    }

    .section-title {
        color: #0F172A !important;
    }

    .section-subtitle {
        color: #64748B !important;
    }

    /* Sidebar in Light Mode */
    .sidebar-brand {
        color: #0F172A !important;
    }

    .sidebar-desc {
        color: #64748B !important;
    }

    .sidebar-nav-item {
        background: #EFF6FF !important;
        color: #2563EB !important;
        border-left: 3px solid #2563EB !important;
    }

    .sidebar-help-box {
        background: #F8FAFC !important;
        border: 1px solid #E2E8F0 !important;
        color: #64748B !important;
    }

    .source-box {
        background-color: #F8FAFC !important;
        border: 1px solid #E2E8F0 !important;
        border-left: 3px solid #2563EB !important;
    }

    .source-box b {
        color: #0F172A !important;
    }

    .chat-caption {
        color: #94A3B8 !important;
    }

    /* Bottom chat container fix in Light Mode - elevated and visible */
    [data-testid="stBottom"], [data-testid="stBottom"] > div {
        background-color: transparent !important;
        background: transparent !important;
    }

    [data-testid="stBottom"] {
        padding-bottom: 22px !important;
        padding-top: 8px !important;
    }

    div[data-testid="stChatInput"] {
        background-color: #FFFFFF !important;
        border: 1.5px solid #CBD5E1 !important;
        border-radius: 14px !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08) !important;
    }

    div[data-testid="stChatInput"]:focus-within {
        border-color: #3B82F6 !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2), 0 4px 20px rgba(0, 0, 0, 0.1) !important;
    }

    div[data-testid="stChatInput"] textarea {
        background-color: transparent !important;
        color: #0F172A !important;
        border: none !important;
    }

    /* Sidebar action buttons in Light Mode */
    section[data-testid="stSidebar"] div[data-testid="stColumn"] div[data-testid="stButton"] > button,
    section[data-testid="stSidebar"] [data-testid="stButton"] button {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        color: #0F172A !important;
    }

    section[data-testid="stSidebar"] [data-testid="stButton"] button:hover {
        border-color: #3B82F6 !important;
        background-color: #F8FAFC !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stToggle"] label,
    section[data-testid="stSidebar"] div[data-testid="stToggle"] label p,
    section[data-testid="stSidebar"] div[data-testid="stToggle"] label span {
        color: #475569 !important;
        font-size: 13.5px !important;
        font-weight: 500 !important;
    }
    """

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }}

    /* Page container spacing - ensures welcome banner is never clipped and chat input never covers cards */
    .block-container {{
        padding-top: 3.5rem !important;
        padding-bottom: 9rem !important;
        max-width: 1200px !important;
    }}

    .welcome-card {{
        border-radius: 14px;
        padding: 16px 22px;
        margin-bottom: 14px;
        position: relative;
    }}

    .welcome-label {{
        font-size: 10.5px;
        font-weight: 700;
        letter-spacing: 1px;
        margin-bottom: 2px;
    }}

    .welcome-title {{
        font-size: 24px;
        font-weight: 800;
        margin-bottom: 4px;
        line-height: 1.2;
    }}

    .welcome-subtitle {{
        font-size: 13px;
        margin-bottom: 12px;
        max-width: 680px;
    }}

    .feature-pills {{
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
    }}

    .feature-pill {{
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 11.5px;
        font-weight: 500;
        display: inline-flex;
        align-items: center;
        gap: 5px;
    }}

    .section-title {{
        font-size: 17px;
        font-weight: 700;
        margin-bottom: 2px;
        display: flex;
        align-items: center;
        gap: 6px;
    }}

    .section-subtitle {{
        font-size: 12.5px;
        margin-bottom: 10px;
    }}

    /* 6 Issue Buttons: White enterprise cards with subtle borders in BOTH themes */
    div[data-testid="stColumn"] div.stButton > button,
    div[data-testid="stColumn"] div[data-testid="stButton"] > button {{
        display: flex !important;
        flex-direction: row !important;
        align-items: center !important;
        justify-content: flex-start !important;
        text-align: left !important;
        height: 52px !important;
        min-height: 52px !important;
        max-height: 52px !important;
        padding: 0 16px !important;
        background-color: #FFFFFF !important;
        background: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 10px !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
        transition: all 0.2s ease-in-out !important;
        cursor: pointer !important;
        width: 100% !important;
    }}

    div[data-testid="stColumn"] div.stButton > button:hover,
    div[data-testid="stColumn"] div[data-testid="stButton"] > button:hover {{
        border-color: #2563EB !important;
        background-color: #F8FAFC !important;
        background: #F8FAFC !important;
        box-shadow: 0 4px 14px rgba(37, 99, 235, 0.12) !important;
        transform: translateY(-1px) !important;
    }}

    div[data-testid="stColumn"] div.stButton > button div[data-testid="stMarkdownContainer"],
    div[data-testid="stColumn"] div[data-testid="stButton"] > button div[data-testid="stMarkdownContainer"] {{
        width: 100% !important;
        text-align: left !important;
        display: flex !important;
        align-items: center !important;
    }}

    div[data-testid="stColumn"] div.stButton > button p,
    div[data-testid="stColumn"] div[data-testid="stButton"] > button p,
    div[data-testid="stColumn"] div.stButton > button span:not([data-testid="stIconMaterial"]),
    div[data-testid="stColumn"] div[data-testid="stButton"] > button span:not([data-testid="stIconMaterial"]) {{
        font-size: 14px !important;
        font-weight: 600 !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        margin: 0 !important;
        padding: 0 !important;
        line-height: 1.3 !important;
        color: #0F172A !important;
    }}

    div[data-testid="stColumn"] div.stButton > button:hover p,
    div[data-testid="stColumn"] div[data-testid="stButton"] > button:hover p {{
        color: #1E40AF !important;
    }}

    /* Lucide-style vector icons consistently in enterprise blue */
    div[data-testid="stColumn"] div.stButton > button span[data-testid="stIconMaterial"],
    div[data-testid="stColumn"] div[data-testid="stButton"] > button span[data-testid="stIconMaterial"] {{
        color: #2563EB !important;
        font-size: 20px !important;
        margin-right: 8px !important;
        display: inline-flex !important;
        align-items: center !important;
    }}

    div[data-testid="stColumn"] div.stButton > button:hover span[data-testid="stIconMaterial"],
    div[data-testid="stColumn"] div[data-testid="stButton"] > button:hover span[data-testid="stIconMaterial"] {{
        color: #1D4ED8 !important;
    }}

    /* Sidebar sticky bottom layout - push toggle to the bottom end */
    section[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {{
        display: flex !important;
        flex-direction: column !important;
        min-height: calc(100vh - 2.5rem) !important;
    }}

    section[data-testid="stSidebar"] div[data-testid="stToggle"] {{
        margin-top: auto !important;
        padding-top: 18px !important;
        padding-bottom: 14px !important;
    }}

    /* Compact sidebar action buttons */
    section[data-testid="stSidebar"] div[data-testid="stColumn"] div[data-testid="stButton"] > button,
    section[data-testid="stSidebar"] [data-testid="stButton"] button {{
        min-height: 44px !important;
        height: 44px !important;
        padding: 8px 12px !important;
        margin: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        white-space: nowrap !important;
        font-size: 13.5px !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
    }}

    section[data-testid="stSidebar"] span[data-testid="stIconMaterial"] {{
        color: #2563EB !important;
        font-size: 18px !important;
        margin-right: 6px !important;
    }}

    /* Keep the two session actions compact */
    section[data-testid="stSidebar"] [data-testid="stHorizontalBlock"] {{
        align-items: flex-start !important;
    }}

    /* Prevent unnecessary vertical spacing around sidebar buttons */
    section[data-testid="stSidebar"] [data-testid="stButton"] {{
        margin-bottom: 6px !important;
    }}

    /* Sidebar Styling */
    .sidebar-brand {{
        font-size: 20px;
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 2px;
    }}

    .sidebar-desc {{
        font-size: 12px;
        line-height: 1.4;
        margin-bottom: 18px;
    }}

    .sidebar-nav-item {{
        font-weight: 600;
        font-size: 14px;
        padding: 8px 14px;
        border-radius: 8px;
        margin-bottom: 14px;
    }}

    .sidebar-help-box {{
        border-radius: 10px;
        padding: 12px 14px;
        font-size: 12px;
        line-height: 1.45;
        margin-top: 24px;
    }}

    /* Knowledge Badges & Source Boxes */
    .match-badge {{
        display: inline-block;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 600;
        background-color: #2563EB;
        color: white;
    }}

    .source-box {{
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 10px;
    }}

    .chat-caption {{
        font-size: 12px;
        text-align: center;
        margin-top: 8px;
    }}

    {theme_specific_css}
    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

prompt_to_submit = None

with st.sidebar:
    st.markdown('<div class="sidebar-brand"><span style="color:#2563EB; font-size:16px;">●</span> ResolveAI</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-desc">SAP SuccessFactors Learning Troubleshooting Assistant</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-nav-item">Chat</div>', unsafe_allow_html=True)

    st.markdown("##### **Session**")
    session_names = list(st.session_state.conversations.keys())

    col_new, col_clear = st.columns(2)
    with col_new:
        if st.button("New Chat", icon=":material/add:", use_container_width=True):
            new_session_name = f"Session {len(st.session_state.conversations) + 1}"
            st.session_state.conversations[new_session_name] = []
            st.session_state.active_session = new_session_name
            st.session_state.messages = st.session_state.conversations[new_session_name]
            st.rerun()

    with col_clear:
        if st.button("Clear Chat", icon=":material/delete_outline:", use_container_width=True):
            st.session_state.conversations[st.session_state.active_session] = []
            st.session_state.messages = []
            st.rerun()

    if len(session_names) > 1:
        current_index = session_names.index(st.session_state.active_session) if st.session_state.active_session in session_names else 0
        selected_session = st.selectbox(
            "Switch Session:",
            session_names,
            index=current_index
        )
        if selected_session != st.session_state.active_session:
            st.session_state.active_session = selected_session
            st.session_state.messages = st.session_state.conversations[selected_session]
            st.rerun()

    st.markdown(
        """
        <div class="sidebar-help-box">
            <b>Admin Guidance</b><br>
            Get step-by-step troubleshooting guidance for SAP SuccessFactors Learning issues.
        </div>
        """,
        unsafe_allow_html=True
    )

    dark_mode_enabled = st.toggle("Dark Mode", value=is_dark, key="theme_toggle_switch")
    if dark_mode_enabled != is_dark:
        st.session_state.theme_mode = "dark" if dark_mode_enabled else "light"
        st.rerun()


# ============================================================
# WELCOME AREA & 6 ISSUE CARDS (3x2 GRID)
# ============================================================

if not st.session_state.messages:
    # Welcome Banner matching reference layout
    st.markdown(
        """
        <div class="welcome-card">
            <div class="welcome-label">WELCOME TO</div>
            <div class="welcome-title">ResolveAI</div>
            <div class="welcome-subtitle">
                Your AI troubleshooting assistant for SAP SuccessFactors Learning Management System
            </div>
            <div class="feature-pills">
                <span class="feature-pill">Knowledge-grounded responses</span>
                <span class="feature-pill">Structured troubleshooting & ServiceNow resolutions</span>
                <span class="feature-pill">SAP documentation with source citations</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Section Heading
    st.markdown(
        """
        <div class="section-title">How can I help you today?</div>
        <div class="section-subtitle">Choose one of the common issues below, or describe your problem in the chat bar:</div>
        """,
        unsafe_allow_html=True
    )

    # Row 1: Cards 1 - 3
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button(
            "Course assigned again",
            icon=":material/school:",
            help="User completed a course but it was assigned to them again.",
            key="card_retraining",
            use_container_width=True
        ):
            prompt_to_submit = "Course assigned again after completion"

    with col2:
        if st.button(
            "Content not launching",
            icon=":material/play_circle:",
            help="Learners report that online course content is not launching.",
            key="card_scorm",
            use_container_width=True
        ):
            prompt_to_submit = "Online content is not launching"

    with col3:
        if st.button(
            "New employee missing",
            icon=":material/person_search:",
            help="A new hire has joined, but their account cannot be found in LMS.",
            key="card_user_sync",
            use_container_width=True
        ):
            prompt_to_submit = "New employee is missing from LMS"

    # Row 2: Cards 4 - 6
    col4, col5, col6 = st.columns(3)

    with col4:
        if st.button(
            "MyLearning access",
            icon=":material/lock_open:",
            help="User is unable to access MyLearning or cannot see assigned courses.",
            key="card_access",
            use_container_width=True
        ):
            prompt_to_submit = "Learner cannot access MyLearning"

    with col5:
        if st.button(
            "Unexpected assignment",
            icon=":material/assignment:",
            help="A user received a course assignment that they shouldn't have.",
            key="card_unexpected",
            use_container_width=True
        ):
            prompt_to_submit = "Course was assigned unexpectedly"

    with col6:
        if st.button(
            "Other LMS issue",
            icon=":material/help_outline:",
            help="Describe your specific issue in the chat below.",
            key="card_other",
            use_container_width=True
        ):
            prompt_to_submit = "Other SAP LMS issue"

    st.markdown(
        '<div class="chat-caption" style="margin-top:16px;">Click any issue above, or describe your specific problem in the chat bar below.</div>',
        unsafe_allow_html=True
    )


# ============================================================
# CHAT TIMELINE
# ============================================================

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message["role"] == "assistant":
            # 1-Click Ticket Copier
            with st.expander("📋 Copy Resolution for ServiceNow Ticket"):
                st.code(message["content"], language="markdown")

            # Verified Source Badges
            sources = message.get("sources", [])
            if sources:
                with st.expander(f"📚 Knowledge Sources ({len(sources)} sources cited)"):
                    for src in sources:
                        is_kba = "SAP" in src.get("source_type", "") or src.get("source", "").endswith("_sap.md")
                        source_icon = "📘" if is_kba else "📖"
                        type_label = "Official SAP KBA" if is_kba else "Expert Playbook"
                        badge_color = "#0284C7" if is_kba else "#2563EB"

                        st.markdown(
                            f"""
                            <div class="source-box">
                                <div style="display:flex; justify-content:space-between; align-items:center;">
                                    <b>{source_icon} {src['source']} <span style="font-size:11px; color:#64748B; font-weight:normal;">({type_label})</span></b>
                                    <span class="match-badge" style="background-color:{badge_color};">Semantic Match: {src['match_score']}%</span>
                                </div>
                                <div style="font-size:13px; color:#64748B; margin-top:4px;">
                                    Scenario: <i>{src['scenario']}</i> &nbsp;•&nbsp; Category: <code>{src['category']}</code>
                                </div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )


# ============================================================
# CHAT INPUT & EXECUTION
# ============================================================

chat_input = st.chat_input("Describe your LMS issue...")
question = prompt_to_submit or chat_input

if question:
    # 1. Store & display user message
    st.session_state.messages.append({
        "role": "user",
        "content": question,
        "sources": []
    })

    with st.chat_message("user"):
        st.markdown(question)

    # 2. Call backend & display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Analyzing verified playbooks..."):
            try:
                data = query_resolveai(question)

                answer = data.get("answer", "No answer returned.")
                sources = data.get("sources", [])

                # Render response
                st.markdown(answer)

                # 1-Click Ticket Copier
                with st.expander("📋 Copy Resolution for ServiceNow Ticket"):
                    st.code(answer, language="markdown")

                # Render knowledge sources with provenance metadata
                if sources:
                    with st.expander(f"📚 Knowledge Sources ({len(sources)} sources cited)"):
                        for src in sources:
                            is_kba = "SAP" in src.get("source_type", "") or src.get("source", "").endswith("_sap.md")
                            source_icon = "📘" if is_kba else "📖"
                            type_label = "Official SAP KBA" if is_kba else "Expert Playbook"
                            badge_color = "#0284C7" if is_kba else "#2563EB"

                            st.markdown(
                                f"""
                                <div class="source-box">
                                    <div style="display:flex; justify-content:space-between; align-items:center;">
                                        <b>{source_icon} {src['source']} <span style="font-size:11px; color:#64748B; font-weight:normal;">({type_label})</span></b>
                                        <span class="match-badge" style="background-color:{badge_color};">Semantic Match: {src['match_score']}%</span>
                                    </div>
                                    <div style="font-size:13px; color:#64748B; margin-top:4px;">
                                        Scenario: <i>{src['scenario']}</i> &nbsp;•&nbsp; Category: <code>{src['category']}</code>
                                    </div>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                # Store response
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "sources": sources
                })
                st.session_state.conversations[st.session_state.active_session] = st.session_state.messages

            except requests.exceptions.Timeout:
                st.error("⚠️ The request timed out. Please try again.")
            except Exception as e:
                st.error(f"⚠️ An unexpected error occurred: {e}")