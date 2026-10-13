"""
ResolveAI — Interactive Support Assistant for SAP SuccessFactors Learning.
Provides troubleshooting guidance, knowledge-source details, and ServiceNow-ready resolutions.
"""

import os
import html
import streamlit as st
import requests


# ============================================================
# CONFIGURATION
# ============================================================

try:
    for key, value in st.secrets.items():
        if isinstance(value, str) and key not in os.environ:
            os.environ[key] = value
except Exception:
    pass


st.set_page_config(
    page_title="ResolveAI | SAP LMS Support",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# RAG / API CONNECTION
# ============================================================

def query_resolveai(question: str) -> dict:
    """Use the configured API, or fall back to the local RAG pipeline."""
    api_url = os.getenv("RESOLVEAI_API_URL", "").strip()

    if api_url:
        try:
            response = requests.post(
                f"{api_url.rstrip('/')}/ask",
                json={"question": question},
                timeout=120,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.ConnectionError:
            pass
        except requests.exceptions.Timeout:
            raise
        except requests.exceptions.RequestException:
            pass

    from src.rag.pipeline import answer_question
    return answer_question(question)


# ============================================================
# SESSION STATE
# ============================================================

if "conversations" not in st.session_state:
    st.session_state.conversations = {"Session 1": []}

if "active_session" not in st.session_state:
    st.session_state.active_session = "Session 1"

if st.session_state.active_session not in st.session_state.conversations:
    st.session_state.active_session = next(
        iter(st.session_state.conversations)
    )

if "messages" not in st.session_state:
    st.session_state.messages = st.session_state.conversations[
        st.session_state.active_session
    ]
else:
    st.session_state.messages = st.session_state.conversations[
        st.session_state.active_session
    ]


# ============================================================
# STYLING
# ============================================================

st.markdown(
    """
    <style>
    @import url(
        'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
    );

    :root {
        --primary: #2563EB;
        --primary-dark: #1D4ED8;
        --text: #0F172A;
        --muted: #64748B;
        --border: #E2E8F0;
        --surface: #FFFFFF;
        --soft-blue: #F1F6FF;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: #FFFFFF;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 2.8rem;
        padding-bottom: 5rem;
    }

    /* Sidebar */

    section[data-testid="stSidebar"] {
        background: #F8FAFC;
        border-right: 1px solid #E8EDF4;
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 1.7rem;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 5px;
    }

    .brand-icon {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 40px;
        height: 40px;
        border-radius: 12px;
        background: #DBEAFE;
        font-size: 22px;
    }

    .brand-name {
        color: #0F172A;
        font-size: 22px;
        font-weight: 800;
        letter-spacing: -0.7px;
    }

    .sidebar-description {
        color: #64748B;
        font-size: 12px;
        line-height: 1.7;
        margin: 8px 0 26px 0;
    }

    .sidebar-label {
        color: #64748B;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin: 18px 0 10px 0;
    }

    /* Main header */

    .topbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding-top: 8px;
        padding-bottom: 16px;
        margin-bottom: 20px;
        border-bottom: 1px solid #EAEFF5;
    }

    .topbar-title {
        color: #0F172A;
        font-size: 15px;
        font-weight: 700;
    }

    .topbar-subtitle {
        color: #64748B;
        font-size: 12px;
        margin-top: 4px;
    }

    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 7px;
        background: #F0FDF4;
        color: #166534;
        border: 1px solid #DCFCE7;
        border-radius: 30px;
        padding: 7px 11px;
        font-size: 11px;
        font-weight: 600;
        white-space: nowrap;
    }

    .status-dot {
        height: 7px;
        width: 7px;
        background: #22C55E;
        border-radius: 50%;
    }

    /* Welcome section */

    .welcome-panel {
        background: linear-gradient(120deg, #F1F6FF 0%, #F8FAFF 100%);
        border: 1px solid #DBEAFE;
        border-radius: 16px;
        padding: 18px 22px;
        margin-bottom: 20px;
    }

    .welcome-eyebrow {
        color: #2563EB;
        font-size: 10.5px;
        font-weight: 800;
        letter-spacing: 1.2px;
        margin-bottom: 6px;
    }

    .welcome-title {
        color: #0F172A;
        font-size: clamp(22px, 2.5vw, 28px);
        line-height: 1.2;
        font-weight: 800;
        letter-spacing: -0.8px;
        margin: 0 0 8px 0;
    }

    .welcome-description {
        color: #52627A;
        font-size: 13.5px;
        line-height: 1.6;
        max-width: 680px;
        margin-bottom: 14px;
    }

    .feature-row {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
    }

    .feature-tag {
        display: inline-block;
        background: #FFFFFF;
        border: 1px solid #DCE7F8;
        color: #31527D;
        padding: 7px 11px;
        border-radius: 8px;
        font-size: 11px;
        font-weight: 600;
    }

    /* Issue cards */

    .section-title {
        color: #0F172A;
        font-size: 20px;
        font-weight: 750;
        letter-spacing: -0.4px;
        margin-bottom: 5px;
    }

    .section-description {
        color: #64748B;
        font-size: 13px;
        line-height: 1.7;
        margin-bottom: 18px;
    }

    .issue-btn button {
        box-sizing: border-box !important;
        min-height: 112px !important;
        height: 112px !important;
        background: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 13px !important;
        padding: 14px 18px !important;
        margin-bottom: 10px !important;
        text-align: left !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: flex-start !important;
        justify-content: flex-start !important;
        transition: border-color 0.2s, background 0.2s, transform 0.2s, box-shadow 0.2s !important;
        overflow: hidden !important;
        white-space: normal !important;
    }

    .issue-btn button:hover {
        border-color: #93C5FD !important;
        background: #FCFDFF !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.08) !important;
    }

    .issue-btn button div,
    .issue-btn button p {
        text-align: left !important;
        white-space: normal !important;
        word-wrap: break-word !important;
        line-height: 1.45 !important;
        margin: 0 !important;
        width: 100% !important;
    }

    /* Buttons */

    .stButton > button {
        border-radius: 9px;
        font-family: 'Inter', sans-serif;
        font-size: 12px;
        font-weight: 600;
        transition: all 0.2s ease;
    }

    section[data-testid="stSidebar"] .stButton > button {
        min-height: 39px;
    }

    .main .stButton > button {
        min-height: 37px;
        border: 1px solid #E2E8F0;
        background: #FFFFFF;
        color: #334155;
    }

    .main .stButton > button:hover {
        border-color: #93C5FD;
        color: #1D4ED8;
        background: #F8FBFF;
    }

    /* Chat */

    [data-testid="stChatMessage"] {
        border: 1px solid #EDF1F6;
        border-radius: 13px;
        padding: 12px 16px;
        margin-bottom: 14px;
    }

    [data-testid="stChatInput"] {
        border-color: #D9E2EF;
        border-radius: 13px;
    }

    .chat-helper {
        text-align: center;
        color: #94A3B8;
        font-size: 11px;
        margin-top: 10px;
        margin-bottom: 14px;
    }

    /* Source details */

    .source-box {
        background: #F8FAFC;
        border: 1px solid #E6EDF5;
        border-left: 3px solid #60A5FA;
        border-radius: 8px;
        padding: 12px;
        margin: 8px 0;
        overflow-wrap: anywhere;
    }

    .source-name {
        color: #1E293B;
        font-size: 12px;
        font-weight: 700;
        margin-bottom: 7px;
    }

    .source-meta {
        color: #64748B;
        font-size: 11px;
        line-height: 1.7;
    }

    .match-badge {
        display: inline-block;
        color: #1D4ED8;
        background: #DBEAFE;
        border-radius: 6px;
        padding: 3px 7px;
        font-size: 10px;
        font-weight: 700;
        margin-top: 3px;
    }

    @media (max-width: 768px) {
        .welcome-panel {
            padding: 22px 18px;
        }

        .issue-card {
            min-height: 140px;
            height: 140px;
            padding: 13px;
        }

        .topbar {
            align-items: flex-start;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def render_sources(sources):
    """Display retrieved knowledge-source metadata."""
    if not sources:
        return

    with st.expander(f"📚 Retrieved Knowledge Sources ({len(sources)})"):
        for src in sources:
            source_name = str(src.get("source", "Knowledge source"))
            source_type = str(src.get("source_type", ""))
            scenario = str(src.get("scenario", "Not specified"))
            category = str(src.get("category", "Not specified"))

            is_kba = (
                "SAP" in source_type.upper()
                or source_name.lower().endswith("_sap.md")
            )

            source_label = "SAP KBA" if is_kba else "Expert Playbook"

            try:
                score = float(src.get("match_score", 0))
                score_text = f"{score:g}%"
            except (TypeError, ValueError):
                score_text = "N/A"

            st.markdown(
                f"""
                <div class="source-box">
                    <div class="source-name">
                        {"📘" if is_kba else "📖"}
                        {html.escape(source_name)}
                        <span style="font-weight:400;color:#64748B;">
                            · {source_label}
                        </span>
                    </div>
                    <div class="source-meta">
                        <b>Scenario:</b> {html.escape(scenario)}<br>
                        <b>Category:</b> {html.escape(category)}
                    </div>
                    <span class="match-badge">
                        Semantic Match: {html.escape(score_text)}
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_assistant_message(message):
    """Display an existing assistant message and its supporting sources."""
    st.markdown(message.get("content", ""))

    with st.expander("📋 ServiceNow Resolution"):
        st.code(message.get("content", ""), language="markdown")

    render_sources(message.get("sources", []))


def submit_question(question):
    """Run a question through ResolveAI and save the conversation."""
    question = question.strip()
    if not question:
        return

    messages = st.session_state.conversations[
        st.session_state.active_session
    ]

    messages.append({
        "role": "user",
        "content": question,
        "sources": [],
    })

    st.session_state.conversations[
        st.session_state.active_session
    ] = messages

    try:
        with st.spinner("Searching relevant knowledge and preparing a resolution..."):
            data = query_resolveai(question)

        answer = data.get("answer", "No answer was returned.")
        sources = data.get("sources", [])

        messages.append({
            "role": "assistant",
            "content": answer,
            "sources": sources,
        })

        st.session_state.conversations[
            st.session_state.active_session
        ] = messages

    except requests.exceptions.Timeout:
        st.session_state.error_message = (
            "The request timed out. Please try again."
        )

    except Exception as exc:
        st.session_state.error_message = (
            f"Unable to process the request: {exc}"
        )


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown(
        """
        <div class="brand">
            <div class="brand-icon">🤖</div>
            <div class="brand-name">ResolveAI</div>
        </div>
        <div class="sidebar-description">
            SAP SuccessFactors Learning<br>
            Intelligent Troubleshooting Assistant
        </div>
        <div class="sidebar-label">Workspace</div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="
            padding: 10px 12px;
            background: #EAF2FF;
            color: #1D4ED8;
            border-radius: 9px;
            font-size: 13px;
            font-weight: 700;
            margin-bottom: 22px;
        ">
            💬 &nbsp; Troubleshooting Chat
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="sidebar-label">Conversation</div>',
        unsafe_allow_html=True,
    )

    col_new, col_clear = st.columns(2)

    with col_new:
        if st.button("＋ New Chat", use_container_width=True):
            existing_numbers = []

            for name in st.session_state.conversations:
                if name.startswith("Session "):
                    try:
                        existing_numbers.append(int(name.split()[-1]))
                    except ValueError:
                        pass

            next_number = max(existing_numbers, default=0) + 1
            new_name = f"Session {next_number}"

            st.session_state.conversations[new_name] = []
            st.session_state.active_session = new_name
            st.session_state.messages = (
                st.session_state.conversations[new_name]
            )

            st.rerun()

    with col_clear:
        if st.button("Clear Chat", use_container_width=True):
            st.session_state.conversations[
                st.session_state.active_session
            ] = []

            st.session_state.messages = []
            st.rerun()

    session_names = list(st.session_state.conversations.keys())

    if len(session_names) > 1:
        current_index = session_names.index(
            st.session_state.active_session
        )

        selected_session = st.selectbox(
            "Switch conversation",
            session_names,
            index=current_index,
        )

        if selected_session != st.session_state.active_session:
            st.session_state.active_session = selected_session
            st.session_state.messages = (
                st.session_state.conversations[selected_session]
            )
            st.rerun()

    st.markdown("---")

    api_configured = bool(
        os.getenv("RESOLVEAI_API_URL", "").strip()
    )

    if api_configured:
        st.caption("🔗 API configured")
    else:
        st.caption("⚙️ Direct RAG pipeline")

    st.caption("Knowledge-grounded support assistance")


# ============================================================
# MAIN HEADER
# ============================================================

st.markdown(
    """
    <div class="topbar">
        <div>
            <div class="topbar-title">
                SAP SuccessFactors Learning Support
            </div>
            <div class="topbar-subtitle">
                Troubleshoot incidents with relevant knowledge and structured resolutions.
            </div>
        </div>
        <div class="status-pill">
            <span class="status-dot"></span>
            Support Assistant
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# WELCOME SCREEN AND ISSUE CARDS
# ============================================================

if not st.session_state.messages:
    st.markdown(
        """
        <div class="welcome-panel">
            <div class="welcome-eyebrow">YOUR SUPPORT WORKSPACE</div>
            <div class="welcome-title">
                Resolve issues.<br>
                Get back to work.
            </div>
            <div class="welcome-description">
                Describe your SAP SuccessFactors Learning issue and get
                structured troubleshooting guidance based on relevant
                knowledge sources.
            </div>
            <div class="feature-row">
                <span class="feature-tag">Knowledge-grounded guidance</span>
                <span class="feature-tag">ServiceNow-ready resolutions</span>
                <span class="feature-tag">Source details</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title">What do you need help with?</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="section-description">
            Select a scenario to get started, or describe your issue below.
        </div>
        """,
        unsafe_allow_html=True,
    )

    issues = [
        {
            "key": "retraining",
            "icon": "🔁",
            "title": "Course assigned again",
            "description": "A completed course has been assigned to the learner again.",
            "prompt": "Course assigned again after completion",
        },
        {
            "key": "content",
            "icon": "▶️",
            "title": "Online content not launching",
            "description": "Course content fails to open or launch for a learner.",
            "prompt": "Online content is not launching",
        },
        {
            "key": "mylearning",
            "icon": "📚",
            "title": "MyLearning access",
            "description": "A learner cannot access MyLearning or view assigned courses.",
            "prompt": "Learner cannot access MyLearning",
        },
        {
            "key": "assignment",
            "icon": "📋",
            "title": "Unexpected course assignment",
            "description": "A learner received a course assignment they did not expect.",
            "prompt": "Course was assigned unexpectedly",
        },
        {
            "key": "employee",
            "icon": "👤",
            "title": "New employee missing",
            "description": "A new employee cannot be found in the LMS.",
            "prompt": "New employee is missing from LMS",
        },
        {
            "key": "other",
            "icon": "🛠️",
            "title": "Other LMS issue",
            "description": "Get help investigating another SAP Learning issue.",
            "prompt": "SAP SuccessFactors LMS troubleshooting checklist",
        },
    ]

    # Two columns of clickable, compact cards.
    left_col, right_col = st.columns(2, gap="medium")

    for index, issue in enumerate(issues):
        target_col = left_col if index % 2 == 0 else right_col

        with target_col:
            st.markdown('<div class="issue-btn">', unsafe_allow_html=True)
            card_text = f"{issue['icon']}  **{issue['title']}**\n\n{issue['description']}"
            if st.button(
                card_text,
                key=f"issue_{issue['key']}",
                use_container_width=True,
            ):
                st.session_state.pending_question = issue["prompt"]
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# CHAT HISTORY
# ============================================================

for message in st.session_state.conversations[
    st.session_state.active_session
]:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant":
            render_assistant_message(message)
        else:
            st.markdown(message.get("content", ""))


# ============================================================
# CHAT INPUT AND EXECUTION
# ============================================================

if "pending_question" not in st.session_state:
    st.session_state.pending_question = None

if "error_message" not in st.session_state:
    st.session_state.error_message = None

chat_input = st.chat_input(
    "Ask ResolveAI..."
)

question = (
    st.session_state.pending_question
    or chat_input
)

if question:
    st.session_state.pending_question = None

    submit_question(question)

    # Rerun so the submitted question and response appear in chat history.
    st.rerun()

if st.session_state.error_message:
    st.error(st.session_state.error_message)

    if st.button("Dismiss error"):
        st.session_state.error_message = None
        st.rerun()

st.markdown(
    """
    <div class="chat-helper">
        Avoid sharing passwords or other sensitive information.
    </div>
    """,
    unsafe_allow_html=True,
)