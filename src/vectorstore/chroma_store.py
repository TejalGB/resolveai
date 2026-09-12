import json
import chromadb

from src.config import settings


def create_vector_store(recreate: bool = True):
    """
    Create or update the ChromaDB vector store.

    Parameters:
    recreate (bool):
        If True, delete the existing collection and rebuild it.
    """

    # Create persistent Chroma client
    client = chromadb.PersistentClient(
        path=str(settings.CHROMA_DIR)
    )

    # Recreate collection when explicitly requested
    if recreate:
        try:
            client.delete_collection(
                name=settings.CHROMA_COLLECTION_NAME
            )
            print("Deleted existing collection.")
        except Exception:
            pass

    # Create or retrieve collection
    collection = client.get_or_create_collection(
        name=settings.CHROMA_COLLECTION_NAME
    )

    # Load embedded chunks
    with open(
        settings.EMBEDDED_CHUNKS_FILE,
        "r",
        encoding="utf-8"
    ) as file:
        chunks = json.load(file)

    # Prepare Chroma data
    ids = []
    documents = []
    metadatas = []
    embeddings = []

    for index, chunk in enumerate(chunks):

        ids.append(f"chunk_{index}")

        documents.append(
            chunk["content"]
        )

        metadatas.append({
            "source": chunk["source"],
            "category": chunk["category"],
            "scenario": chunk["scenario"]
        })

        embeddings.append(
            chunk["embedding"]
        )

    # Add data to Chroma
    collection.add(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
        embeddings=embeddings
    )

    print(
        f"Added {len(chunks)} chunks to Chroma."
    )

    print(
        f"Collection count: {collection.count()}"
    )

    return collection


if __name__ == "__main__":

    create_vector_store(
        recreate=True
    )