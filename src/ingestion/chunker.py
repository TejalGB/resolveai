import json
import re
from pathlib import Path
from collections import defaultdict

from .loader import load_documents


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def extract_section(content, section_name):
    """
    Extract text under an exact ## section heading
    until the next ## section heading.
    """

    lines = content.splitlines()

    collected_lines = []
    collecting = False

    target_heading = f"## {section_name}".lower()

    for line in lines:

        stripped_line = line.strip()

        # Start collecting after requested section
        if stripped_line.lower() == target_heading:
            collecting = True
            continue

        if collecting:

            # Stop at next major section
            if stripped_line.startswith("## "):
                break

            if stripped_line:
                collected_lines.append(
                    stripped_line.replace("**", "")
                )

    return "\n".join(collected_lines).strip()


def combine_sections(content, section_names):
    """
    Combine multiple related sections into one logical chunk.
    """

    combined_content = []

    for section_name in section_names:

        section_content = extract_section(
            content,
            section_name
        )

        if section_content:

            combined_content.append(
                f"{section_name.upper()}:\n{section_content}"
            )

    return "\n\n".join(combined_content).strip()


def create_chunk(
    document,
    category,
    incident,
    problem_understanding,
    scenario,
    content
):
    """
    Create a standardized knowledge chunk.
    """

    return {
        "source": document["source"],
        "source_type": document["source_type"],
        "category": category,
        "incident": incident,
        "problem_understanding": problem_understanding,
        "scenario": scenario,
        "content": content
    }


# ============================================================
# EXPERT PLAYBOOK CHUNKING
# ============================================================

def chunk_expert_playbook(document):
    """
    Chunk Expert Resolution Playbooks based on
    logical troubleshooting sections.
    """

    content = document["content"]

    category = extract_section(
        content,
        "Category"
    )

    incident = extract_section(
        content,
        "Incident"
    )

    problem_understanding = extract_section(
        content,
        "Problem Understanding"
    )

    chunks = []

    # --------------------------------------------------------
    # CHUNK 1: Troubleshooting Steps
    # --------------------------------------------------------

    troubleshooting = extract_section(
        content,
        "Troubleshooting Steps"
    )

    if troubleshooting:

        chunks.append(
            create_chunk(
                document,
                category,
                incident,
                problem_understanding,
                "Troubleshooting Steps",
                troubleshooting
            )
        )

    # --------------------------------------------------------
    # CHUNK 2: Decision Flow
    # --------------------------------------------------------

    decision_flow = extract_section(
        content,
        "Decision Flow"
    )

    if decision_flow:

        chunks.append(
            create_chunk(
                document,
                category,
                incident,
                problem_understanding,
                "Decision Flow",
                decision_flow
            )
        )

    # --------------------------------------------------------
    # CHUNK 3: Common Causes + Resolution
    # --------------------------------------------------------

    resolution_content = combine_sections(
        content,
        [
            "Common Causes",
            "Resolution Logic",
            "Common Resolution"
        ]
    )

    if resolution_content:

        chunks.append(
            create_chunk(
                document,
                category,
                incident,
                problem_understanding,
                "Common Causes and Resolution",
                resolution_content
            )
        )

    # --------------------------------------------------------
    # CHUNK 4: Important Considerations
    # --------------------------------------------------------

    considerations = extract_section(
        content,
        "Important Considerations"
    )

    if considerations:

        chunks.append(
            create_chunk(
                document,
                category,
                incident,
                problem_understanding,
                "Important Considerations",
                considerations
            )
        )

    # --------------------------------------------------------
    # CHUNK 5: Escalation + Evidence
    # --------------------------------------------------------

    escalation_content = combine_sections(
        content,
        [
            "Escalation",
            "Evidence for Escalation",
            "Escalation Information"
        ]
    )

    if escalation_content:

        chunks.append(
            create_chunk(
                document,
                category,
                incident,
                problem_understanding,
                "Escalation and Evidence",
                escalation_content
            )
        )

    return chunks


# ============================================================
# SAP KBA / OFFICIAL KNOWLEDGE CHUNKING
# ============================================================

def chunk_sap_knowledge(document):
    """
    Chunk SAP Official Documentation / KBA files.

    SAP knowledge documents are structured around
    'Knowledge Area:' sections rather than incident
    troubleshooting sections.
    """

    content = document["content"]

    category = extract_section(
        content,
        "Category"
    )

    product = extract_section(
        content,
        "Product"
    )

    # Use product as incident context if no incident exists
    incident = product

    problem_understanding = (
        "Official SAP documentation and knowledge base information."
    )

    chunks = []

    # --------------------------------------------------------
    # FIND ALL KNOWLEDGE AREA SECTIONS
    # --------------------------------------------------------

    pattern = r"^## Knowledge Area:\s*(.+?)\s*$"

    matches = list(
        re.finditer(
            pattern,
            content,
            re.MULTILINE
        )
    )

    # Extract each Knowledge Area
    for index, match in enumerate(matches):

        knowledge_area = match.group(1).strip()

        start_position = match.end()

        # End at next Knowledge Area or next major section
        if index + 1 < len(matches):

            end_position = matches[index + 1].start()

        else:

            # Look for remaining major sections
            remaining_content = content[start_position:]

            next_section = re.search(
                r"^## (?!Knowledge Area:)",
                remaining_content,
                re.MULTILINE
            )

            if next_section:

                end_position = (
                    start_position
                    + next_section.start()
                )

            else:

                end_position = len(content)

        section_content = content[
            start_position:end_position
        ].strip()

        if section_content:

            chunks.append(
                create_chunk(
                    document,
                    category,
                    incident,
                    problem_understanding,
                    knowledge_area,
                    section_content
                )
            )

    # --------------------------------------------------------
    # RESOLUTION LOGIC
    # --------------------------------------------------------

    resolution_logic = extract_section(
        content,
        "Resolution Logic"
    )

    if resolution_logic:

        chunks.append(
            create_chunk(
                document,
                category,
                incident,
                problem_understanding,
                "Resolution Logic",
                resolution_logic
            )
        )

    # --------------------------------------------------------
    # IMPORTANT CONSIDERATIONS
    # --------------------------------------------------------

    considerations = extract_section(
        content,
        "Important Considerations"
    )

    if considerations:

        chunks.append(
            create_chunk(
                document,
                category,
                incident,
                problem_understanding,
                "Important Considerations",
                considerations
            )
        )

    # --------------------------------------------------------
    # COMMON TECHNICAL INVESTIGATION POINTS
    # --------------------------------------------------------

    investigation_points = extract_section(
        content,
        "Common Technical Investigation Points"
    )

    if investigation_points:

        chunks.append(
            create_chunk(
                document,
                category,
                incident,
                problem_understanding,
                "Common Technical Investigation Points",
                investigation_points
            )
        )

    return chunks


# ============================================================
# MAIN DOCUMENT ROUTER
# ============================================================

def chunk_document(document):
    """
    Route documents to the appropriate chunking strategy
    based on source type.
    """

    source_type = document.get(
        "source_type",
        ""
    )

    if source_type == "Expert Resolution Playbook":

        return chunk_expert_playbook(
            document
        )

    elif source_type == "SAP Official Documentation / KBA":

        return chunk_sap_knowledge(
            document
        )

    else:

        print(
            f"Warning: Unknown source type "
            f"for {document['source']}"
        )

        return []


# ============================================================
# LOAD DOCUMENTS
# ============================================================

documents = load_documents()

all_chunks = []

for document in documents:

    chunks = chunk_document(
        document
    )

    all_chunks.extend(
        chunks
    )


print(
    f"\nCreated {len(all_chunks)} chunks."
)


# ============================================================
# SAVE PROCESSED CHUNKS
# ============================================================

output_dir = Path(
    "data/processed"
)

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


print(
    f"Saved chunks to: {output_file}"
)


# ============================================================
# VALIDATION: CHUNK DISTRIBUTION
# ============================================================

print(
    "\nChunk distribution by document:\n"
)

chunk_summary = defaultdict(list)


for chunk in all_chunks:

    chunk_summary[
        chunk["source"]
    ].append(
        chunk["scenario"]
    )


for source, scenarios in chunk_summary.items():

    print(source)

    print(
        f"  Chunks: {len(scenarios)}"
    )

    for scenario in scenarios:

        print(
            f"   - {scenario}"
        )

    print()