from loader import load_document
from chunker import chunk_text

# Step 1: Load the document
text = load_document("data/sample.txt")

# Step 2: Split into chunks
chunks = chunk_text(text)

# Step 3: Print total chunks
print(f"\nTotal Chunks: {len(chunks)}\n")

# Step 4: Print each chunk
for index, chunk in enumerate(chunks, start=1):
    print("=" * 60)
    print(f"Chunk {index}")
    print("=" * 60)
    print(chunk)
    print()