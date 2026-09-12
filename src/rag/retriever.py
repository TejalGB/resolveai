import chromadb
from sentence_transformers import SentenceTransformer

from src.config import settings


class KnowledgeRetriever:
    """
    Unified knowledge retriever for ResolveAI.

    Uses expert resolution playbooks as the primary retrieval source.
    SAP KBAs that have been merged into those playbooks are not retrieved
    separately.
    """

    def __init__(self):
        self._client = None
        self._collection = None
        self._model = None

    @property
    def client(self):
        if self._client is None:
            self._client = chromadb.PersistentClient(
                path=str(settings.CHROMA_DIR)
            )
        return self._client

    @property
    def collection(self):
        if self._collection is None:
            try:
                self._collection = self.client.get_collection(
                    name=settings.CHROMA_COLLECTION_NAME
                )
                if self._collection.count() == 0:
                    print("Chroma collection is empty. Auto-indexing knowledge base...")
                    from src.ingestion.pipeline import run_pipeline
                    run_pipeline()
                    self._collection = self.client.get_collection(
                        name=settings.CHROMA_COLLECTION_NAME
                    )
            except Exception as error:
                print(f"Collection not found ({error}). Initializing knowledge base...")
                from src.ingestion.pipeline import run_pipeline
                run_pipeline()
                self._collection = self.client.get_collection(
                    name=settings.CHROMA_COLLECTION_NAME
                )
        return self._collection

    @property
    def model(self):
        if self._model is None:
            self._model = SentenceTransformer(
                settings.EMBEDDING_MODEL_NAME
            )
        return self._model

    def detect_sources(self, query: str) -> list[str]:
        """
        Detect the relevant expert playbook(s) for the query.

        Important:
        SAP KBAs that have been merged into expert playbooks are NOT
        returned here. This prevents duplicate retrieval.
        """

        query_lower = query.lower()
        sources = []

        # ---------------------------------------------------------
        # USER CONNECTOR / USER SYNCHRONIZATION
        # ---------------------------------------------------------
        if any(k in query_lower for k in [
            "user connector",
            "synchronization",
            "synchronize",
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
            sources.append("user_connector_issues.md")

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
            sources.append("mylearning_access.md")

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
            sources.append("login_issues.md")

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
            sources.append("curriculum_retraining.md")

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
            sources.append("assignment_profiles.md")

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
            sources.append("scorm_online_content_issues.md")

        # ---------------------------------------------------------
        # LEARNING HISTORY / COMPLETION
        # ---------------------------------------------------------
        if any(k in query_lower for k in [
            "learning history",
            "completion history",
            "course completion",
            "completed course",
            "completion record",
            "completion status",
            "training history",
            "course history"
        ]):
            sources.append("learning_history.md")

        # ---------------------------------------------------------
        # OTHER EXISTING EXPERT PLAYBOOKS
        # ---------------------------------------------------------

        if any(k in query_lower for k in [
            "class enrollment",
            "enroll in class",
            "class registration",
            "scheduled offering",
            "instructor led",
            "ilt"
        ]):
            sources.append("class_enrollment_issues.md")

        if any(k in query_lower for k in [
            "content issue",
            "learning content",
            "content configuration",
            "content object"
        ]):
            sources.append("content_issues.md")

        if any(k in query_lower for k in [
            "curriculum configuration",
            "curriculum setup",
            "curriculum settings"
        ]):
            sources.append("curriculum_configuration.md")

        if any(k in query_lower for k in [
            "item configuration",
            "learning item configuration",
            "item settings"
        ]):
            sources.append("item_configuration.md")

        if any(k in query_lower for k in [
            "scheduled offering",
            "offering configuration",
            "offering setup"
        ]):
            sources.append("scheduled_offering_configuration.md")

        if any(k in query_lower for k in [
            "security",
            "admin access",
            "administrator access",
            "permission",
            "permissions",
            "role access"
        ]):
            sources.append("security_and_admin_access.md")

        # Remove duplicates while preserving order
        return list(dict.fromkeys(sources))

    def _calculate_match_score(self, distance: float) -> float:
        """
        Convert Chroma distance into a 0-100 match score.

        Current calibration:
            similarity = 1 - (distance / 2)

        The result is bounded between 0 and 100.
        """

        similarity = max(
            0.0,
            1.0 - (distance / 2.0)
        )

        return round(similarity * 100.0, 1)

    def retrieve(
        self,
        query: str,
        n_results: int = 3,
        threshold: float | None = None
    ) -> list[dict]:
        """
        Retrieve relevant knowledge chunks.

        If a domain is detected, retrieval is first restricted to the
        corresponding expert playbook.

        If no domain is detected, semantic search is performed across
        the complete knowledge base.
        """

        if threshold is None:
            threshold = settings.RELEVANCE_THRESHOLD * 100.0

        detected_sources = self.detect_sources(query)

        if detected_sources:
            print("\nDetected knowledge sources:")
            for source in detected_sources:
                print(f" - {source}")
        else:
            print("\nNo specific knowledge source detected.")
            print("Searching across the complete knowledge base.")

        # Generate query embedding
        query_embedding = self.model.encode(query).tolist()

        results = None

        # ---------------------------------------------------------
        # TARGETED RETRIEVAL
        # ---------------------------------------------------------
        if detected_sources:

            # If multiple expert playbooks are relevant, query each
            # one separately and combine the results.
            combined_results = []

            for source in detected_sources:
                try:
                    source_results = self.collection.query(
                        query_embeddings=[query_embedding],
                        n_results=n_results,
                        where={"source": source}
                    )

                    if (
                        source_results
                        and source_results.get("documents")
                        and source_results["documents"][0]
                    ):
                        for i in range(
                            len(source_results["documents"][0])
                        ):
                            combined_results.append({
                                "id": source_results["ids"][0][i],
                                "content": source_results["documents"][0][i],
                                "metadata": source_results["metadatas"][0][i],
                                "distance": source_results["distances"][0][i]
                            })

                except Exception as error:
                    print(
                        f"Warning: Could not search {source}: {error}"
                    )

            # Sort all targeted results by distance
            combined_results.sort(
                key=lambda x: x["distance"]
            )

            # Keep the best n_results
            combined_results = combined_results[:n_results]

            # Convert into the same structure used below
            if combined_results:
                results = {
                    "ids": [[item["id"] for item in combined_results]],
                    "documents": [[
                        item["content"]
                        for item in combined_results
                    ]],
                    "metadatas": [[
                        item["metadata"]
                        for item in combined_results
                    ]],
                    "distances": [[
                        item["distance"]
                        for item in combined_results
                    ]]
                }

        # ---------------------------------------------------------
        # GLOBAL SEMANTIC FALLBACK
        # ---------------------------------------------------------
        if (
            not results
            or not results.get("documents")
            or len(results["documents"][0]) == 0
        ):
            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=n_results
            )

        # ---------------------------------------------------------
        # PROCESS RESULTS
        # ---------------------------------------------------------
        retrieved_chunks = []

        if results and results.get("documents"):

            for i in range(len(results["documents"][0])):

                distance = results["distances"][0][i]

                match_score = self._calculate_match_score(
                    distance
                )

                print(
                    f"Retrieved: "
                    f"{results['metadatas'][0][i].get('scenario', 'Unknown')} "
                    f"| Distance: {distance:.4f} "
                    f"| Match: {match_score}%"
                )

                # Discard chunks below relevance threshold
                if match_score < threshold:
                    continue

                metadata = results["metadatas"][0][i]

                chunk = {
                    "id": results["ids"][0][i],
                    "content": results["documents"][0][i],
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
                    "distance": round(
                        distance,
                        4
                    ),
                    "match_score": match_score
                }

                retrieved_chunks.append(chunk)

        return retrieved_chunks


# ---------------------------------------------------------
# GLOBAL SINGLETON
# ---------------------------------------------------------

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


# ---------------------------------------------------------
# DIRECT TEST MODE
# ---------------------------------------------------------

if __name__ == "__main__":

    print("\n--- ResolveAI Retriever Test ---")

    while True:

        test_query = input(
            "\nEnter your question (or 'exit' to quit): "
        )

        if test_query.lower() in ["exit", "quit"]:
            break

        results = retrieve_context(
            test_query,
            n_results=3
        )

        print(
            f"\nRetrieved {len(results)} "
            f"chunks above threshold:\n"
        )

        for idx, res in enumerate(
            results,
            start=1
        ):

            print(
                f"[{idx}] "
                f"{res['source']} | "
                f"{res['scenario']} | "
                f"Match: {res['match_score']}%"
            )

            print(
                f"Content: "
                f"{res['content'][:250]}..."
            )