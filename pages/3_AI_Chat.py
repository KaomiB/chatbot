"""
AI Chat page: conversational HSA help using OpenAI's API.
Uses the key in .streamlit/secrets.toml (OPENAI_API_KEY).
Emotionally-aware system prompt to reduce anxiety and overwhelm.
"""
import streamlit as st
from openai import OpenAI

# Emotionally-aware system prompt — addresses anxiety gap without changing backend
HSA_SYSTEM_PROMPT = """You are a calm, knowledgeable HSA guide for young adults who often feel anxious or overwhelmed about finances. Your job is two things equally: give accurate HSA information, AND make the person feel less stressed about it.

Rules:
- Never use urgent language ("you need to," "you should have," "don't miss out")
- If someone expresses confusion or stress, acknowledge it briefly before answering: "That's genuinely confusing — here's the clearer version."
- Keep answers short (3-5 sentences max unless asked for more detail)
- End every answer with one of: a next small step they could take, a reassurance that they don't have to decide right now, or an invitation to ask a follow-up
- If someone seems overwhelmed (asks multiple questions at once, says "I don't understand any of this"), respond to only ONE thing and say: "Let's just focus on this one piece first."
- Never make the person feel behind or like they've made a mistake"""

st.set_page_config(page_title="AI Chat (WIP)", page_icon="🤖")
st.title("AI Chat (WIP)")
st.caption("Ask in your own words. This is the only place with real conversational AI.")

# Get API key from Streamlit secrets
if "OPENAI_API_KEY" not in st.secrets:
    st.error(
        "**OpenAI API key not found.** Add it in `.streamlit/secrets.toml`:\n\n"
        "```toml\nOPENAI_API_KEY = \"your-key-here\"\n```"
    )
    st.stop()

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Session state for chat messages
if "ai_messages" not in st.session_state:
    st.session_state.ai_messages = []

# Show chat history
for msg in st.session_state.ai_messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Message the AI..."):
    st.session_state.ai_messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            messages_for_api = [
                {"role": "system", "content": HSA_SYSTEM_PROMPT},
                *[{"role": m["role"], "content": m["content"]} for m in st.session_state.ai_messages],
            ]
            stream = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages_for_api,
                stream=True,
            )
            reply = ""
            placeholder = st.empty()
            for chunk in stream:
                if chunk.choices[0].delta.content:
                    reply += chunk.choices[0].delta.content
                    placeholder.markdown(reply + "▌")
            placeholder.markdown(reply)
            st.session_state.ai_messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            st.error(f"API error: {e}")
            # Don't add failed reply to history

st.caption("**Next:** Explore by topic → **HSA topics** · Break a task into steps → **Task Breaker** (sidebar).")
