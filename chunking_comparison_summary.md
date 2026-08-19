# Chunking Comparison Summary

## Chunk Counts
- Fixed: 57 chunks
- Recursive: 71 chunks
- Sentence/paragraph: 58 chunks

## Test Setup
- Documents tested: 10
- Questions tested: 5
- Embedding model: all-MiniLM-L6-v2
- Retrieval: Top-3 cosine similarity

## Observations
- Recursive chunking performed best for Python and RAG questions.
- Sentence/paragraph chunking performed best for database, machine learning, and software testing questions.
- Fixed chunking worked, but some chunks start mid-word or mid-sentence, so readability is weaker.
- Recursive and sentence-based chunking preserve context better than fixed chunking.

## Conclusion
Sentence/paragraph and recursive chunking gave better readable results than fixed chunking. Fixed chunking is simple, but it may break useful context.