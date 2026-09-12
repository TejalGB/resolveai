from src.rag.retriever import retrieve_context
from src.llm.generator import generate_response


def build_context(retrieved_chunks: list[dict]) -> str:
    """
    Convert retrieved chunks into formatted context for Gemini.
    """
    context_parts = []

    for i, chunk in enumerate(retrieved_chunks, start=1):
        context_parts.append(
            f"""
SOURCE {i}
File: {chunk['source']}
Category: {chunk['category']}
Scenario: {chunk['scenario']}
Match Confidence: {chunk['match_score']}%

{chunk['content']}
"""
        )

    return "\n---\n".join(context_parts)


def answer_question(question: str) -> dict:
    """
    Complete RAG pipeline:
    1. Retrieve relevant context above threshold
    2. Format context
    3. Generate grounded answer via Gemini
    4. Return answer + verified source metadata
    """
    print("\nSearching knowledge base...")
    retrieved_chunks = retrieve_context(question)

    # Dynamic Threshold Fallback (Prevent Hallucination)
    if not retrieved_chunks:
        return {
            "answer": (
                "I could not find sufficient information in the SAP SuccessFactors "
                "knowledge base to provide a reliable troubleshooting response for this issue. "
                "Please verify the issue details or consult standard SAP administration procedures."
            ),
            "sources": []
        }

    context = build_context(retrieved_chunks)

    print("Generating response...\n")
    answer = generate_response(
        question=question,
        context=context
    )

    # Build structured citations
    sources = [
        {
            "source": chunk["source"],
            "scenario": chunk["scenario"],
            "category": chunk["category"],
            "match_score": chunk["match_score"]
        }
        for chunk in retrieved_chunks
    ]

    return {
        "answer": answer,
        "sources": sources
    }


if __name__ == "__main__":
    print("\n==============================")
    print("       ResolveAI Assistant")
    print("==============================")
    print("\nHello! I'm ResolveAI, your SAP SuccessFactors LMS support assistant.")

    while True:
        question = input("\nDescribe your SAP LMS issue (or 'exit' to quit): ")
        if question.lower() in ["exit", "quit", "no"]:
            print("\nThank you for using ResolveAI. Goodbye! 👋")
            break

        if not question.strip():
            print("\nPlease enter a question.")
            continue

        result = answer_question(question)

        print("\nResolveAI Response:\n")
        print(result["answer"])

        if result["sources"]:
            print("\n📚 Verified Sources:")
            for s in result["sources"]:
                print(f" - {s['source']} > {s['scenario']} (Match: {s['match_score']}%)")

        another = input("\nDo you have another question? (yes/no): ")
        if another.lower() not in ["yes", "y"]:
            print("\nThank you for using ResolveAI. Goodbye! 👋")
            break