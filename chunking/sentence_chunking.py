import os
import json
import re

INPUT_DIR = "data/chunking_docs"
OUTPUT_DIR = "data/chunks/sentence"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def split_into_chunks(text, max_chars=500):

    paragraphs = [
        p.strip()
        for p in text.split("\n\n")
        if p.strip()
    ]

    chunks = []
    current = ""

    for paragraph in paragraphs:

        sentences = re.split(
            r'(?<=[.!?])\s+',
            paragraph
        )

        for sentence in sentences:

            sentence = sentence.strip()

            if not sentence:
                continue

            if current and len(current) + len(sentence) + 1 > max_chars:

                chunks.append(current.strip())
                current = sentence

            else:

                if current:
                    current += " "

                current += sentence

    if current:
        chunks.append(current.strip())

    return chunks


for filename in os.listdir(INPUT_DIR):

    if not filename.endswith(".txt"):
        continue

    filepath = os.path.join(INPUT_DIR, filename)

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = split_into_chunks(text)

    output = []

    for i, chunk in enumerate(chunks):

        output.append({
            "chunk_id": f"{filename}_{i}",
            "source": filename,
            "chunk_index": i,
            "text": chunk
        })

    output_file = os.path.join(
        OUTPUT_DIR,
        filename.replace(".txt", ".json")
    )

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(
            output,
            f,
            indent=2,
            ensure_ascii=False
        )

    print(f"{filename}: {len(output)} chunks")


print("\nSentence/paragraph chunking completed.")