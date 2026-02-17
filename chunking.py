"""
Heading/section-aware text chunking for RAG.
Splits on markdown headings first, then paragraph, then sentence/char limit.
"""
from __future__ import annotations


def recursive_split(
    text: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 50,
    separators: list[str] | None = None,
) -> list[str]:
    """
    Split text by separators (in order) so that chunks stay under chunk_size
    with overlap between chunks. Prefer splitting on structure (e.g. ##, \\n\\n) first.
    """
    if separators is None:
        separators = ["\n## ", "\n### ", "\n\n", "\n", ". ", " "]

    text = text.strip()
    if not text:
        return []

    def _split_by(sep: str) -> list[str]:
        if not sep:
            return list(text)
        return [s.strip() for s in text.split(sep) if s.strip()]

    def _merge_with_overlap(chunks: list[str], sep: str) -> list[str]:
        merged: list[str] = []
        current = ""
        for i, c in enumerate(chunks):
            candidate = (current + sep + c) if current else c
            if len(candidate) <= chunk_size:
                current = candidate
            else:
                if current:
                    merged.append(current)
                if len(c) > chunk_size:
                    # Recursively split this chunk with remaining separators
                    next_seps = [s for s in separators if s != sep]
                    if next_seps:
                        sub = recursive_split(c, chunk_size, chunk_overlap, next_seps)
                        merged.extend(sub)
                    else:
                        merged.append(c)
                    current = ""
                else:
                    current = c
        if current:
            merged.append(current)
        return merged

    for sep in separators:
        parts = _split_by(sep)
        if len(parts) <= 1:
            continue
        chunks = _merge_with_overlap(parts, sep)
        if len(chunks) > 1:
            # Add overlap: include tail of previous chunk at start of next
            result: list[str] = []
            for i, ch in enumerate(chunks):
                if chunk_overlap and i > 0 and len(chunks[i - 1]) >= chunk_overlap:
                    overlap = chunks[i - 1][-chunk_overlap:]
                    result.append(overlap + " " + ch)
                else:
                    result.append(ch)
            return result

    # Single chunk
    if len(text) <= chunk_size:
        return [text]
    # Force split by character
    out = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        out.append(text[start:end])
        start = end - chunk_overlap if chunk_overlap else end
    return out


def chunk_markdown(
    content: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 50,
    source: str = "",
) -> list[tuple[str, dict]]:
    """
    Chunk markdown text with structure awareness. Returns list of (chunk_text, metadata).
    """
    chunks = recursive_split(content, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return [(c, {"source": source}) for c in chunks]
