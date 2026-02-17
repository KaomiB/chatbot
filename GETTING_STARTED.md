# How to Start the Project

This project is an **HSA (Health Savings Account) chatbot** that uses **Python**, a **virtual environment**, and **Streamlit**. By default it runs in **knowledge-base only** mode (no LLM): answers come from the HSA docs in `docs/` and from pre-baked scenario Q&A.

## Prerequisites

- **Python 3.9–3.13** (or 3.14 if supported)
- A terminal
- (Optional) A code editor (e.g. VS Code)

## 1. Go to the project folder

```bash
cd /path/to/chatbot
```

(Use the actual path to your `chatbot` project.)

## 2. Create a virtual environment (first time only)

If the `.venv` folder does not exist yet:

```bash
python -m venv .venv
```

This creates a `.venv` directory with an isolated Python environment.

## 3. Activate the environment

Run **one** of these, depending on your OS:

**Windows (Command Prompt):**
```bash
.venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**macOS and Linux:**
```bash
source .venv/bin/activate
```

When it’s active, you’ll see `(.venv)` at the start of your prompt.

## 4. Install dependencies (first time or after pull)

With the environment activated:

```bash
pip install streamlit
```

Or install all dependencies (Streamlit + RAG + PDF ingest):

```bash
pip install -r requirements.txt
```

## 5. Run the app

**Main app (chatbot):**
```bash
streamlit run HSA_Topics.py
```

A browser tab will open with the chat UI. If the command fails, try:
```bash
python -m streamlit run HSA_Topics.py
```

**Optional – Streamlit demo (sanity check):**
```bash
streamlit hello
```

## 6. HSA knowledge-base (default: no LLM)

The chatbot runs in **knowledge-base only** mode by default: it answers from retrieved chunks and pre-baked Q&A only. **No LLM is used** (no API keys required).

1. **Install RAG dependencies** (needed for retrieval):  
   `pip install -r requirements.txt`
2. **Build the vector index** from the docs in `docs/` (HSA knowledge base is already there):  
   `python memory_builder.py`
3. Run the app: `streamlit run HSA_Topics.py`. Questions are answered from the knowledge base; if nothing is found, you’ll see a short fallback message.

To re-enable LLM synthesis later, set `CHATBOT_MODE=llm` and configure `OPENAI_API_KEY` or `OPENAI_API_BASE` (see [config.py](config.py)).

---

## Quick reference

| Step              | Command (Linux/macOS)           |
|-------------------|---------------------------------|
| Activate venv     | `source .venv/bin/activate`    |
| Install Streamlit | `pip install streamlit`         |
| Run demo          | `streamlit hello`               |
| Run your app      | `streamlit run HSA_Topics.py`  |

Always activate the virtual environment before running or installing anything in this project.
