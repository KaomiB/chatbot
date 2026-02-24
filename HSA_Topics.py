"""
HSA topics: explore by topic (no chat — pre-recorded answers from content script, pre-baked Q&A, or retrieval).
"""
import re
import streamlit as st

from config import CHATBOT_MODE
from content_script import (
    DEFAULT_WELCOME_TOPIC_IDS,
    get_all_topics,
    get_topic_by_id,
    get_topic_by_label,
    get_topic_by_suggested_question,
    get_topic_difficulty,
    get_topics_by_difficulty_filter,
    get_welcome_topics,
)

# Welcome: 5 default topic buttons (what_is_hsa, young_adults, triple_tax, misconceptions, qualified_expenses).
WELCOME_TOPICS = [t.label for t in get_welcome_topics()]


def _format_suggested_topics(labels: list[str]) -> str:
    return "\n".join(f"- {t}" for t in labels)

# Greeting triggers (normalized).
GREETING_PATTERNS = re.compile(
    r"^(hi|hello|hey|howdy|hiya|yo|greetings|good\s*(morning|afternoon|evening)|hey\s+there|what'?s\s+up|sup)[\s!.]*$",
    re.IGNORECASE,
)

WELCOME_MESSAGE = f"""Hi! I'm here to help with **Health Savings Account (HSA)** questions.

You can ask me about:

{_format_suggested_topics(WELCOME_TOPICS)}

Type a question below or pick a topic to get started."""

GREETING_RESPONSE = f"""Hi! I'm here to help with HSA questions.

Here are some things you can ask:

{_format_suggested_topics(WELCOME_TOPICS)}"""

# Fallbacks: redirect to suggested topics instead of technical messages.
FALLBACK_NO_INDEX = f"""I don't have an answer from the knowledge base right now, but here are topics I can help with once the index is built:

{_format_suggested_topics(WELCOME_TOPICS)}

*Tip: Run `python memory_builder.py` from the project folder to index the HSA docs.*"""

FALLBACK_NO_MATCH = f"""I couldn't find anything about that in my knowledge base. Here are topics I can help with:

{_format_suggested_topics(WELCOME_TOPICS)}

Try asking one of these, or rephrase your question."""


def _is_greeting(text: str) -> bool:
    t = text.strip()
    if not t or len(t) > 80:
        return False
    if GREETING_PATTERNS.match(t):
        return True
    # Very short and only common greeting-like words
    words = set(t.lower().split())
    return words <= {"hi", "hello", "hey", "howdy", "yo", "sup", "hiya"} and len(words) <= 3


def get_assistant_response(user_message: str) -> tuple[str, list[str], "Topic | None"]:
    """
    Return (reply_text, citations, topic_used).
    topic_used is set when we match by label or suggested_question so the UI can show "Related topics" buttons.
    Order: greeting -> exact label -> suggested_question match -> pre-baked -> retrieval/LLM.
    """

    # Greeting
    if _is_greeting(user_message):
        return GREETING_RESPONSE, [], None

    # Exact match to a suggested topic button (label)
    topic = get_topic_by_label(user_message)
    if topic:
        return topic.answer, list(topic.citations), topic

    # Free-text match to any topic's suggested_questions
    topic = get_topic_by_suggested_question(user_message)
    if topic:
        return topic.answer, list(topic.citations), topic

    # Pre-baked Q&A (keyword match)
    try:
        from prebaked_qa import get_prebaked_answer
        prebaked = get_prebaked_answer(user_message)
        if prebaked:
            return prebaked, [], None
    except Exception:
        pass

    # Knowledge-only retrieval (no LLM)
    if CHATBOT_MODE == "knowledge_only":
        try:
            from rag import knowledge_only_response
            reply, citations = knowledge_only_response(user_message)
            if reply:
                return reply, citations, None
            return FALLBACK_NO_MATCH, [], None
        except Exception:
            return FALLBACK_NO_INDEX, [], None

    # LLM mode
    if CHATBOT_MODE == "llm":
        try:
            from rag import rag_response
            reply = rag_response(user_message)
            if reply:
                return reply, [], None
        except Exception:
            pass
    return FALLBACK_NO_MATCH, [], None


def _set_pending(label: str):
    """Callback for topic buttons — sets pending_prompt before Streamlit reruns."""
    st.session_state.pending_prompt = label


def _next_is_popular_only(next_ids: list[str]) -> bool:
    """True when next_suggested_topics is exactly the 7 popular topics (no separate 'related' block)."""
    return set(next_ids) == set(DEFAULT_WELCOME_TOPIC_IDS) and len(next_ids) == len(DEFAULT_WELCOME_TOPIC_IDS)


# Page config and title (topics/facts, not chat)
st.set_page_config(page_title="Explore HSA by topic", page_icon="📋")

# Sidebar "Go to topic" button + header block (match healandsave-all-palettes: .m-tag / .m-title)
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] .stButton > button {
        background-color: #FFB8D1 !important;
        color: #1e1e1e !important;
    }
    .m-tag { font-size: 0.90rem; letter-spacing: 0.1em; text-transform: uppercase; opacity: 0.4; margin-bottom: 4px; }
    .m-title {font-size: 2.5rem; font-weight: 700; line-height: 1.2; margin-bottom: 4px; }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="m-tag">Explore</div><div class="m-title">HSA by Topic</div>',
    unsafe_allow_html=True,
)
st.caption("Browse at your own pace & find answers instantly. No sign-up needed.")

# Session state: list of {role, content, citations?, topic_id?}; topic_id = for "You might also ask" buttons
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "assistant", "content": WELCOME_MESSAGE, "citations": [], "topic_id": None})

# Topic buttons: clicking one sends that question (set as pending so we process on rerun)
if "pending_prompt" not in st.session_state:
    st.session_state.pending_prompt = None

# Capture pending prompt so we process it before "Choose a popular topic" (so topic appears under the response)
_prompt_from_button = st.session_state.pending_prompt
if _prompt_from_button:
    st.session_state.pending_prompt = None

# Render chat history
for idx, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        # Related topics (skip when they're the same as popular topics to avoid duplicate)
        if msg["role"] == "assistant" and msg.get("topic_id"):
            topic = get_topic_by_id(msg["topic_id"])
            if topic and topic.next_suggested_topics and not _next_is_popular_only(topic.next_suggested_topics):
                st.caption("Choose a related topic:")
                follow_cols = st.columns(min(3, len(topic.next_suggested_topics)))
                for i, next_id in enumerate(topic.next_suggested_topics):
                    next_t = get_topic_by_id(next_id)
                    if next_t:
                        with follow_cols[i % len(follow_cols)]:
                            st.button(next_t.label, key=f"follow_{idx}_{next_id}",
                                      on_click=_set_pending, args=(next_t.label,))
                st.caption("**Next:** Break a task into steps → **Task Breaker** · Ask in your own words → **AI Chat** (sidebar).")
        if msg["role"] == "assistant" and msg.get("citations"):
            with st.expander("Sources / citations"):
                for c in msg["citations"]:
                    st.caption(c)

# Other ways to interact: sidebar (with difficulty filter)
with st.sidebar:
    st.subheader("Browse topics")
    difficulty_filter = st.selectbox(
        "Filter by pace",
        options=["All", "Good starting point", "A little more detail", "When you're ready"],
        key="sidebar_difficulty_filter",
    )
    filtered_topics = get_topics_by_difficulty_filter(
        None if difficulty_filter == "All" else difficulty_filter
    )
    # Build options: "🟢 What is an HSA?" etc.
    topic_options = ["— Pick a topic —"] + [
        f"{get_topic_difficulty(t.id)['emoji']} {t.label}" if get_topic_difficulty(t.id) else t.label
        for t in filtered_topics
    ]
    chosen_display = st.selectbox(
        "All topics" if difficulty_filter == "All" else difficulty_filter,
        options=topic_options,
        key="sidebar_topic_select",
    )
    if st.button("Go to topic", key="sidebar_go") and chosen_display and chosen_display != "— Pick a topic —":
        chosen_label = chosen_display
        for t in get_all_topics():
            d = get_topic_difficulty(t.id)
            if d and chosen_display == f"{d['emoji']} {t.label}":
                chosen_label = t.label
                break
            elif chosen_display == t.label:
                chosen_label = t.label
                break
        st.session_state.pending_prompt = chosen_label

# Process prompt (from topic button or chat input)
prompt = _prompt_from_button or st.chat_input("Ask about HSAs...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Show the user's selection/question in this run (otherwise it only appears after the next action)
    with st.chat_message("user"):
        st.markdown(prompt)

    full_reply, citations, topic_used = get_assistant_response(prompt)
    # Append assistant message *before* rendering follow-up buttons, so clicking a
    # follow-up and rerunning doesn't drop this reply from history
    st.session_state.messages.append({
        "role": "assistant",
        "content": full_reply,
        "citations": citations,
        "topic_id": topic_used.id if topic_used else None,
    })
    with st.chat_message("assistant"):
        st.markdown(full_reply)
        if topic_used and topic_used.next_suggested_topics and not _next_is_popular_only(topic_used.next_suggested_topics):
            st.caption("Choose a related topic:")
            follow_cols = st.columns(min(3, len(topic_used.next_suggested_topics)))
            for i, next_id in enumerate(topic_used.next_suggested_topics):
                next_t = get_topic_by_id(next_id)
                if next_t:
                    with follow_cols[i % len(follow_cols)]:
                        st.button(next_t.label, key=f"follow_new_{next_id}",
                                  on_click=_set_pending, args=(next_t.label,))
            st.caption("**Next:** Break a task into steps → **Task Breaker** · Ask in your own words → **AI Chat** (sidebar).")
        if citations:
            with st.expander("Sources / citations"):
                for c in citations:
                    st.caption(c)

# Popular topic buttons — after all messages (including the one we just added) so they appear under the response
_last_msg = st.session_state.messages[-1] if st.session_state.messages else None
_last_topic = get_topic_by_id(_last_msg["topic_id"]) if _last_msg and _last_msg.get("topic_id") else None
_show_another = _last_topic and _last_topic.next_suggested_topics and _next_is_popular_only(_last_topic.next_suggested_topics)
if len(st.session_state.messages) >= 1:
    st.caption("Choose another popular topic:" if _show_another else "Choose a popular topic:")
    cols = st.columns(2)
    for i, topic_label in enumerate(WELCOME_TOPICS):
        with cols[i % 2]:
            st.button(topic_label, key=f"topic_{i}",
                      on_click=_set_pending, args=(topic_label,))

# Footer: gentle permission to leave + no dead ends
st.divider()
st.caption("There's a lot here. Bookmarking one topic and coming back is completely fine.")
st.caption("**Explore:** Task Breaker (break tasks into steps) · AI Chat (ask in your own words) — use the sidebar.")
