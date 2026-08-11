import chromadb
from sentence_transformers import SentenceTransformer

# ==========================================
# 1. Load Embedding Model
# ==========================================

# ==========================================
# Embedding Model (Lazy Loading)
# ==========================================

model = None


def get_model():
    """
    Loads the embedding model only once.
    """

    global model

    if model is None:

        print("Loading embedding model...")

        model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        print("Embedding model loaded.")

    return model


# ==========================================
# 2. Connect to ChromaDB
# ==========================================

# ==========================================
# ChromaDB (Lazy Loading)
# ==========================================

collection = None


def get_collection():
    """
    Connects to ChromaDB only once.
    """

    global collection

    if collection is None:

        client = chromadb.PersistentClient(
            path="chroma_db"
        )

        try:

            collection = client.get_collection(
                name="rag_documents"
            )

            print("Connected to ChromaDB.")

        except Exception as e:

           raise RuntimeError(
        "Chroma collection not found. "
        "Run 'python main.py' followed by "
        "'python embed_store.py' first."
    ) from e

    return collection


# ==========================================
# 3. Retrieval Function
# ==========================================

def retrieve_chunks(query, top_k=8):
    """
    Retrieves the most relevant chunks
    for the given user query.

    Returns:
        ids
        documents
        metadatas
        distances
    """

    model = get_model()

    query_embedding = model.encode(query).tolist()

    collection = get_collection()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    ids = results["ids"][0]
    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    return ids, documents, metadatas, distances

# ==========================================
# 4. Main Function
# ==========================================

def main():

    query = input("Enter your question: ")

    if not query.strip():
        print("Question cannot be empty.")
        return

    ids, documents, metadatas, distances = retrieve_chunks(query)

    for i in range(len(documents)):

        print("=" * 60)
        print(f"Rank #{i + 1}")
        print(f"Chunk ID     : {ids[i]}")
        print(f"Distance     : {distances[i]:.4f}")

        metadata = metadatas[i]

        print(f"Source       : {metadata['source']}")
        print(f"Chunk Index  : {metadata['chunk_index']}")
        print(f"Chunk Size   : {metadata['chunk_size']}")
        print(f"Overlap      : {metadata['overlap']}")

        print("\nRetrieved Text:\n")
        print(documents[i])

        print("=" * 60)
        print()


# ==========================================
# 5. Entry Point
# ==========================================

if __name__ == "__main__":
    main()