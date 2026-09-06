import streamlit as st
import requests


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
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 0px;
    }

    .subtitle {
        font-size: 18px;
        color: #666;
        margin-bottom: 30px;
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

with st.sidebar:

    st.header("🤖 ResolveAI")

    st.write(
        "AI-powered troubleshooting assistant for "
        "SAP SuccessFactors Learning."
    )

    st.divider()

    st.subheader("Try asking:")

    st.caption("• Course assigned again after completion")

    st.caption("• SCORM content not launching")

    st.caption("• User missing from LMS after joining")

    st.caption("• Cannot access MyLearning")

    st.caption("• Course assigned unexpectedly")

    st.divider()

    if st.button("🗑 Clear Conversation"):

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


# --------------------------------------------------
# CHAT INPUT
# --------------------------------------------------

question = st.chat_input(
    "Describe your SAP SuccessFactors LMS issue..."
)


# --------------------------------------------------
# PROCESS QUESTION
# --------------------------------------------------

if question:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Display user message
    with st.chat_message("user"):

        st.markdown(question)


    # Assistant response
    with st.chat_message("assistant"):

        with st.spinner(
            "ResolveAI is analyzing the issue..."
        ):

            try:

                response = requests.post(
                    "http://127.0.0.1:8000/ask",
                    json={
                        "question": question
                    },
                    timeout=120
                )

                response.raise_for_status()

                answer = response.json()["answer"]

                st.markdown(answer)


                # Store assistant response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )


            except requests.exceptions.ConnectionError:

                error_message = (
                    "⚠️ Unable to connect to the ResolveAI API. "
                    "Please make sure FastAPI is running."
                )

                st.error(error_message)


            except requests.exceptions.Timeout:

                error_message = (
                    "⚠️ The request took too long to complete. "
                    "Please try again."
                )

                st.error(error_message)


            except Exception as error:

                error_message = (
                    f"⚠️ Something went wrong: {error}"
                )

                st.error(error_message)