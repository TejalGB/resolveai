from pathlib import Path

PLAYBOOK_DIR = Path("data/raw/expert_playbooks")


def load_playbooks():
    documents = []

    for file in PLAYBOOK_DIR.glob("*.md"):
        content = file.read_text(encoding="utf-8")

        documents.append({
            "source": file.name,
            "content": content
        })

    return documents


documents = load_playbooks()

print(f"Loaded {len(documents)} playbooks.")

for document in documents:
    print(f"- {document['source']}")