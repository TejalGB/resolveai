import argparse
import hashlib
import json
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

from src.config import settings
from src.ingestion.loader import load_documents
from src.ingestion.chunker import chunk_document


def compute_chunk_id(source: str, scenario: str, content: str) -> str:
    """
    Generate a deterministic 16-character SHA-256 fingerprint ID for each chunk.
    Enables incremental updates and avoids duplicate embeddings.
    """
    unique_string = f"{source}::{scenario}::{content.strip()}"
    return hashlib.sha256(unique_string.encode("utf-8")).hexdigest()[:16]


def run_pipeline(reindex: bool = False):
    """
    Run the complete ingestion pipeline:
    1. Load raw markdown documents
    2. Chunk documents into structured scenarios
    3. Generate deterministic chunk IDs
    4. Compute embeddings
    5. Upsert into ChromaDB
    6. Save processed outputs to disk
    """
    print("\n" + "=" * 50)
    print("      ResolveAI Knowledge Ingestion Pipeline")
    print("=" * 50)

    # 1. Load raw documents
    print("\n[1/5] Loading documents from raw knowledge base...")
    documents = load_documents()
    print(f"Loaded {len(documents)} source documents.")

    # 2. Chunk documents
    print("\n[2/5] Parsing documents into semantic chunks...")
    all_chunks = []
    for doc in documents:
        chunks = chunk_document(doc)
        all_chunks.extend(chunks)

    print(f"Generated {len(all_chunks)} semantic chunks.")

    # 3. Compute deterministic IDs
    print("\n[3/5] Generating SHA-256 chunk fingerprints...")
    for chunk in all_chunks:
        chunk["id"] = compute_chunk_id(
            chunk["source"],
            chunk["scenario"],
            chunk["content"]
        )

    # Save chunks to data/processed/chunks.json
    settings.PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    with open(settings.CHUNKS_FILE, "w", encoding="utf-8") as file:
        json.dump(all_chunks, file, indent=2, ensure_ascii=False)
    print(f"Saved chunk catalog to: {settings.CHUNKS_FILE}")

    # 4. Connect to ChromaDB
    print("\n[4/5] Connecting to ChromaDB vector store...")
    settings.CHROMA_DIR.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(settings.CHROMA_DIR))

    if reindex:
        print("Flag --reindex received: resetting collection...")
        try:
            client.delete_collection(name=settings.CHROMA_COLLECTION_NAME)
            print("Existing collection deleted.")
        except Exception:
            pass

    collection = client.get_or_create_collection(
        name=settings.CHROMA_COLLECTION_NAME
    )

    # Check which chunks are new vs existing (incremental upsert)
    existing_ids = set()
    if not reindex:
        try:
            existing_data = collection.get()
            existing_ids = set(existing_data["ids"])
        except Exception:
            pass

    chunks_to_embed = [c for c in all_chunks if c["id"] not in existing_ids]

    if not chunks_to_embed:
        print("All chunks are already indexed. No new embeddings required.")
        print(f"Total chunks in vector store: {collection.count()}")
        return

    print(f"New or modified chunks to embed: {len(chunks_to_embed)} (out of {len(all_chunks)})")

    # 5. Generate embeddings
    print(f"\n[5/5] Generating embeddings using '{settings.EMBEDDING_MODEL_NAME}'...")
    model = SentenceTransformer(settings.EMBEDDING_MODEL_NAME)

    texts_to_embed = []
    for chunk in chunks_to_embed:
        enriched_text = f"""
Category: {chunk['category']}

Incident:
{chunk['incident']}

Problem Understanding:
{chunk['problem_understanding']}

Scenario: {chunk['scenario']}

Content:
{chunk['content']}
"""
        texts_to_embed.append(enriched_text)

    embeddings = model.encode(texts_to_embed)

    ids = [chunk["id"] for chunk in chunks_to_embed]
    documents = [chunk["content"] for chunk in chunks_to_embed]
    metadatas = [
        {
            "source": chunk["source"],
            "source_type": chunk["source_type"],
            "category": chunk["category"],
            "scenario": chunk["scenario"]
        }
        for chunk in chunks_to_embed
    ]

    # Upsert into ChromaDB
    collection.upsert(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
        embeddings=embeddings.tolist()
    )

    # Attach embeddings to chunk list and save embedded_chunks.json
    for chunk, emb in zip(chunks_to_embed, embeddings):
        chunk["embedding"] = emb.tolist()

    with open(settings.EMBEDDED_CHUNKS_FILE, "w", encoding="utf-8") as file:
        json.dump(all_chunks, file, indent=2, ensure_ascii=False)

    print(f"Successfully upserted {len(chunks_to_embed)} chunks into ChromaDB.")
    print(f"Total active items in collection '{settings.CHROMA_COLLECTION_NAME}': {collection.count()}")
    print("\nPipeline execution complete!\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run ResolveAI knowledge ingestion pipeline."
    )
    parser.add_argument(
        "--reindex",
        action="store_true",
        help="Wipe and rebuild the vector database collection from scratch."
    )
    args = parser.parse_args()

    run_pipeline(reindex=args.reindex)