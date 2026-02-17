"""
Build the vector index: load Markdown from docs/, chunk, embed, store in Chroma.
Run this after adding or changing documents under docs/.
"""
from __future__ import annotations

import sys
from pathlib import Path

import chromadb
from chromadb.api.types import Documents, EmbeddingFunction, Embeddings

from config import (
    CHUNK_OVERLAP,
    CHUNK_SIZE,
    DEFAULT_CHROMA_COLLECTION,
    DOCS_DIR,
    VECTOR_STORE_DIR,
)
from chunking import chunk_markdown
from embeddings import embed


class OurEmbeddingFunction(EmbeddingFunction[Documents]):
    def __call__(self, input: Documents) -> Embeddings:
        return embed(list(input))


def load_markdown_docs(docs_dir: Path) -> list[tuple[str, str]]:
    """Load all .md files from docs_dir. Returns list of (content, source_path)."""
    if not docs_dir.exists():
        return []
    out = []
    for path in sorted(docs_dir.rglob("*.md")):
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
            out.append((content, str(path)))
        except Exception as e:
            print(f"Warning: could not read {path}: {e}", file=sys.stderr)
    return out


def build_index(
    docs_dir: Path | None = None,
    chunk_size: int = CHUNK_SIZE,
    chunk_overlap: int = CHUNK_OVERLAP,
    collection_name: str = DEFAULT_CHROMA_COLLECTION,
) -> int:
    """
    Load Markdown from docs_dir, chunk, embed, and persist to Chroma.
    Returns the number of chunks indexed.
    """
    docs_dir = docs_dir or DOCS_DIR
    docs_dir = Path(docs_dir)
    pairs = load_markdown_docs(docs_dir)
    if not pairs:
        print(f"No .md files found under {docs_dir}", file=sys.stderr)
        return 0

    all_chunks: list[str] = []
    all_metadatas: list[dict] = []
    for content, source in pairs:
        for chunk_text, meta in chunk_markdown(
            content, chunk_size=chunk_size, chunk_overlap=chunk_overlap, source=source
        ):
            all_chunks.append(chunk_text)
            all_metadatas.append(meta)

    if not all_chunks:
        return 0

    VECTOR_STORE_DIR.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(VECTOR_STORE_DIR))
    try:
        client.delete_collection(name=collection_name)
    except Exception:
        pass
    ef = OurEmbeddingFunction()
    collection = client.create_collection(
        name=collection_name,
        embedding_function=ef,
        metadata={"description": "RAG document chunks"},
    )

    # Add in batches to avoid memory spikes (and API limits for remote)
    batch_size = 32
    for i in range(0, len(all_chunks), batch_size):
        batch_ids = [f"chunk_{i + j}" for j in range(len(all_chunks[i : i + batch_size]))]
        collection.add(
            documents=all_chunks[i : i + batch_size],
            metadatas=all_metadatas[i : i + batch_size],
            ids=batch_ids,
        )

    print(f"Indexed {len(all_chunks)} chunks from {len(pairs)} file(s).")
    return len(all_chunks)


def main() -> None:
    import argparse

    ap = argparse.ArgumentParser(description="Build RAG vector index from docs/")
    ap.add_argument("--chunk-size", type=int, default=CHUNK_SIZE)
    ap.add_argument("--chunk-overlap", type=int, default=CHUNK_OVERLAP)
    ap.add_argument("--docs-dir", type=Path, default=DOCS_DIR)
    args = ap.parse_args()
    n = build_index(docs_dir=args.docs_dir, chunk_size=args.chunk_size, chunk_overlap=args.chunk_overlap)
    sys.exit(0 if n >= 0 else 1)


if __name__ == "__main__":
    main()
