import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from retriever import retrieve_chunks

load_dotenv()


# ==========================================
# 1. Decide Whether History Is Needed
# ==========================================

def needs_history(question, chat_history):

    if not chat_history:
        return False

    q = question.lower().strip()
    words = q.replace("?", "").split()

    followup_pronouns = {
        "it", "its", "they", "them", "this", "that",
        "these", "those", "he", "she", "his", "her"
    }

    followup_phrases = [
        "explain more",
        "tell me more",
        "what about",
        "how about",
        "why so",
        "same thing",
        "above topic",
        "previous topic"
    ]

    # Strong standalone signal
    if len(words) >= 7:
        return False

    # Explicit follow-up phrases
    if any(phrase in q for phrase in followup_phrases):
        return True

    # Pronoun/reference-based follow-up
    if any(word in words for word in followup_pronouns):
        return True

    return False


# ==========================================
# 2. Query Rewriting
# ==========================================

def rewrite_query(query, chat_history):

    use_history = needs_history(
        query,
        chat_history
    )

    print(f"History used for rewriting: {use_history}")

    # --------------------------------------
    # Case 1: History is required
    # --------------------------------------

    if use_history:

        history_text = "\n".join(
            f"{message['role']}: {message['content']}"
            for message in chat_history
        )

        prompt = f"""
You are a query rewriting assistant for a
Retrieval-Augmented Generation system.

Rewrite the user's latest question into a clear,
standalone search query.

Use conversation history ONLY to resolve unclear
references such as:
- it
- its
- they
- them
- this
- that
- these
- those
- above
- previous

If the latest question has its own clear subject,
ignore conversation history.

Do NOT answer the question.

Do NOT add facts that are not present in the
question or required history.

Do NOT introduce unrelated topics from the
conversation history.

Never add entities from history unless the
latest question contains an unclear reference.

Conversation history:
{history_text}

Latest question:
{query}

Return ONLY the rewritten search query.
"""

    # --------------------------------------
    # Case 2: No history required
    # --------------------------------------

    else:

        prompt = f"""
You are a query rewriting assistant for a
Retrieval-Augmented Generation system.

Rewrite the user's question into a clear,
standalone search query.

The question is already standalone, so DO NOT
use conversation history.

Do NOT answer the question.

Do NOT add any topic, entity, or fact that is
not present in the question.

Do NOT introduce information from previous
conversation.

Question:
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

        # Keep output on one line
        rewritten_query = rewritten_query.replace(
            "\n", " "
        ).strip()

        return rewritten_query

    except Exception as e:

        print(f"Query rewriting error: {e}")

        # If rewriting fails, use original query
        return query


# ==========================================
# 3. Generate Answer
# ==========================================

def generate_answer(query, chat_history=None):

    if chat_history is None:
        chat_history = []

    # --------------------------------------
    # Query rewriting
    # --------------------------------------

    rewritten_query = rewrite_query(
        query,
        chat_history
    )

    print(f"\nOriginal query: {query}")
    print(f"Rewritten query: {rewritten_query}\n")

    # --------------------------------------
    # Retrieval + Reranking
    # --------------------------------------

    ids, documents, metadatas, distances = retrieve_chunks(
        rewritten_query
    )

    context = "\n\n".join(documents)

    # --------------------------------------
    # Generate final answer
    # --------------------------------------

    prompt = f"""
You are a helpful AI assistant.

Answer the exact question directly first.
Do not add extra explanation unless it is needed.
Keep the answer concise and focused.

Answer ONLY using the information provided
in the context below.

If the answer cannot be found in the context,
reply exactly:

Not enough information in the uploaded documents.

Context:
{context}

Question:
{rewritten_query}
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

    # --------------------------------------
    # Store conversation history
    # --------------------------------------

    chat_history.append({
        "role": "user",
        "content": query
    })

    chat_history.append({
        "role": "assistant",
        "content": answer
    })

    return answer, metadatas, documents, distances

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

        for index, metadata in enumerate(
            metadatas,
            start=1
        ):

            page = metadata.get("page", "N/A")

            print(
                f"{index}. {metadata['source']} "
                f"(Page {page}, "
                f"Chunk {metadata['chunk_index']})"
            )

        print("=" * 70)


# ==========================================
# 5. Entry Point
# ==========================================

if __name__ == "__main__":
    main()