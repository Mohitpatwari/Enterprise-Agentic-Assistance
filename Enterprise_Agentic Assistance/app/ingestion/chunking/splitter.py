from typing import List
import logfire


def _split_long(text: str, size: int) -> List[str]:
    """Hard-split a long string into pieces of at most `size` chars."""
    return [text[i:i + size] for i in range(0, len(text), size)]


def chunk_text(text: str, chunk_size: int = 1500) -> List[str]:
    """
    Paragraph-based chunker. Oversized paragraphs are split by line,
    and oversized lines are hard-split, so no chunk exceeds chunk_size.
    """
    with logfire.span("Text Chunking", text_length=len(text)):
        if not text.strip():
            return []

        # 1. Break text into pieces that each fit in chunk_size
        pieces = []
        for p in text.split("\n\n"):
            if len(p) <= chunk_size:
                pieces.append(p)
            else:
                for line in p.split("\n"):
                    if len(line) <= chunk_size:
                        pieces.append(line)
                    else:
                        pieces.extend(_split_long(line, chunk_size))

        # 2. Greedily pack pieces into chunks
        chunks = []
        current_chunk = ""
        for p in pieces:
            if len(current_chunk) + len(p) + 2 <= chunk_size:
                current_chunk += p + "\n\n"
            else:
                if current_chunk.strip():
                    chunks.append(current_chunk.strip())
                current_chunk = p + "\n\n"

        if current_chunk.strip():
            chunks.append(current_chunk.strip())

        valid_chunks = [c for c in chunks if c.strip()]
        logfire.info(f"Generated {len(valid_chunks)} chunks")
        return valid_chunks
