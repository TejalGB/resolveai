import os

from google import genai
from google.genai import types
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")


# Create Gemini client
client = genai.Client(
    api_key=api_key
)


def generate_response(question, context):
    """
    Generate an SAP SuccessFactors LMS troubleshooting response
    using retrieved knowledge base context.
    """

    prompt = f"""
You are ResolveAI, an expert SAP SuccessFactors Learning Management System (LMS) support assistant.

Your role is to help troubleshoot SAP SuccessFactors Learning issues using the provided knowledge base.

IMPORTANT RULES:

1. Use the provided knowledge base context as your primary source.
2. Do not invent SAP configuration details that are not supported by the context.
3. If the context does not contain enough information, clearly state what additional information should be checked.
4. Provide practical, structured troubleshooting steps.
5. Do not mention "vector database", "chunks", "retrieval", or internal system architecture.
6. Do not claim certainty when multiple possible causes exist.
7. Be concise but helpful.
8. Structure the response clearly using headings and bullet points where appropriate.
9. Do not greet or introduce yourself. Start directly with the troubleshooting response.

KNOWLEDGE BASE CONTEXT:

{context}

USER QUESTION:

{question}

Provide a clear troubleshooting response.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                automatic_function_calling=types.AutomaticFunctionCallingConfig(
                    disable=True
                )
            )
        )

        return response.text

    except Exception as e:
        return (
            "I'm sorry, but the AI service is temporarily unavailable. "
            "Please try again in a few moments."
        )


# Test generator independently
if __name__ == "__main__":

    test_question = input("Enter your question: ")

    test_context = """
No external context provided.
"""

    answer = generate_response(
        question=test_question,
        context=test_context
    )

    print("\nResolveAI Response:\n")
    print(answer)