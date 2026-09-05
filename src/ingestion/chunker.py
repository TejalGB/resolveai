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

            if stripped_line.startswith("## "):
                break

            if stripped_line:
                collected_lines.append(
                    stripped_line.replace("**", "")
                )

    return "\n".join(collected_lines).strip()


def extract_troubleshooting_steps(content):
    """
    Extract the complete Troubleshooting Steps section.

    Instead of creating one tiny chunk for every ### heading,
    we keep the troubleshooting flow together as one meaningful
    retrieval unit.
    """

    lines = content.splitlines()

    collected_lines = []
    collecting = False

    for line in lines:

        stripped_line = line.strip()

        # Start collecting after Troubleshooting Steps heading
        if stripped_line.lower() == "## troubleshooting steps":
            collecting = True
            continue

        if collecting:

            # Stop at the next major ## heading
            if stripped_line.startswith("## "):
                break

            if stripped_line:
                collected_lines.append(
                    stripped_line.replace("**", "")
                )

    return "\n".join(collected_lines).strip()


def extract_section_content(content, section_name):
    """
    Generic extraction for sections such as:
    Decision Flow
    Common Causes
    Resolution Logic
    Important Considerations
    """

    return extract_section(content, section_name)


def chunk_document(document):
    """
    Create meaningful knowledge chunks.

    Each document is divided into larger logical sections
    instead of tiny individual troubleshooting steps.
    """

    content = document["content"]

    category = extract_section(content, "Category")
    incident = extract_section(content, "Incident")
    problem_understanding = extract_section(
        content,
        "Problem Understanding"
    )

    chunks = []

    # -----------------------------------
    # CHUNK 1: Problem + Troubleshooting
    # -----------------------------------

    troubleshooting = extract_troubleshooting_steps(content)

    if troubleshooting:

        chunks.append({
            "source": document["source"],
            "category": category,
            "incident": incident,
            "problem_understanding": problem_understanding,
            "scenario": "Troubleshooting Steps",
            "content": troubleshooting
        })

    # -----------------------------------
    # CHUNK 2: Decision Flow
    # -----------------------------------

    decision_flow = extract_section_content(
        content,
        "Decision Flow"
    )

    if decision_flow:

        chunks.append({
            "source": document["source"],
            "category": category,
            "incident": incident,
            "problem_understanding": problem_understanding,
            "scenario": "Decision Flow",
            "content": decision_flow
        })

    # -----------------------------------
    # CHUNK 3: Common Causes + Resolution
    # -----------------------------------

    common_causes = extract_section_content(
        content,
        "Common Causes"
    )

    resolution_logic = extract_section_content(
        content,
        "Resolution Logic"
    )

    combined_resolution = ""

    if common_causes:
        combined_resolution += (
            "COMMON CAUSES:\n"
            + common_causes
            + "\n\n"
        )

    if resolution_logic:
        combined_resolution += (
            "RESOLUTION LOGIC:\n"
            + resolution_logic
        )

    if combined_resolution.strip():

        chunks.append({
            "source": document["source"],
            "category": category,
            "incident": incident,
            "problem_understanding": problem_understanding,
            "scenario": "Common Causes and Resolution Logic",
            "content": combined_resolution.strip()
        })

    # -----------------------------------
    # CHUNK 4: Important Considerations
    # -----------------------------------

    considerations = extract_section_content(
        content,
        "Important Considerations"
    )

    if considerations:

        chunks.append({
            "source": document["source"],
            "category": category,
            "incident": incident,
            "problem_understanding": problem_understanding,
            "scenario": "Important Considerations",
            "content": considerations
        })

    # -----------------------------------
    # CHUNK 5: Escalation / Evidence
    # -----------------------------------

    escalation = extract_section_content(
        content,
        "Escalation"
    )

    evidence = extract_section_content(
        content,
        "Evidence for Escalation"
    )

    escalation_content = ""

    if escalation:
        escalation_content += (
            "ESCALATION:\n"
            + escalation
            + "\n\n"
        )

    if evidence:
        escalation_content += (
            "EVIDENCE FOR ESCALATION:\n"
            + evidence
        )

    if escalation_content.strip():

        chunks.append({
            "source": document["source"],
            "category": category,
            "incident": incident,
            "problem_understanding": problem_understanding,
            "scenario": "Escalation and Evidence",
            "content": escalation_content.strip()
        })

    return chunks


# -----------------------------------
# Load all playbooks
# -----------------------------------

documents = load_playbooks()

all_chunks = []

for document in documents:

    chunks = chunk_document(document)

    all_chunks.extend(chunks)


print(f"Created {len(all_chunks)} chunks.")


# -----------------------------------
# Save processed chunks
# -----------------------------------

output_dir = Path("data/processed")

output_dir.mkdir(
    parents=True,
    exist_ok=True
)

output_file = output_dir / "chunks.json"


with open(
    output_file,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        all_chunks,
        file,
        indent=2,
        ensure_ascii=False
    )


print(f"Saved chunks to: {output_file}")