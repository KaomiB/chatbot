"""
HSA chatbot content script: decision-tree topics with refined answers and citations.
Single source of truth for suggested-topic buttons; every button maps to a scripted response.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

@dataclass
class Topic:
    id: str
    label: str
    answer: str
    citations: list[str]

# Topic tree: each suggested button has a guaranteed answer and optional citations.
TOPICS: list[Topic] = [
    Topic(
        id="what_is_hsa",
        label="What is an HSA?",
        answer="""An **HSA (Health Savings Account)** is a tax-advantaged savings account for qualified medical expenses. It must be paired with an **HSA-qualified High Deductible Health Plan (HDHP)**.

**Key things to know:**
- **You** own the account—not your employer. It stays with you when you change jobs.
- Money **rolls over** year to year; there’s no “use it or lose it” like with an FSA.
- You can use it for **current health costs** (copays, prescriptions, therapy) or **save it for retirement** healthcare.
- Many people don’t know: you can **invest** HSA funds (stocks, funds) and let them grow tax-free.""",
        citations=["IRS Publication 969", "HSA Knowledge Base – Core Facts"],
    ),
    Topic(
        id="eligibility",
        label="Am I eligible for an HSA?",
        answer="""To contribute to an HSA you must meet **all** of these:

1. **Be covered by an HSA-qualified HDHP** on the first day of the month (e.g. minimum deductible $1,650 single / $3,300 family for 2025).
2. **Have no other health coverage** (with limited exceptions—e.g. dental, vision, or a “limited purpose” FSA is OK).
3. **Not be on Medicare.**
4. **Not be claimed as a dependent** on someone else’s tax return.

If you’re on your **parents’ plan** but file your own taxes and aren’t their dependent, you can often have your **own** HSA—and sometimes contribute the full family max. (See “Can I have an HSA on my parents’ plan?”)""",
        citations=["IRS Publication 969", "NotebookLLMHSA – Eligibility", "HSA Knowledge Base – Eligibility"],
    ),
    Topic(
        id="triple_tax",
        label="What is the triple tax advantage?",
        answer="""The **triple tax advantage** is why many people call the HSA the best account in the tax code:

1. **Tax-free contributions** — Money goes in pre-tax (if via payroll) or is tax-deductible (if you contribute yourself). That lowers your taxable income now.
2. **Tax-free growth** — Interest and investment earnings in the account are **not** taxed.
3. **Tax-free withdrawals** — Money you take out for **qualified medical expenses** is never taxed.

**Bonus:** With payroll deduction you also avoid **FICA** (7.65%) on that money—something 401(k) contributions don’t get. So for the “next dollar” of savings, the HSA can beat a 401(k).""",
        citations=["HSA Knowledge Base – Triple Tax Advantage", "NotebookLLMHSA – Core Definitions"],
    ),
    Topic(
        id="hsa_vs_401k",
        label="HSA vs 401(k) — which first?",
        answer="""A simple order that works for many young adults:

1. **401(k) up to the employer match** — Don’t leave free money on the table.
2. **Max out the HSA next** — It’s triple-tax advantaged (often better than 401(k) on that next dollar) and can act like a retirement account after 65. Plus it’s portable if you change jobs.
3. **Then** put more into 401(k) or an IRA with what’s left.

So: match first, then HSA, then the rest. If you’re on a family HDHP (e.g. parents’ plan) and eligible, the family HSA limit is much higher—so that “HSA next” step can be powerful.""",
        citations=["NotebookLLMHSA – Scenario B: Healthy Saver vs 401(k)", "HSA Knowledge Base – HSA vs Other Accounts"],
    ),
    Topic(
        id="parents_plan",
        label="Can I have an HSA on my parents' plan?",
        answer="""**Yes, in a common situation.** If you’re covered by your **parents’ family HDHP** but you’re **not** claimed as their tax dependent (e.g. you have a job and file your own return), you can open **your own** HSA.

**The “superpower”:** Because you’re on a **family** plan, you can contribute up to the **full family maximum** ($8,750 in 2026) to **your** account—on top of whatever your parents put in theirs. That’s a lot of tax-advantaged space early in life.

**Check:** You must actually be eligible (no other coverage, not on Medicare, not a dependent). When in doubt, check with your plan or a tax pro.""",
        citations=["NotebookLLMHSA – Scenario A: Adult Child Loophole", "HSA Knowledge Base – Young Adult Scenarios"],
    ),
    Topic(
        id="qualified_expenses",
        label="What counts as a qualified medical expense?",
        answer="""**You can use HSA money tax-free for things like:**

- Doctor visits, hospital stays, surgery, ER
- **Mental health:** therapy, psychiatric care
- Dental (cleanings, fillings, braces) and vision (exams, glasses, contacts, Lasik)
- Prescription drugs and many **over-the-counter** items (pain relievers, allergy meds, menstrual products, etc.)
- Medical supplies (e.g. diabetic supplies), acupuncture, chiropractic

**Generally not allowed** (taxable + possible penalty): insurance premiums (with specific exceptions), cosmetic procedures, gym memberships or general vitamins unless prescribed.

**Insurance exceptions:** COBRA, premiums while on unemployment, long-term care insurance, and Medicare (Parts A, B, D) *after* 65 can be paid from the HSA.""",
        citations=["IRS Publication 502", "NotebookLLMHSA – Qualified Expenses", "HSA Knowledge Base – QMEs"],
    ),
    Topic(
        id="contribution_limits",
        label="What are the contribution limits?",
        answer="""**2025 limits (typical):**

| Coverage        | Annual limit |
|-----------------|-------------|
| Self-only       | $4,300      |
| Family          | $8,550      |
| Catch-up (55+)  | +$1,000     |

**2026 (when available):** Individual about $4,400, family about $8,750 (plus catch-up).

**Important:** The limit includes **all** contributions (yours, employer’s, family). You can contribute for a tax year until the **tax filing deadline** (usually April 15) of the *next* year. There’s **no** “use it or lose it”—money stays yours and can be invested.""",
        citations=["IRS Publication 969", "NotebookLLMHSA – 2026 Rules & Limits", "HSA Knowledge Base – Contribution Limits"],
    ),
    Topic(
        id="first_job",
        label="I just got my first job — where do I start?",
        answer="""Start small so it doesn’t feel overwhelming:

- **See if your employer offers an HDHP + HSA.** If they do, even **$50 per paycheck** into the HSA adds up and gives you an immediate tax break.
- **Use payroll deduction** if you can—easiest and you save FICA too.
- Keep funds in **cash** at first until you’re comfortable; you can switch to investing later.
- Focus on the **immediate benefit:** every dollar you put in lowers your taxable income. For example, $1,000 in the HSA might only “cost” you ~\$650 after tax savings (depending on your bracket).

Young adults often get a lot of benefit info at once; it’s OK to prioritize one thing (like “sign up for the HSA and set a small amount”) and learn more over time.""",
        citations=["NotebookLLMHSA – Scenario 3", "HSA Knowledge Base – Young Adult Scenarios"],
    ),
    Topic(
        id="therapy_mental_health",
        label="Can I use my HSA for therapy or mental health?",
        answer="""**Yes.** Mental health therapy and psychiatric care are **qualified medical expenses**. You can use HSA funds tax-free for sessions, prescriptions for mental health, and many related costs.

**Why it matters for young adults:** A lot of people cut mental health first when money is tight. Putting even part of your HSA toward therapy effectively makes it cheaper (you get a tax break on the contribution). For example, a $4,300 HSA contribution might save you ~\$946 in federal taxes alone (in the 22% bracket)—so the “real” cost of using the HSA for therapy is lower than paying fully out of pocket.""",
        citations=["HSA Knowledge Base – QMEs, Scenario 2", "NotebookLLMHSA – Qualified Expenses"],
    ),
    Topic(
        id="never_sick",
        label="I'm healthy / never go to the doctor — why an HSA?",
        answer="""Even if you rarely see a doctor, an HSA can still be a great move:

- **Use it for things you might not think of:** therapy, contacts, dental cleanings, birth control, preventive care, prescriptions when you need them.
- **It rolls over forever**—no “use it or lose it.” Money you don’t spend stays in the account and can be **invested** (e.g. in funds). Over decades that can grow into a big tax-free pot for healthcare in retirement—or for a future year when you do have more expenses.
- **It’s portable**—if you change jobs, the account and any investments go with you.

So it’s not only for people who go to the doctor a lot; it can double as a long-term, tax-advantaged savings bucket that happens to be great for health costs when they come up.""",
        citations=["NotebookLLMHSA – Scenario D: Invincible Skeptic", "HSA Knowledge Base – Misconceptions"],
    ),
    Topic(
        id="shoebox_strategy",
        label="What's the 'shoebox' or receipt strategy?",
        answer="""The **“shoebox” strategy** (sometimes called receipt stashing):

1. **Pay a medical bill with cash** from your checking account (not from the HSA).
2. **Save the receipt** (digitally or physically—“shoebox”).
3. **Leave the same amount in your HSA** and, if you can, **invest** it.
4. **Years later** you can “reimburse” yourself from the HSA for that old bill—**tax-free**—and keep all the investment growth.

**Example:** You pay a $200 bill with cash today. You leave $200 in the HSA invested. In 20 years that $200 might be $800. You can then withdraw $200 tax-free (using the old receipt) and keep the extra $600 growing. There’s **no time limit** on when you reimburse, as long as the expense happened after you opened the HSA.""",
        citations=["NotebookLLMHSA – Scenario C: Shoebox Strategy", "HSA Knowledge Base – Recordkeeping"],
    ),
]

# Ordered list of topic labels for buttons (same order as TOPICS unless we want a subset).
SUGGESTED_TOPIC_LABELS: list[str] = [t.label for t in TOPICS]


def get_topic_by_id(topic_id: str) -> Optional[Topic]:
    for t in TOPICS:
        if t.id == topic_id:
            return t
    return None


def get_topic_by_label(label: str) -> Optional[Topic]:
    label_clean = label.strip()
    for t in TOPICS:
        if t.label.strip() == label_clean:
            return t
    return None


def get_all_topics() -> list[Topic]:
    return list(TOPICS)
