def chunk_text(text, source, chunk_size=300):
    """
    Split text into chunks without breaking words
    and attach metadata to each chunk.
    """

    chunks = []
    start = 0
    chunk_id = 1

    while start < len(text):

        end = start + chunk_size

        if end >= len(text):
            chunk = text[start:].strip()

            chunks.append({
                "chunk_id": chunk_id,
                "text": chunk,
                "source": source
            })

            break

        while end > start and text[end] != " ":
            end -= 1

        if end == start:
            end = start + chunk_size

        chunk = text[start:end].strip()

        chunks.append({
            "chunk_id": chunk_id,
            "text": chunk,
            "source": source
        })

        chunk_id += 1
        start = end + 1

    return chunks