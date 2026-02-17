"""
Embedding backend: local (sentence-transformers) or remote (OpenAI-compatible API).
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from config import (
    EMBEDDING_BACKEND,
    EMBEDDING_MODEL_LOCAL,
    OPENAI_API_BASE,
    OPENAI_API_KEY,
    OPENAI_EMBEDDING_MODEL,
)

if TYPE_CHECKING:
    pass


def _local_embed(texts: list[str]) -> list[list[float]]:
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(EMBEDDING_MODEL_LOCAL)
    embeddings = model.encode(texts, convert_to_numpy=True)
    return embeddings.tolist()


def _remote_embed(texts: list[str]) -> list[list[float]]:
    from openai import OpenAI

    client = OpenAI(api_key=OPENAI_API_KEY or "not-needed", base_url=OPENAI_API_BASE or None)
    resp = client.embeddings.create(input=texts, model=OPENAI_EMBEDDING_MODEL)
    return [e.embedding for e in resp.data]


def embed(texts: list[str]) -> list[list[float]]:
    """Compute embeddings for a list of texts. Uses backend from config."""
    if not texts:
        return []
    if EMBEDDING_BACKEND == "remote":
        return _remote_embed(texts)
    return _local_embed(texts)
