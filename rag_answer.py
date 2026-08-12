

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from retriever import retrieve_chunks

load_dotenv()

chat_history = []


def rewrite_query(query, chat_history):

    if chat_history:
        history_text = "\n".join(
            f"{message['role']}: {message['content']}"
            for message in chat_history
        )
    else:
        history_text = "No previous conversation."

    prompt = f"""
You are a query rewriting assistant for a Retrieval-Augmented Generation system.

Your job is ONLY to rewrite the user's latest question into a clear,
standalone search query.

Use the conversation history only to resolve references such as:
- it
- this
- that
- they
- those
- where
- why
- how

Do NOT answer the question.
Do NOT add facts that are not present in the conversation.
Do NOT invent information.

Conversation history:
{history_text}

Latest user question:
{query}

Return ONLY the rewritten search query.
"""

    try:
        llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0,
            api_key=os.getenv("GROQ_API_KEY"),
        )

        rewritten_query = llm.invoke(prompt).content.strip()

        return rewritten_query

    except Exception as e:
        print(f"Query rewriting error: {e}")
        return query

def generate_answer(query, chat_history=None):
    

    if chat_history is None:
        chat_history = []

    rewritten_query = rewrite_query(
        query,
        chat_history
    )

    print(f"\nOriginal query: {query}")
    print(f"Rewritten query: {rewritten_query}")

    ids, documents, metadatas, distances = retrieve_chunks(
        rewritten_query
    )

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

    chat_history.append({
        "role": "user",
        "content": query
    })

    chat_history.append({
        "role": "assistant",
        "content": answer
    })
   
    return answer, metadatas, documents, distances

# ==========================================
# 3. Main Function
# ==========================================

def main():

   chat_history = []

while True:

    query = input(
        "Enter your question (type 'exit' to quit): "
    )

    if query.lower() == "exit":
        break

    if not query.strip():
        print("Question cannot be empty.")
        continue

    answer, metadatas, _, _ = generate_answer(
        query,
        chat_history
    )

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

   

# ==========================================
# 4. Entry Point
# ==========================================

if __name__ == "__main__":
    main()