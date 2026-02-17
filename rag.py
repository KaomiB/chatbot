"""
RAG query path: retrieve relevant chunks from Chroma, then synthesize answer with LLM.
"""
from __future__ import annotations

from pathlib import Path

import chromadb
from chromadb.api.types import Documents, EmbeddingFunction, Embeddings

from config import (
    DEFAULT_CHROMA_COLLECTION,
    LLM_BACKEND,
    LLM_MODEL,
    OPENAI_API_BASE,
    OPENAI_API_KEY,
    RAG_TOP_K,
    VECTOR_STORE_DIR,
)
from embeddings import embed


class OurEmbeddingFunction(EmbeddingFunction[Documents]):
    def __call__(self, input: Documents) -> Embeddings:
        return embed(list(input))


def get_chroma_collection():
    """Get the persisted Chroma collection, or None if not built yet."""
    if not (VECTOR_STORE_DIR / "chroma.sqlite3").exists():
        return None
    client = chromadb.PersistentClient(path=str(VECTOR_STORE_DIR))
    try:
        return client.get_collection(
            name=DEFAULT_CHROMA_COLLECTION,
            embedding_function=OurEmbeddingFunction(),
        )
    except Exception:
        return None


def get_relevant_chunks(query: str, k: int | None = None) -> list[tuple[str, dict]]:
    """
    Embed query, retrieve top-k chunks from Chroma. Returns list of (chunk_text, metadata).
    """
    k = k or RAG_TOP_K
    coll = get_chroma_collection()
    if coll is None:
        return []
    n = coll.count()
    if n == 0:
        return []
    res = coll.query(query_texts=[query], n_results=min(k, n))
    if not res or not res["documents"] or not res["documents"][0]:
        return []
    docs = res["documents"][0]
    metadatas = (res.get("metadatas") or [None])[0]
    if metadatas is None:
        metadatas = [{}] * len(docs)
    return list(zip(docs, metadatas))


def synthesize_with_llm(query: str, context: str) -> str:
    """Generate an answer using the configured LLM backend (remote OpenAI-compatible)."""
    if LLM_BACKEND != "remote":
        return (
            "[Local LLM not implemented. Set LLM_BACKEND=remote and OPENAI_API_KEY or OPENAI_API_BASE.]"
        )

    from openai import OpenAI

    client = OpenAI(api_key=OPENAI_API_KEY or "not-needed", base_url=OPENAI_API_BASE or None)
    messages = [
        {
            "role": "system",
            "content": "Answer the user's question using only the following context. If the context does not contain enough information, say so. Be concise.",
        },
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"},
    ]
    resp = client.chat.completions.create(model=LLM_MODEL, messages=messages)
    return resp.choices[0].message.content or ""


def knowledge_only_response(query: str, top_k: int | None = None) -> tuple[str | None, list[str]]:
    """
    Return (answer, citations) from the knowledge base only (no LLM).
    Citations are source paths from chunk metadata. Returns (None, []) if no chunks.
    """
    chunks = get_relevant_chunks(query, k=top_k or RAG_TOP_K)
    if not chunks:
        return None, []
    parts = []
    citations_seen: set[str] = set()
    for text, meta in chunks:
        source = meta.get("source", "")
        if source:
            citations_seen.add(source)
            parts.append(f"{text}\n\n*Source: {source}*")
        else:
            parts.append(text)
    reply = "Here's what we have on that:\n\n" + "\n\n---\n\n".join(parts)
    return reply, sorted(citations_seen)


def rag_response(query: str, top_k: int | None = None) -> str | None:
    """
    Run RAG: retrieve chunks, synthesize with LLM. Returns None if index not built or RAG disabled.
    """
    chunks = get_relevant_chunks(query, k=top_k or RAG_TOP_K)
    if not chunks:
        return None
    context = "\n\n---\n\n".join(text for text, _ in chunks)
    return synthesize_with_llm(query, context)
