# Host the HSA chatbot online (GitHub + Streamlit Cloud)

Deploy the app so it **runs in the browser** for you and your group—no install for them, just a link.

---

## How it works

1. You push the project to GitHub.
2. You connect the repo to **Streamlit Community Cloud** (free).
3. Streamlit builds and hosts the app and gives you a URL like `https://your-app.streamlit.app`.
4. Anyone who opens that URL in a browser gets the chatbot. No Python, no terminal—it just works in the browser.

---

## Steps

### 1. Put the project on GitHub

- Create a new repo (e.g. `hsa-chatbot`) on GitHub.
- From your machine, push the contents of your `chatbot` folder. Don’t push `.venv` or `vector_store` (add them to `.gitignore` if you like).

**Requirements for Cloud:** The repo needs a `requirements.txt`. For this app (scripted answers + prebaked Q&A only), you only need Streamlit:

```
streamlit>=1.28.0
```

So either keep that as your `requirements.txt` in the repo or make sure it’s in the root.

### 2. Deploy on Streamlit Community Cloud

- Go to **[share.streamlit.io](https://share.streamlit.io)**.
- Sign in with GitHub.
- Click **New app**.
- **Repository:** `your-username/hsa-chatbot` (or your repo name).
- **Branch:** `main`.
- **Main file path:** `HSA_Topics.py`.
- Click **Deploy**.

### 3. Share the link

After the build finishes (usually a couple of minutes), you’ll see a URL like `https://hsa-chatbot-xxxx.streamlit.app`. Send that link to your group—they open it in any browser and use the chatbot.

---

**Summary:** Yes—with the GitHub route, the app is hosted by Streamlit and works from the browser for everyone with the link.
