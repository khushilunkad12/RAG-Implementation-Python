import json
import os
import chromadb
from sentence_transformers import SentenceTransformer

# ----------------------------
# Check if chunk file exists
# ----------------------------
if not os.path.exists("output_chunks.json"):
    print("Error: output_chunks.json not found.")
    print("Run:")
    print("python main.py")
    exit()

# ----------------------------
# Load chunks
# ----------------------------
with open("output_chunks.json", "r", encoding="utf-8") as file:
    chunks = json.load(file)

print(f"Loaded {len(chunks)} chunks.")

# ----------------------------
# Load embedding model
# ----------------------------
print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Embedding model loaded.")

# ----------------------------
# Connect to ChromaDB
# ----------------------------
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="rag_documents"
)

print("Connected to ChromaDB.")

# ----------------------------
# Store embeddings
# ----------------------------
for chunk in chunks:

    embedding = model.encode(chunk["text"]).tolist()

    collection.upsert(
        ids=[chunk["chunk_id"]],
        documents=[chunk["text"]],
        embeddings=[embedding],
        metadatas=[chunk["metadata"]]
    )

print("Embeddings stored successfully.")