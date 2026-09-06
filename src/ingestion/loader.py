from pathlib import Path


EXPERT_PLAYBOOK_DIR = Path("data/raw/expert_playbooks")
SAP_KBA_DIR = Path("data/raw/sap_kbas")


def load_documents():
    """
    Load knowledge documents from different knowledge sources.
    """

    documents = []

    # Load Expert Resolution Playbooks
    for file in EXPERT_PLAYBOOK_DIR.glob("*.md"):

        content = file.read_text(encoding="utf-8")

        documents.append({
            "source": file.name,
            "source_type": "Expert Resolution Playbook",
            "content": content
        })

    # Load SAP Knowledge / KBA documents
    for file in SAP_KBA_DIR.glob("*.md"):

        content = file.read_text(encoding="utf-8")

        documents.append({
            "source": file.name,
            "source_type": "SAP Official Documentation / KBA",
            "content": content
        })

    return documents


if __name__ == "__main__":

    documents = load_documents()

    print(f"\nLoaded {len(documents)} knowledge documents:\n")

    for document in documents:
        print(
            f"- {document['source']} "
            f"({document['source_type']})"
        )