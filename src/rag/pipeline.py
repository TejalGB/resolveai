from src.vectorstore.search import retrieve_context
from src.llm.generator import generate_response


def build_context(retrieved_chunks):
    """
    Convert retrieved chunks into formatted context
    that can be provided to the LLM.
    """

    context = ""

    for i, chunk in enumerate(retrieved_chunks):

        context += f"""
SOURCE {i + 1}
Category: {chunk['category']}
Scenario: {chunk['scenario']}

{chunk['content']}

---
"""

    return context


def answer_question(question):
    """
    Complete RAG pipeline:

    User Question
        ↓
    Retrieve relevant context
        ↓
    Send context + question to Gemini
        ↓
    Generate answer
    """

    print("\nSearching knowledge base...")

    retrieved_chunks = retrieve_context(question)

    context = build_context(retrieved_chunks)

    print("Generating response...\n")

    answer = generate_response(
        question=question,
        context=context
    )

    return answer


if __name__ == "__main__":

    print("\n==============================")
    print("       ResolveAI Assistant")
    print("==============================")

    while True:

        question = input(
            "\nDescribe your SAP LMS issue (or type 'exit' to quit): "
        )

        # Exit condition
        if question.lower() in ["exit", "quit", "no"]:
            print("\nThank you for using ResolveAI. Goodbye! 👋")
            break

        # Skip empty questions
        if not question.strip():
            print("\nPlease enter a question or describe your issue.")
            continue

        answer = answer_question(question)

        print("\nResolveAI Response:\n")
        print(answer)

        # Ask whether user has another question
        another_question = input(
            "\nDo you have another question? (yes/no): "
        )

        if another_question.lower() not in ["yes", "y"]:
            print("\nThank you for using ResolveAI. Goodbye! 👋")
            break