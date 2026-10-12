import time
import os

from google import genai
from google.genai import types
from dotenv import load_dotenv

from src.config import settings


# Load environment variables
load_dotenv()


def get_api_key() -> str | None:
    """
    Retrieve Gemini API key with multi-source fallback:
    1. Environment variable (os.environ)
    2. Streamlit Cloud Secrets (st.secrets)
    """
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        try:
            import streamlit as st
            key = st.secrets.get("GEMINI_API_KEY")
        except Exception:
            pass
    return key


def direct_playbook_fallback(question: str, context: str) -> str:
    """
    Zero-downtime safety net:
    If the external LLM API is unavailable, extract verified troubleshooting steps
    and closure notes directly from the retrieved knowledge base chunks and format
    them cleanly into the corporate ServiceNow closure template.
    """
    return f"""### 🎫 Incident Analysis
* **Symptom:** {question}
* **Resolution Mode:** Verified SAP SuccessFactors Knowledge Base (Direct Playbook Resolution)

### 🔍 SAP LMS Admin Diagnostic Checklist
Based on verified SAP SuccessFactors documentation for this incident:

{context.strip()}

### 📋 ServiceNow Closure Notes
Failure point/Cause Code: SAP SuccessFactors LMS Configuration / Administrative Verification
Problem Description: {question}
Impact: NA
Workaround: NA
Resolution steps taken/ Solution/ Fix/ Preventive action: Verified reported issue against standard SAP SuccessFactors expert playbooks and official KBAs. Applied diagnostic checks and validation rules outlined in the administrative checklist above.
Knowledge Object: NA
Problem Ticket/Story: NA

### ✉️ Customer Resolution (Additional Comments)
"Hello, our support team has investigated your reported inquiry regarding '{question}'. Please review the diagnostic verification and resolution details documented in this ticket. If you require further assistance or need an administrator review, please update this incident."
"""


def generate_response(question: str, context: str) -> str:
    """
    Generate a grounded SAP SuccessFactors LMS troubleshooting
    response using dynamically retrieved knowledge context.
    """

    prompt = f"""
You are ResolveAI, an expert Tier-2/Tier-3 SAP SuccessFactors Learning Management System (LMS) Support Specialist handling ServiceNow incidents.

Your role is to investigate and resolve SAP LMS support incidents reported in ServiceNow by learners, managers, or HR administrators using the provided verified context.

Your response must be strictly grounded ONLY in the provided context below.

CRITICAL RULES:
1. Grounding: Use ONLY technical facts, behaviors, and troubleshooting logic supported by the provided context.
2. Accuracy: Do not invent SAP configuration settings, database tables, navigation paths, or system behaviors not substantiated by the context.
3. Specificity: Avoid vague generic advice like "check settings". State exactly WHAT configuration parameter, field, or record to inspect (e.g., Retraining Basis, Required Date, APM execution, Assignment Profile criteria, SCORM launch method, etc.).
4. Decision Logic: Use clear IF-THEN diagnostic logic where multiple scenarios or configuration types exist.
5. Tone: Professional, analytical, and incident-oriented, formatted specifically for ServiceNow support operations.
6. Exclusion: Never mention other ticketing systems, knowledge base, vector database, chunks, embeddings, retrieval, RAG, or internal AI architecture.
7. Format: Do NOT include opening greetings or pleasantries (e.g., "Hello", "As an assistant..."). Start directly with the incident analysis.

REQUIRED SERVICENOW INCIDENT STRUCTURE:

### 🎫 Incident Analysis
* **Symptom:** Concise restatement of the reported problem.
* **Root Cause Assessment:** Primary technical cause(s) supported by the context.

### 🔍 SAP LMS Admin Diagnostic Checklist
Step-by-step investigation checklist for the support engineer in SAP SuccessFactors Admin:
* Concrete areas to inspect (user records, tabs, settings, timestamps, or background jobs).
* Clear IF-THEN branching logic (e.g., "If Event-Based retraining..." vs. "If Calendar-Based retraining...").

### 📋 ServiceNow Closure Notes
Failure point/Cause Code: [Short technical description of the failure point based on context]
Problem Description: [Description of the issue reported by the user]
Impact: NA
Workaround: NA
Resolution steps taken/ Solution/ Fix/ Preventive action: [Detailed technical explanation of what was verified, why the issue occurred, and the resolution or preventive action taken per the context]
Knowledge Object: NA
Problem Ticket/Story: NA

### ✉️ Customer Resolution (Additional Comments)
[Professional, user-friendly communication ready to send to the learner/manager resolving the ticket]

CONTEXT:
{context}

USER INCIDENT / QUESTION:
{question}

Generate a comprehensive, incident-oriented ServiceNow troubleshooting resolution:
"""

    api_key = get_api_key()
    if not api_key:
        print("Notice: GEMINI_API_KEY is not available. Using Direct Playbook Fallback.")
        return direct_playbook_fallback(question, context)

    # Model cascade: try primary model, fall back to secondary model
    primary_model = os.getenv("GEMINI_MODEL", settings.GEMINI_MODEL)
    models_to_try = [primary_model, "gemini-2.5-flash"]
    models_to_try = list(dict.fromkeys(models_to_try))

    client = genai.Client(api_key=api_key)

    for model_name in models_to_try:
        for attempt in range(2):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        automatic_function_calling=types.AutomaticFunctionCallingConfig(
                            disable=True
                        )
                    )
                )
                if response and response.text:
                    return response.text
            except Exception as error:
                print(f"Warning: Model '{model_name}' (attempt {attempt + 1}) encountered error: {error}")
                time.sleep(1)

    # Direct Playbook Fallback if all external model attempts fail
    print("Notice: External AI service unreachable. Engaging Direct Playbook Fallback.")
    return direct_playbook_fallback(question, context)