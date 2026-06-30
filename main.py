from loader import load_document
from chunker import chunk_text

file_path = "data/sample.txt"

text = load_document(file_path)

chunks = chunk_text(text, file_path)

print(f"\nTotal Chunks: {len(chunks)}\n")

for chunk in chunks:
    print("=" * 60)
    print(f"Chunk ID : {chunk['chunk_id']}")
    print(f"Source   : {chunk['source']}")
    print("Text:")
    print(chunk["text"])
    print("=" * 60)
    print()