import json
from pathlib import Path

from loader import load_playbooks


def extract_category(content):
    lines = content.splitlines()

    category = ""

    for i, line in enumerate(lines):
        line = line.strip()

        if line.lower() == "## category":
            if i + 1 < len(lines):
                category = lines[i + 1].strip()

    return category


def chunk_document(document):
    content = document["content"]

    category = extract_category(content)

    sections = content.split("### ")

    chunks = []

    for section in sections[1:]:
        lines = section.strip().split("\n", 1)

        title = lines[0].strip()

        if title.lower() == "troubleshooting steps":
            continue

        if len(lines) > 1:
            body = lines[1].strip()
        else:
            body = ""

        body = body.replace("## Troubleshooting Steps", "").strip()

        chunks.append({
            "source": document["source"],
            "category": category,
            "scenario": title,
            "content": body
        })

    return chunks


documents = load_playbooks()

all_chunks = []

for document in documents:
    chunks = chunk_document(document)
    all_chunks.extend(chunks)


print(f"Created {len(all_chunks)} chunks.")


# Save processed chunks
output_dir = Path("data/processed")
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "chunks.json"

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(all_chunks, file, indent=2, ensure_ascii=False)


print(f"Saved chunks to: {output_file}")


# Display first 5 chunks
print("\nFirst 5 chunks:")

for chunk in all_chunks[:5]:
    print("\n---")
    print(f"Source: {chunk['source']}")
    print(f"Category: {chunk['category']}")
    print(f"Scenario: {chunk['scenario']}")
    print(chunk["content"])