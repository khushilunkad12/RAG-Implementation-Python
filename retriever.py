import chromadb


# ==========================================
# 1. Models (Lazy Loading)
# ==========================================

_model = None
_reranker = None


def get_model():
    """
    Loads the embedding model only once.
    """
    global _model

    if _model is None:
        print("Loading embedding model...")

        from sentence_transformers import SentenceTransformer

        _model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        print("Embedding model loaded.")

    return _model


def get_reranker():
    """
    Loads the CrossEncoder reranker only once.
    """
    global _reranker

    if _reranker is None:
        print("Loading reranker...")

        from sentence_transformers import CrossEncoder

        _reranker = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

        print("Reranker loaded.")

    return _reranker


# ==========================================
# 2. Connect to ChromaDB
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

def retrieve_chunks(query, top_k=15, top_n=5):

    # Stage 1: Embedding retrieval
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

    # Stage 2: Reranking
    reranker = get_reranker()

    pairs = [(query, doc) for doc in documents]

    scores = reranker.predict(pairs)

    # Sort by reranker score
    ranked = sorted(
        zip(
            scores,
            ids,
            documents,
            metadatas,
            distances
        ),
        key=lambda x: x[0],
        reverse=True
    )[:top_n]

    ids = [r[1] for r in ranked]
    documents = [r[2] for r in ranked]
    metadatas = [r[3] for r in ranked]
    distances = [r[4] for r in ranked]

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