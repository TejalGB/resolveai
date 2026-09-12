from pathlib import Path


EXPERT_PLAYBOOK_DIR = Path("data/raw/expert_playbooks")
SAP_KBA_DIR = Path("data/raw/sap_kbas")


# SAP KBAs that have been incorporated into the
# corresponding Expert Resolution Playbooks.
MERGED_KBAS = {
    "assignment_profiles_sap.md",
    "learning_assignment_sap.md",
    "learning_history_completion_sap.md",
    "login_authentication_sap.md",
    "mylearning_access_sap.md",
    "scorm_online_content_sap.md",
    "user_connector_sap_knowledge.md",
    "curriculum_retraining_sap.md",
}


def load_documents():
    """
    Load knowledge documents from the ResolveAI knowledge base.

    Expert Resolution Playbooks are the primary troubleshooting
    knowledge source.

    SAP KBAs that have already been merged into the corresponding
    Expert Resolution Playbooks are excluded from retrieval to
    prevent duplicate knowledge.
    """

    documents = []

    # ---------------------------------------------------------
    # EXPERT RESOLUTION PLAYBOOKS
    # ---------------------------------------------------------

    for file in EXPERT_PLAYBOOK_DIR.glob("*.md"):

        content = file.read_text(
            encoding="utf-8"
        )

        documents.append({
            "source": file.name,
            "source_type": "Expert Resolution Playbook",
            "content": content
        })

    # ---------------------------------------------------------
    # SAP KBAs
    # ---------------------------------------------------------

    excluded_kbas = []

    for file in SAP_KBA_DIR.glob("*.md"):

        if file.name in MERGED_KBAS:
            excluded_kbas.append(file.name)
            continue

        content = file.read_text(
            encoding="utf-8"
        )

        documents.append({
            "source": file.name,
            "source_type": "SAP Official Documentation / KBA",
            "content": content
        })

    # ---------------------------------------------------------
    # SUMMARY
    # ---------------------------------------------------------

    print(
        f"\nLoaded {len(documents)} knowledge documents:"
    )

    for document in documents:
        print(
            f"- {document['source']} "
            f"({document['source_type']})"
        )

    print(
        f"\nTotal documents loaded: {len(documents)}"
    )

    print(
        f"SAP KBAs excluded because they are merged: "
        f"{len(excluded_kbas)}"
    )

    return documents


if __name__ == "__main__":

    load_documents()