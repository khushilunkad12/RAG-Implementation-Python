import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="chroma_db")

try:
    collection = client.get_collection(
        name="rag_documents"
    )
except Exception:
    print("Error: Chroma collection not found.")
    print()
    print("Run the following first:")
    print("python main.py")
    print("python embed_store.py")
    exit()

print("Connected to ChromaDB.")

# User query
query = input("Enter your question: ")

# Convert query to embedding
query_embedding = model.encode(query).tolist()

# Retrieve top 3 chunks
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

# Extract results
documents = results["documents"][0]
ids = results["ids"][0]
metadatas = results["metadatas"][0]
distances = results["distances"][0]

# Display retrieved chunks
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