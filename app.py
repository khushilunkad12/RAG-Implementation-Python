
import os
import shutil

import chromadb
import streamlit as st

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

st.set_page_config(
    page_title="RAG Document QA",
    page_icon="📄",
    layout="wide",
)

if "document_ready" not in st.session_state:
    st.session_state.document_ready = False

if "current_documents" not in st.session_state:
    st.session_state.current_documents = []

st.title("📄 RAG Document Question Answering")

st.write(
    "Upload one or more documents, process them, and ask questions using Retrieval-Augmented Generation."
)

st.divider()

uploaded_files = st.file_uploader(
    "Choose one or more documents",
    type=["pdf", "txt"],
    accept_multiple_files=True,
)

if uploaded_files:
    st.success(f"{len(uploaded_files)} document(s) selected.")

    st.subheader("📂 Selected Documents")

    for file in uploaded_files:
        st.write(f"• {file.name}")

    if st.button("⚙️ Process Documents"):
        from main import process_documents
        from embed_store import store_embeddings

        if os.path.exists("documents"):
            shutil.rmtree("documents")

        os.makedirs("documents", exist_ok=True)

        for uploaded_file in uploaded_files:
            file_path = os.path.join("documents", uploaded_file.name)

            with open(file_path, "wb") as file:
                file.write(uploaded_file.getbuffer())

        st.session_state.document_ready = False

        with st.spinner("Processing documents..."):
            try:
                reset_chroma_collection()

                stats = process_documents()

                if stats is None:
                    st.error("Failed to process documents.")
                    st.session_state.current_documents = []
                    st.session_state.document_ready = False
                    st.stop()

                store_embeddings()

                st.session_state.current_documents = [
                    file.name for file in uploaded_files
                ]

                st.session_state.document_ready = True

                st.success("✅ Documents processed successfully!")

                uploaded_names = "\n".join(
                    f"• {file.name}" for file in uploaded_files
                )

                st.info(
                    f"""
📄 *Processed Documents*

{uploaded_names}

📑 *Total Pages:* {stats["pages"]}

🧩 *Total Chunks:* {stats["chunks"]}
"""
                )

            except Exception as error:
                st.error(f"Document processing failed: {error}")
                st.session_state.current_documents = []
                st.session_state.document_ready = False
                st.stop()

st.divider()

st.subheader("📂 Processed Documents")

if st.session_state.current_documents:
    for file in st.session_state.current_documents:
        st.write(f"• {file}")
else:
    st.info("No documents processed.")

st.divider()

if st.button("🗑️ Reset Session"):
    if os.path.exists("documents"):
        shutil.rmtree("documents")

    if os.path.exists("output_chunks.json"):
        os.remove("output_chunks.json")

    reset_chroma_collection()

    st.session_state.current_documents = []
    st.session_state.document_ready = False

    st.success("Session cleared successfully.")
    st.rerun()

st.divider()

if not st.session_state.document_ready:
    st.info("Please upload and process one or more documents before asking questions.")
else:
    question = st.text_input("Ask a question about your uploaded documents")
if st.button("🔍 Ask Question"):
        from rag_answer import generate_answer

        if not question.strip():
            st.warning("Please enter a question.")
        else:
            with st.spinner("Retrieving answer..."):
                try:
                    answer, sources, chunks, distances, rewritten_query = generate_answer(
                        question
                    )
                except Exception as error:
                    st.error(f"Answer generation failed: {error}")
                    st.stop()

            st.success("Answer generated!")

            if answer.strip() == "Not enough information in the uploaded documents.":
                st.warning(
                    "⚠️ The uploaded documents do not contain enough information to answer this question."
                )

            elif answer.strip() == "LLM/API unavailable.":
                st.error("⚠️ Groq service is currently unavailable.")

                st.info(
                    """
The language model is currently unavailable, for example due to API quota,
network issues, or service availability.

The retrieval pipeline has completed successfully.
Please verify the retrieved sources and chunks shown below.
"""
                )

            else:
                st.subheader("🤖 Answer")
                st.write(answer)

            st.subheader("📚 Sources")

            if len(sources) == 0:
                st.info("No relevant sources were found.")
            else:
                for index, source in enumerate(sources, start=1):
                    st.write(
                        f"{index}. "
                        f"{source['source']} "
                        f"(Page {source.get('page', 'N/A')}, "
                        f"Chunk {source['chunk_index']})"
                    )

            st.subheader("📄 Retrieved Chunks")

            if len(chunks) == 0:
                st.info("No chunks retrieved.")
            else:
                for i in range(len(chunks)):
                    with st.expander(
                        f"Retrieved Chunk {i + 1} "
                        f"(Distance: {distances[i]:.4f})",
                        expanded=False,
                    ):
                        st.write(f"*Source:* {sources[i]['source']}")
                        st.write(f"*Page:* {sources[i].get('page', 'N/A')}")
                        st.write(f"*Chunk Index:* {sources[i]['chunk_index']}")
                        st.markdown("---")
                        st.write(chunks[i])
 