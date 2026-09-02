import json
from sentence_transformers import SentenceTransformer


# Load chunks
with open("data/processed/chunks.json", "r", encoding="utf-8") as file:
    chunks = json.load(file)

print(f"Loaded {len(chunks)} chunks.")


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Create enriched text for embeddings
texts = []

for chunk in chunks:
    embedding_text = f"""
Category: {chunk['category']}

Incident:
{chunk['incident']}

Problem Understanding:
{chunk['problem_understanding']}

Scenario: {chunk['scenario']}

Content:
{chunk['content']}
"""

    texts.append(embedding_text)


# Generate embeddings
embeddings = model.encode(texts)


# Add embeddings to each chunk
for chunk, embedding in zip(chunks, embeddings):
    chunk["embedding"] = embedding.tolist()


# Save chunks with embeddings
with open("data/processed/embedded_chunks.json", "w", encoding="utf-8") as file:
    json.dump(chunks, file, indent=2, ensure_ascii=False)


print(f"Created {len(embeddings)} embeddings.")
print(f"Embedding dimensions: {len(embeddings[0])}")
print("Saved embeddings to data/processed/embedded_chunks.json")