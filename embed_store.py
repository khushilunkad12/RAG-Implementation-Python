import json
import os
import chromadb



# ==========================================
# Store Embeddings
# ==========================================

def store_embeddings(model=None):

    """
    Reads output_chunks.json,
    generates embeddings,
    and stores them in ChromaDB.
    """

    # ----------------------------
    # Check if chunk file exists
    # ----------------------------

    from sentence_transformers import SentenceTransformer
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

    if model is None:

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
    # Generate embeddings in batch
    # ----------------------------

    texts = [chunk["text"] for chunk in chunks]

    embeddings = model.encode(
        texts,
        batch_size=32,
        show_progress_bar=True
    ).tolist()

    # ----------------------------
    # Store embeddings
    # ----------------------------

    collection.upsert(
        ids=[chunk["chunk_id"] for chunk in chunks],
        documents=texts,
        embeddings=embeddings,
        metadatas=[chunk["metadata"] for chunk in chunks]
    )

    print("Embeddings stored successfully.")


# ==========================================
# Main Function
# ==========================================

def main():

    store_embeddings(model=None)


# ==========================================
# Entry Point
# ==========================================

if __name__ == "__main__":
    main()