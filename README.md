# RAG Implementation in Python

![Python](https://img.shields.io/badge/Python-3.12-blue)
![ChromaDB](https://img.shields.io/badge/Vector%20DB-ChromaDB-green)
![Sentence Transformers](https://img.shields.io/badge/Embeddings-all--MiniLM--L6--v2-orange)
![Groq](https://img.shields.io/badge/LLM-GPT--OSS--120B-red)
![Status](https://img.shields.io/badge/Status-Portfolio%20Project-success)

---

# Overview

This project demonstrates an end-to-end **Retrieval-Augmented Generation (RAG)** pipeline built using Python.

The application loads `.txt` and `.pdf` documents, splits them into overlapping chunks, generates vector embeddings using Sentence Transformers, stores them in ChromaDB, retrieves relevant chunks using semantic search and cross-encoder reranking, and generates grounded answers using the Groq API.

The project is designed as a modular Retrieval-Augmented Generation application that demonstrates document ingestion, semantic retrieval, query rewriting, reranking, grounded answer generation, guardrails, evaluation, and a Streamlit web interface.

---

# Features

* Supports `.txt` and `.pdf` documents.
* Automatic document loading.
* Configurable chunk size and overlap.
* Metadata generation for every chunk.
* Sentence Transformer embeddings using `all-MiniLM-L6-v2`.
* Persistent vector storage using ChromaDB.
* Semantic similarity search.
* Top-K retrieval.
* Query rewriting for improved retrieval.
* Cross-encoder reranking.
* Context-aware answer generation using Groq (`GPT-OSS-120B`).
* Source information including filename, page number, and chunk number.
* Guardrail for unsupported questions.
* Retrieval evaluation and chunking comparison.
* Guardrail testing using assertions.
* Streamlit web interface.
* Modular project architecture.

---

# Testing

The project was tested on Windows using Python 3.12.

## Commands Executed

```bash
python main.py
python embed_store.py
python retriever.py
python rag_answer.py
streamlit run app.py
python retrieval/compare_chunking.py
python retrieval/evaluate_retrieval.py
python evaluation/test_guardrail.py
python evaluation/evaluate.py
```

Evaluation outputs include:

* `chunking_comparison_results.csv`
* `chunking_comparison_summary.md`
* `retrieval_evaluation.csv`
* `retrieval_metrics_summary.csv`
* `evaluation_results.csv`

---

# Test Cases

## Test 1 – Upload Document

**Input:** Python Notes PDF

**Expected Result:**

* Document uploads successfully.
* Previous uploaded document is removed.
* Current document is displayed.

**Status:** ✅ Pass

---

## Test 2 – Document Processing

**Expected Result:**

* Pages extracted successfully.
* Text chunked correctly.
* Embeddings generated.
* ChromaDB updated.

**Status:** ✅ Pass

---

## Test 3 – Retrieval Pipeline

**Expected Result:**

* Relevant chunks retrieved.
* Source filename displayed.
* Page number displayed.
* Chunk number displayed.
* Retrieved chunks are available for inspection.

**Status:** ✅ Pass

---

## Test 4 – Question Answering

**Expected Result:**

Groq generates a grounded answer from the retrieved context.

**Status:** ✅ Pass

Verified:

* Answer generation from retrieved context.
* Answers remain grounded in uploaded documents.
* Unsupported questions trigger the guardrail.
* Retrieved sources remain available when LLM/API generation is unavailable.

---

## Test 5 – Reset Session

**Expected Result:**

* Documents removed.
* ChromaDB collection cleared.
* Current document state reset.
* User can upload a new document.

**Status:** ✅ Pass

---

## Notes

When the Groq API is unavailable, the application:

* Shows an informative error message.
* Displays retrieved sources.
* Displays retrieved chunks.
* Allows verification of the retrieval pipeline without an LLM response.

---

# Tech Stack

* Python 3.12
* Sentence Transformers
* ChromaDB
* Groq (`GPT-OSS-120B`)
* Streamlit
* PyPDF
* python-dotenv

---

# Project Structure

```text
RAG-Implementation-Python/

│
├── retrieval/
│   ├── compare_chunking.py
│   ├── evaluate_retrieval.py
│   └── relevance_dataset.csv
│
├── evaluation/
│   ├── evaluate.py
│   ├── sample_dataset.py
│   ├── ragas_config.py
│   └── test_guardrail.py
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
├── chunking_comparison_results.csv
├── chunking_comparison_summary.md
├── retrieval_evaluation.csv
├── retrieval_metrics_summary.csv
├── evaluation_results.csv
│
├── output_chunks.json
├── requirements.txt
├── README.md
├── FINAL_PROJECT_REPORT.md
├── .env.example
└── .gitignore
```

Generated runtime folders such as `documents/` and `chroma_db/` are used locally by the application and are not required to be committed as source files.

---

# File Description

| File                 | Description                                                        |
| -------------------- | ------------------------------------------------------------------ |
| `document_loader.py` | Loads `.txt` and `.pdf` documents.                                 |
| `chunker.py`         | Splits documents into overlapping chunks and generates metadata.   |
| `main.py`            | Runs document loading and chunking.                                |
| `embed_store.py`     | Generates embeddings and stores them in ChromaDB.                  |
| `retriever.py`       | Retrieves and reranks relevant chunks.                             |
| `rag_answer.py`      | Handles query rewriting and grounded answer generation using Groq. |
| `app.py`             | Streamlit web interface.                                           |
| `test_loader.py`     | Basic document-loading tests.                                      |
| `retrieval/`         | Retrieval and chunking evaluation scripts and relevance dataset.   |
| `evaluation/`        | RAGAS and guardrail evaluation scripts.                            |

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
Query Rewriting
        │
        ▼
Semantic Retrieval
        │
        ▼
Cross-Encoder Reranking
        │
        ▼
Groq GPT-OSS-120B
        │
        ▼
Guardrail
        │
        ▼
Final Answer + Source Information
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/khushilunkad12/Phase2_Rag_Practice.git
```

```bash
cd Phase2_Rag_Practice
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Activate

**Windows Command Prompt**

```bash
venv\Scripts\activate
```

**Windows PowerShell**

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
GROQ_API_KEY=YOUR_GROQ_API_KEY_HERE
```

> The first installation may take several minutes because Sentence Transformers downloads the required embedding model and PyTorch dependencies.

---

# Quick Start

After installing the dependencies and configuring the `.env` file, run:

```bash
pip install -r requirements.txt
python main.py
streamlit run app.py

# Project Workflow

## Step 1 — Load and Chunk Documents

```bash
python main.py
```

This step:

* Loads documents.
* Extracts text.
* Splits documents into chunks.
* Generates metadata.
* Saves chunks into `output_chunks.json`.

---

## Step 2 — Generate Embeddings

```bash
python embed_store.py
```

This step:

* Reads `output_chunks.json`.
* Generates embeddings using `all-MiniLM-L6-v2`.
* Stores embeddings and metadata inside ChromaDB.

---

## Step 3 — Test Semantic Retrieval

```bash
python retriever.py
```

The retrieval pipeline performs semantic search and uses a cross-encoder to rerank the retrieved chunks.

---

## Step 4 — Generate Final RAG Answer

```bash
python rag_answer.py
```

Pipeline:

* User enters a question.
* Query may be rewritten for retrieval.
* Relevant chunks are retrieved.
* Retrieved chunks are reranked.
* Retrieved context is passed to Groq.
* Groq generates a grounded answer.
* Source information is displayed.

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
* View retrieved sources.
* View retrieved chunks.
* Reset the current session.

---

# Supported Documents

* `.txt`
* `.pdf`

---

# Embedding Model

**Sentence Transformer**

```text
all-MiniLM-L6-v2
```

**Embedding Dimension**

```text
384
```

---

# Vector Database

**Database**

```text
ChromaDB
```

**Persistent Storage**

```text
chroma_db/
```

**Collection Name**

```text
rag_documents
```

---

# Evaluation

The project includes retrieval and RAG evaluation components.

### Retrieval Evaluation

Retrieval quality is evaluated using:

* Relevance labels.
* Precision@3.
* Mean Reciprocal Rank (MRR).
* Best relevant chunk rank.
* Relevant chunks found.

### Chunking Comparison

Different chunking strategies are compared using:

```text
chunking_comparison_results.csv
chunking_comparison_summary.md
```

### RAG Evaluation

RAGAS evaluation results are stored in:

```text
evaluation_results.csv
```

---

# Example Query

```text
What is Retrieval-Augmented Generation?
```

Example answer:

```text
Retrieval-Augmented Generation (RAG) improves Large Language Models by retrieving relevant information from external documents before generating an answer. This allows responses to remain grounded in the uploaded knowledge base instead of relying only on the model's internal knowledge.
```

---

# Multiple Document Workflow

1. Upload one or more PDF/TXT files.
2. Click **Process Documents**.
3. The application reads the uploaded documents.
4. Documents are split into chunks.
5. Embeddings are generated.
6. Embeddings are stored in ChromaDB.
7. Ask questions about the uploaded documents.
8. Retrieved sources display the file name, page number, and chunk number.
9. Click **Reset Session** to remove the current documents and embeddings.

---

# Screenshots

Application screenshots demonstrating:

* Document upload and processing.
* Generated answers.
* Retrieved sources.
* Retrieved chunks.

Evidence and screenshots are maintained as part of the project submission material.

---

# What I Learned

Through this project I gained practical experience with:

* Retrieval-Augmented Generation (RAG)
* Sentence Transformer embeddings
* ChromaDB vector databases
* Semantic similarity search
* Query rewriting
* Cross-encoder reranking
* Prompt engineering
* Groq API integration
* Streamlit application development
* Retrieval evaluation
* Guardrail testing
* Modular Python project architecture

---

# Requirements

* Python 3.12
* Internet connection for Groq API and initial model downloads

> The first execution may take a few minutes because the Sentence Transformer model is downloaded automatically.

---

# Future Improvements

Possible future improvements include:

* DOCX document support.
* Adaptive chunking based on document structure.
* Hybrid keyword + vector search.
* Additional embedding model experiments.
* Improved hallucination detection.
* More extensive evaluation datasets.
* Improved logging and error handling.
* Docker deployment.
* Further retrieval latency optimization.

---

# Author

**Khushi Lunkad**

GitHub: https://github.com/khushilunkad12

---

