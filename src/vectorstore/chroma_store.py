import json
import chromadb


# Create a persistent Chroma client
client = chromadb.PersistentClient(path="data/chroma")


# Delete the old collection if it exists
try:
    client.delete_collection(name="resolveai_knowledge")
    print("Deleted existing collection.")
except Exception:
    pass


# Create a fresh collection
collection = client.create_collection(
    name="resolveai_knowledge"
)


# Load embedded chunks
with open(
    "data/processed/embedded_chunks.json",
    "r",
    encoding="utf-8"
) as file:
    chunks = json.load(file)


# Prepare data for Chroma
ids = []
documents = []
metadatas = []
embeddings = []

for index, chunk in enumerate(chunks):
    ids.append(f"chunk_{index}")

    documents.append(chunk["content"])

    metadatas.append({
        "source": chunk["source"],
        "category": chunk["category"],
        "scenario": chunk["scenario"]
    })

    embeddings.append(chunk["embedding"])


# Add data to Chroma
collection.add(
    ids=ids,
    documents=documents,
    metadatas=metadatas,
    embeddings=embeddings
)


print(f"Added {len(chunks)} chunks to Chroma.")
print(f"Collection count: {collection.count()}")