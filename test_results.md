# RAG Document QA – Test Results

## Test Environment

* **Application:** RAG Document Question Answering
* **Vector Database:** ChromaDB
* **Embedding Model:** all-MiniLM-L6-v2
* **LLM:** Gemini 2.5 Flash
* **Supported Documents:** PDF, TXT

---

## Mixed Question Testing

### Test Case 1

**Question:**
 Where do funds engage across a wide range of themes?

**Answer Returned:**
The funds engage across a wide range of themes, including the defence of the territories, adaptation, sustainable livelihoods, biodiversity, forests and agroecology, food.

**Source Files:**
1. Financing social and environmental justice in the global South.pdf (Page 2, Chunk 7)
2. Financing social and environmental justice in the global South.pdf (Page 1, Chunk 3)
3. Financing social and environmental justice in the global South.pdf (Page 2, Chunk 12)
4. Financing social and environmental justice in the global South.pdf (Page 4, Chunk 24)
5. Financing social and environmental justice in the global South.pdf (Page 2, Chunk 2)

**Page/Chunk References:**
Retrieved Chunk 1 (Distance: 0.7839)

Retrieved Chunk 2 (Distance: 0.8094)

Retrieved Chunk 3 (Distance: 0.8287)

Retrieved Chunk 4 (Distance: 0.8398)

Retrieved Chunk 5 (Distance: 0.8583)

**Result:**
PASS ✅

**Proof:**
Screenshot: https://drive.google.com/drive/folders/1yqM91Ci3in9wo9r-hSrnWo51j7mHI1Pu?usp=sharing



### Test Case 2

**Question:**
What is Python ?

**Answer Returned:**
Python is a high-level, interpreted, and general-purpose programming language that emphasizes simplicity and readability. In simple terms, Python is a programming language that's like a set of instructions you give to a computer to make it do something.

**Source Files:**
python notes.pdf (Page 1, Chunk 5)
python notes.pdf (Page 1, Chunk 6)
python notes.pdf (Page 1, Chunk 7)
python notes.pdf (Page 1, Chunk 8)
python notes.pdf (Page 1, Chunk 9)


**Page/Chunk References:**
Retrieved Chunk 1 (Distance: 0.4021)

Retrieved Chunk 2 (Distance: 0.4801)

Retrieved Chunk 3 (Distance: 0.5003)

Retrieved Chunk 4 (Distance: 0.5147)

Retrieved Chunk 5 (Distance: 0.5674)

**Result:**
PASS ✅

**Proof:**
Screenshot: https://drive.google.com/drive/folders/1yqM91Ci3in9wo9r-hSrnWo51j7mHI1Pu?usp=sharing


### Test Case 3

**Question:**
len() function?

**Answer Returned:**
len() finds out how many characters are in a string. For example, if myName is 'Al', len(myName) will print 2 because "Al" has 2 letters.

**Source Files:**
python notes.pdf (Page 8, Chunk 6)
python notes.pdf (Page 8, Chunk 7)
python notes.pdf (Page 7, Chunk 4)
python notes.pdf (Page 2, Chunk 9)
python notes.pdf (Page 8, Chunk 8)

**Page/Chunk References:**
Retrieved Chunk 1 (Distance: 0.8133)

Retrieved Chunk 2 (Distance: 0.8595)

Retrieved Chunk 3 (Distance: 1.1436)

Retrieved Chunk 4 (Distance: 1.1738)

Retrieved Chunk 5 (Distance: 1.2263)

**Result:**
PASS ✅

**Proof:**
Screenshot: https://drive.google.com/drive/folders/1yqM91Ci3in9wo9r-hSrnWo51j7mHI1Pu?usp=sharing



### Test Case 4

**Question:**
communities are most affected by what ?

**Answer Returned:**
climate, environmental, social and economic shocks

**Source Files:**
Financing social and environmental justice in the global South.pdf (Page 1, Chunk 9)
Financing social and environmental justice in the global South.pdf (Page 2, Chunk 2)
Financing social and environmental justice in the global South.pdf (Page 3, Chunk 5)
Financing social and environmental justice in the global South.pdf (Page 4, Chunk 11)
Financing social and environmental justice in the global South.pdf (Page 1, Chunk 12)

**Page/Chunk References:**
Retrieved Chunk 1 (Distance: 0.9205)

Retrieved Chunk 2 (Distance: 0.9971)

Retrieved Chunk 3 (Distance: 1.1131)

Retrieved Chunk 4 (Distance: 1.1430)

Retrieved Chunk 5 (Distance: 1.1451)

**Result:**
PASS ✅

**Proof:**
Screenshot: https://drive.google.com/drive/folders/1yqM91Ci3in9wo9r-hSrnWo51j7mHI1Pu?usp=sharing



### Test Case 5

**Question:**
what is interactive shell ?

**Answer Returned:**
The interactive shell is a place where you can type Python code and immediately see the result.

**Source Files:**
python notes.pdf (Page 2, Chunk 3)
python notes.pdf (Page 7, Chunk 3)
python notes.pdf (Page 7, Chunk 1)
python notes.pdf (Page 20, Chunk 2)
python notes.pdf (Page 1, Chunk 11)

**Page/Chunk References:**
 Retrieved Chunk 1 (Distance: 0.8274)

Retrieved Chunk 2 (Distance: 1.0776)

Retrieved Chunk 3 (Distance: 1.1285)

Retrieved Chunk 4 (Distance: 1.1950)

Retrieved Chunk 5 (Distance: 1.2408)

**Result:**
PASS ✅

**Proof:**
Screenshot: https://drive.google.com/drive/folders/1yqM91Ci3in9wo9r-hSrnWo51j7mHI1Pu?usp=sharing

## Retrieval & Gemini Validation

### Retrieval Pipeline (Verified)

| Test ID | Test                  | Result                                                                  | Status |
| ------- | --------------------- | ----------------------------------------------------------------------- | ------ |
| R-01    | Upload PDF            | Successfully uploaded and processed                                     | ✅ Pass |
| R-02    | Chunk Generation      | Chunks created successfully                                             | ✅ Pass |
| R-03    | Embedding Storage     | Stored successfully in ChromaDB                                         | ✅ Pass |
| R-04    | Semantic Retrieval    | Relevant top chunks retrieved                                           | ✅ Pass |
| R-05    | Source Citation       | File name, page number and chunk displayed correctly                    | ✅ Pass |
| R-06    | Out-of-document Query | Correctly indicated insufficient information based on retrieved context | ✅ Pass |
| R-07    | Retrieved Chunks UI   | Retrieved chunks displayed in collapsible sections                      | ✅ Pass |

---

### Gemini Answer Generation 

| Test ID | Test                                                | Result                                                                         | Status                |
| ------- | --------------------------------------------------- | ------------------------------------------------------------------------------ | --------------------- |
| G-01 | Live mixed-question answer generation | Verified with 5 questions | ✅ Pass |
| G-02    | LLM unavailable handling                            | Application continues to display retrieved sources and chunks without crashing | ✅ Pass |
          
----

# RAG Application Test Results

Date: 14 July 2026

---

## Environment

- OS: Windows 11
- Python: 3.12
- Embedding Model: all-MiniLM-L6-v2
- Vector Database: ChromaDB
- LLM: Gemini 2.5 Flash
- UI: Streamlit

---

# Test Results

## 1. Document Upload

Result:
- PDF uploaded successfully.
- Previous document removed.
- Current uploaded document displayed.

Status: ✅ PASS

---

## 2. Document Processing

Verified:

- PDF loaded correctly.
- Pages extracted.
- Text chunked.
- Metadata generated.
- JSON file created.

Status: ✅ PASS

---

## 3. Embedding Generation

Verified:

- Embeddings created successfully.
- Stored in ChromaDB.
- Old collection replaced with new collection.

Status: ✅ PASS

---

## 4. Retrieval Pipeline

Verified:

- Relevant chunks retrieved.
- Filename displayed.
- Page number displayed.
- Chunk number displayed.
- Retrieved chunks shown in UI.

Status: ✅ PASS

---

## 5. Gemini Answer Generation

Result:

- Live Gemini answers verified using 5 mixed/document-specific questions.
- Sources, page numbers, chunks, and retrieved context were displayed.
- LLM unavailable fallback was also tested earlier and handled correctly.

Status: ✅ PASS





---

## 6. Reset Session

Verified:

- Documents folder cleared.
- Chroma collection deleted.
- Session state reset.
- New document can be uploaded.

Status: ✅ PASS

---

# Overall Status

| Module | Status |
|---------|--------|
| Document Upload | ✅ PASS |
| Processing | ✅ PASS |
| Chunking | ✅ PASS |
| Embeddings | ✅ PASS |
| Retrieval | ✅ PASS |
| Source Display | ✅ PASS |
| Reset Session | ✅ PASS |


---

## Remarks

The Retrieval-Augmented Generation (RAG) pipeline has been successfully validated through retrieval and Gemini answer generation.


## Overall Status

* ✅ Document upload verified
* ✅ Automatic document processing verified
* ✅ PDF/TXT document support verified
* ✅ Chunk generation verified
* ✅ ChromaDB integration verified
* ✅ Retrieval pipeline verified
* ✅ Source citation verified
* ✅ Multiple-document workflow verified
* ✅ Session reset verified
* ✅ Graceful handling when the LLM/API is unavailable



---

