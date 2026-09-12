import os

from google import genai
from google.genai import types
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


# Module-level client holder for lazy initialization
_client = None


def get_gemini_client():
    """
    Lazily initialize and return the Gemini API client.
    Prevents unhandled crashes on import if GEMINI_API_KEY is missing.
    """
    global _client
    if _client is None:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is not set. "
                "Please check your .env file."
            )
        _client = genai.Client(api_key=api_key)
    return _client


def generate_response(question, context):
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

### 📋 ServiceNow Ticket Documentation
* **Internal Work Notes:** Concise technical summary of the findings and audit trail to log in the ServiceNow activity stream.
* **Customer Resolution (Additional Comments):** Professional, user-friendly communication ready to send to the user/manager resolving the ticket.

CONTEXT:
{context}

USER INCIDENT / QUESTION:
{question}

Generate a comprehensive, incident-oriented ServiceNow troubleshooting resolution:
"""

    try:
        model_name = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")
        client = get_gemini_client()

        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
            config=types.GenerateContentConfig(
                automatic_function_calling=types.AutomaticFunctionCallingConfig(
                    disable=True
                )
            )
        )

        return response.text

    except Exception as error:
        print(f"\nGenerator error: {error}")
        return (
            "I'm sorry, but the AI service is temporarily unavailable. "
            "Please try again in a few moments."
        )