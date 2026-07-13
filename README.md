# RAG Implementation in Python

![Python](https://img.shields.io/badge/Python-3.12-blue)
![ChromaDB](https://img.shields.io/badge/Vector%20DB-ChromaDB-green)
![Sentence Transformers](https://img.shields.io/badge/Embeddings-all--MiniLM--L6--v2-orange)
![Gemini](https://img.shields.io/badge/LLM-Gemini%202.5%20Flash-red)
![Status](https://img.shields.io/badge/Status-Portfolio%20Project-success)

---

# Overview

This project demonstrates an end-to-end **Retrieval-Augmented Generation (RAG)** pipeline built using Python.

The application loads `.txt` and `.pdf` documents, splits them into overlapping chunks, generates vector embeddings using Sentence Transformers, stores them in ChromaDB, retrieves the most relevant chunks using semantic search, and generates context-aware answers using Google's Gemini API.

The project is designed as a modular Retrieval-Augmented Generation application that demonstrates document ingestion, semantic retrieval, and grounded answer generation through both a command-line interface and a Streamlit web application.

---

# Features

* Supports both `.txt` and `.pdf` documents.
* Automatic document loading.
* Configurable chunk size and overlap.
* Metadata generation for every chunk.
* Sentence Transformer embeddings (`all-MiniLM-L6-v2`).
* Persistent vector storage using ChromaDB.
* Semantic similarity search.
* Retrieval of Top-K relevant chunks.
* Context-aware answer generation using Gemini 2.5 Flash.
* Source citations for every generated answer.
* Streamlit web interface.
* Modular project architecture.
* Basic automated testing using assertions.

---

## Testing

The project was tested on Windows using Python 3.12.

### Commands Executed

```bash
python main.py
python embed_store.py
python retriever.py
python rag_answer.py
streamlit run app.py
```

---

### Test Cases

#### Test 1 – Upload Document
**Input:** Python Notes PDF

**Expected Result:**
- Document uploads successfully.
- Previous document is removed.
- Current document is displayed.

**Status:** ✅ Pass

---

#### Test 2 – Document Processing

**Expected Result:**
- Pages extracted successfully.
- Text chunked correctly.
- Embeddings generated.
- ChromaDB updated.

**Status:** ✅ Pass

---

#### Test 3 – Retrieval Pipeline

**Expected Result:**
- Relevant chunks retrieved.
- Source filename displayed.
- Page number displayed.
- Chunk number displayed.

**Status:** ✅ Pass

---

#### Test 4 – Question Answering

**Expected Result:**
Gemini generates an answer from retrieved context.

**Status:** ⏳ Pending Retest

Reason:
Gemini API quota was exceeded during testing. Retrieval pipeline was verified successfully.

---

#### Test 5 – Reset Session

**Expected Result:**
- Documents removed.
- Chroma collection cleared.
- Current document reset.
- User can upload a new document.

**Status:** ✅ Pass

---

### Notes

When Gemini API is unavailable, the application:

- Shows an informative error message.
- Displays retrieved sources.
- Displays retrieved chunks.
- Allows verification of the retrieval pipeline without LLM response.
# Tech Stack

* Python 3.12
* Sentence Transformers
* ChromaDB
* Google Gemini 2.5 Flash
* Streamlit
* PyPDF
* python-dotenv

---

# Project Structure

```text
RAG-Implementation-Python/

│
├── documents/
│
├── chroma_db/
│
├── document_loader.py
├── chunker.py
├── main.py
├── embed_store.py
├── retriever.py
├── rag_answer.py
├── app.py
├── test_loader.py
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

| File                 | Description                                                      |
| -------------------- | ---------------------------------------------------------------- |
| `document_loader.py` | Loads `.txt` and `.pdf` documents.                               |
| `chunker.py`         | Splits documents into overlapping chunks and generates metadata. |
| `main.py`            | Runs the document loading and chunking pipeline.                 |
| `embed_store.py`     | Generates embeddings and stores them in ChromaDB.                |
| `retriever.py`       | Retrieves the most relevant chunks using semantic search.        |
| `rag_answer.py`      | Generates grounded answers using Gemini.                         |
| `app.py`             | Streamlit web interface.                                         |
| `test_loader.py`     | Basic automated tests.                                           |
| `documents/`         | Source documents.                                                |
| `chroma_db/`         | Persistent vector database.                                      |
| `output_chunks.json` | Generated document chunks.                                       |

---

# RAG Architecture

```text
User Uploads Document
        │
        ▼
Document Loader
        │
        ▼
Text Chunking
        │
        ▼
Embedding Generation
        │
        ▼
ChromaDB Vector Store
        │
        ▼
Semantic Retrieval
        │
        ▼
Gemini 2.5 Flash
        │
        ▼
Final Answer + Source Citations
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

**Windows (Command Prompt)**

```bash
venv\Scripts\activate
```

**Windows (PowerShell)**

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

---

# Project Workflow

## Step 1 — Load and Chunk Documents

```bash
python main.py
```

This step:

* Loads all documents
* Splits documents into chunks
* Generates metadata
* Saves chunks into `output_chunks.json`

---

## Step 2 — Generate Embeddings

```bash
python embed_store.py
```

This step:

* Reads `output_chunks.json`
* Generates embeddings using Sentence Transformers
* Stores embeddings inside ChromaDB

---

## Step 3 — Test Semantic Retrieval

```bash
python retriever.py
```

Example:

```text
What is RAG?
```

The program retrieves the Top-3 most relevant chunks.

---

## Step 4 — Generate Final RAG Answer

```bash
python rag_answer.py
```

Pipeline:

* User enters a question
* Relevant chunks are retrieved
* Retrieved chunks become context
* Gemini generates a grounded answer
* Sources are displayed

---

## Step 5 — Launch the Web Application

```bash
streamlit run app.py
```

Using the Streamlit application you can:

* Upload `.txt` and `.pdf` documents.
* Process documents.
* Ask questions.
* View generated answers.
* View retrieved chunks.
* View source citations.

---

# Supported Documents

* `.txt`
* `.pdf`

---

# Embedding Model

Sentence Transformer

```text
all-MiniLM-L6-v2
```

Embedding Dimension

```text
384
```

---

# Vector Database

Database

```text
ChromaDB
```

Persistent Storage

```text
chroma_db/
```

Collection Name

```text
rag_documents
```

---

# Example Query

```text
What is Retrieval-Augmented Generation?
```

Example Answer

```text
Retrieval-Augmented Generation (RAG) improves Large Language Models by retrieving relevant information from external documents before generating an answer. This allows responses to remain grounded in the uploaded knowledge base instead of relying only on the model's internal knowledge.
```

---

# Screenshots

## Home Page

*Add screenshot here.*

## Generated Answer

*Add screenshot here.*

## Retrieved Chunks

*Add screenshot here.*

---

# What I Learned

Through this project I gained practical experience with:

* Retrieval-Augmented Generation (RAG)
* Sentence Transformer embeddings
* ChromaDB vector databases
* Semantic similarity search
* Prompt engineering
* Google Gemini API integration
* Streamlit application development
* Modular Python project architecture
* Basic software testing

---

# Requirements

* Python 3.12
* Internet connection (required for Gemini API)

> **Note:** The first execution may take a few minutes because the Sentence Transformer model is downloaded automatically.

---

# Future Improvements

* DOCX document support
* Token-based chunking
* Hybrid search (Keyword + Vector)
* Retrieval reranking
* Conversation memory
* RAG evaluation metrics
* Local LLM support
* Docker deployment

---

# Author

**Khushi Lukkad**

GitHub: https://github.com/khushilunkad12
