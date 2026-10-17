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
# CLEAN, MODERN ENTERPRISE STYLING
# ============================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }

    /* Enforce Clean Light Mode permanently */
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

    /* Page container spacing - ensures welcome banner is never clipped by Streamlit toolbar */
    .block-container {
        padding-top: 4.75rem !important;
        padding-bottom: 3rem !important;
        max-width: 1200px !important;
    }

    /* Welcome Banner */
    .welcome-card {
        background: linear-gradient(135deg, #F0F7FF 0%, #E8F2FE 100%);
        border: 1px solid #D6E4F6;
        border-radius: 16px;
        padding: 24px 28px;
        margin-bottom: 24px;
        position: relative;
        box-shadow: 0 2px 8px rgba(37, 99, 235, 0.04);
    }

    .welcome-label {
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1px;
        color: #2563EB;
        margin-bottom: 4px;
    }

    .welcome-title {
        font-size: 28px;
        font-weight: 800;
        color: #0F172A;
        margin-bottom: 6px;
    }

    .welcome-subtitle {
        font-size: 14px;
        color: #475569;
        margin-bottom: 16px;
        max-width: 680px;
    }

    .feature-pills {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
    }

    .feature-pill {
        background: #FFFFFF;
        border: 1px solid #DBEAFE;
        color: #1E40AF;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 500;
        display: inline-flex;
        align-items: center;
        gap: 6px;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.03);
    }

    /* Section Header */
    .section-title {
        font-size: 18px;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 4px;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    .section-subtitle {
        font-size: 13px;
        color: #64748B;
        margin-bottom: 16px;
    }

    /* 6 Issue Cards Styling: full card clickable without truncation */
    div[data-testid="stColumn"] div.stButton > button {
        display: flex !important;
        flex-direction: column !important;
        align-items: flex-start !important;
        justify-content: flex-start !important;
        text-align: left !important;
        white-space: normal !important;
        word-break: break-word !important;
        height: 100% !important;
        min-height: 110px !important;
        padding: 16px 18px !important;
        border-radius: 14px !important;
        background: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04) !important;
        transition: all 0.2s ease-in-out !important;
        cursor: pointer !important;
    }

    div[data-testid="stColumn"] div.stButton > button:hover {
        border-color: #3B82F6 !important;
        background: #F8FAFC !important;
        box-shadow: 0 6px 16px rgba(59, 130, 246, 0.12) !important;
        transform: translateY(-2px) !important;
    }

    div[data-testid="stColumn"] div.stButton > button div[data-testid="stMarkdownContainer"] {
        width: 100% !important;
        text-align: left !important;
        white-space: normal !important;
    }

    div[data-testid="stColumn"] div.stButton > button p {
        white-space: normal !important;
        word-break: break-word !important;
        text-align: left !important;
        line-height: 1.45 !important;
        font-size: 12.5px !important;
        color: #64748B !important;
        margin: 0 !important;
    }

    div[data-testid="stColumn"] div.stButton > button strong {
        display: block !important;
        font-size: 14.5px !important;
        font-weight: 700 !important;
        color: #0F172A !important;
        margin-bottom: 6px !important;
        line-height: 1.35 !important;
    }

    /* Sidebar Clean Styling */
    .sidebar-brand {
        font-size: 20px;
        font-weight: 700;
        color: #0F172A;
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 2px;
    }

    .sidebar-desc {
        font-size: 12px;
        color: #64748B;
        line-height: 1.4;
        margin-bottom: 18px;
    }

    .sidebar-nav-item {
        background: #EFF6FF;
        color: #2563EB;
        font-weight: 600;
        font-size: 14px;
        padding: 8px 14px;
        border-radius: 8px;
        border-left: 3px solid #2563EB;
        margin-bottom: 18px;
    }

    .sidebar-help-box {
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 12px 14px;
        font-size: 12px;
        color: #64748B;
        line-height: 1.45;
        margin-top: 24px;
    }

    /* Knowledge Badges & Source Boxes */
    .match-badge {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 600;
        background-color: #2563EB;
        color: white;
    }

    .source-box {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-left: 3px solid #2563EB;
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 10px;
    }

    .chat-caption {
        font-size: 12px;
        color: #94A3B8;
        text-align: center;
        margin-top: 8px;
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
# SIDEBAR
# ============================================================

prompt_to_submit = None

with st.sidebar:
    st.markdown('<div class="sidebar-brand">🤖 ResolveAI</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-desc">SAP SuccessFactors Learning Troubleshooting Assistant</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-nav-item">💬 Chat</div>', unsafe_allow_html=True)

    st.markdown("##### 🗂️ **Session**")
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
        if st.button("🗑️ Clear Chat", use_container_width=True):
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
            💡 <b>Admin Guidance</b><br>
            Get step-by-step troubleshooting guidance for SAP SuccessFactors Learning issues.
        </div>
        """,
        unsafe_allow_html=True
    )


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
                <span class="feature-pill">🔍 Knowledge-grounded responses</span>
                <span class="feature-pill">🛡️ Structured troubleshooting and ServiceNow resolutions</span>
                <span class="feature-pill">📚 Relevant SAP documentation with source citations</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Section Heading
    st.markdown(
        """
        <div class="section-title">✨ How can I help you today?</div>
        <div class="section-subtitle">Choose one of the common issues below, or describe your problem in the chat bar:</div>
        """,
        unsafe_allow_html=True
    )

    # Row 1: Cards 1 - 3
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button(
            "**🎓 Course assigned again after completion**\n\nUser completed a course but it was assigned to them again. ›",
            key="card_retraining",
            use_container_width=True
        ):
            prompt_to_submit = "Course assigned again after completion"

    with col2:
        if st.button(
            "**▶️ Online content is not launching**\n\nLearners report that online course content is not launching. ›",
            key="card_scorm",
            use_container_width=True
        ):
            prompt_to_submit = "Online content is not launching"

    with col3:
        if st.button(
            "**👤 New employee is missing from LMS**\n\nA new hire has joined, but their account cannot be found in LMS. ›",
            key="card_user_sync",
            use_container_width=True
        ):
            prompt_to_submit = "New employee is missing from LMS"

    # Row 2: Cards 4 - 6
    col4, col5, col6 = st.columns(3)

    with col4:
        if st.button(
            "**📖 Learner cannot access MyLearning**\n\nUser is unable to access MyLearning or cannot see assigned courses. ›",
            key="card_access",
            use_container_width=True
        ):
            prompt_to_submit = "Learner cannot access MyLearning"

    with col5:
        if st.button(
            "**📋 Course was assigned unexpectedly**\n\nA user received a course assignment that they shouldn't have. ›",
            key="card_unexpected",
            use_container_width=True
        ):
            prompt_to_submit = "Course was assigned unexpectedly"

    with col6:
        if st.button(
            "**⚙️ Other SAP LMS issue**\n\nDescribe your specific issue in the chat below. ›",
            key="card_other",
            use_container_width=True
        ):
            prompt_to_submit = "Other SAP LMS issue"

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

chat_input = st.chat_input("Describe your SAP LMS issue (e.g., 'User completed course but assigned again')...")
question = prompt_to_submit or chat_input

if not st.session_state.messages:
    st.markdown(
        '<div class="chat-caption">✦ Be as specific as possible to get the most relevant troubleshooting guidance.</div>',
        unsafe_allow_html=True
    )

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