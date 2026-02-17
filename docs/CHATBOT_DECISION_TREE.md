# HSA Chatbot: Decision Tree & Structure Plan

This document outlines the overall structure of the HSA chatbot content and decision flow, with a focus on **young adults** who are new to or unsure about HSAs.

---

## 1. High-level decision tree

```
Start
  ├── Greeting (hi / hello / hey)
  │     └── Respond with welcome + suggested topics
  │
  ├── Exact topic button click (e.g. "What is an HSA?")
  │     └── Return scripted answer + citations from content_script.py
  │
  ├── Free-text question
  │     ├── Keyword match (prebaked_qa) → pre-baked answer
  │     ├── RAG (index built) → retrieved chunks + citations
  │     └── No match → Redirect: "Here are topics I can help with…" + topic list
  │
  └── (Future: follow-up / "tell me more" could branch to sub-topics)
```

**No LLM in the default path.** Every suggested-topic **button** maps to a single scripted answer in `content_script.py`, so each button is guaranteed a response with citations.

---

## 2. Content tree (topics)

Topics are ordered for **discovery**: basics first, then eligibility, then “why it’s good,” then comparisons and young-adult situations.

| # | Topic ID            | Button label                              | When to use |
|---|---------------------|-------------------------------------------|-------------|
| 1 | what_is_hsa         | What is an HSA?                           | "What is this?" / total beginner |
| 2 | eligibility         | Am I eligible for an HSA?                 | "Can I get one?" |
| 3 | triple_tax          | What is the triple tax advantage?        | "Why HSA?" / comparing accounts |
| 4 | hsa_vs_401k         | HSA vs 401(k) — which first?              | Prioritization / first job |
| 5 | parents_plan        | Can I have an HSA on my parents' plan?    | Young adults on family HDHP |
| 6 | qualified_expenses  | What counts as a qualified medical expense? | "Can I pay for X?" |
| 7 | contribution_limits | What are the contribution limits?        | Numbers / planning |
| 8 | first_job           | I just got my first job — where do I start? | New to benefits |
| 9 | therapy_mental_health | Can I use my HSA for therapy or mental health? | Mental health / Gen Z |
|10 | never_sick          | I'm healthy / never go to the doctor — why an HSA? | "I don't need it" |
|11 | shoebox_strategy    | What's the 'shoebox' or receipt strategy? | Savers / advanced |

---

## 3. Questions that apply to young adults (and “clueless” users)

These map to the tree above and to the script/prebaked content.

**Orientation (“I don’t know what this is”)**
- What is an HSA?
- How is it different from my regular savings / FSA / 401(k)?
- Do I need one?

**Eligibility (“Can I even have one?”)**
- Am I eligible for an HSA?
- I’m on my parents’ insurance — can I still have an HSA?
- I have another plan / FSA — does that block me?

**Motivation (“Why bother?”)**
- What is the triple tax advantage?
- I’m healthy / never go to the doctor — why would I want one?
- Why would I choose an HSA over a 401(k)?

**Practical use (“How do I use it?”)**
- What can I pay for with my HSA? (qualified expenses)
- Can I use it for therapy / mental health / birth control / contacts?
- How much can I put in? (contribution limits)

**Life stage**
- I just got my first job — where do I start?
- I have student debt — should I still put money in an HSA?
- What’s the “shoebox” or receipt strategy?

**Scenarios (prebaked keyword matches)**
- Parents’ plan / “adult child” / family max
- HSA vs 401(k) order (match → HSA → rest)
- Shoebox / pay cash, save receipt, reimburse later
- “I’m never sick” / invincible skeptic

---

## 4. Where content lives

| Source                | Role |
|-----------------------|------|
| `content_script.py`   | **Scripted answers** for every suggested-topic button; includes citations. Single source of truth for button → answer. |
| `prebaked_qa.py`      | **Keyword-based** answers for free-text (e.g. "parents plan", "401k", "shoebox"). No citations today; can add later. |
| `docs/*.md`           | **RAG index** (after `memory_builder.py`). Used when no script/prebaked match; answers are retrieved chunks + source as citation. |

---

## 5. Citations

- **Scripted answers:** Each topic in `content_script.py` has a `citations` list (e.g. "IRS Publication 969", "HSA Knowledge Base – Core Facts"). These are shown in the **Sources / citations** expander under the bot reply.
- **RAG answers:** Citations come from chunk metadata (`source` path or doc name). Same expander.
- **Pre-baked:** Currently no citations; could add a `citations` field to prebaked entries later.

---

## 6. Possible extensions

- **Follow-up branches:** e.g. After "What is an HSA?" offer "Am I eligible?" or "What can I pay for?"
- **Sub-topics:** Under "Qualified expenses" add buttons for "Mental health," "Dental," "OTC," etc.
- **Simple flow:** "I'm 24 and on my parents' plan" → short flow that asks dependent status and then gives the Adult Child answer.
- **State-specific:** Link to state tax note (e.g. CA, NJ) from eligibility or contribution limits.

This structure keeps the bot predictable (every button has a response), citable (sources in the UI), and aligned with young adults who are new to or unsure about HSAs.
