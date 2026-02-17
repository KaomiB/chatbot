"""
Configuration for embedding and LLM backends.
Set via environment variables or override in code.
"""
import os
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent
DOCS_DIR = PROJECT_ROOT / "docs"
VECTOR_STORE_DIR = PROJECT_ROOT / "vector_store"
DEFAULT_CHROMA_COLLECTION = "rag_docs"

# Embedding: "local" (sentence-transformers) or "remote" (OpenAI-compatible API)
EMBEDDING_BACKEND = os.environ.get("EMBEDDING_BACKEND", "local")
EMBEDDING_MODEL_LOCAL = "sentence-transformers/all-MiniLM-L6-v2"
OPENAI_API_BASE = os.environ.get("OPENAI_API_BASE", "")  # e.g. http://server:11434/v1 for Ollama
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
OPENAI_EMBEDDING_MODEL = os.environ.get("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")

# LLM: "local" (future: llama-cpp-python) or "remote" (OpenAI-compatible API)
LLM_BACKEND = os.environ.get("LLM_BACKEND", "remote")
LLM_MODEL = os.environ.get("LLM_MODEL", "gpt-3.5-turbo")  # or e.g. llama3.1 for Ollama

# Chatbot: "knowledge_only" (retrieval + pre-baked, no LLM) or "llm" (use rag_response with synthesis)
CHATBOT_MODE = os.environ.get("CHATBOT_MODE", "knowledge_only")

# RAG
RAG_TOP_K = int(os.environ.get("RAG_TOP_K", "4"))
CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", "1000"))
CHUNK_OVERLAP = int(os.environ.get("CHUNK_OVERLAP", "50"))
