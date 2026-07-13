
import os
import shutil
import chromadb
import streamlit as st

from main import process_documents
from embed_store import store_embeddings
from rag_answer import generate_answer

CHROMA_DB_PATH = "chroma_db"
COLLECTION_NAME = "rag_documents"

def reset_chroma_collection():
    try:
        client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
        try:
            client.delete_collection(COLLECTION_NAME)
        except Exception:
            pass
    except Exception as error:
        st.warning(f"ChromaDB reset warning: {error}")

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="RAG Document QA",
    page_icon="📄",
    layout="wide"
)

# ==========================================
# Session State
# ==========================================

if "document_ready" not in st.session_state:
    st.session_state.document_ready = False

if "current_document" not in st.session_state:
    st.session_state.current_document = None

# ==========================================
# Title
# ==========================================

st.title("📄 RAG Document Question Answering")

st.write(
    "Upload a document, process it, and ask questions using Retrieval-Augmented Generation (RAG)."
)

st.divider()

# ==========================================
# Upload Document
# ==========================================

uploaded_file = st.file_uploader(
    "Choose a document",
    type=["txt", "pdf"]
)

if uploaded_file is not None:
    if st.session_state.current_document != uploaded_file.name:

        if os.path.exists("documents"):
            shutil.rmtree("documents")

        os.makedirs("documents", exist_ok=True)

        file_path = os.path.join("documents", uploaded_file.name)

        with open(file_path, "wb") as file:
            file.write(uploaded_file.getbuffer())

        st.session_state.document_ready = False
        st.success(f"{uploaded_file.name} uploaded successfully!")

        with st.spinner("Processing document..."):
            reset_chroma_collection()

            stats = process_documents()

            if stats is None:
                st.error("Failed to process document.")
                st.session_state.current_document = None
                st.session_state.document_ready = False
                st.stop()

            store_embeddings()

        st.session_state.current_document = uploaded_file.name
        st.session_state.document_ready = True

        st.success("✅ Document processed successfully!")

        st.info(
            f"""
📄 *File:* {uploaded_file.name}

📑 *Pages:* {stats['pages']}

🧩 *Chunks Created:* {stats['chunks']}
"""
        )

st.divider()

# ==========================================
# Current Document
# ==========================================

st.subheader("📂 Current Document")

if st.session_state.current_document:
    st.write(f"*{st.session_state.current_document}*")
else:
    st.info("No document uploaded.")

st.divider()

# ==========================================
# Reset Session
# ==========================================

if st.button("🗑️ Reset Session"):
    if os.path.exists("documents"):
        shutil.rmtree("documents")

    if os.path.exists("output_chunks.json"):
        os.remove("output_chunks.json")

    reset_chroma_collection()

    st.session_state.current_document = None
    st.session_state.document_ready = False

    st.success("Session cleared successfully.")
    st.rerun()

st.divider()

# ==========================================
# Ask Question
# ==========================================

if not st.session_state.document_ready:
    st.info("Please upload and process a document before asking questions.")

else:
    question = st.text_input("Ask a question about your document")

    if st.button("🔍 Ask Question"):
        if not question.strip():
            st.warning("Please enter a question.")

        else:
            with st.spinner("Generating answer..."):
                answer, sources, chunks, distances = generate_answer(question)

            st.success("Answer generated!")

            if answer.strip() == "Not enough information in the uploaded documents.":
                st.warning(
                    "⚠️ The uploaded documents do not contain enough information to answer this question."
                )

            elif answer.strip() == "LLM/API unavailable. Retrieved context is shown below.":
                st.error("⚠️ Gemini service is currently unavailable.")
                st.info(
                    """
The language model is currently unavailable, for example due to API quota,
network issue, or service availability.

The retrieved sources and document chunks are still shown below so you can
verify that the retrieval pipeline is working correctly.
"""
                )

            else:
                st.subheader("🤖 Answer")
                st.write(answer)

            st.subheader("📚 Sources")

            for index, source in enumerate(sources, start=1):
                st.write(
                    f"{index}. {source['source']} "
                    f"(Page {source.get('page', 'N/A')}, "
                    f"Chunk {source['chunk_index']})"
                )

            st.subheader("📄 Retrieved Chunks")

            for i in range(len(chunks)):
                with st.expander(
                    f"Retrieved Chunk {i + 1} (Distance: {distances[i]:.4f})",
                    expanded=False
                ):
                    st.write(f"*Source:* {sources[i]['source']}")
                    st.write(f"*Page:* {sources[i].get('page', 'N/A')}")
                    st.write(f"*Chunk Index:* {sources[i]['chunk_index']}")
                    st.write(chunks[i])


