import json
from sentence_transformers import SentenceTransformer


# Load chunks
with open("data/processed/chunks.json", "r", encoding="utf-8") as file:
    chunks = json.load(file)

print(f"Loaded {len(chunks)} chunks.")


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Extract text from each chunk
texts = [chunk["content"] for chunk in chunks]


# Generate embeddings
embeddings = model.encode(texts)


# Add embeddings to each chunk
for chunk, embedding in zip(chunks, embeddings):
    chunk["embedding"] = embedding.tolist()


# Save chunks with embeddings
with open("data/processed/embedded_chunks.json", "w", encoding="utf-8") as file:
    json.dump(chunks, file, indent=2)


print(f"Created {len(embeddings)} embeddings.")
print(f"Embedding dimensions: {len(embeddings[0])}")
print("Saved embeddings to data/processed/embedded_chunks.json")