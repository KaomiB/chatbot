# Prompt: Build HSA Chatbot Q&A Architecture (Implementation-Ready)

**Copy the text below and paste it into an AI that has access to your HSA knowledge base (e.g. HealthEquity Guidebook, HSAs For Dummies, WageWorks, Generational HSA Divide, etc.).** The goal is to get back a **structured Q&A architecture** we can implement in code—not just quotes, but nodes, questions, answers, and citations in a consistent format.

---

## Prompt (copy from here)

I'm building a **scripted HSA chatbot** for young adults (including people who are new to or unsure about HSAs). We already have a **quote library** with sourced excerpts organized by topic (see attached or referenced file: `hsa_chatbot_quote_library.md`). We need you to help us turn that into an **implementation-ready Q&A architecture**—clear structure we can plug into our code.

### What we need from you

1. **Decision tree structure**
   - Define **top-level topics** (nodes) that match or refine the quote library’s sections (e.g. What is an HSA, Triple Tax Advantage, Eligibility, Contribution Limits, Qualified Expenses, Investment, HSA vs 401(k)/FSA, Portability, Age 65/Medicare, Young Adults, Recordkeeping, Misconceptions, etc.).
   - For each topic node, specify:
     - **topic_id** (short snake_case, e.g. `what_is_hsa`, `triple_tax`, `qualified_expenses`).
     - **display_label** (short phrase for a button or menu, e.g. "What is an HSA?").
     - **2–5 suggested user questions** that should lead to this topic (e.g. "What is an HSA?", "What's an HSA?", "Explain HSAs" → same node).
     - **Optional follow-up / next suggested topics** (e.g. after "What is an HSA?" suggest "Am I eligible?" and "What is the triple tax advantage?").

2. **One primary answer per topic (implementation format)**
   - For each topic, write **one concise answer** (2–5 short paragraphs) that we can show as the bot’s reply. Prefer language that:
     - Uses our quote library where possible (you can paraphrase or lightly edit for flow).
     - Is clear for young adults and first-time HSA learners.
     - Stays accurate and within the sources (no invented rules).
   - **Citations:** For each answer, list **exact citations** in a consistent format we can store and display, e.g.:
     - `HealthEquity HSA Guidebook, p. 25`
     - `HSAs For Dummies, Optum Financial Special Edition, p. 24`
   - If an answer draws from multiple quotes, list every source used for that answer.

3. **Optional: sub-topics or sub-questions**
   - For big topics (e.g. Qualified Medical Expenses), optionally break into **sub-topics** with their own short answer + citations (e.g. "Dental & vision," "Mental health," "OTC & prescriptions," "Insurance premiums exceptions"). We can implement these as extra buttons or follow-up nodes.

4. **Suggested flow for “clueless” or new users**
   - Propose an **order** of topics for first-time users (e.g. What is an HSA? → Triple tax → Eligibility → What can I pay for? → Contribution limits → …). This will guide our default “suggested topics” order and any simple flow logic.

5. **Output format**
   - Please give the decision tree and Q&A in a **structured form** we can copy into code or config, for example:
     - **Option A:** A markdown document with clear sections and, for each topic, blocks like:
       ```text
       ## topic_id: what_is_hsa
       display_label: "What is an HSA?"
       suggested_questions: ["What is an HSA?", "What's an HSA?", "Explain HSA"]
       next_suggested_topics: [eligibility, triple_tax]
       answer: |
         [2–5 paragraph answer here]
       citations:
         - "HealthEquity HSA Guidebook, p. 25"
         - "HSAs For Dummies, Optum Financial Special Edition, Introduction, p. 1"
       ```
     - **Option B:** A table (e.g. CSV or markdown table) with columns: topic_id, display_label, suggested_questions (pipe-separated), answer (or summary), citations (pipe-separated).
   - Whichever you use, keep it **consistent** so we can parse it or copy-paste into our Python content script.

### Context to align with

- **Audience:** Young adults (e.g. 18–30), including people who have never had an HSA or are on a parent’s plan, and people who are skeptical (“I’m healthy, why do I need this?”).
- **Existing quote library:** Our `hsa_chatbot_quote_library.md` is organized into 17 sections (What is an HSA, Triple Tax, Eligibility, Contribution Limits, Qualified Expenses, Investment, HSA vs Other Accounts, Funding, Portability, Age 65 & Medicare, Retirement, Recordkeeping, HSA-Qualified Plans, Young Adults, Complementary Accounts, Misconceptions, Decision-Making). Use that as the basis for your topic nodes; you can merge or split sections if it makes the tree clearer.
- **Recommended flow** (from our notes): Start with What is an HSA? / Triple Tax → Eligibility → Qualified Expenses → Investment → Comparisons → Life-stage content (young adults, age 65+, retirement). Your suggested flow can refine this.
- **No LLM:** Our bot is scripted only. Every button or chosen question maps to exactly one answer (plus citations). So we need a **complete** set of topic nodes and answers—no “generate at runtime.”

### What we will do with your output

- We will add or update **topic nodes** in our `content_script.py` (each with id, label, answer, citations).
- We will use **suggested_questions** to improve matching when users type free text (e.g. in a prebaked Q&A layer).
- We will use **next_suggested_topics** to show “You might also ask…” or follow-up buttons.
- We will display **citations** under each answer in the UI.

Please produce the full decision tree and all topic answers with citations in the structured format above. If the full set is very long, you may deliver the first 8–10 topics in full format and the rest in a shorter summary form, as long as we have enough to implement the main flow.

---

## End of prompt

**After you get the response:** You can paste the AI’s structured output into a new file (e.g. `docs/QA_ARCHITECTURE_FROM_KB.md`) and we can then map it into `content_script.py` and any prebaked Q&A or follow-up logic.
