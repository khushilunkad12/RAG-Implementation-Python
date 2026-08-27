Final Project Report — RAG Practice Project
1. Objective

The objective of this project was to build and evaluate a Retrieval-Augmented Generation (RAG) system that answers user questions using information available in uploaded documents.

The system combines document chunking, embeddings, ChromaDB vector search, query rewriting, cross-encoder reranking, answer generation, guardrails, and retrieval evaluation to improve answer relevance and reduce unsupported or hallucinated responses.

2. Architecture Flow

The complete RAG pipeline follows:

Document Upload → Chunking → Embeddings → ChromaDB → Query Rewriting → Retrieval → Cross-Encoder Reranking → Answer Generation → Guardrail → Evaluation

2.1 Document Upload

Documents are uploaded to the system and processed to create the knowledge base used for answering questions.

2.2 Chunking

Documents are divided into smaller chunks so that relevant sections can be retrieved efficiently.

2.3 Embeddings

Each document chunk is converted into a vector representation using an embedding model. These vectors represent the semantic meaning of the document content.

2.4 ChromaDB

The generated embeddings and corresponding document chunks are stored in ChromaDB, which is used as the vector database for similarity-based retrieval.

2.5 Query Rewriting

The user's question is rewritten into a cleaner and more retrieval-friendly query before searching the vector database.

Example:

Original query: What is Python?
Rewritten query: Python
2.6 Retrieval

The rewritten query is converted into an embedding and used to retrieve relevant chunks from ChromaDB.

2.7 Cross-Encoder Reranking

The initially retrieved chunks are passed through a cross-encoder reranker. The reranker evaluates the relevance between the query and retrieved chunks and reorders them accordingly.

2.8 Answer Generation

The highest-ranked relevant context is provided to the answer-generation component, which generates an answer based on the retrieved information.

2.9 Guardrail

A guardrail prevents the system from answering questions when sufficient information is not available in the uploaded documents.

For unsupported questions, the system returns:

Not enough information in the uploaded documents.

2.10 Evaluation

The system contains retrieval and guardrail evaluation scripts to verify retrieval quality and ensure that supported and unsupported questions are handled correctly.

3. Features Completed

The following features have been implemented:

Document ingestion
Document chunking
Embedding generation
ChromaDB vector storage
Query rewriting
Vector retrieval
Cross-encoder reranking
RAG-based answer generation
Unsupported-question guardrail
Retrieval evaluation
Chunking comparison
Relevance dataset
Retrieval metrics
Guardrail testing
4. Evaluation Approach

The evaluation was performed mainly in two areas.

4.1 Retrieval Evaluation

Different chunking and retrieval configurations were compared to determine how effectively relevant information could be retrieved.

The evaluation work includes:

retrieval/compare_chunking.py
retrieval/evaluate_retrieval.py
retrieval/relevance_dataset.csv
chunking_comparison_results.csv
chunking_comparison_summary.md
retrieval_evaluation.csv
retrieval_metrics_summary.csv

A relevance dataset was used to evaluate whether retrieved chunks were relevant to the user's query.

4.2 Guardrail Evaluation

The guardrail was tested using two types of questions:

A question that the system should be able to answer.
A question whose information is not available in the uploaded documents.

This verifies both normal RAG behavior and unsupported-question handling.

5. Guardrail Test Results

The guardrail test was executed using:

python evaluation\test_guardrail.py
Supported Question

Original Query:

What is Python?

Rewritten Query:

Python

Answer:

Python is a high-level, interpreted, general-purpose programming language
that emphasizes simplicity and readability and is designed to be easy to
learn and use.

Result:

✓ Supported question test passed

Unsupported Question

Original Query:

What is the capital of France?

Rewritten Query:

capital of France

Answer:

Not enough information in the uploaded documents.

Result:

✓ Unsupported question test passed

Overall Result
============================================================
ALL GUARDRAIL TESTS PASSED
============================================================

The guardrail successfully passed both supported and unsupported question tests.

6. Commands Tested
Guardrail Test
python evaluation\test_guardrail.py
Python Compilation Check
python -m py_compile app.py

Retrieval and evaluation scripts were also executed during development for chunking comparison and retrieval evaluation.

7. Proof / Screenshots
7.1 Guardrail Test Output

Screenshot: https://drive.google.com/drive/folders/1yqM91Ci3in9wo9r-hSrnWo51j7mHI1Pu?usp=sharing


7.2 Application UI

Screenshot / Video: https://drive.google.com/drive/folders/1yqM91Ci3in9wo9r-hSrnWo51j7mHI1Pu?usp=sharing


7.3 Retrieval Evaluation

Evidence: https://drive.google.com/drive/folders/1yqM91Ci3in9wo9r-hSrnWo51j7mHI1Pu?usp=sharing


8. Limitations

The current implementation has the following limitations:

Answer quality depends on the quality and coverage of the uploaded documents.
Poor chunking can negatively affect retrieval quality.
Query rewriting may occasionally remove useful context.
Vector similarity search may retrieve semantically similar but less relevant content.
Cross-encoder reranking adds additional processing time.
The system cannot reliably answer questions when the required information is absent from the document collection.
The current evaluation dataset can be expanded for more comprehensive testing.
External embedding/model downloads can be affected by network availability and Hugging Face rate limits.

9. Future Improvements

Possible future improvements include:

Implement adaptive chunking based on document structure.
Expand the retrieval relevance dataset.
Add more retrieval metrics.
Experiment with different embedding models.
Compare multiple reranking models.
Improve query rewriting using conversation history.
Add source citations to generated answers.
Improve hallucination detection.
Strengthen guardrails using retrieval-confidence thresholds.
Add support for additional document formats.
Improve logging and error handling.
Optimize retrieval and reranking latency.
Add automated regression testing for the complete RAG pipeline.

10. Final Project Status

Status: COMPLETED / READY FOR FINAL REVIEW

The core RAG pipeline has been implemented and tested. The project includes document processing, chunking, embeddings, ChromaDB retrieval, query rewriting, cross-encoder reranking, answer generation, retrieval evaluation, and guardrail testing.

The guardrail successfully passed both supported and unsupported question tests.