import chromadb
from sentence_transformers import SentenceTransformer

from src.config import settings


class KnowledgeRetriever:
    """
    Unified knowledge retriever for ResolveAI.

    Supports multiple knowledge-base source files for the same domain
    and combines targeted retrieval with semantic vector search.
    """

    def __init__(self):
        self._client = None
        self._collection = None
        self._model = None

    @property
    def client(self):
        """Lazily initialize the persistent Chroma client."""
        if self._client is None:
            self._client = chromadb.PersistentClient(
                path=str(settings.CHROMA_DIR)
            )
        return self._client

    @property
    def collection(self):
        """Lazily load the ResolveAI knowledge collection."""
        if self._collection is None:
            self._collection = self.client.get_collection(
                name=settings.CHROMA_COLLECTION_NAME
            )
        return self._collection

    @property
    def model(self):
        """Lazily load the embedding model."""
        if self._model is None:
            self._model = SentenceTransformer(
                settings.EMBEDDING_MODEL_NAME
            )
        return self._model

    def detect_sources(self, query: str) -> list[str]:
        """
        Detect relevant knowledge-base sources from the user query.

        Multiple source files can belong to the same domain, so this
        method returns all relevant variants rather than a single file.
        """

        query_lower = query.lower()
        sources = []

        # ---------------------------------------------------------
        # USER CONNECTOR / USER SYNCHRONIZATION
        # ---------------------------------------------------------
        if any(k in query_lower for k in [
            "user connector",
            "synchronization",
            "sync",
            "not synced",
            "missing from lms",
            "missing in lms",
            "not in lms",
            "inactive in lms",
            "active in pd",
            "pd but",
            "user missing",
            "profile missing",
            "user not updated",
            "not updated",
            "new user missing",
            "user missing after joining",
            "new joiner"
        ]):
            sources.extend([
                "user_connector_sap_knowledge.md",
                "user_connector_issues.md"
            ])

        # ---------------------------------------------------------
        # MYLEARNING ACCESS
        # ---------------------------------------------------------
        if any(k in query_lower for k in [
            "cannot access mylearning",
            "can't access mylearning",
            "cannot open mylearning",
            "can't open mylearning",
            "mylearning not available",
            "mylearning unavailable",
            "access to mylearning",
            "mylearning access"
        ]):
            sources.extend([
                "mylearning_access_sap.md",
                "mylearning_access.md"
            ])

        # ---------------------------------------------------------
        # LOGIN / AUTHENTICATION
        # ---------------------------------------------------------
        if any(k in query_lower for k in [
            "login",
            "log in",
            "sign in",
            "signin",
            "cannot login",
            "can't login",
            "validation error",
            "authentication"
        ]):
            sources.extend([
                "login_authentication_sap.md",
                "login_issues.md"
            ])

        # ---------------------------------------------------------
        # CURRICULUM / RETRAINING
        # ---------------------------------------------------------
        if any(k in query_lower for k in [
            "assigned again after completion",
            "course assigned again",
            "course assigned after completion",
            "completed but assigned again",
            "retraining",
            "retraining requirement",
            "retraining period",
            "course keeps coming back",
            "course keeps getting assigned again",
            "recurring training",
            "repeat training requirement"
        ]):
            sources.extend([
                "curriculum_retraining_sap.md",
                "curriculum_retraining.md"
            ])

        # ---------------------------------------------------------
        # ASSIGNMENT PROFILES
        # ---------------------------------------------------------
        if any(k in query_lower for k in [
            "assigned unexpectedly",
            "course assigned unexpectedly",
            "item assigned unexpectedly",
            "course not assigned",
            "item not assigned",
            "unexpected assignment",
            "wrong course assigned",
            "wrong item assigned",
            "assignment profile",
            "assignment criteria",
            "multiple assignment profiles",
            "why was this course assigned"
        ]):
            sources.extend([
                "assignment_profiles_sap.md",
                "assignment_profiles.md"
            ])

        # ---------------------------------------------------------
        # SCORM / ONLINE CONTENT
        # ---------------------------------------------------------
        if any(k in query_lower for k in [
            "scorm",
            "content not launching",
            "course not launching",
            "online content not launching",
            "content won't launch",
            "content does not launch",
            "scorm error",
            "scorm completion",
            "content stuck loading"
        ]):
            sources.extend([
                "scorm_online_content_sap.md",
                "scorm_online_content_issues.md"
            ])

        # Remove duplicates while preserving order
        return list(dict.fromkeys(sources))

    def _calculate_match_score(self, distance: float) -> float:
        """
        Convert Chroma distance into a simple 0-100 relevance score.

        This preserves the scoring approach currently used by ResolveAI.
        """

        similarity = max(
            0.0,
            1.0 - (distance / 2.0)
        )

        return round(similarity * 100.0, 1)

    def _query_source(
        self,
        query_embedding: list[float],
        source: str,
        n_results: int
    ):
        """Run a targeted Chroma search for one source file."""

        try:
            return self.collection.query(
                query_embeddings=[query_embedding],
                n_results=n_results,
                where={"source": source}
            )
        except Exception:
            return None

    def _query_all(
        self,
        query_embedding: list[float],
        n_results: int
    ):
        """Run semantic search across the complete knowledge base."""

        try:
            return self.collection.query(
                query_embeddings=[query_embedding],
                n_results=n_results
            )
        except Exception:
            return None

    def _process_results(
        self,
        results,
        retrieved_chunks: list[dict],
        seen_ids: set
    ):
        """Convert Chroma results into ResolveAI chunk objects."""

        if not results:
            return

        if not results.get("documents"):
            return

        documents = results["documents"][0]

        if not documents:
            return

        ids = results.get("ids", [[]])[0]
        distances = results.get("distances", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]

        for i, document in enumerate(documents):

            chunk_id = (
                ids[i]
                if i < len(ids)
                else f"chunk_{len(retrieved_chunks)}"
            )

            # Avoid duplicate chunks when the same knowledge appears
            # through multiple retrieval paths.
            if chunk_id in seen_ids:
                continue

            seen_ids.add(chunk_id)

            distance = (
                distances[i]
                if i < len(distances)
                else 1.0
            )

            metadata = (
                metadatas[i]
                if i < len(metadatas) and metadatas[i]
                else {}
            )

            match_score = self._calculate_match_score(distance)

            retrieved_chunks.append({
                "id": chunk_id,
                "content": document,
                "source": metadata.get(
                    "source",
                    "Unknown"
                ),
                "source_type": metadata.get(
                    "source_type",
                    "Knowledge Base"
                ),
                "category": metadata.get(
                    "category",
                    "General"
                ),
                "scenario": metadata.get(
                    "scenario",
                    "Standard Resolution"
                ),
                "distance": round(distance, 4),
                "match_score": match_score
            })

    def retrieve(
        self,
        query: str,
        n_results: int = 3,
        threshold: float | None = None
    ) -> list[dict]:
        """
        Retrieve relevant knowledge chunks.

        Process:
        1. Detect relevant domain sources.
        2. Search all matching source variants.
        3. If targeted retrieval fails, use global semantic search.
        4. Remove duplicate chunks.
        5. Sort by relevance.
        6. Apply relevance threshold.
        """

        if threshold is None:
            threshold = settings.RELEVANCE_THRESHOLD * 100.0

        detected_sources = self.detect_sources(query)

        # Generate query embedding once.
        query_embedding = self.model.encode(query).tolist()

        retrieved_chunks = []
        seen_ids = set()

        # ---------------------------------------------------------
        # TARGETED SEARCH
        # ---------------------------------------------------------
        for source in detected_sources:

            results = self._query_source(
                query_embedding=query_embedding,
                source=source,
                n_results=n_results
            )

            self._process_results(
                results=results,
                retrieved_chunks=retrieved_chunks,
                seen_ids=seen_ids
            )

        # ---------------------------------------------------------
        # GLOBAL FALLBACK
        # ---------------------------------------------------------
        if not retrieved_chunks:

            results = self._query_all(
                query_embedding=query_embedding,
                n_results=n_results
            )

            self._process_results(
                results=results,
                retrieved_chunks=retrieved_chunks,
                seen_ids=seen_ids
            )

        # ---------------------------------------------------------
        # SORT BY BEST MATCH
        # ---------------------------------------------------------
        retrieved_chunks.sort(
            key=lambda x: x["match_score"],
            reverse=True
        )

        # ---------------------------------------------------------
        # APPLY THRESHOLD
        # ---------------------------------------------------------
        filtered_chunks = [
            chunk
            for chunk in retrieved_chunks
            if chunk["match_score"] >= threshold
        ]

        # Limit final context to the requested number.
        return filtered_chunks[:n_results]


# =============================================================
# GLOBAL RETRIEVER INSTANCE
# =============================================================

retriever = KnowledgeRetriever()


def retrieve_context(
    query: str,
    n_results: int = 3,
    threshold: float | None = None
) -> list[dict]:
    """
    Convenience function used by the RAG pipeline.
    """

    return retriever.retrieve(
        query=query,
        n_results=n_results,
        threshold=threshold
    )


# =============================================================
# DIRECT TESTING
# =============================================================

if __name__ == "__main__":

    print("\n--- ResolveAI Retriever Test ---")

    while True:

        test_query = input(
            "\nEnter your question (or 'exit' to quit): "
        )

        if test_query.lower() in ["exit", "quit"]:
            break

        detected = retriever.detect_sources(test_query)

        if detected:
            print("\nDetected knowledge sources:")
            for source in detected:
                print(f" - {source}")
        else:
            print("\nNo specific domain detected. Using global search.")

        results = retrieve_context(
            test_query,
            n_results=3
        )

        print(
            f"\nRetrieved {len(results)} chunks above threshold:\n"
        )

        for idx, result in enumerate(results, start=1):

            print(
                f"[{idx}] "
                f"{result['source']} | "
                f"{result['scenario']} | "
                f"Match: {result['match_score']}%"
            )

            print(
                f"Content: "
                f"{result['content'][:200]}..."
            )

            print()