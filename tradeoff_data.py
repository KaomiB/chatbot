"""
Trade-Off Tool: hardcoded scenario definitions (from cursor_prompt_tradeoff_tool.md).
All logic is local — no API. get_result(scenario_id, answers) returns {headline, body, next_task_id?, learn_more_topic_id?}.
"""

from __future__ import annotations

from typing import Any

ENTRY_CARDS = [
    {"id": "A", "icon": "💡", "title": "I'm not sure if I should open an HSA", "scenario_id": "A1"},
    {"id": "B", "icon": "⚖️", "title": "I have limited money — help me prioritize", "scenario_id": "B1"},
    {"id": "C", "icon": "📈", "title": "I already have an HSA and want to use it better", "scenario_id": "C2"},
]

MORE_OPTIONS = [
    {"id": "D2", "title": "I'm overwhelmed and don't know where to start"},
    {"id": "bill", "title": "I got a bill or expense I need to handle", "link": "task_breaker", "task_id": "surprise_medical_bill"},
    {"id": "C4", "title": "I want to understand the long-term value"},
]

# Scenario id -> list of questions. Each question: {"prompt": str, "options": [{"key": str, "label": str}]}
# No questions = static result (e.g. A1, D1, C4).
SCENARIO_QUESTIONS: dict[str, list[dict[str, Any]]] = {
    "A1": [],  # Static card
    "A2": [
        {"prompt": "How do you get your health insurance?", "options": [
            {"key": "employer", "label": "Through my employer"},
            {"key": "school", "label": "Through school / student insurance"},
            {"key": "own", "label": "On my own (marketplace / ACA)"},
            {"key": "parent", "label": "I'm on a parent's plan"},
        ]},
        {"prompt": "Does your plan name include any of these words?", "options": [
            {"key": "hdhp", "label": "HDHP, High-Deductible, HSA-eligible, or Consumer Choice"},
            {"key": "ppo", "label": "PPO, HMO, EPO, or Gold/Platinum"},
            {"key": "unsure", "label": "I'm not sure / I can't find it"},
        ]},
    ],
    "B1": [
        {"prompt": "How much do you have set aside for emergencies right now?", "options": [
            {"key": "none", "label": "Nothing / less than $500"},
            {"key": "1m", "label": "About 1 month of expenses"},
            {"key": "2_3m", "label": "2–3 months of expenses"},
            {"key": "3m", "label": "3+ months — I'm covered"},
        ]},
        {"prompt": "Does your employer contribute to your HSA?", "options": [
            {"key": "yes", "label": "Yes — they add money to my HSA"},
            {"key": "no", "label": "No employer contribution"},
            {"key": "unsure", "label": "I'm not sure"},
        ]},
        {"prompt": "Roughly how much do you have left after rent and bills each month?", "options": [
            {"key": "under100", "label": "Under $100"},
            {"key": "100_300", "label": "$100–$300"},
            {"key": "300_600", "label": "$300–$600"},
            {"key": "600", "label": "More than $600"},
        ]},
    ],
    "B2": [
        {"prompt": "What kind of debt are you thinking about?", "options": [
            {"key": "student", "label": "Student loans"},
            {"key": "cc", "label": "Credit card debt"},
            {"key": "both", "label": "Both"},
            {"key": "other", "label": "Other (car loan, personal loan, etc.)"},
        ]},
        {"prompt": "Roughly what's the interest rate on that debt?", "options": [
            {"key": "under5", "label": "Under 5%"},
            {"key": "5_10", "label": "5%–10%"},
            {"key": "10_20", "label": "10%–20%"},
            {"key": "over20", "label": "Over 20% (likely credit card)"},
            {"key": "dont_know", "label": "I don't know"},
        ]},
        {"prompt": "Does your employer contribute to your HSA?", "options": [
            {"key": "yes", "label": "Yes"},
            {"key": "no", "label": "No"},
            {"key": "unsure", "label": "Not sure"},
        ]},
    ],
    "B3": [
        {"prompt": "What's your coverage type?", "options": [
            {"key": "self", "label": "Just me (self-only)"},
            {"key": "family", "label": "Me + family"},
        ]},
        {"prompt": "Does your employer contribute to your HSA?", "options": [
            {"key": "1_500", "label": "Yes — $1 to $500/year"},
            {"key": "500_1500", "label": "Yes — $500 to $1,500/year"},
            {"key": "1500", "label": "Yes — more than $1,500/year"},
            {"key": "no", "label": "No employer contribution"},
        ]},
        {"prompt": "How much do you have left after rent and bills each month?", "options": [
            {"key": "under100", "label": "Under $100"},
            {"key": "100_300", "label": "$100–$300"},
            {"key": "300_600", "label": "$300–$600"},
            {"key": "600", "label": "More than $600"},
        ]},
    ],
    "C1": [
        {"prompt": "What kind of expense are you thinking about?", "options": [
            {"key": "mental", "label": "Mental health / therapy / counseling"},
            {"key": "dental", "label": "Dental work"},
            {"key": "vision", "label": "Glasses, contacts, or eye care"},
            {"key": "rx", "label": "Prescription or OTC medication"},
            {"key": "other", "label": "Something else"},
        ]},
    ],
    "C2": [
        {"prompt": "How would you describe your current health expenses?", "options": [
            {"key": "rare", "label": "I rarely use healthcare — maybe once a year"},
            {"key": "regular", "label": "I have regular, predictable expenses (prescriptions, therapy, etc.)"},
            {"key": "big", "label": "I had a big unexpected expense recently"},
            {"key": "unsure", "label": "I'm not sure what to expect"},
        ]},
        {"prompt": "Can you cover your medical expenses out of pocket right now?", "options": [
            {"key": "yes", "label": "Yes — I could pay and not touch my HSA"},
            {"key": "sometimes", "label": "Sometimes — depends on the expense"},
            {"key": "no", "label": "No — I need the HSA to cover current costs"},
        ]},
    ],
    "C3": [
        {"prompt": "What's your current HSA cash balance (roughly)?", "options": [
            {"key": "under1k", "label": "Under $1,000"},
            {"key": "1k_3k", "label": "$1,000–$3,000"},
            {"key": "over3k", "label": "Over $3,000"},
            {"key": "dont_know", "label": "I don't know"},
        ]},
        {"prompt": "When do you think you might need this money?", "options": [
            {"key": "year", "label": "Within the next year (upcoming expense or uncertain)"},
            {"key": "1_5", "label": "Probably 1–5 years from now"},
            {"key": "long", "label": "Long-term — retirement or far future"},
        ]},
        {"prompt": "How do you feel about investment risk?", "options": [
            {"key": "safe", "label": "I'd rather keep it safe in cash"},
            {"key": "some", "label": "Some risk is okay if there's long-term gain"},
            {"key": "ok", "label": "I'm comfortable with market risk"},
        ]},
    ],
    "C4": [],  # Static
    "D1": [],  # Static
    "D2": [],  # Static — shows 3 options that route to A1, C2, or Task Breaker
    "D3": [
        {"prompt": "What feels true about why you haven't engaged with it?", "options": [
            {"key": "dont_know_use", "label": "I don't know what I can actually use it for"},
            {"key": "forget", "label": "I forget it exists / never think about it"},
            {"key": "balance", "label": "I have a balance but don't know what to do with it"},
            {"key": "wrong", "label": "I'm worried I'll do something wrong"},
        ]},
    ],
}

# A2: Q1 only shown for all; Q2 only for employer or own. We need conditional flow.
# For simplicity we show Q1 always; if employer or own we show Q2; if school we show result; if parent we show result.
# So A2 has 2 questions but Q2 is conditional. Easiest: always show 2 questions, and for school/parent we use a dummy or skip. Actually the spec says "QUESTION 2 (shown after A or C selected)". So we need branching. I'll implement A2 as: after Q1, if A or C go to Q2; else go to result. So we need a way to have conditional next question. For now I'll make A2 have both questions and results keyed by (q0, q1) or (q0,) when q0 is school or parent.
# Let me make get_result handle A2: answers has 0 or 1 or 2 keys. If only "q0" and it's school -> result. If only "q0" and parent -> result. If q0 and q1 (employer or own) -> result by q2 value.
# Actually in the UI we only collect one answer per "step". So answers might be {"0": "employer", "1": "hdhp"}. So question index 0, 1. For A2, when index 0 is school or parent we're done (no question 2). So the QUESTIONS for A2 should be dynamic: after Q1 if answer is employer or own, show Q2. So we need get_next_question(scenario_id, answers) that returns the next question or None if done. That way we can have conditional flows.
# I'll implement: for A2, questions list has 2 items but we have a "show_if" on question 2: only show if answers["0"] in ["employer", "own"]. When we're at index 1 and show_if fails, we skip to result. So in the page we do: questions = SCENARIO_QUESTIONS[A2]; for i, q in enumerate(questions): if i == 1 and answers.get("0") in ["school", "parent"]: don't show, go to result. So we need to know "should_show_question(i, answers)". I'll add optional "show_if" to each question: "show_if": lambda answers: answers.get("0") in ["employer", "own"]. That's a bit heavy. Simpler: in get_result for A2 we accept answers with keys 0,1. If "0" is school or parent, we don't need "1". So the flow is: we have 2 questions for A2. When user selects employer or own we go to question 2. When user selects school or parent we go to result (so we need to detect that and not show question 2). So in the page logic: if scenario is A2 and we have 1 answer and answer[0] in [school, parent], then we're at result. Otherwise if we have 2 answers (for employer/own) we're at result. So the number of questions "to show" varies. I'll store in SCENARIO_QUESTIONS a structure that can include conditional: for A2, questions = [q1, q2_conditional]. And we have a helper: get_num_questions(scenario_id, answers) that returns how many questions to show. For A2: if len(answers)==0 return 2 (we show q0). If answers[0] in [school, parent] return 1 (only q0, then result). Else return 2. So we show question index 0, then if index 0 answer is employer/own we show index 1, else result. So current_question_index can be 0 or 1. When we're at index 0 and user picks school/parent, we go to result. When we're at index 0 and user picks employer/own, we go to index 1. When we're at index 1 we have 2 answers so we go to result. So the "questions" for A2 could be 2 items, and we just need the page to: when advancing from 0, check if answer is school or parent -> go to result; else go to 1. I'll implement that in the page. get_result(A2, {"0": "school"}) -> school result. get_result(A2, {"0": "parent"}) -> parent result. get_result(A2, {"0": "employer", "1": "hdhp"}) -> employer+hdhp result. So we need to pass answers as dict of "0", "1" etc. and get_result handles all branches.
# Implementing get_result now for all scenarios.
def get_result(scenario_id: str, answers: dict[str, str]) -> dict[str, Any]:
    """Returns {headline, body, next_task_id?, learn_more_topic_id?, employer_note?}."""
    q0 = answers.get("0")
    q1 = answers.get("1")
    q2 = answers.get("2")

    if scenario_id == "A1":
        return {
            "headline": "An HSA is basically a tax-free savings account for healthcare.",
            "body": "You put money in before taxes, use it for medical expenses (doctor visits, prescriptions, therapy, dental, vision), and it never expires. If you have a qualifying health plan through work or on your own, you can open one.",
            "next_task_id": None,
            "next_label": "Check if my plan qualifies →",
            "next_goes_to": "A2",
            "learn_more_topic_id": "what_is_hsa",
        }

    if scenario_id == "A2":
        if q0 == "school":
            return {"headline": "Student plans usually don't qualify — but check first.", "body": "Most university health plans are not HSA-eligible because they don't meet the high-deductible requirement. Check your plan documents or ask your student health center.", "learn_more_topic_id": "hdhp_basics"}
        if q0 == "parent":
            return {"headline": "It depends on whether your parent's plan is HSA-qualified.", "body": "Being on a parent's plan doesn't automatically disqualify you — it depends on the specific plan type. Ask your parent to check if their plan is labeled HDHP or HSA-eligible.", "learn_more_topic_id": "eligibility"}
        if q0 in ("employer", "own") and q1 == "hdhp":
            return {"headline": "You're likely eligible.", "body": "Your plan sounds HSA-qualified. The next step is confirming with HR and opening your account — it usually takes about 10 minutes online.", "next_task_id": "open_hsa", "learn_more_topic_id": None}
        if q0 == "employer" and q1 == "ppo":
            return {"headline": "Your plan probably doesn't qualify — but it's worth confirming.", "body": "PPO and HMO plans typically don't qualify for an HSA. Ask HR: 'Is my plan HSA-eligible?' — they get this question often.", "next_task_id": "check_eligibility", "learn_more_topic_id": None}
        if q0 == "employer" and q1 == "unsure":
            return {"headline": "Easy way to check: look at your insurance card.", "body": "Find your plan name on your insurance card or in your benefits email. Look for 'HDHP' or 'HSA-eligible' anywhere in the name. Still unsure? Text HR.", "next_task_id": "check_eligibility", "learn_more_topic_id": None}
        if q0 == "own" and q1 == "hdhp":
            return {"headline": "You're likely eligible.", "body": "Bronze and Catastrophic ACA plans are often HSA-qualified. Confirm by checking your plan's Summary of Benefits for the annual deductible — it needs to be at least $1,650 for 2025.", "next_task_id": "open_hsa", "learn_more_topic_id": None}
        return {"headline": "Check your plan details.", "body": "Look for HDHP or HSA-eligible on your plan name or ask your provider.", "next_task_id": "check_eligibility", "learn_more_topic_id": "eligibility"}

    if scenario_id == "B1":
        if q0 == "none":
            body = "Without any emergency savings, an unexpected expense could force you to pull money out of your HSA early (triggering taxes and a 20% penalty). Aim for $500–$1,000 as a starter buffer, then start contributing to your HSA."
            if q1 == "yes":
                body += " One exception: capture your employer's HSA contribution if it's automatic — that's free money that arrives regardless."
            return {"headline": "Build a basic emergency buffer first — then HSA.", "body": body, "next_task_id": "open_hsa"}
        if q0 == "1m" and q1 == "yes":
            return {"headline": "Capture the employer match — it beats almost everything.", "body": "You have a basic safety net, and your employer is offering free money. Contribute at least enough to get the full employer match. That's a 100% instant return — better than any savings rate or debt payoff.", "next_task_id": "set_contribution"}
        if q0 == "1m" and q1 != "yes":
            return {"headline": "Split it: build your cushion and contribute a small amount.", "body": "With 1 month saved and no employer match, a balanced approach works: put most of your extra toward getting to 2 months of savings, and contribute a small amount to HSA ($25–$50/month) to start the account.", "next_task_id": "set_contribution"}
        if q0 in ("2_3m", "3m"):
            body = "With 2+ months of emergency savings, you're in a good position to prioritize your HSA. The tax savings are real and the money never expires."
            if q1 == "yes":
                body += " Start by maxing your employer match, then decide how much more you want to contribute."
            if q2 == "under100":
                body += " Even $25/month is a meaningful start given your budget."
            return {"headline": "You have enough cushion — HSA contributions make sense now.", "body": body, "next_task_id": "set_contribution"}
        return {"headline": "HSA contributions make sense.", "body": "Consider contributing what you can; you can change it anytime.", "next_task_id": "set_contribution"}

    if scenario_id == "B2":
        base = "Regardless of your debt: if your employer matches HSA contributions, capture that match first. It's a 100% instant return — better than paying down any loan. "
        if q1 == "under5" and q2 == "yes":
            return {"headline": "HSA first (after capturing the employer match).", "body": base + "Your debt rate is low enough that the HSA's triple tax advantage — potentially saving 25–30% on contributions — likely beats the guaranteed savings from paying down low-interest debt early.", "next_task_id": "set_contribution"}
        if q1 == "under5" and q2 != "yes":
            return {"headline": "HSA is still likely the better move.", "body": base + "Even without an employer match, the tax savings on HSA contributions often exceed the cost of low-interest debt. Consider contributing up to the IRS limit, or split the difference.", "next_task_id": "set_contribution"}
        if q1 == "5_10":
            return {"headline": "It's close — splitting is a reasonable approach.", "body": base + "At 5–10% interest, the math is roughly equal. A common strategy: put 50% toward debt and 50% toward HSA contributions. That way you make progress on both without overthinking it.", "next_task_id": "set_contribution"}
        if q1 == "10_20":
            return {"headline": "Pay down the high-interest debt first, after your employer match.", "body": base + "A guaranteed 10–20% 'return' from paying off this debt likely beats the HSA's tax benefit. Minimum HSA contribution to keep the account active is fine; put the rest toward debt.", "next_task_id": "set_contribution"}
        if q1 == "over20":
            return {"headline": "Credit card debt first — this is the clearest case.", "body": base + "20%+ interest is very hard to beat with any tax advantage. Get this paid down first. Keep your HSA active with the minimum contribution (or employer match only), then redirect to HSA once the card is paid off.", "next_task_id": "set_contribution"}
        if q1 == "dont_know":
            return {"headline": "First — find your interest rate. It changes the answer.", "body": "Check your loan servicer app or your credit card statement. The interest rate (APR) is usually listed on the first page. Under 7% → probably favor HSA. Over 15% → probably favor debt.", "next_task_id": "set_contribution"}
        return {"headline": "Consider your interest rate.", "body": base, "next_task_id": "set_contribution"}

    if scenario_id == "B3":
        if q2 == "under100":
            body = "On a tight budget, the goal is just to open and activate the account. Any contribution gets you the tax benefit and keeps the account growing."
            if q1 in ("1_500", "500_1500", "1500"):
                body += " Your employer is already adding money — you don't need to contribute much yourself."
            return {"headline": "Start small — even $10–$25/month counts.", "body": body, "next_task_id": "set_contribution"}
        if q2 == "100_300" and q1 == "no":
            return {"headline": "Aim for $50–$100/month as a starting point.", "body": "That's $600–$1,200/year — meaningful tax savings and a growing balance without straining your budget. You can always increase it later.", "next_task_id": "set_contribution"}
        if q2 == "100_300" and q1 in ("1_500", "500_1500"):
            return {"headline": "Contribute enough to maximize the employer match, then decide the rest.", "body": "Your employer is already doing some of the work. Contribute at least enough to get the full match, then add whatever your budget allows beyond that.", "next_task_id": "set_contribution"}
        if q2 == "300_600" and q0 == "self":
            return {"headline": "A target of $150–$250/month gets you to a strong annual balance.", "body": "That's $1,800–$3,000/year — well on your way toward the $4,300 individual limit. Adjust based on your expected medical expenses for the year.", "next_task_id": "set_contribution"}
        if q2 == "600" and q0 == "self":
            return {"headline": "Consider maxing out — the 2025 limit is $4,300 for individuals.", "body": "That's about $358/month. Maxing the HSA gives you the full triple-tax benefit. If your employer contributes, subtract that from your target. Any amount above that limit stays in your paycheck.", "next_task_id": "set_contribution"}
        if q2 == "600" and q0 == "family":
            return {"headline": "Consider maxing out — the 2025 family limit is $8,750.", "body": "That's about $729/month. With a family plan, healthcare costs tend to be less predictable, so a larger HSA buffer is especially valuable.", "next_task_id": "set_contribution"}
        return {"headline": "Contribute what fits your budget.", "body": "You can change the amount anytime.", "next_task_id": "set_contribution"}

    if scenario_id == "C1":
        if q0 == "mental":
            return {"headline": "Yes — therapy and mental health care qualify.", "body": "You can use your HSA for therapy, counseling, and mental health prescriptions. Many people don't realize this.", "next_task_id": "use_for_therapy", "learn_more_topic_id": "qualified_expenses_mental_health"}
        if q0 in ("dental", "vision"):
            return {"headline": "Yes — dental and vision expenses qualify.", "body": "Cleanings, fillings, braces, eye exams, glasses, contacts, and LASIK all count.", "next_task_id": "use_for_dental_vision", "learn_more_topic_id": "qualified_expenses_dental_vision"}
        if q0 == "rx":
            return {"headline": "Yes — prescriptions and many OTC items qualify.", "body": "Almost all prescriptions qualify. Many OTC items do too since 2020.", "next_task_id": "use_for_therapy", "learn_more_topic_id": "qualified_expenses_otc"}
        return {"headline": "Most medical expenses qualify.", "body": "The general rule: if it prevents or treats a physical or mental condition, it's likely covered. When in doubt, save your receipt.", "learn_more_topic_id": "qualified_expenses"}

    if scenario_id == "C2":
        if q0 == "rare" and q1 == "yes":
            return {"headline": "Let it grow — this is the ideal investing situation.", "body": "If you're healthy and can pay expenses out of pocket, leaving your HSA untouched and invested is the most powerful thing you can do. The tax-free compounding over 10–30 years can be substantial.", "next_task_id": "start_investing"}
        if q0 == "regular" and q1 == "yes":
            return {"headline": "Pay out of pocket now and keep your receipts.", "body": "For regular, predictable expenses you can afford, paying out of pocket and letting the HSA grow is smarter long-term. Keep every receipt — you can reimburse yourself years later with no deadline.", "next_task_id": "setup_recordkeeping"}
        if q0 == "regular" and q1 == "sometimes":
            return {"headline": "Use HSA for larger expenses, pay out of pocket for small ones.", "body": "A practical split: cover routine small expenses yourself, use the HSA card for anything over $50–$100. This keeps your balance growing while making sure you're not stressed about current costs.", "next_task_id": None}
        if q1 == "no":
            return {"headline": "Use it — that's what it's for.", "body": "If you need the HSA to cover current medical costs, use it. There's no benefit in letting it sit if you're going into debt or skipping care to avoid spending it.", "next_task_id": "surprise_medical_bill"}
        return {"headline": "Use your HSA when it helps.", "body": "You can always reimburse yourself later if you pay out of pocket now. Keep receipts.", "next_task_id": "setup_recordkeeping"}

    if scenario_id == "C3":
        if q0 == "under1k":
            return {"headline": "Not yet — you haven't hit the investing threshold.", "body": "Most HSA providers require a minimum cash balance of $1,000–$2,000 before you can invest. Keep contributing and you'll get there soon.", "next_task_id": "set_contribution"}
        if q0 in ("1k_3k", "over3k") and q1 == "year":
            return {"headline": "Keep it in cash for now — you may need it soon.", "body": "Investing makes sense for money you won't need in the near term. If you might have upcoming medical expenses, keep that portion in cash so it's available without waiting for funds to liquidate.", "next_task_id": None}
        if q0 in ("1k_3k", "over3k") and q1 in ("1_5", "long") and q2 == "safe":
            return {"headline": "You could invest a portion while keeping a cash buffer.", "body": "A common approach: keep 1–2 months of expected medical costs in cash, and invest the rest. That way you have liquidity for near-term expenses and growth potential for the rest.", "next_task_id": "start_investing"}
        if q0 in ("1k_3k", "over3k") and q1 in ("1_5", "long") and q2 in ("some", "ok"):
            return {"headline": "Investing your HSA is one of the best moves available to you.", "body": "For long-term savings you won't need soon, investing in a low-cost index fund or target-date fund means tax-free growth for decades. $3,000/year invested at 7% grows to ~$306,000 over 30 years — vs $90,000 in cash. The risk is real but manageable for a long time horizon.", "next_task_id": "start_investing"}
        return {"headline": "Consider investing once you have a buffer.", "body": "Keep a cash cushion for near-term expenses; invest the rest for growth.", "next_task_id": "start_investing"}

    if scenario_id == "C4":
        return {"headline": "An HSA is one of the best tools for exactly this worry.", "body": "A married couple retiring today will need an estimated $366,000 for out-of-pocket medical costs in retirement (EBRI). An HSA invested over your working years grows entirely tax-free — and withdrawals for medical expenses are never taxed, even in retirement. Starting in your 20s or 30s means decades of tax-free compounding. Even small contributions now make a meaningful difference later.", "next_task_id": "start_investing", "learn_more_topic_id": "retirement_planning"}

    if scenario_id == "D1":
        return {"headline": "There's very little you can actually mess up here.", "body": "The main rule is: use HSA funds for qualified medical expenses. Almost everything medical qualifies. If you're unsure, save your receipt — you can always look it up later. The only real penalty is using it for clearly non-medical purchases before 65, and that's easy to avoid. Steps: (1) Check if your plan qualifies. (2) Open the account (10 min online). (3) Set any contribution amount — even $25/month. (4) Use it when you have a medical expense. (5) Save receipts. You can always adjust, change, or pause contributions. Nothing about this is permanent or irreversible.", "next_task_id": "open_hsa"}

    if scenario_id == "D2":
        # Shown as 3 options; handled in UI
        return {"headline": "Pick one. Just one.", "body": "You don't have to understand all of it today. Which of these feels most relevant to where you are right now?", "show_options": ["A1", "C2", "task_breaker"]}

    if scenario_id == "D3":
        if q0 == "dont_know_use":
            return {"headline": "You can use it for a lot more than you probably think.", "body": "Dental, vision, therapy, OTC products, and more. Explore the qualified expenses topic.", "learn_more_topic_id": "qualified_expenses"}
        if q0 == "forget":
            return {"headline": "Set up a receipt folder — the easiest re-entry point.", "body": "Takes 5 min. You'll be ready next time you have a medical expense.", "next_task_id": "setup_recordkeeping"}
        if q0 == "balance":
            return {"headline": "If you have a balance sitting in cash, investing it is probably the single highest-impact thing you can do.", "body": "Consider the investing scenario for next steps.", "next_task_id": "start_investing"}
        if q0 == "wrong":
            return {"headline": "A lot of people feel this way — and it makes sense given how confusing this system is.", "body": "There's very little you can actually mess up. Use it for medical expenses, save receipts. That's the core.", "next_task_id": "open_hsa"}
        return {"headline": "Pick a next step that feels doable.", "body": "Task Breaker can walk you through it.", "next_task_id": "open_hsa"}

    return {"headline": "Here’s what we recommend.", "body": "Use the Task Breaker or HSA topics in the sidebar for next steps.", "next_task_id": None}


def get_questions_for_display(scenario_id: str, answers: dict[str, str]) -> list[dict]:
    """Returns list of questions to show; for A2, Q2 is skipped if Q1 is school or parent."""
    questions = SCENARIO_QUESTIONS.get(scenario_id, [])
    if scenario_id == "A2" and len(questions) >= 2 and answers.get("0") in ("school", "parent"):
        return [questions[0]]  # Only first question, then result
    return questions


def should_show_question(scenario_id: str, question_index: int, answers: dict[str, str]) -> bool:
    """For A2: don't show question 2 if answer 0 is school or parent."""
    if scenario_id == "A2" and question_index == 1:
        return answers.get("0") in ("employer", "own")
    return True
