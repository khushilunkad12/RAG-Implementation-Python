import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from retriever import retrieve_chunks

load_dotenv()

def generate_answer(query):
    ids, documents, metadatas, distances = retrieve_chunks(query)
    context = "\n\n".join(documents)

    prompt = f"""You are a helpful AI assistant.
Answer ONLY using the information provided in the context below.
If the answer cannot be found in the context, reply exactly:
Not enough information in the uploaded documents.

Context:
{context}

Question:
{query}
"""
    try:
        llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0,
            api_key=os.getenv("GROQ_API_KEY"),
        )
        answer = llm.invoke(prompt).content
    except Exception as e:
        print(f"Groq Error: {e}")
        answer = "LLM/API unavailable."

    return answer, metadatas, documents, distances


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