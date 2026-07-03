from document_loader import load_documents

documents = load_documents()

print(f"Loaded {len(documents)} documents.\n")

for document in documents:

    print(document["filename"])

    print(document["text"][:100])

    print("-"*50)