import json
import os
import chromadb
from sentence_transformers import SentenceTransformer


# ==========================================
# Store Embeddings
# ==========================================

def store_embeddings():
    """
    Reads output_chunks.json,
    generates embeddings,
    and stores them in ChromaDB.
    """

    # ----------------------------
    # Check if chunk file exists
    # ----------------------------

    if not os.path.exists("output_chunks.json"):
        print("Error: output_chunks.json not found.")
        print()
        print("Run:")
        print("python main.py")
        return

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

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    print("Embedding model loaded.")

       # ----------------------------
    # Connect to ChromaDB
    # ----------------------------

    client = chromadb.PersistentClient(
        path="chroma_db"
    )

    # Remove old collection if it exists
    try:
        client.delete_collection("rag_documents")
        print("Old collection removed.")
    except Exception:
        pass

    # Create a fresh collection
    collection = client.get_or_create_collection(
        name="rag_documents"
    )

    print("Connected to ChromaDB.")

    # ----------------------------
    # Store embeddings
    # ----------------------------

    for chunk in chunks:

        embedding = model.encode(
            chunk["text"]
        ).tolist()

        collection.upsert(
            ids=[chunk["chunk_id"]],
            documents=[chunk["text"]],
            embeddings=[embedding],
            metadatas=[chunk["metadata"]]
        )

    print("Embeddings stored successfully.")
# ==========================================
# Main Function
# ==========================================

def main():
    store_embeddings()


# ==========================================
# Entry Point
# ==========================================

if __name__ == "__main__":
    main()