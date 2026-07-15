def clean_text(text: str) -> str:
    """
    Clean the provided text by removing extra spaces and newlines.
    """
    words = text.split()
    cleaned_text = ' '.join(words)
    return cleaned_text


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """
    Split text into smaller word-based chunks.
    """

    if overlap >= chunk_size:
        raise ValueError(
            "Overlap must be smaller than chunk size."
        )

    words = text.split()
    chunks = []
    current_chunk = []


    for word in words:
        current_chunk.append(word)
        if len(current_chunk) >= chunk_size:
            chunks.append(' '.join(current_chunk))

            current_chunk = current_chunk[-overlap:]


    if len(current_chunk) > overlap:
        chunks.append(' '.join(current_chunk))

    return chunks

def create_chunk_metadata(chunks: list[str]) -> list[dict]:
    """
    Create metadata for each chunk.
    """

    metadata = []

    for i, chunk in enumerate(chunks, start=1):
        metadata.append({
            "chunk_id": i,
            "word_count": len(chunk.split()),
            "text": chunk
        })

    return metadata
