import json

from document_loader import load_documents
from chunker import chunk_text

# ==========================================
# Load all documents
# ==========================================

documents = load_documents()

print(f"Loaded {len(documents)} documents.\n")

all_chunks = []

# ==========================================
# Chunk every document
# ==========================================

for document in documents:

    print(f"Processing: {document['filename']}")

    chunks = chunk_text(
        document["text"],
        document["filename"]
    )

    all_chunks.extend(chunks)

# ==========================================
# Save chunks
# ==========================================

with open(
    "output_chunks.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        all_chunks,
        file,
        indent=4
    )

print("\nChunks saved to output_chunks.json")

print(f"\nTotal Documents : {len(documents)}")
print(f"Total Chunks    : {len(all_chunks)}\n")

# ==========================================
# Display chunks
# ==========================================

for chunk in all_chunks:

    print("=" * 60)
    print(f"Chunk ID    : {chunk['chunk_id']}")
    print(f"Source      : {chunk['metadata']['source']}")
    print(f"Chunk Index : {chunk['metadata']['chunk_index']}")
    print(f"Chunk Size  : {chunk['metadata']['chunk_size']} characters")
    print(f"Overlap     : {chunk['metadata']['overlap']} characters")
    print("\nText:\n")
    print(chunk["text"])
    print("=" * 60)
    print()