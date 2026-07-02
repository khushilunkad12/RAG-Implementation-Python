# RAG Phase 2 - Document Loading & Chunking

## Project Overview
This project demonstrates the first stage of a Retrieval-Augmented Generation (RAG) pipeline. It reads a text document, splits it into meaningful chunks of approximately 300 characters without breaking words, and prints the chunks in the terminal.

## Files
- `loader.py` – Reads text from the document.
- `chunker.py` – Splits the text into chunks.
- `main.py` – Connects the loader and chunker and prints the output.
- `output_chunks.json` - this file is generated when we run main.py , chunks get saved here
## How to Run

```bash
python main.py
```

## Expected Output

- Reads `data/sample.txt`
- Splits the document into chunks
- Prints the total number of chunks
- Displays each chunk with its chunk number

## Phase 2 - Embeddings

### Features
- Load document from `data/sample.txt`
- Split text into overlapping chunks
- Add metadata to each chunk
- Save chunks to `output_chunks.json`
- Generate embeddings using `sentence-transformers/all-MiniLM-L6-v2`
- Store embeddings in ChromaDB

### Run

```bash
python main.py
python embed_store.py
```

### Output

- output_chunks.json
- ChromaDB collection containing embeddings

## Phase 3 - Retrieval

This phase performs semantic search using ChromaDB.

### Run

```bash
python main.py
python embed_store.py
python retriever.py
```

The retriever:
- Converts the user query into an embedding
- Searches ChromaDB
- Retrieves the top 3 most relevant chunks
- Displays chunk text, metadata, and similarity distance

### Clone the repository

```bash
git clone <repository-url>
cd Phase2_Rag_Practice
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate

Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### Run the project

```bash
python main.py
python embed_store.py
python retriever.py
python rag_answer.py
```