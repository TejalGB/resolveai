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
    page_title="ResolveAI — SAP LMS Support Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CLEAN, MODERN DUAL-THEME STYLING
# ============================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* CSS Theme Variables - Default / Light */
    :root {
        --card-bg: #FFFFFF;
        --card-border: #E2E8F0;
        --card-hover-border: #3B82F6;
        --card-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        --text-primary: #0F172A;
        --text-secondary: #64748B;
        --hero-bg: linear-gradient(135deg, rgba(239, 246, 255, 0.95) 0%, rgba(219, 234, 254, 0.7) 100%);
        --hero-border: #BFDBFE;
        --pill-bg: #FFFFFF;
        --pill-border: #DBEAFE;
        --pill-text: #1E40AF;
        --sidebar-nav-bg: #EFF6FF;
        --sidebar-nav-color: #2563EB;
        --source-box-bg: rgba(37, 99, 235, 0.04);
    }

    /* Dark Mode Tokens */
    @media (prefers-color-scheme: dark) {
        :root {
            --card-bg: #1E293B;
            --card-border: #334155;
            --card-hover-border: #60A5FA;
            --card-shadow: 0 2px 6px rgba(0, 0, 0, 0.35);
            --text-primary: #F8FAFC;
            --text-secondary: #94A3B8;
            --hero-bg: linear-gradient(135deg, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.8) 100%);
            --hero-border: #334155;
            --pill-bg: #0F172A;
            --pill-border: #334155;
            --pill-text: #93C5FD;
            --sidebar-nav-bg: #1E293B;
            --sidebar-nav-color: #60A5FA;
            --source-box-bg: rgba(255, 255, 255, 0.03);
        }
    }

    /* Streamlit Dark Theme Detection */
    [data-theme="dark"],
    [data-testid="stAppViewContainer"][data-theme="dark"] {
        --card-bg: #1E293B;
        --card-border: #334155;
        --card-hover-border: #60A5FA;
        --card-shadow: 0 2px 6px rgba(0, 0, 0, 0.35);
        --text-primary: #F8FAFC;
        --text-secondary: #94A3B8;
        --hero-bg: linear-gradient(135deg, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.8) 100%);
        --hero-border: #334155;
        --pill-bg: #0F172A;
        --pill-border: #334155;
        --pill-text: #93C5FD;
        --sidebar-nav-bg: #1E293B;
        --sidebar-nav-color: #60A5FA;
        --source-box-bg: rgba(255, 255, 255, 0.03);
    }

    /* Top Bar */
    .top-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-bottom: 8px;
        margin-bottom: 8px;
    }
    .user-avatar {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        background: #2563EB;
        color: white;
        font-size: 12px;
        font-weight: 700;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 2px 4px rgba(37, 99, 235, 0.25);
    }

    /* Compact Hero Banner */
    .hero-banner {
        background: var(--hero-bg);
        border: 1px solid var(--hero-border);
        border-radius: 12px;
        padding: 16px 20px;
        margin-bottom: 16px;
    }
    .hero-badge {
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.8px;
        color: #2563EB;
        margin-bottom: 4px;
    }
    .hero-title {
        font-size: 26px;
        font-weight: 700;
        color: var(--text-primary);
        line-height: 1.1;
        margin-bottom: 4px;
    }
    .hero-subtitle {
        font-size: 13px;
        color: var(--text-secondary);
        margin-bottom: 12px;
    }
    .hero-pills {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
    }
    .hero-pill {
        display: inline-flex;
        align-items: center;
        font-size: 11px;
        font-weight: 500;
        color: var(--pill-text);
        background: var(--pill-bg);
        border: 1px solid var(--pill-border);
        padding: 4px 10px;
        border-radius: 20px;
    }

    /* Section Heading */
    .section-header {
        font-size: 15px;
        font-weight: 700;
        color: var(--text-primary);
        margin-top: 10px;
        margin-bottom: 2px;
    }
    .section-caption {
        font-size: 12px;
        color: var(--text-secondary);
        margin-bottom: 12px;
    }

    /* Compact Issue Card Buttons */
    .main .stButton > button {
        background-color: var(--card-bg) !important;
        border: 1px solid var(--card-border) !important;
        border-radius: 10px !important;
        padding: 10px 14px !important;
        text-align: left !important;
        min-height: 68px !important;
        color: var(--text-primary) !important;
        box-shadow: var(--card-shadow) !important;
        transition: all 0.2s ease-in-out !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
    }
    .main .stButton > button:hover {
        border-color: var(--card-hover-border) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.12) !important;
    }
    .main .stButton > button p {
        text-align: left !important;
        margin: 0 !important;
        font-size: 12.5px !important;
        line-height: 1.35 !important;
    }

    /* Sidebar Navigation Style */
    .sidebar-nav-item {
        background: var(--sidebar-nav-bg);
        color: var(--sidebar-nav-color);
        border-left: 3px solid #2563EB;
        padding: 8px 12px;
        border-radius: 0 8px 8px 0;
        font-weight: 600;
        font-size: 13px;
        margin-bottom: 16px;
    }
    .sidebar-tip-card {
        background: var(--card-bg);
        border: 1px solid var(--card-border);
        border-radius: 8px;
        padding: 10px 12px;
        font-size: 11px;
        color: var(--text-secondary);
        line-height: 1.4;
        margin-top: 24px;
    }

    /* Chat Helper Text */
    .chat-helper-text {
        font-size: 11px;
        color: var(--text-secondary);
        text-align: center;
        margin-top: 4px;
        margin-bottom: 12px;
    }

    /* Source Citation Boxes */
    .match-badge {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 10px;
        font-size: 11px;
        font-weight: 600;
        color: white;
    }
    .source-box {
        background-color: var(--source-box-bg);
        border-left: 3px solid #2563EB;
        border-radius: 6px;
        padding: 10px 12px;
        margin-bottom: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "conversations" not in st.session_state:
    st.session_state.conversations = {"Session 1": []}

if "active_session" not in st.session_state:
    st.session_state.active_session = "Session 1"

st.session_state.messages = st.session_state.conversations.get(
    st.session_state.active_session, []
)


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

prompt_to_submit = None

with st.sidebar:
    st.markdown(
        """
        <div style="display:flex; align-items:center; gap:8px; margin-bottom:4px;">
            <span style="font-size:22px;">✨</span>
            <span style="font-size:20px; font-weight:700;">ResolveAI</span>
        </div>
        <div style="font-size:12px; color:var(--text-secondary); margin-bottom:14px;">
            SAP SuccessFactors Learning Troubleshooting Assistant
        </div>
        <div class="sidebar-nav-item">
            💬 Chat
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("##### ⏱️ **Session**")
    session_names = list(st.session_state.conversations.keys())

    col_new, col_clear = st.columns(2)
    with col_new:
        if st.button("➕ New Chat", use_container_width=True):
            new_session_name = f"Session {len(st.session_state.conversations) + 1}"
            st.session_state.conversations[new_session_name] = []
            st.session_state.active_session = new_session_name
            st.session_state.messages = st.session_state.conversations[new_session_name]
            st.rerun()

    with col_clear:
        if st.button("🗑 Clear Chat", use_container_width=True):
            st.session_state.conversations[st.session_state.active_session] = []
            st.session_state.messages = []
            st.rerun()

    if len(session_names) > 1:
        current_index = session_names.index(st.session_state.active_session) if st.session_state.active_session in session_names else 0
        selected_session = st.selectbox(
            "Active Session:",
            session_names,
            index=current_index
        )
        if selected_session != st.session_state.active_session:
            st.session_state.active_session = selected_session
            st.session_state.messages = st.session_state.conversations[selected_session]
            st.rerun()

    st.divider()

    st.markdown("##### ⚙️ **Engine Status**")
    active_api = os.getenv("RESOLVEAI_API_URL", "").strip()
    if active_api:
        st.caption(f"Status: `Connected ({active_api})` 🟢")
    else:
        st.caption("Status: `Self-Contained RAG Pipeline` 🟢")

    st.markdown(
        """
        <div class="sidebar-tip-card">
            💡 <b>Admin Guidance:</b> Enter specific symptoms, error codes, or APM job behaviors to get verified resolution steps and ServiceNow closure notes.
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# TOP HEADER BAR
# ============================================================

st.markdown(
    """
    <div class="top-header">
        <div style="display:flex; align-items:center; gap:8px;">
            <span style="font-size:18px;">✨</span>
            <span style="font-weight:700; font-size:17px; color:var(--text-primary);">ResolveAI</span>
            <span style="font-size:12px; color:var(--text-secondary); margin-left:8px; border-left:1px solid var(--card-border); padding-left:10px;">
                SAP SuccessFactors Learning Troubleshooting Assistant
            </span>
        </div>
        <div>
            <div class="user-avatar" title="Tejal B">TB</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# COMPACT HERO BANNER & ISSUE CARDS (WHEN CHAT IS EMPTY)
# ============================================================

if not st.session_state.messages:
    st.markdown(
        """
        <div class="hero-banner">
            <div class="hero-badge">WELCOME TO</div>
            <div class="hero-title">Resolve<span style="color:#2563EB;">AI</span></div>
            <div class="hero-subtitle">Your AI troubleshooting assistant for SAP SuccessFactors Learning Management System</div>
            <div class="hero-pills">
                <span class="hero-pill">🔍 Knowledge-grounded responses</span>
                <span class="hero-pill">🛡️ Structured troubleshooting & ServiceNow resolutions</span>
                <span class="hero-pill">🗄️ Relevant SAP documentation with source citations</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="section-header">✨ How can I help you today?</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">Choose one of the common issues below, or describe your problem in the chat bar:</div>',
        unsafe_allow_html=True
    )

    # Compact 3-Column x 2-Row Issue Grid
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button(
            "🎓 **Course assigned again**\n\nUser completed course but assigned again",
            key="card_retraining",
            use_container_width=True
        ):
            prompt_to_submit = "Course assigned again after completion"

        if st.button(
            "📖 **Learner cannot access MyLearning**\n\nUser cannot see tile or access courses",
            key="card_mylearning",
            use_container_width=True
        ):
            prompt_to_submit = "Learner cannot access MyLearning"

    with col2:
        if st.button(
            "▶️ **Online content not launching**\n\nSCORM or online course launch failure",
            key="card_scorm",
            use_container_width=True
        ):
            prompt_to_submit = "Online content is not launching"

        if st.button(
            "📄 **Course assigned unexpectedly**\n\nUnexpected course assignment via profile",
            key="card_assignment",
            use_container_width=True
        ):
            prompt_to_submit = "Course was assigned unexpectedly"

    with col3:
        if st.button(
            "👤 **New employee missing from LMS**\n\nActive in HR but account missing in LMS",
            key="card_user_connector",
            use_container_width=True
        ):
            prompt_to_submit = "New employee is missing from LMS"

        if st.button(
            "⚙️ **Other SAP LMS issue**\n\nGeneral diagnostic checklist & admin guidance",
            key="card_other",
            use_container_width=True
        ):
            prompt_to_submit = "SAP SuccessFactors LMS troubleshooting checklist"

    st.markdown("<br>", unsafe_allow_html=True)


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
                                    <b>{source_icon} {src['source']} <span style="font-size:11px; color:#9CA3AF; font-weight:normal;">({type_label})</span></b>
                                    <span class="match-badge" style="background-color:{badge_color};">Semantic Match: {src['match_score']}%</span>
                                </div>
                                <div style="font-size:13px; color:#A1A1AA; margin-top:4px;">
                                    Scenario: <i>{src['scenario']}</i> &nbsp;•&nbsp; Category: <code>{src['category']}</code>
                                </div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )


# ============================================================
# CHAT INPUT & EXECUTION
# ============================================================

chat_input = st.chat_input("Ask ResolveAI...")
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
                                        <b>{source_icon} {src['source']} <span style="font-size:11px; color:#9CA3AF; font-weight:normal;">({type_label})</span></b>
                                        <span class="match-badge" style="background-color:{badge_color};">Semantic Match: {src['match_score']}%</span>
                                    </div>
                                    <div style="font-size:13px; color:#A1A1AA; margin-top:4px;">
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

st.markdown('<div class="chat-helper-text">✦ Be as specific as possible to get the most relevant troubleshooting guidance.</div>', unsafe_allow_html=True)