import chromadb
from sentence_transformers import SentenceTransformer


# Connect to the existing Chroma database
client = chromadb.PersistentClient(path="data/chroma")


# Get the ResolveAI knowledge collection
collection = client.get_collection(
    name="resolveai_knowledge"
)


# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve_context(query, n_results=3):
    """
    Retrieve relevant knowledge chunks from ChromaDB
    based on the user's question.
    """

    # Convert user question into embedding
    query_embedding = model.encode(query).tolist()

    # Search ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    retrieved_chunks = []

    for i in range(len(results["documents"][0])):

        chunk = {
            "content": results["documents"][0][i],
            "source": results["metadatas"][0][i]["source"],
            "category": results["metadatas"][0][i]["category"],
            "scenario": results["metadatas"][0][i]["scenario"],
            "distance": results["distances"][0][i]
        }

        retrieved_chunks.append(chunk)

    return retrieved_chunks