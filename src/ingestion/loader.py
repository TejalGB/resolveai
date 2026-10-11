from src.config import settings


def load_documents():
    """
    Load knowledge documents from the ResolveAI knowledge base:
    1. Expert Resolution Playbooks (troubleshooting checklists & resolution logic)
    2. Official SAP KBAs (authoritative technical articles & background knowledge)
    """

    documents = []

    # ---------------------------------------------------------
    # EXPERT RESOLUTION PLAYBOOKS
    # ---------------------------------------------------------
    for file in sorted(settings.EXPERT_PLAYBOOK_DIR.glob("*.md")):
        content = file.read_text(encoding="utf-8")
        documents.append({
            "source": file.name,
            "source_type": "Expert Resolution Playbook",
            "content": content
        })

    # ---------------------------------------------------------
    # OFFICIAL SAP KBAs
    # ---------------------------------------------------------
    for file in sorted(settings.SAP_KBA_DIR.glob("*.md")):
        content = file.read_text(encoding="utf-8")
        documents.append({
            "source": file.name,
            "source_type": "SAP Official Documentation / KBA",
            "content": content
        })

    # ---------------------------------------------------------
    # SUMMARY
    # ---------------------------------------------------------
    print(f"\nLoaded {len(documents)} knowledge documents:")
    for document in documents:
        print(f" - {document['source']} ({document['source_type']})")

    print(f"\nTotal documents loaded: {len(documents)}")
    return documents


if __name__ == "__main__":

    load_documents()