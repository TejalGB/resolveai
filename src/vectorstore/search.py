import chromadb
from sentence_transformers import SentenceTransformer


# Connect to our existing Chroma database
client = chromadb.PersistentClient(path="data/chroma")


# Get our existing collection
collection = client.get_collection(
    name="resolveai_knowledge"
)


# Load the same embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# User's question
query = input("Enter your question: ")


# Convert the question into an embedding
query_embedding = model.encode(query).tolist()


# Search Chroma
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)


# Display results
print("\nSearch results:")

for i in range(len(results["documents"][0])):
    print("\n---")
    print(f"Result {i + 1}")
    print(f"Distance: {results['distances'][0][i]}")
    print(f"Source: {results['metadatas'][0][i]['source']}")
    print(f"Category: {results['metadatas'][0][i]['category']}")
    print(f"Scenario: {results['metadatas'][0][i]['scenario']}")
    print(f"Content: {results['documents'][0][i]}")