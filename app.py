"""
ResolveAI — Interactive Support Assistant for SAP SuccessFactors Learning.
Provides real-time troubleshooting, source citations, and ticket resolutions.
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
# CLEAN, MODERN STYLING
# ============================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .main-title {
        font-size: 34px;
        font-weight: 700;
        margin-bottom: 2px;
    }

    .subtitle {
        font-size: 15px;
        color: #71717A;
        margin-bottom: 25px;
    }

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
        background-color: rgba(128, 128, 128, 0.05);
        border-left: 3px solid #2563EB;
        border-radius: 6px;
        padding: 12px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ============================================================
# SIDEBAR
# ============================================================

prompt_to_submit = None

with st.sidebar:
    st.markdown("### 🤖 **ResolveAI**")
    st.caption("Troubleshooting assistant for **SAP SuccessFactors Learning**")

    st.divider()

    st.markdown("##### 💬 **Common Inquiries**")
    st.caption("Click any question to ask immediately:")

    sample_questions = [
        "Course assigned again after completion",
        "Online content is not launching",
        "New employee is missing from LMS",
        "Learner cannot access MyLearning",
        "Course was assigned unexpectedly"
    ]

    for q in sample_questions:
        if st.button(f"👉 {q}", use_container_width=True):
            prompt_to_submit = q

    st.divider()

    st.markdown("##### ⚙️ **Engine Status**")
    active_api = os.getenv("RESOLVEAI_API_URL", "").strip()
    if active_api:
        st.caption(f"Status: `Connected ({active_api})` 🟢")
    else:
        st.caption("Status: `Self-Contained RAG Pipeline` 🟢")

    if st.button("🗑 Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ============================================================
# MAIN HEADER
# ============================================================

st.markdown('<div class="main-title">ResolveAI 🤖</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Your AI troubleshooting assistant for SAP SuccessFactors Learning Management System</div>',
    unsafe_allow_html=True
)


# ============================================================
# WELCOME AREA (NATURAL ENGLISH QUESTIONS)
# ============================================================

if not st.session_state.messages:
    st.markdown("##### 💡 **How can I help you today?**")
    st.caption("Choose one of the common issues below, or describe your problem in the chat bar:")

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "📌 **A user finished a course, but it was assigned to them again.**",
            use_container_width=True
        ):
            prompt_to_submit = "Course assigned again after completion"

        if st.button(
            "📌 **Learners report that online course content is not launching.**",
            use_container_width=True
        ):
            prompt_to_submit = "SCORM content not launching"

    with col2:
        if st.button(
            "📌 **A new hire has joined, but their account cannot be found in LMS.**",
            use_container_width=True
        ):
            prompt_to_submit = "User missing from LMS after joining"

        if st.button(
            "📌 **A user received a course assignment that they shouldn't have.**",
            use_container_width=True
        ):
            prompt_to_submit = "Course assigned unexpectedly"

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
                with st.expander(f"📚 Verified Knowledge Sources ({len(sources)} playbooks cited)"):
                    for src in sources:
                        st.markdown(
                            f"""
                            <div class="source-box">
                                <div style="display:flex; justify-content:space-between; align-items:center;">
                                    <b>📖 {src['source']}</b>
                                    <span class="match-badge">{src['match_score']}% Match</span>
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

chat_input = st.chat_input("Describe your SAP LMS issue (e.g., 'User completed course but assigned again')...")
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

                # Render verified knowledge sources
                if sources:
                    with st.expander(f"📚 Verified Knowledge Sources ({len(sources)} playbooks cited)"):
                        for src in sources:
                            st.markdown(
                                f"""
                                <div class="source-box">
                                    <div style="display:flex; justify-content:space-between; align-items:center;">
                                        <b>📖 {src['source']}</b>
                                        <span class="match-badge">{src['match_score']}% Match</span>
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

            except requests.exceptions.Timeout:
                st.error("⚠️ The request timed out. Please try again.")
            except Exception as e:
                st.error(f"⚠️ An unexpected error occurred: {e}")