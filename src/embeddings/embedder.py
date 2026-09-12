import json

from sentence_transformers import SentenceTransformer

from src.config import settings


def generate_chunk_embeddings():
    """
    Load processed chunks, generate embeddings using SentenceTransformer,
    and save them to the configured embedded chunks file.
    """

    # Load processed chunks
    with open(
        settings.CHUNKS_FILE,
        "r",
        encoding="utf-8"
    ) as file:
        chunks = json.load(file)

    print(f"Loaded {len(chunks)} chunks.")

    # Load embedding model
    model = SentenceTransformer(
        settings.EMBEDDING_MODEL_NAME
    )

    # Create enriched text for embeddings
    texts = []

    for chunk in chunks:

        embedding_text = f"""
Category: {chunk['category']}

Incident:
{chunk['incident']}

Problem Understanding:
{chunk['problem_understanding']}

Scenario:
{chunk['scenario']}

Content:
{chunk['content']}
"""

        texts.append(embedding_text)

    # Generate embeddings
    embeddings = model.encode(
    texts,
    normalize_embeddings=True
)

    # Add embeddings to each chunk
    for chunk, embedding in zip(chunks, embeddings):
        chunk["embedding"] = embedding.tolist()

    # Save embedded chunks
    with open(
        settings.EMBEDDED_CHUNKS_FILE,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            chunks,
            file,
            indent=2,
            ensure_ascii=False
        )

    print(
        f"Created {len(embeddings)} embeddings."
    )

    print(
        f"Embedding dimensions: {len(embeddings[0])}"
    )

    print(
        f"Saved embeddings to {settings.EMBEDDED_CHUNKS_FILE}"
    )

    return chunks


if __name__ == "__main__":
    generate_chunk_embeddings()