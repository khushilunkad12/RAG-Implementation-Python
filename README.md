# RAG Practice - End-to-End Retrieval Augmented Generation Pipeline

This project demonstrates an end-to-end Retrieval-Augmented Generation (RAG) pipeline using Python.

The pipeline performs:

- Document Loading
- Text Chunking with Overlap
- Metadata Generation
- Sentence Transformer Embeddings
- ChromaDB Vector Storage
- Semantic Retrieval
- Gemini 2.5 Flash Answer Generation

---

# Tech Stack

- Python 3.12
- Sentence Transformers
- ChromaDB
- Google Gemini 2.5 Flash
- python-dotenv

---

# Project Structure

```
Phase2_Rag_Practice/
│
├── data/
│   └── sample.txt          # Sample document used for RAG.
│
├── loader.py               # Loads text documents from the data folder.
│
├── chunker.py              # Splits documents into overlapping text chunks and generates metadata.
│
├── main.py                 # Executes the document loading and chunking pipeline, producing output_chunks.json.
│
├── embed_store.py          # Generates embeddings for each chunk using Sentence Transformers and stores them in ChromaDB.
│
├── retriever.py            # Converts the user's query into an embedding and retrieves the most relevant chunks from ChromaDB.
│
├── rag_answer.py           # Complete RAG pipeline: retrieves relevant chunks and generates an answer using Gemini.
│
├── output_chunks.json      # Generated file containing all text chunks and metadata. (Created after running main.py)
│
├── chroma_db/              # Persistent ChromaDB vector database storing document embeddings. (Created after running embed_store.py)
│
├── requirements.txt        # Project dependencies.
│
├── .env.example            # Example environment variable file for Gemini API configuration.
│
├── .gitignore              # Specifies files and folders ignored by Git.
│
├── README.md               # Project documentation.
│
└── venv/                   # Python virtual environment (not tracked by Git).
```
---
# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/khushilunkad12/RAG-Implementation-Python.git
```

```bash
cd RAG-Implementation-Python
```

---

## 2. Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

Command Prompt

```bash
venv\Scripts\activate
```

PowerShell

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

.\venv\Scripts\Activate.ps1
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a file named

```
.env
```

Add your Gemini API Key

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

# Project Workflow

The project should be executed in the following order.

---

## Step 1 — Chunk Documents

Run

```bash
python main.py
```

This will

- Load documents
- Create overlapping chunks
- Generate metadata
- Save all chunks into

```
output_chunks.json
```

---

## Step 2 — Generate Embeddings

Run

```bash
python embed_store.py
```

This will

- Read `output_chunks.json`
- Generate embeddings using

```
all-MiniLM-L6-v2
```

- Store vectors inside

```
chroma_db/
```

using ChromaDB Persistent Storage.

---

## Step 3 — Test Semantic Retrieval

Run

```bash
python retriever.py
```

Enter a question.

Example

```
What is RAG?
```

The program retrieves the Top-3 most relevant chunks based on vector similarity.

---

## Step 4 — Generate Final RAG Answer

Run

```bash
python rag_answer.py
```

Flow

- User enters a question
- Query embedding is generated
- Top-3 relevant chunks are retrieved
- Retrieved chunks become context
- Gemini 2.5 Flash generates the final answer using only the retrieved context

---

# Embedding Model

Sentence Transformer

```
all-MiniLM-L6-v2
```

Embedding Dimension

```
384
```

---

# Vector Database

ChromaDB

Persistent Storage

```
chroma_db/
```

Collection Name

```
rag_documents
```

---

# Example Query

```
What is RAG?
```

Retrieved Context

- Chunk 2
- Chunk 3
- Chunk 1

Final Answer

```
Retrieval-Augmented Generation (RAG) improves LLM responses by retrieving relevant information from external documents before generating an answer. Instead of relying only on the model's internal knowledge, RAG searches through documents, retrieves useful chunks, and provides them as context.
```

---

# Features

- Document Loader
- Configurable Chunk Size
- Overlapping Chunk Generation
- Metadata Storage
- Sentence Transformer Embeddings
- Persistent ChromaDB Storage
- Semantic Similarity Search
- Retrieval-Augmented Generation
- Gemini API Integration
- Environment Variable Support
- Modular Project Structure

---

# Requirements

- Python 3.12
- Internet connection (required for Gemini API)

---

# Future Improvements

- PDF Document Support
- Multiple Document Upload
- Web Interface (Streamlit)
- Conversation Memory
- Source Citation in Answers
- Hybrid Search (Keyword + Vector)
- Reranking
- Local LLM Support
- Docker Deployment

---

# Author

Khushi Lunkad