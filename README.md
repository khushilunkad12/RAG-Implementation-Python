# RAG Implementation in Python

![Python](https://img.shields.io/badge/Python-3.12-blue)
![ChromaDB](https://img.shields.io/badge/Vector%20DB-ChromaDB-green)
![Sentence Transformers](https://img.shields.io/badge/Embeddings-all--MiniLM--L6--v2-orange)
![Gemini](https://img.shields.io/badge/LLM-Gemini%202.5%20Flash-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

# Overview

This project demonstrates an end-to-end **Retrieval-Augmented Generation (RAG)** pipeline built using Python.

The application loads multiple documents, splits them into overlapping chunks, generates vector embeddings using Sentence Transformers, stores them in ChromaDB, retrieves the most relevant chunks through semantic search, and finally generates context-aware answers using Google's Gemini API.

The project is designed as a modular learning implementation of a modern RAG architecture.

---

# Features

- Load multiple `.txt` documents automatically from the `documents/` folder.
- Configurable chunk size and overlap.
- Metadata generation for every chunk.
- Sentence Transformer embeddings.
- Persistent vector storage using ChromaDB.
- Semantic similarity search.
- Retrieval of Top-K relevant chunks.
- Context-aware answer generation using Gemini 2.5 Flash.
- Modular project architecture.
- Easy to extend with additional document types.

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
RAG-Implementation-Python/

│
├── documents/
│   ├── sample.txt
│   └── rag.txt
│
├── chroma_db/
│
├── document_loader.py
├── chunker.py
├── main.py
├── embed_store.py
├── retriever.py
├── rag_answer.py
│
├── output_chunks.json
│
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

# File Description

| File | Description |
|------|-------------|
| `document_loader.py` | Loads all text documents from the `documents/` folder. |
| `chunker.py` | Splits documents into overlapping chunks while generating metadata. |
| `main.py` | Runs the document loading and chunking pipeline, producing `output_chunks.json`. |
| `embed_store.py` | Generates embeddings using Sentence Transformers and stores them in ChromaDB. |
| `retriever.py` | Retrieves the most relevant chunks for a user query using semantic search. |
| `rag_answer.py` | Complete Retrieval-Augmented Generation pipeline using Gemini. |
| `documents/` | Folder containing source documents. |
| `chroma_db/` | Persistent vector database. |
| `output_chunks.json` | Generated chunked representation of all processed documents. |

---

# RAG Pipeline

```
                +----------------------+
                |   documents/ folder  |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | document_loader.py   |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |    chunker.py        |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | output_chunks.json   |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |   embed_store.py     |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |      ChromaDB        |
                +----------+-----------+
                           |
                     User Query
                           |
                           v
                +----------------------+
                |    retriever.py      |
                +----------+-----------+
                           |
                    Retrieved Chunks
                           |
                           v
                +----------------------+
                |    rag_answer.py     |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |   Gemini 2.5 Flash   |
                +----------+-----------+
                           |
                           v
                     Final Answer
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

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Activate

**Command Prompt**

```bash
venv\Scripts\activate
```

**PowerShell**

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

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

You can use the provided `.env.example` as a reference.

---

# Project Workflow

## Step 1 — Load and Chunk Documents

```bash
python main.py
```

This step:

- Loads all documents from `documents/`
- Splits them into overlapping chunks
- Generates metadata
- Saves the result as `output_chunks.json`

---

## Step 2 — Generate Embeddings

```bash
python embed_store.py
```

This step:

- Reads `output_chunks.json`
- Generates embeddings using `all-MiniLM-L6-v2`
- Stores embeddings in ChromaDB (`chroma_db/`)

---

## Step 3 — Test Semantic Retrieval

```bash
python retriever.py
```

Example query:

```
What is RAG?
```

The program retrieves the Top-3 most relevant chunks using semantic similarity.

---

## Step 4 — Generate Final RAG Answer

```bash
python rag_answer.py
```

Pipeline:

- User enters a question
- Query embedding is generated
- Top-3 relevant chunks are retrieved
- Retrieved chunks are combined into context
- Gemini generates the final grounded answer

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

**Database**

```
ChromaDB
```

**Persistent Storage**

```
chroma_db/
```

**Collection Name**

```
rag_documents
```

---

# Supported Documents

Current:

- `.txt`

Upcoming:

- `.pdf`

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

# Requirements

- Python 3.12
- Internet connection (required for Gemini API)

---

# Future Improvements

- PDF Document Support
- Automatic Duplicate Document Detection
- Multiple Document Upload
- Streamlit Web Interface
- Conversation Memory
- Source Citation in Answers
- Hybrid Search (Keyword + Vector)
- Reranking
- Local LLM Support
- Docker Deployment

---

# Author

**Khushi Lunkad**

GitHub: https://github.com/khushilunkad12