import os
import streamlit as st
import requests


# --------------------------------------------------
# CONFIGURATION & ENVIRONMENT
# --------------------------------------------------

API_URL = os.getenv("RESOLVEAI_API_URL", "http://127.0.0.1:8000")


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="ResolveAI",
    page_icon="🤖",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------

st.markdown(
    """
    <style>
    .main-title {
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .subtitle {
        font-size: 16px;
        color: #888;
        margin-bottom: 25px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# INITIALIZE CHAT HISTORY
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

prompt_to_submit = None

with st.sidebar:
    st.header("🤖 ResolveAI")
    st.write(
        "AI-powered troubleshooting assistant for "
        "SAP SuccessFactors Learning."
    )

    st.divider()
    st.subheader("💡 Common Troubleshooting Queries")
    st.caption("Click any query below to run it instantly:")

    sample_prompts = [
        "Course assigned again after completion",
        "SCORM content not launching",
        "User missing from LMS after joining",
        "Cannot access MyLearning",
        "Course assigned unexpectedly"
    ]

    for p in sample_prompts:
        if st.button(f"👉 {p}", use_container_width=True):
            prompt_to_submit = p

    st.divider()

    if st.button("🗑 Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# --------------------------------------------------
# MAIN HEADER
# --------------------------------------------------

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


# --------------------------------------------------
# DISPLAY CHAT HISTORY
# --------------------------------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message["role"] == "assistant":
            # 1-Click Copy Box for ServiceNow / Jira
            with st.expander("📋 Copy Solution for Ticket"):
                st.code(message["content"], language="markdown")

            # Verified Knowledge Sources Card
            if message.get("sources"):
                with st.expander("📚 Verified Sources & Playbooks"):
                    for src in message["sources"]:
                        st.markdown(
                            f"- **{src['source']}** — *{src['scenario']}* "
                            f"(`{src['match_score']}% match` | {src['category']})"
                        )


# --------------------------------------------------
# CHAT INPUT & SUBMISSION
# --------------------------------------------------

chat_input = st.chat_input("Describe your SAP SuccessFactors LMS issue...")
question = prompt_to_submit or chat_input


if question:
    # Store and display user question
    st.session_state.messages.append({
        "role": "user",
        "content": question,
        "sources": []
    })

    with st.chat_message("user"):
        st.markdown(question)

    # Assistant response
    with st.chat_message("assistant"):
        with st.spinner("ResolveAI is analyzing verified playbooks..."):
            try:
                response = requests.post(
                    f"{API_URL.rstrip('/')}/ask",
                    json={"question": question},
                    timeout=120
                )
                response.raise_for_status()
                data = response.json()

                answer = data["answer"]
                sources = data.get("sources", [])

                # Render AI response
                st.markdown(answer)

                # 1-Click Copy Box
                with st.expander("📋 Copy Solution for Ticket"):
                    st.code(answer, language="markdown")

                # Render Source Provenance
                if sources:
                    with st.expander("📚 Verified Sources & Playbooks"):
                        for src in sources:
                            st.markdown(
                                f"- **{src['source']}** — *{src['scenario']}* "
                                f"(`{src['match_score']}% match` | {src['category']})"
                            )

                # Store assistant response with sources
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "sources": sources
                })

            except requests.exceptions.ConnectionError:
                st.error(
                    f"⚠️ Unable to connect to the ResolveAI API at `{API_URL}`. "
                    "Please ensure the FastAPI server is running."
                )
            except requests.exceptions.Timeout:
                st.error("⚠️ The request took too long to complete. Please try again.")
            except Exception as error:
                st.error(f"⚠️ An error occurred: {error}")