import os
import json
import numpy as np

from sentence_transformers import SentenceTransformer


# ==========================================
# Paths
# ==========================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CHUNK_DIRS = {
    "Fixed": os.path.join(BASE_DIR, "data", "chunks", "fixed"),
    "Recursive": os.path.join(BASE_DIR, "data", "chunks", "recursive"),
    "Sentence": os.path.join(BASE_DIR, "data", "chunks", "sentence"),
}


# ==========================================
# Embedding Model
# ==========================================

model = SentenceTransformer("all-MiniLM-L6-v2")


# ==========================================
# Test Questions
# ==========================================

questions = [
    "What is Python used for?",
    "What is retrieval augmented generation?",
    "What is a database?",
    "What is machine learning?",
    "What is software testing?",
]


# ==========================================
# Load Chunks
# ==========================================

def load_chunks(folder):

    chunks = []

    if not os.path.exists(folder):
        print(f"Folder not found: {folder}")
        return chunks

    for filename in os.listdir(folder):

        if not filename.endswith(".json"):
            continue

        filepath = os.path.join(folder, filename)

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Support either a list of chunks
        # or {"chunks": [...]}
        if isinstance(data, list):
            file_chunks = data

        elif isinstance(data, dict):
            file_chunks = data.get("chunks", [])

        else:
            file_chunks = []

        for chunk in file_chunks:

            if isinstance(chunk, str):
                chunks.append({
                    "text": chunk,
                    "source": filename
                })

            elif isinstance(chunk, dict):

                chunks.append({
                    "text": chunk.get(
    "text",
    chunk.get("chunk_text", "")
),
                    "source": chunk.get(
                        "source",
                        filename
                    ),
                    "chunk_id": chunk.get(
                        "chunk_id",
                        "N/A"
                    )
                })

    return chunks


# ==========================================
# Cosine Similarity
# ==========================================

def cosine_similarity(a, b):

    denominator = (
        np.linalg.norm(a) *
        np.linalg.norm(b)
    )

    if denominator == 0:
        return 0

    return np.dot(a, b) / denominator


# ==========================================
# Retrieve Top K
# ==========================================

def retrieve_top_k(chunks, question, k=3):

    if not chunks:
        return []

    texts = [
        chunk["text"]
        for chunk in chunks
        if chunk["text"].strip()
    ]

    if not texts:
        return []

    # Embed chunks
    chunk_embeddings = model.encode(
        texts,
        normalize_embeddings=True
    )

    # Embed question
    question_embedding = model.encode(
        question,
        normalize_embeddings=True
    )

    scores = np.dot(
        chunk_embeddings,
        question_embedding
    )

    ranked_indices = np.argsort(
        scores
    )[::-1][:k]

    results = []

    valid_chunks = [
        chunk for chunk in chunks
        if chunk["text"].strip()
    ]

    for index in ranked_indices:

        chunk = valid_chunks[index]

        results.append({
            "score": float(scores[index]),
            "text": chunk["text"],
            "source": chunk.get(
                "source",
                "N/A"
            ),
            "chunk_id": chunk.get(
                "chunk_id",
                "N/A"
            )
        })

    return results


# ==========================================
# Main Comparison
# ==========================================

def main():

    print("=" * 70)
    print("CHUNKING RETRIEVAL COMPARISON")
    print("=" * 70)

    all_chunks = {}

    # --------------------------------------
    # Load all three strategies
    # --------------------------------------

    for strategy, folder in CHUNK_DIRS.items():

        print(f"\nLoading {strategy} chunks...")

        chunks = load_chunks(folder)

        all_chunks[strategy] = chunks

        print(
            f"{strategy}: "
            f"{len(chunks)} chunks loaded"
        )

    # --------------------------------------
    # Run questions
    # --------------------------------------

    for question_number, question in enumerate(
        questions,
        start=1
    ):

        print("\n")
        print("=" * 70)
        print(
            f"QUESTION {question_number}: "
            f"{question}"
        )
        print("=" * 70)

        for strategy, chunks in all_chunks.items():

            print(f"\n--- {strategy} ---")

            results = retrieve_top_k(
                chunks,
                question,
                k=3
            )

            if not results:
                print("No chunks found.")
                continue

            for rank, result in enumerate(
                results,
                start=1
            ):

                print(
                    f"\n{rank}. "
                    f"Score: {result['score']:.4f}"
                )

                print(
                    f"Source: "
                    f"{result['source']}"
                )

                print(
                    f"Chunk ID: "
                    f"{result['chunk_id']}"
                )

                print(
                    f"Text: "
                    f"{result['text'][:400]}"
                )

    print("\n")
    print("=" * 70)
    print("COMPARISON COMPLETED")
    print("=" * 70)


if __name__ == "__main__":
    main()