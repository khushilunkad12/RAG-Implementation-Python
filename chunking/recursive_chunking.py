import os
import json
from langchain_text_splitters import RecursiveCharacterTextSplitter

INPUT_DIR = "data/chunking_docs"
OUTPUT_DIR = "data/chunks/recursive"

os.makedirs(OUTPUT_DIR, exist_ok=True)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=["\n\n", "\n", ". ", " ", ""]
)

for filename in os.listdir(INPUT_DIR):

    if not filename.endswith(".txt"):
        continue

    filepath = os.path.join(INPUT_DIR, filename)

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = splitter.create_documents([text])

    output = []

    for i, chunk in enumerate(chunks):

        output.append({
            "chunk_id": f"{filename}_{i}",
            "source": filename,
            "chunk_index": i,
            "text": chunk.page_content
        })

    output_file = os.path.join(
        OUTPUT_DIR,
        filename.replace(".txt", ".json")
    )

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"{filename}: {len(output)} chunks")

print("\nRecursive chunking completed.")