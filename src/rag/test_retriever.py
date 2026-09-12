from src.rag.retriever import retrieve_context


query = input("Enter your question: ")

results = retrieve_context(query)


print("\nRetrieved Context:")

for i, result in enumerate(results, start=1):
    print("\n---")
    print(f"Result {i}")
    print(f"Scenario: {result['scenario']}")
    print(f"Category: {result['category']}")
    print(f"Content: {result['content']}")