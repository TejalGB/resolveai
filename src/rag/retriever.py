import chromadb
from sentence_transformers import SentenceTransformer


# -----------------------------------
# Connect to ChromaDB
# -----------------------------------

client = chromadb.PersistentClient(
    path="data/chroma"
)


# Get ResolveAI knowledge collection
collection = client.get_collection(
    name="resolveai_knowledge"
)


# -----------------------------------
# Load Embedding Model
# -----------------------------------

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# -----------------------------------
# Retrieve Relevant Knowledge
# -----------------------------------

def retrieve_context(query, n_results=5):
    """
    Retrieve relevant knowledge chunks from ChromaDB
    based on the user's question.
    """

    # Convert user question into embedding
    query_embedding = model.encode(
        query
    ).tolist()


    # Search ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )


    # Store retrieved chunks
    retrieved_chunks = []


    for i in range(
        len(results["documents"][0])
    ):

        chunk = {
            "content": results["documents"][0][i],
            "source": results["metadatas"][0][i]["source"],
            "category": results["metadatas"][0][i]["category"],
            "scenario": results["metadatas"][0][i]["scenario"],
            "distance": results["distances"][0][i]
        }

        retrieved_chunks.append(chunk)


    return retrieved_chunks


# -----------------------------------
# Test Retriever Independently
# -----------------------------------

if __name__ == "__main__":

    while True:

        test_query = input(
            "\nEnter your question "
            "(or type 'exit' to quit): "
        )


        if test_query.lower() == "exit":
            print("\nExiting ResolveAI Retriever.")
            break


        results = retrieve_context(
            query=test_query,
            n_results=5
        )


        print("\nSearch results:\n")


        for index, result in enumerate(
            results,
            start=1
        ):

            print("---")

            print(
                f"Result {index}"
            )

            print(
                f"Distance: "
                f"{result['distance']}"
            )

            print(
                f"Source: "
                f"{result['source']}"
            )

            print(
                f"Category: "
                f"{result['category']}"
            )

            print(
                f"Scenario: "
                f"{result['scenario']}"
            )

            print(
                f"Content: "
                f"{result['content']}"
            )

            print()


        print("=" * 60)