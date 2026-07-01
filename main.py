import json

from loader import load_document
from chunker import chunk_text

# Step 1: Specify the file path
file_path = "data/sample.txt"

# Step 2: Load the document
text = load_document(file_path)

# Step 3: Split the document into chunks with metadata
chunks = chunk_text(text, file_path)

# ==============================
# Step 4: Save chunks to JSON
# ==============================
with open("output_chunks.json", "w", encoding="utf-8") as file:
    json.dump(chunks, file, indent=4)

print("Chunks saved to output_chunks.json")

# ==============================
# Step 5: Print total chunks
# ==============================
print(f"\nTotal Chunks: {len(chunks)}\n")

# ==============================
# Step 6: Print each chunk
# ==============================
for chunk in chunks:
    print("=" * 60)
    print(f"Chunk ID : {chunk['chunk_id']}")
    print(f"Source   : {chunk['source']}")
    print("Text:")
    print(chunk["text"])
    print("=" * 60)
    print()
