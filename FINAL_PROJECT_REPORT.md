# Final Project Report — RAG Practice Project

## 1. Objective

The objective of this project was to build and evaluate a Retrieval-Augmented Generation (RAG) system that answers user questions using information available in uploaded documents.

The system combines document chunking, embeddings, ChromaDB vector search, query rewriting, cross-encoder reranking, answer generation, guardrails, and retrieval evaluation to improve answer relevance and reduce unsupported responses.

## 2. Architecture Flow

The complete RAG pipeline follows:

**Document Upload → Chunking → Embeddings → ChromaDB → Query Rewriting → Retrieval → Cross-Encoder Reranking → Answer Generation → Guardrail → Evaluation**

### 2.1 Document Upload

Documents are uploaded to the system and processed to create the knowledge base used for answering questions.

### 2.2 Chunking

Documents are divided into smaller overlapping chunks so that relevant sections can be retrieved efficiently.

### 2.3 Embeddings

Each document chunk is converted into a vector representation using the Sentence Transformer embedding model `all-MiniLM-L6-v2`.

### 2.4 ChromaDB

The generated embeddings, document chunks, and metadata are stored in ChromaDB, which is used as the persistent vector database.

### 2.5 Query Rewriting

The user's question can be rewritten into a cleaner and more retrieval-friendly query before searching the vector database.

Example:

**Original query:** What is Python?

**Rewritten query:** Python

### 2.6 Retrieval

The rewritten query is converted into an embedding and used to retrieve relevant chunks from ChromaDB.

### 2.7 Cross-Encoder Reranking

The initially retrieved chunks are passed through a cross-encoder reranker. The reranker evaluates the relevance between the query and retrieved chunks and reorders them accordingly.

### 2.8 Answer Generation

The highest-ranked retrieved context is provided to the answer-generation component, which generates a grounded answer using the Groq API and the configured `GPT-OSS-120B` model.

### 2.9 Guardrail

A guardrail prevents the system from answering questions when sufficient information is not available in the uploaded documents.

For unsupported questions, the system returns:

```text
Not enough information in the uploaded documents.
```

### 2.10 Evaluation

The project contains retrieval, chunking, RAGAS, and guardrail evaluation components to verify retrieval quality and supported/unsupported question handling.

---

## 3. Features Completed

The following features have been implemented:

* Document ingestion
* PDF and TXT support
* Document chunking
* Embedding generation
* ChromaDB vector storage
* Query rewriting
* Vector retrieval
* Cross-encoder reranking
* RAG-based answer generation
* Unsupported-question guardrail
* Retrieval evaluation
* Chunking comparison
* Relevance dataset
* Retrieval metrics
* RAGAS evaluation
* Guardrail testing
* Streamlit web interface

---

## 4. Evaluation Approach

The evaluation was performed mainly in three areas.

### 4.1 Retrieval Evaluation

Different chunking and retrieval configurations were compared to determine how effectively relevant information could be retrieved.

The evaluation work includes:

```text
retrieval/compare_chunking.py
retrieval/evaluate_retrieval.py
retrieval/relevance_dataset.csv
chunking_comparison_results.csv
chunking_comparison_summary.md
retrieval_evaluation.csv
retrieval_metrics_summary.csv
```

The relevance dataset was used to evaluate whether retrieved chunks were relevant to the user's query.

Metrics include:

* Precision@3
* Mean Reciprocal Rank (MRR)
* Best relevant chunk rank
* Relevant chunks found

### 4.2 RAGAS Evaluation

RAGAS evaluation was performed to assess RAG response and retrieval quality using the configured evaluation dataset.

The evaluation results are stored in:

```text
evaluation_results.csv
```

### 4.3 Guardrail Evaluation

The guardrail was tested using two types of questions:

1. A question that the system should be able to answer from the uploaded document.
2. A question whose information is not available in the uploaded document.

This verifies both normal RAG behavior and unsupported-question handling.

---

## 5. Guardrail Test Results

The guardrail test was executed using:

```bash
python evaluation/test_guardrail.py
```

### Supported Question

**Original Query:**

```text
What is Python?
```

**Rewritten Query:**

```text
Python
```

**Answer:**

```text
Python is a high-level, interpreted, general-purpose programming language
that emphasizes simplicity and readability and is designed to be easy to
learn and use.
```

**Result:**

```text
✓ Supported question test passed
```

### Unsupported Question

**Original Query:**

```text
What is the capital of France?
```

**Rewritten Query:**

```text
capital of France
```

**Answer:**

```text
Not enough information in the uploaded documents.
```

**Result:**

```text
✓ Unsupported question test passed
```

### Overall Result

```text
============================================================
ALL GUARDRAIL TESTS PASSED
============================================================
```

The guardrail successfully passed both supported and unsupported question tests.

---

## 6. Commands Tested

### Application

```bash
python main.py
python embed_store.py
streamlit run app.py
```

### Retrieval and Evaluation

```bash
python retrieval/compare_chunking.py
python retrieval/evaluate_retrieval.py
python evaluation/evaluate.py
```

### Guardrail

```bash
python evaluation/test_guardrail.py
```

### Python Compilation Check

```bash
python -m py_compile app.py
```

The application and evaluation scripts were executed during final testing.

---

## 7. Proof / Screenshots

### 7.1 Guardrail Test Output

Evidence is maintained in the project submission material.

### 7.2 Application UI

The Streamlit application was successfully tested with a PDF document.

The UI demonstrated:

* Document upload
* Document processing
* Generated answer
* Source information
* Retrieved chunks

### 7.3 Retrieval Evaluation

Retrieval evaluation evidence is maintained through the generated CSV files:

```text
chunking_comparison_results.csv
retrieval_evaluation.csv
retrieval_metrics_summary.csv
evaluation_results.csv
```

---

## 8. Limitations

The current implementation has the following limitations:

* Answer quality depends on the quality and coverage of uploaded documents.
* Poor chunking can negatively affect retrieval quality.
* Query rewriting may occasionally remove useful context.
* Vector similarity search may retrieve semantically similar but less relevant content.
* Cross-encoder reranking adds additional processing time.
* The system cannot reliably answer questions when the required information is absent from the document collection.
* The current evaluation dataset can be expanded for more comprehensive testing.
* External embedding/model downloads can be affected by network availability and Hugging Face rate limits.

---

## 9. Future Improvements

Possible future improvements include:

* Adaptive chunking based on document structure.
* Hybrid keyword + vector search.
* Additional embedding model experiments.
* Comparison of additional reranking models.
* Improved hallucination detection.
* More extensive evaluation datasets.
* Stronger retrieval-confidence thresholds for guardrails.
* Additional document formats.
* Improved logging and error handling.
* Further optimization of retrieval and reranking latency.
* Docker deployment.
* Automated regression testing for the complete RAG pipeline.

---

## 10. Final Project Status

**Status: COMPLETED / READY FOR FINAL REVIEW**

The core RAG pipeline has been implemented and tested. The project includes:

* Document processing
* Chunking
* Embeddings
* ChromaDB retrieval
* Query rewriting
* Cross-encoder reranking
* Groq-based answer generation
* Unsupported-question guardrail
* Retrieval evaluation
* Chunking comparison
* RAGAS evaluation
* Guardrail testing
* Streamlit application

The application was successfully tested end-to-end with document upload, processing, retrieval, reranking, answer generation, source display, and retrieved-chunk inspection.

The guardrail successfully passed both supported and unsupported question tests.

The project is ready for final review and submission.
