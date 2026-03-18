# HSA Chatbot

An HSA (Health Savings Account) guide built with Streamlit: explore by topic, get step-by-step task breakdowns, use a scenario-based trade-off tool, and ask in your own words on the Explore page.

- **HSA topics (Explore)** — Browse answers by topic; ask free-form questions (we match to the closest topic or use our knowledge base / AI with a disclaimer). Filter by pace in the sidebar.
- **Task Breaker** — Pick an HSA scenario and get a checklist (overview, standard, or step-by-step).
- **Trade-Off Tool** — Answer a few questions and get a tailored recommendation.

## Run locally

```bash
cd chatbot
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
streamlit run HSA_Topics.py
```

See [GETTING_STARTED.md](GETTING_STARTED.md) for more detail.

## Deploy (Streamlit Community Cloud.)

1. Push this repo to GitHub .
2. Go to [share.streamlit.io](https://share.streamlit.io), sign in with GitHub, and create a **New app**.
3. Set **Main file path** to `HSA_Topics.py`.
4. Add secrets in the Cloud dashboard (e.g. `OPENAI_API_KEY`) if you want AI/knowledge-base answers on the Explore page. See [DEPLOY.md](DEPLOY.md).

## Secrets (optional)

For **Explore page** (closest-topic matching uses local embeddings; optional retrieval/AI uses `OPENAI_API_KEY`) and **Task Breaker** (custom task breakdown), create `.streamlit/secrets.toml` (never commit it). Copy from `.streamlit/secrets.toml.example` and add your key.

## Local dark-mode screenshot (optional)

```bash
bash scripts/capture-dark-streamlit-screenshot.sh
```

Writes **`screenshots/dark-streamlit-hsa.png`** (folder is gitignored). Override URL with `STREAMLIT_DARK_URL=...` for a local dev server.

#testing