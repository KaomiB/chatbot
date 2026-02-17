# Sample document

This is a sample Markdown file for the RAG chatbot.

## What is RAG?

RAG stands for Retrieval-Augmented Generation. The system first retrieves relevant passages from a document store, then uses those passages as context when generating an answer.

## How to use

1. Add more `.md` files under `docs/`.
2. Run `python memory_builder.py` to rebuild the vector index.
3. Ask questions in the chat; answers will use retrieved context when the index exists.
