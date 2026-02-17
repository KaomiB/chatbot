"""
Pre-baked Q&A for key HSA scenarios. Checked before retrieval; no LLM.
Answers are from the knowledge base / NotebookLLMHSA scenarios.
"""
from __future__ import annotations

# (keywords or phrases to match in user message, answer text)
PREBAKED: list[tuple[list[str], str]] = [
    # Adult Child / parents' plan
    (
        ["parents", "parent's", "parents'", "mom", "dad", "family plan", "on my parents insurance", "adult child", "24", "loophole"],
        "**The \"Adult Child\" scenario:** If you're covered by your parents' family HDHP but you're not a tax dependent (e.g. you have a job and file your own taxes), you *can* open your **own** HSA. Even better: because you're on a *family* plan, you can contribute the **full family maximum** ($8,750 in 2026) to your own account, in addition to whatever your parents contribute to theirs.",
    ),
    # Triple tax advantage
    (
        ["triple tax", "triple-tax", "tax advantage", "what is the advantage", "why hsa", "better than 401"],
        "**The triple-tax advantage** is the big reason HSAs are so powerful:\n1. **Tax-free contributions** – Money goes in pre-tax (payroll) or is tax-deductible.\n2. **Tax-free growth** – Investment earnings in the account are not taxed.\n3. **Tax-free withdrawals** – Money used for qualified medical expenses is never taxed.\n\nThat’s the only triple-tax advantage in the U.S. tax code, and it can make the HSA better than 401(k) for the \"next best dollar\" of savings.",
    ),
    # Shoebox strategy
    (
        ["shoebox", "receipt", "pay cash", "pay out of pocket", "reimburse later", "save receipt"],
        "**The \"Shoebox\" strategy:** If you can pay a medical bill with cash from your checking account, do that. Save the receipt (digital \"shoebox\"). Leave the money in your HSA and invest it. Years later, that amount could grow tax-free (e.g. $200 → $800). You can reimburse yourself for that old bill anytime in the future, tax-free, and keep the investment growth.",
    ),
    # 401(k) vs HSA
    (
        ["401k", "401(k)", "hsa vs 401", "prioritize", "which first"],
        "**Healthy Saver strategy (HSA vs 401(k)):** 1) Contribute to 401(k) up to the employer match (don’t leave free money). 2) Max out the HSA next—it’s triple-tax advantaged and acts as a retirement account after 65. 3) Then put more in 401(k) or IRA with what’s left.",
    ),
    # Invincible / never sick / why high deductible
    (
        ["never sick", "invincible", "why high deductible", "don't need it", "healthy", "young"],
        "It's great you're healthy! HSA funds can pay for therapy, contact lenses, dental cleanings, and more. If you don’t use it this year, it rolls over and can turn into a retirement savings account that moves with you if you change jobs. There’s no \"use it or lose it\" like with an FSA.",
    ),
    # What is HSA
    (
        ["what is an hsa", "what is hsa", "what's an hsa", "define hsa", "what is a health savings"],
        "An **HSA (Health Savings Account)** is a tax-advantaged account used to pay for qualified medical expenses. It must be paired with an HSA-qualified High Deductible Health Plan (HDHP). You own the account (not your employer), funds roll over year to year with no \"use it or lose it,\" and it’s portable when you change jobs. It can be used for current expenses or saved for retirement healthcare.",
    ),
    # Can I get one / eligibility
    (
        ["eligible", "can i get one", "can i have an hsa", "qualify", "eligibility", "who can"],
        "To contribute to an HSA you must: be covered by an HSA-qualified HDHP; have no other health coverage (with limited exceptions); not be on Medicare; and not be claimed as a dependent on someone else’s tax return.",
    ),
]


def _normalize(text: str) -> str:
    return text.lower().strip()


def get_prebaked_answer(user_message: str) -> str | None:
    """
    If the user message matches any pre-baked question (by keyword/phrase), return that answer.
    Otherwise return None so the app can use retrieval.
    """
    if not user_message or not user_message.strip():
        return None
    normalized = _normalize(user_message)
    for keywords, answer in PREBAKED:
        if any(kw in normalized for kw in keywords):
            return answer
    return None
