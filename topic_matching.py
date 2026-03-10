"""
Semantic matching of free-form user questions to the closest HSA topic.
Uses embeddings to find the best-matching pre-programmed topic when there's no exact match.
"""
from __future__ import annotations

from content_script import Topic, get_all_topics


def _cosine_similarity(a: list[float], b: list[float]) -> float:
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = sum(x * x for x in a) ** 0.5
    norm_b = sum(x * x for x in b) ** 0.5
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


# Minimum similarity (0–1) to consider a topic a "match"
CLOSEST_TOPIC_THRESHOLD = 0.45


def get_closest_topic(user_message: str) -> tuple[Topic | None, float]:
    """
    Embed the user message and all topics (label + suggested questions), return the
    closest topic and its similarity score. Returns (None, 0.0) if no topic meets
    the threshold or if embedding fails.
    """
    if not user_message or not user_message.strip():
        return None, 0.0
    try:
        from embeddings import embed
    except Exception:
        return None, 0.0
    topics = get_all_topics()
    if not topics:
        return None, 0.0
    # One search string per topic: label + suggested questions so "how do I invest" matches investment topic
    search_texts = [
        f"{t.label} {' '.join(t.suggested_questions)}" for t in topics
    ]
    try:
        query_emb = embed([user_message.strip()])
        topic_embs = embed(search_texts)
    except Exception:
        return None, 0.0
    if not query_emb or not topic_embs or len(topic_embs) != len(topics):
        return None, 0.0
    q = query_emb[0]
    best_score = 0.0
    best_topic: Topic | None = None
    for i, t_emb in enumerate(topic_embs):
        sim = _cosine_similarity(q, t_emb)
        if sim > best_score:
            best_score = sim
            best_topic = topics[i]
    if best_topic and best_score >= CLOSEST_TOPIC_THRESHOLD:
        return best_topic, best_score
    return None, best_score
