from google import genai
import chromadb
import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer


#load key
load_dotenv()
# ==========================================
# 1. Gemini API Key
# ==========================================
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Please add it to the .env file."
    )

client = genai.Client(api_key=API_KEY)

# ==========================================
# 2. Load Embedding Model
# ==========================================
print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Embedding model loaded.")

# ==========================================
# 3. Connect to ChromaDB
# ==========================================
client_db = chromadb.PersistentClient(path="chroma_db")

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

print("Connected to ChromaDB.")

# ==========================================
# 4. Get User Query
# ==========================================
query = input("\nEnter your question: ")

# ==========================================
# 5. Convert Query into Embedding
# ==========================================
query_embedding = model.encode(query).tolist()

# ==========================================
# 6. Retrieve Top 3 Chunks
# ==========================================
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

documents = results["documents"][0]
metadatas = results["metadatas"][0]
distances = results["distances"][0]

print("\nRetrieved Chunks:\n")

for i in range(len(documents)):
    print("=" * 60)
    print(f"Rank : {i+1}")
    print(f"Distance : {distances[i]:.4f}")
    print(f"Source : {metadatas[i]['source']}")
    print(f"Chunk : {metadatas[i]['chunk_index']}")
    print()
    print(documents[i])
    print("=" * 60)

# ==========================================
# 7. Build Context
# ==========================================
context = "\n\n".join(documents)

# ==========================================
# 8. Prompt Engineering
# ==========================================
prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the information provided in the context below.

If the answer cannot be found in the context, reply exactly:

Not enough information in the uploaded documents.

Context:
{context}

Question:
{query}
"""

# ==========================================
# 9. Generate Answer using Gemini
# ==========================================
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

# ==========================================
# 10. Print Final Answer
# ==========================================
print("\n")
print("=" * 70)
print("FINAL ANSWER")
print("=" * 70)
print(response.text)
print("=" * 70)