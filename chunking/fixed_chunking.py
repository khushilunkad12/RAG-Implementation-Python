import os
import json


DATA_DIR = "data/chunking_docs"
OUTPUT_FILE = "data/chunks/fixed/fixed_chunks.json"

CHUNK_SIZE = 500
OVERLAP = 50


def fixed_size_chunks(text, chunk_size=500, overlap=50):

    chunks = []

    start = 0
    chunk_id = 0

    while start < len(text):

        end = min(start + chunk_size, len(text))

        chunk_text = text[start:end]

        chunks.append({
            "chunk_id": chunk_id,
            "chunk_text": chunk_text,
            "start_position": start,
            "end_position": end
        })

        chunk_id += 1

        if end == len(text):
            break

        start = end - overlap

    return chunks


def process_documents():

    all_chunks = []

    for filename in os.listdir(DATA_DIR):

        if not filename.endswith(".txt"):
            continue

        filepath = os.path.join(DATA_DIR, filename)

        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read()

        chunks = fixed_size_chunks(
            text,
            CHUNK_SIZE,
            OVERLAP
        )

        for chunk in chunks:

            chunk["source"] = filename

            all_chunks.append(chunk)

    return all_chunks


if __name__ == "__main__":

    chunks = process_documents()

    os.makedirs(
    os.path.dirname(OUTPUT_FILE),
    exist_ok=True
)

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            chunks,
            file,
            indent=2,
            ensure_ascii=False
        )

    print(
        f"Created {len(chunks)} fixed-size chunks."
    )

    print(
        f"Saved to: {OUTPUT_FILE}"
    )