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


def detect_source(query):
    """
    Detect the most likely knowledge base domain
    based on the user's issue.

    Strong domain signals are used to improve retrieval accuracy
    for known SAP SuccessFactors LMS issue categories.
    """

    query = query.lower()

    # -----------------------------------
    # USER CONNECTOR / SYNCHRONIZATION
    # -----------------------------------

    if any(keyword in query for keyword in [
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
        return "user_connector_issues.md"


    # -----------------------------------
    # MYLEARNING ACCESS
    # -----------------------------------

    if any(keyword in query for keyword in [
        "cannot access mylearning",
        "can't access mylearning",
        "cannot open mylearning",
        "can't open mylearning",
        "mylearning not available",
        "mylearning unavailable",
        "access to mylearning",
        "mylearning access"
    ]):
        return "mylearning_access.md"


    # -----------------------------------
    # LOGIN ISSUES
    # -----------------------------------

    if any(keyword in query for keyword in [
        "login",
        "log in",
        "sign in",
        "signin",
        "cannot login",
        "can't login",
        "validation error",
        "authentication"
    ]):
        return "login_issues.md"


    # -----------------------------------
    # ASSIGNMENT PROFILE ISSUES
    # -----------------------------------

    if any(keyword in query for keyword in [
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

        # Important:
        # Queries specifically mentioning completion/retraining
        # should be handled by curriculum retraining instead.
        if not any(keyword in query for keyword in [
            "after completion",
            "completed",
            "retraining",
            "assigned again",
            "recurring"
        ]):
            return "assignment_profiles.md"


    # -----------------------------------
    # CURRICULUM RETRAINING
    # -----------------------------------

    if any(keyword in query for keyword in [
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
        return "curriculum_retraining.md"


    # -----------------------------------
    # SCORM / ONLINE CONTENT
    # -----------------------------------

    if any(keyword in query for keyword in [
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
        return "scorm_online_content_issues.md"


    # No strong domain detected
    return None


def retrieve_context(query, n_results=3):
    """
    Retrieve the most relevant knowledge chunks from ChromaDB.

    If a strong issue domain is detected, retrieval is restricted
    to the relevant knowledge source. Otherwise, semantic search
    is performed across the full knowledge base.
    """

    # Detect likely source/domain
    detected_source = detect_source(query)

    # Convert user question into embedding
    query_embedding = model.encode(query).tolist()

    # Apply metadata filter if a source is detected
    if detected_source:

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
            where={
                "source": detected_source
            }
        )

    else:

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


# Run this section only when search.py is executed directly
if __name__ == "__main__":

    while True:

        query = input(
            "\nEnter your question (or type 'exit' to quit): "
        )

        if query.lower() in ["exit", "quit"]:

            print("\nExiting search.")
            break

        retrieved_chunks = retrieve_context(query)

        print("\nSearch results:")

        for i, chunk in enumerate(retrieved_chunks):

            print("\n---")
            print(f"Result {i + 1}")
            print(f"Distance: {chunk['distance']}")
            print(f"Source: {chunk['source']}")
            print(f"Category: {chunk['category']}")
            print(f"Scenario: {chunk['scenario']}")
            print(f"Content: {chunk['content']}")