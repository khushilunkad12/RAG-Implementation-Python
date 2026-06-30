# RAG Phase 2 - Document Loading & Chunking

## Project Overview
This project demonstrates the first stage of a Retrieval-Augmented Generation (RAG) pipeline. It reads a text document, splits it into meaningful chunks of approximately 300 characters without breaking words, and prints the chunks in the terminal.

## Files
- `loader.py` – Reads text from the document.
- `chunker.py` – Splits the text into chunks.
- `main.py` – Connects the loader and chunker and prints the output.

## How to Run

```bash
python main.py
```

## Expected Output

- Reads `data/sample.txt`
- Splits the document into chunks
- Prints the total number of chunks
- Displays each chunk with its chunk number