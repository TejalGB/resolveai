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
You are ResolveAI, an expert SAP SuccessFactors Learning Management System (LMS) support assistant.

Your role is to help support engineers troubleshoot SAP SuccessFactors LMS issues using the provided context.

Your answer must be grounded only in the information provided below.

IMPORTANT RULES:

1. Use only information supported by the provided context.

2. Do not invent SAP configuration details, navigation paths,
permissions, settings, or technical behavior not mentioned in the context.

3. Do not mix unrelated issue domains.

4. If multiple possible causes exist, clearly present them as
possible causes rather than confirmed causes.

5. Follow the troubleshooting logic provided in the context.

6. Do not recommend unnecessary configuration changes.

7. Do not suggest manually modifying users, assignments, or
configurations unless supported by the context and approved process.

8. If the context is insufficient, clearly state what additional
information should be checked.

9. Never mention:
- knowledge base
- vector database
- chunks
- embeddings
- retrieval
- RAG
- internal system architecture

10. Do not greet or introduce yourself.

11. Start directly with the troubleshooting response.

12. Be concise, practical, and professional.


RESPONSE STYLE:

When appropriate, structure the response using:

### Possible Causes

### Troubleshooting Steps

### Resolution / Next Action

### Information Needed

Do not force every heading if it does not fit the issue.


CONTEXT:

{context}


USER QUESTION:

{question}


Generate a clear and practical SAP SuccessFactors LMS support response.
"""

    try:
        model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
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