# RAG Document QA – Test Results

## 1. Test Environment

- **Application:** RAG Document Question Answering
- **Vector Database:** ChromaDB
- **Embedding Model:** all-MiniLM-L6-v2
- **Embedding Dimension:** 384
- **LLM:** Groq — GPT-OSS-120B
- **Supported Documents:** PDF, TXT
- **UI:** Streamlit
- **Python:** 3.12
- **OS:** Windows

---

## 2. Application Test Cases

### Test Case 1 — Mixed Question

**Question:**

```text
Where do funds engage across a wide range of themes?

Answer Returned:

The funds engage across a wide range of themes, including the defence of the territories, adaptation, sustainable livelihoods, biodiversity, forests and agroecology, food.

Source Files:

Financing social and environmental justice in the global South.pdf (Page 2, Chunk 7)
Financing social and environmental justice in the global South.pdf (Page 1, Chunk 3)
Financing social and environmental justice in the global South.pdf (Page 2, Chunk 12)
Financing social and environmental justice in the global South.pdf (Page 4, Chunk 24)
Financing social and environmental justice in the global South.pdf (Page 2, Chunk 2)

Page/Chunk References:

Retrieved Chunk 1 — Distance: 0.7839
Retrieved Chunk 2 — Distance: 0.8094
Retrieved Chunk 3 — Distance: 0.8287
Retrieved Chunk 4 — Distance: 0.8398
Retrieved Chunk 5 — Distance: 0.8583

Result:

PASS ✅

Proof:

Screenshot:

https://drive.google.com/drive/folders/1yqM91Ci3in9wo9r-hSrnWo51j7mHI1Pu?usp=sharing

Test Case 2 — Python Definition

Question:

What is Python?

Answer Returned:

Python is a high-level, interpreted, and general-purpose programming language that emphasizes simplicity and readability. In simple terms, Python is a programming language that's like a set of instructions you give to a computer to make it do something.

Source Files:

python notes.pdf (Page 1, Chunk 5)
python notes.pdf (Page 1, Chunk 6)
python notes.pdf (Page 1, Chunk 7)
python notes.pdf (Page 1, Chunk 8)
python notes.pdf (Page 1, Chunk 9)

Page/Chunk References:

Retrieved Chunk 1 — Distance: 0.4021
Retrieved Chunk 2 — Distance: 0.4801
Retrieved Chunk 3 — Distance: 0.5003
Retrieved Chunk 4 — Distance: 0.5147
Retrieved Chunk 5 — Distance: 0.5674

Result:

PASS ✅

Proof:

Screenshot:

https://drive.google.com/drive/folders/1yqM91Ci3in9wo9r-hSrnWo51j7mHI1Pu?usp=sharing

Test Case 3 — len() Function

Question:

len() function?

Answer Returned:

len() finds out how many characters are in a string. For example, if myName is 'Al', len(myName) will print 2 because "Al" has 2 letters.

Source Files:

python notes.pdf (Page 8, Chunk 6)
python notes.pdf (Page 8, Chunk 7)
python notes.pdf (Page 7, Chunk 4)
python notes.pdf (Page 2, Chunk 9)
python notes.pdf (Page 8, Chunk 8)

Page/Chunk References:

Retrieved Chunk 1 — Distance: 0.8133
Retrieved Chunk 2 — Distance: 0.8595
Retrieved Chunk 3 — Distance: 1.1436
Retrieved Chunk 4 — Distance: 1.1738
Retrieved Chunk 5 — Distance: 1.2263

Result:

PASS ✅

Proof:

Screenshot:

https://drive.google.com/drive/folders/1yqM91Ci3in9wo9r-hSrnWo51j7mHI1Pu?usp=sharing

Test Case 4 — Community Impact

Question:

communities are most affected by what?

Answer Returned:

climate, environmental, social and economic shocks

Source Files:

Financing social and environmental justice in the global South.pdf (Page 1, Chunk 9)
Financing social and environmental justice in the global South.pdf (Page 2, Chunk 2)
Financing social and environmental justice in the global South.pdf (Page 3, Chunk 5)
Financing social and environmental justice in the global South.pdf (Page 4, Chunk 11)
Financing social and environmental justice in the global South.pdf (Page 1, Chunk 12)

Page/Chunk References:

Retrieved Chunk 1 — Distance: 0.9205
Retrieved Chunk 2 — Distance: 0.9971
Retrieved Chunk 3 — Distance: 1.1131
Retrieved Chunk 4 — Distance: 1.1430
Retrieved Chunk 5 — Distance: 1.1451

Result:

PASS ✅

Proof:

Screenshot:

https://drive.google.com/drive/folders/1yqM91Ci3in9wo9r-hSrnWo51j7mHI1Pu?usp=sharing

Test Case 5 — Interactive Shell

Question:

what is interactive shell?

Answer Returned:

The interactive shell is a place where you can type Python code and immediately see the result.

Source Files:

python notes.pdf (Page 2, Chunk 3)
python notes.pdf (Page 7, Chunk 3)
python notes.pdf (Page 7, Chunk 1)
python notes.pdf (Page 20, Chunk 2)
python notes.pdf (Page 1, Chunk 11)

Page/Chunk References:

Retrieved Chunk 1 — Distance: 0.8274
Retrieved Chunk 2 — Distance: 1.0776
Retrieved Chunk 3 — Distance: 1.1285
Retrieved Chunk 4 — Distance: 1.1950
Retrieved Chunk 5 — Distance: 1.2408

Result:

PASS ✅

Proof:

Screenshot:

https://drive.google.com/drive/folders/1yqM91Ci3in9wo9r-hSrnWo51j7mHI1Pu?usp=sharing

3. Retrieval Pipeline Validation

The retrieval pipeline was validated through document upload, processing, embedding generation, semantic retrieval, source tracking, and display of retrieved chunks.

Test ID	Test	Result	Status
R-01	Upload PDF	Successfully uploaded and processed	✅ Pass
R-02	Chunk Generation	Chunks created successfully	✅ Pass
R-03	Embedding Storage	Embeddings stored successfully in ChromaDB	✅ Pass
R-04	Semantic Retrieval	Relevant top chunks retrieved	✅ Pass
R-05	Source Citation	File name, page number and chunk displayed correctly	✅ Pass
R-06	Out-of-document Query	Correctly indicated insufficient information based on retrieved context	✅ Pass
R-07	Retrieved Chunks UI	Retrieved chunks displayed in collapsible sections	✅ Pass
4. Groq Answer Generation Validation

The answer-generation pipeline was tested using Groq GPT-OSS-120B with retrieved document context.

Test ID	Test	Result	Status
G-01	Live answer generation	Verified with 5 document-based questions	✅ Pass
G-02	Grounded answer generation	Answers generated using retrieved document context	✅ Pass
G-03	Source display with answer	Sources and retrieved chunks displayed with generated answers	✅ Pass
G-04	LLM unavailable handling	Application handles LLM/API failure without crashing	✅ Pass
5. Document Processing Validation

The document-processing pipeline was tested to verify that uploaded documents are correctly loaded, chunked, embedded, and stored.

Test ID	Component	Validation	Status
D-01	Document Loader	PDF document loaded successfully	✅ Pass
D-02	Text Extraction	Text extracted from document pages	✅ Pass
D-03	Chunking	Document divided into retrievable chunks	✅ Pass
D-04	Metadata	File name, page number and chunk metadata generated	✅ Pass
D-05	Embeddings	384-dimensional embeddings generated successfully	✅ Pass
D-06	ChromaDB	Embeddings stored in persistent ChromaDB collection	✅ Pass
6. Embedding Model Validation

The application uses the all-MiniLM-L6-v2 Sentence Transformer model.

Validation performed:

Embedding model loaded successfully.
Embedding dimension verified as 384.
Embeddings generated for document chunks.
Embeddings stored in ChromaDB.
The Streamlit application uses a cached embedding model to avoid repeatedly loading the model during application reruns.

Status: ✅ PASS

7. Query and Retrieval Validation

The retrieval workflow was validated using multiple questions across different uploaded documents.

The pipeline successfully performed:

User question input.
Query rewriting when required.
Semantic similarity search.
Retrieval of relevant document chunks.
Cross-encoder reranking of retrieved results.
Selection of the most relevant context.
Passing retrieved context to the LLM.
Display of source file, page and chunk information.

Status: ✅ PASS

8. Guardrail Validation

The application was tested for questions that are both supported and unsupported by the uploaded documents.

Supported Question

Question:

What is Python?

Expected Behavior:

The system should answer using information available in the uploaded documents.

Result:

Supported question answered using retrieved document context.

Status: ✅ PASS

Unsupported Question

Question:

What is the capital of France?

Expected Behavior:

The system should not generate an answer when sufficient information is unavailable in the uploaded documents.

Result:

Not enough information in the uploaded documents.

Status: ✅ PASS

Guardrail Summary
Test	Expected Behavior	Status
Supported question	Answer using uploaded document context	✅ Pass
Unsupported question	Refuse to answer when information is unavailable	✅ Pass
9. Streamlit UI Validation

The Streamlit interface was tested for the complete user workflow.

Validated functionality:

PDF/TXT document upload.
Previous document handling.
Document processing.
Embedding generation.
ChromaDB storage.
Question input.
Answer generation.
Source file display.
Page number display.
Chunk number display.
Retrieved chunk display.
Unsupported-question guardrail.
LLM/API unavailable handling.
Session reset.

Status: ✅ PASS

10. Session Reset Validation

The reset functionality was tested to verify that the application can start a new document-processing session.

Verified:

Documents folder cleared.
Existing ChromaDB collection deleted/reset.
Session state reset.
New document can be uploaded.
New document can be processed successfully.

Status: ✅ PASS

11. Evaluation Artifacts

The project also contains separate evaluation artifacts used to analyze retrieval and RAG performance.

Retrieval Evaluation

Generated artifacts include:

retrieval/relevance_dataset.csv
retrieval/retrieval_evaluation.csv
retrieval/retrieval_metrics_summary.csv

These files are used to evaluate retrieval relevance and retrieval performance.

Chunking Comparison

Generated artifacts include:

chunking_comparison_results.csv
chunking_comparison_summary.md

These files are used to compare different chunking strategies.

RAG Evaluation

The RAG evaluation pipeline produces:

evaluation_results.csv

The evaluation covers RAG quality metrics such as:

Faithfulness
Answer relevancy
Context precision
Context recall
12. Overall Test Status
Module	Status
Document Upload	✅ PASS
PDF/TXT Support	✅ PASS
Document Processing	✅ PASS
Text Extraction	✅ PASS
Chunking	✅ PASS
Embedding Generation	✅ PASS
Cached Embedding Model	✅ PASS
ChromaDB Integration	✅ PASS
Semantic Retrieval	✅ PASS
Cross-Encoder Reranking	✅ PASS
Query Rewriting	✅ PASS
Source Citation	✅ PASS
Retrieved Chunks Display	✅ PASS
Groq Answer Generation	✅ PASS
Grounded Answers	✅ PASS
Unsupported Query Guardrail	✅ PASS
LLM/API Failure Handling	✅ PASS
Streamlit UI	✅ PASS
Session Reset	✅ PASS
13. Final Remarks

The RAG Document Question Answering application was successfully validated through document processing, embedding generation, semantic retrieval, reranking, grounded answer generation, source citation, guardrail testing, and Streamlit UI testing.

The application successfully retrieves relevant document context and generates answers using Groq GPT-OSS-120B while displaying the corresponding source information.

The system also handles unsupported questions by preventing answers that are not grounded in the uploaded documents.

Overall Status: ✅ PROJECT TESTING COMPLETED