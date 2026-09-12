import os
import streamlit as st
import requests


# ============================================================
# CONFIGURATION
# ============================================================

API_URL = os.getenv(
    "RESOLVEAI_API_URL",
    "http://127.0.0.1:8000"
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="ResolveAI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM STYLING
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 40px;
        font-weight: 700;
        margin-bottom: 0px;
    }

    .subtitle {
        font-size: 16px;
        color: #888;
        margin-bottom: 25px;
    }

    .source-card {
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 8px;
    }

    .status-box {
        padding: 8px 12px;
        border-radius: 8px;
        font-size: 14px;
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

    st.header("🤖 ResolveAI")

    st.write(
        "AI-powered troubleshooting assistant for "
        "SAP SuccessFactors Learning."
    )

    st.divider()


    # --------------------------------------------------------
    # QUICK PROMPTS
    # --------------------------------------------------------

    st.subheader("💡 Quick Troubleshooting")

    st.caption(
        "Select a common SAP SuccessFactors Learning issue:"
    )

    sample_prompts = [
        "Course assigned again after completion",
        "SCORM content not launching",
        "User missing from LMS after joining",
        "Cannot access MyLearning",
        "Course assigned unexpectedly"
    ]

    for prompt in sample_prompts:

        if st.button(
            f"👉 {prompt}",
            use_container_width=True
        ):
            prompt_to_submit = prompt

    st.divider()

    # --------------------------------------------------------
    # CLEAR CHAT
    # --------------------------------------------------------

    if st.button(
        "🗑 Clear Conversation",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()


# ============================================================
# MAIN HEADER
# ============================================================

st.markdown(
    '<div class="main-title">ResolveAI 🤖</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Your SAP SuccessFactors Learning troubleshooting assistant'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# WELCOME MESSAGE
# ============================================================

if not st.session_state.messages:

    st.info(
        "👋 Describe an SAP SuccessFactors Learning issue "
        "or select a troubleshooting scenario from the sidebar."
    )


# ============================================================
# DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        # ----------------------------------------------------
        # ASSISTANT-ONLY INFORMATION
        # ----------------------------------------------------

        if message["role"] == "assistant":

            # Copy solution
            with st.expander(
                "📋 Copy Solution for ServiceNow / Jira"
            ):
                st.code(
                    message["content"],
                    language="markdown"
                )

            # Sources
            sources = message.get("sources", [])

            if sources:

                with st.expander(
                    "📚 Verified Knowledge Sources"
                ):

                    for source in sources:

                        st.markdown(
                            f"""
                            **{source['source']}**

                            Scenario: *{source['scenario']}*  
                            Category: `{source['category']}`  
                            Match: **{source['match_score']}%**
                            """
                        )

                        st.divider()


# ============================================================
# CHAT INPUT
# ============================================================

chat_input = st.chat_input(
    "Describe your SAP SuccessFactors LMS issue..."
)

question = prompt_to_submit or chat_input


# ============================================================
# PROCESS QUESTION
# ============================================================

if question:

    # --------------------------------------------------------
    # STORE USER MESSAGE
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
            "sources": []
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # --------------------------------------------------------
    # GENERATE ASSISTANT RESPONSE
    # --------------------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner(
            "ResolveAI is analyzing verified playbooks..."
        ):

            try:

                response = requests.post(
                    f"{API_URL.rstrip('/')}/ask",
                    json={
                        "question": question
                    },
                    timeout=120
                )

                response.raise_for_status()

                data = response.json()

                answer = data.get(
                    "answer",
                    "No answer was returned."
                )

                sources = data.get(
                    "sources",
                    []
                )

                # ------------------------------------------------
                # ANSWER
                # ------------------------------------------------

                st.markdown(answer)

                # ------------------------------------------------
                # COPY SOLUTION
                # ------------------------------------------------

                with st.expander(
                    "📋 Copy Solution for ServiceNow / Jira"
                ):

                    st.code(
                        answer,
                        language="markdown"
                    )

                # ------------------------------------------------
                # SOURCES
                # ------------------------------------------------

                if sources:

                    with st.expander(
                        "📚 Verified Knowledge Sources"
                    ):

                        for source in sources:

                            st.markdown(
                                f"""
                                **{source['source']}**

                                Scenario: *{source['scenario']}*  
                                Category: `{source['category']}`  
                                Match: **{source['match_score']}%**
                                """
                            )

                            st.divider()

                # ------------------------------------------------
                # STORE ASSISTANT RESPONSE
                # ------------------------------------------------

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "sources": sources
                    }
                )

            # ----------------------------------------------------
            # ERROR HANDLING
            # ----------------------------------------------------

            except requests.exceptions.ConnectionError:

                st.error(
                    "⚠️ Unable to connect to the ResolveAI backend."
                )

                st.caption(
                    f"Backend URL: {API_URL}"
                )

            except requests.exceptions.Timeout:

                st.error(
                    "⚠️ The request took too long to complete. "
                    "Please try again."
                )

            except requests.exceptions.HTTPError as error:

                st.error(
                    f"⚠️ Backend returned an HTTP error: {error}"
                )

            except Exception as error:

                st.error(
                    f"⚠️ An unexpected error occurred: {error}"
                )