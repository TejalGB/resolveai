import json
from pathlib import Path

from loader import load_playbooks


def extract_section(content, section_name):
    """
    Extract text under a ## section until the next ## section.
    """

    lines = content.splitlines()
    collected_lines = []
    collecting = False

    for line in lines:
        stripped_line = line.strip()

        if stripped_line.lower() == f"## {section_name}".lower():
            collecting = True
            continue

        if collecting:
            # Stop when the next level-2 heading starts
            if stripped_line.startswith("## "):
                break

            if stripped_line:
                collected_lines.append(stripped_line.replace("**", ""))

    return "\n".join(collected_lines).strip()


def extract_category(content):
    return extract_section(content, "Category")


def extract_incident(content):
    return extract_section(content, "Incident")


def extract_problem_understanding(content):
    return extract_section(content, "Problem Understanding")


def chunk_document(document):
    content = document["content"]

    category = extract_category(content)
    incident = extract_incident(content)
    problem_understanding = extract_problem_understanding(content)

    sections = content.split("### ")

    chunks = []

    for section in sections[1:]:

        lines = section.strip().split("\n", 1)

        title = lines[0].strip()

        # Skip the parent heading
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
            "incident": incident,
            "problem_understanding": problem_understanding,
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
