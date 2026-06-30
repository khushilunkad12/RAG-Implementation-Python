def chunk_text(text, chunk_size=300):
    """
    Split text into chunks without breaking words.
    """

    chunks = []
    start = 0

    while start < len(text):

        end = start + chunk_size

        if end >= len(text):
            chunks.append(text[start:].strip())
            break

        # Find the last space before the limit
        while end > start and text[end] != " ":
            end -= 1

        # If no space found, split at chunk size
        if end == start:
            end = start + chunk_size

        chunks.append(text[start:end].strip())

        start = end + 1

    return chunks