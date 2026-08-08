from google import genai
import os
from dotenv import load_dotenv

from retriever import retrieve_chunks

# ==========================================
# 1. Load Gemini Client
# ==========================================

def get_gemini_client():
    """
    Loads the Gemini client when needed.
    """

    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY not found. Please add it to the .env file."
        )

    return genai.Client(api_key=api_key)


# ==========================================
# 2. Generate RAG Answer
# ==========================================

def generate_answer(query):
    """
    Retrieves relevant chunks and generates
    an answer using Gemini.

    Returns:
        answer
        metadatas
        documents
        distances
    """

    ids, documents, metadatas, distances = retrieve_chunks(query)

    # ==========================================
    # Build Context
    # ==========================================

    context = "\n\n".join(documents)

    # ==========================================
    # Prompt
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
    # Gemini
    # ==========================================

    try:

        gemini_client = get_gemini_client()

        response = gemini_client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        answer = response.text

    except Exception as e:

        print(f"Gemini Error: {e}")

        answer = (
            "LLM/API unavailable. Retrieved context is shown below."
        )

    return (
        answer,
        metadatas,
        documents,
        distances
    )


# ==========================================
# 3. Main Function
# ==========================================

def main():

    query = input("Enter your question: ")

    if not query.strip():
        print("Question cannot be empty.")
        return

    answer, metadatas, _, _ = generate_answer(query)

    print("\n")
    print("=" * 70)
    print("FINAL ANSWER")
    print("=" * 70)
    print(answer)

    print("\n")
    print("=" * 70)
    print("SOURCES")
    print("=" * 70)

    for index, metadata in enumerate(metadatas, start=1):

        page = metadata.get("page", "N/A")

        print(
            f"{index}. {metadata['source']} "
            f"(Page {page}, Chunk {metadata['chunk_index']})"
        )

    print("=" * 70)


# ==========================================
# 4. Entry Point
# ==========================================

if __name__ == "__main__":
    main()