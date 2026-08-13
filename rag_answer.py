

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from retriever import retrieve_chunks

load_dotenv()

chat_history = []

def needs_history(question, chat_history):

    if not chat_history:
        return False

    history_text = "\n".join(
        f"{message['role']}: {message['content']}"
        for message in chat_history
    )

    prompt = f"""
You are a conversation context classifier for a Retrieval-Augmented Generation system.

Determine whether the user's latest question requires the previous
conversation to understand what the user means.

Return ONLY:
true
or
false

Rules:

- Return true if the question is incomplete, ambiguous, or contains
  an implicit reference to something discussed earlier.
- Return true for questions like:
  "where is it used?"
  "why is it easy?"
  "where used?"
  "explain more"
  "what about its features?"
- Return false if the question is already understandable as a
  standalone question.
- A question mentioning an entity explicitly is usually standalone.
- Do NOT assume that the current question is related to previous
  topics just because the previous conversation contains them.

Conversation history:
{history_text}

Latest question:
{question}

Does the latest question require conversation history?

Return ONLY true or false.
"""

    try:

        llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0,
            api_key=os.getenv("GROQ_API_KEY"),
        )

        result = llm.invoke(prompt).content.strip().lower()

        return result == "true"

    except Exception as e:

        print(f"History classification error: {e}")

        return False

def rewrite_query(query, chat_history):

    # Decide whether previous conversation is needed
    use_history = needs_history(
        query,
        chat_history
    )

    print(f"History used for rewriting: {use_history}")

    if use_history:

        history_text = "\n".join(
            f"{message['role']}: {message['content']}"
            for message in chat_history
        )

        prompt = f"""
You are a query rewriting assistant for a Retrieval-Augmented Generation system.

Rewrite the user's latest question into a clear, standalone search query.

Use the conversation history ONLY to resolve unclear references
such as it, its, they, them, this, that, above, or previous.

Do NOT answer the question.
Do NOT add facts that are not present in the conversation.
Do NOT introduce unrelated topics from the conversation history.

Conversation history:
{history_text}

Latest user question:
{query}

Return ONLY the rewritten search query.
"""

    else:

        prompt = f"""
You are a query rewriting assistant for a Retrieval-Augmented Generation system.

Rewrite the user's question into a clear, standalone search query.

The question is already standalone, so DO NOT use conversation history.

Do NOT answer the question.
Do NOT add any topic, entity, or fact that is not present in the question.
Do NOT introduce information from previous conversation.

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

        # Keep rewritten query on one line
        rewritten_query = rewritten_query.replace("\n", " ").strip()

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
    print(f"Rewritten query: {rewritten_query}\n")

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
        query = input("Enter your question (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        if not query.strip():
            print("Question cannot be empty.")
            continue

        answer, metadatas, _, _ = generate_answer(query, chat_history)
        print(answer)

if __name__ == "__main__":
    main()
