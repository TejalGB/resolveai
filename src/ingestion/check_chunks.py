import json


with open(
    "data/processed/chunks.json",
    "r",
    encoding="utf-8"
) as file:
    chunks = json.load(file)


for i, chunk in enumerate(chunks):

    if chunk["source"] == "assignment_profiles.md":

        print("\n---")
        print(f"Chunk {i}")
        print(f"Scenario: {chunk['scenario']}")
        print(f"Content:\n{chunk['content']}")