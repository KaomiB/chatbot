# Cursor Prompt: Trade-Off Tool / Scenario Explorer Page

## Overview

Build a new page called the **Trade-Off Tool** (nav label: "Trade-Off Tool" or
"Scenario Explorer"). This page helps users navigate real HSA decisions based
on their specific situation — not general facts, but personalized guidance.

It is based on 12 pre-defined scenarios across 7 categories. All logic is
**fully hardcoded** — no AI API calls needed. Users answer 2–4 short
questions using buttons, sliders, or dropdowns (never free text), and receive
a tailored recommendation with explanation.

This page is distinct from the HSA Guide/Explorer (topic chatbot). That page
answers "what is this?" — this page answers "what should I do?"

---

## Page Structure

### Header
Title: "Trade-Off Tool" (or "Scenario Explorer")
Subtitle: "Tell us what's going on — get a recommendation that fits your situation"

Below the subtitle, show 3 entry point cards. Each card is a scenario
category. Clicking one starts that scenario flow.

DO NOT show all scenarios at once. Show only the 3 most relevant entry
cards on load, then let users browse "more situations" below.

### Entry cards (always visible on load)
Card 1: "I'm not sure if I should open an HSA"
  → icon: 💡
  → routes to: SCENARIO GROUP A (Awareness + Eligibility)

Card 2: "I have limited money — help me prioritize"
  → icon: ⚖️
  → routes to: SCENARIO GROUP B (Tradeoffs: debt, emergency fund, budget)

Card 3: "I already have an HSA and want to use it better"
  → icon: 📈
  → routes to: SCENARIO GROUP C (Using HSA, investing, long-term)

### "More situations" expandable section below cards
- "I'm overwhelmed and don't know where to start" → routes to GROUP D (Emotional)
- "I got a bill or expense I need to handle" → Task Simplifier page link
- "I want to understand the long-term value" → routes to GROUP C

---

## Scenario Flows — Full Hardcoded Logic

Each flow is a SHORT question sequence (2–4 questions max) followed by
a result screen. Questions use BUTTONS ONLY — no text input, no sliders
unless specified. Keep each question to 3–4 answer options maximum.

Result screens show:
1. A 1–2 sentence direct recommendation
2. A "Why this?" expandable explanation (2–3 sentences)
3. A "What's my next step?" button → links to Task Simplifier with
   the relevant task pre-loaded
4. A "Learn more about this" button → links to the relevant topic
   node in the HSA Guide

---

### GROUP A: Understanding HSAs + Eligibility

#### Scenario A1 — "I saw my employer mention an HSA but I don't know what it is"

No questions needed. Render a direct explanation card:

RESULT:
  Headline: "An HSA is basically a tax-free savings account for healthcare."
  Body: "You put money in before taxes, use it for medical expenses
  (doctor visits, prescriptions, therapy, dental, vision), and it never
  expires. If you have a qualifying health plan through work or on your
  own, you can open one."
  Next step button: "Check if my plan qualifies →" (routes to A2)
  Learn more button: "See full HSA basics →" (links to what_is_hsa topic)

---

#### Scenario A2 — "Can I open an HSA? / Does my plan qualify?"

QUESTION 1:
  "How do you get your health insurance?"
  Options:
    A → "Through my employer"
    B → "Through school / student insurance"
    C → "On my own (marketplace / ACA)"
    D → "I'm on a parent's plan"

QUESTION 2 (shown after A or C selected):
  "Does your plan name include any of these words?"
  Options:
    A → "HDHP, High-Deductible, HSA-eligible, or Consumer Choice"
    B → "PPO, HMO, EPO, or Gold/Platinum"
    C → "I'm not sure / I can't find it"

RESULTS:

  If Q1=A AND Q2=A:
    Headline: "You're likely eligible."
    Body: "Your employer plan sounds HSA-qualified. The next step is
    confirming with HR and opening your account — it usually takes
    about 10 minutes online."
    Next step: "Show me how to open one →" (Task Simplifier: open_hsa)

  If Q1=A AND Q2=B:
    Headline: "Your plan probably doesn't qualify — but it's worth confirming."
    Body: "PPO and HMO plans typically don't qualify for an HSA.
    Ask HR: 'Is my plan HSA-eligible?' — they get this question often."
    Next step: "What to ask HR →" (Task Simplifier: check_eligibility)

  If Q1=A AND Q2=C:
    Headline: "Easy way to check: look at your insurance card."
    Body: "Find your plan name on your insurance card or in your
    benefits email. Look for 'HDHP' or 'HSA-eligible' anywhere in
    the name. Still unsure? Text HR."
    Next step: "Help me check →" (Task Simplifier: check_eligibility)

  If Q1=B (student insurance):
    Headline: "Student plans usually don't qualify — but check first."
    Body: "Most university health plans are not HSA-eligible because
    they don't meet the high-deductible requirement. Check your plan
    documents or ask your student health center."
    Learn more: "Why does the plan type matter?" (links to hdhp_basics)

  If Q1=C AND Q2=A:
    Headline: "You're likely eligible."
    Body: "Bronze and Catastrophic ACA plans are often HSA-qualified.
    Confirm by checking your plan's Summary of Benefits for the
    annual deductible — it needs to be at least $1,650 for 2025."
    Next step: "Open an HSA on my own →" (Task Simplifier: open_hsa)

  If Q1=D:
    Headline: "It depends on whether your parent's plan is HSA-qualified."
    Body: "Being on a parent's plan doesn't automatically disqualify
    you — it depends on the specific plan type. Ask your parent
    to check if their plan is labeled HDHP or HSA-eligible."
    Learn more: "See eligibility details →" (links to eligibility topic)

---

### GROUP B: Financial Tradeoff Scenarios

#### Scenario B1 — "I have limited money — what do I prioritize?"
(HSA vs Emergency Fund)

QUESTION 1:
  "How much do you have set aside for emergencies right now?"
  Options:
    A → "Nothing / less than $500"
    B → "About 1 month of expenses"
    C → "2–3 months of expenses"
    D → "3+ months — I'm covered"

QUESTION 2:
  "Does your employer contribute to your HSA?"
  Options:
    A → "Yes — they add money to my HSA"
    B → "No employer contribution"
    C → "I'm not sure"

QUESTION 3:
  "Roughly how much do you have left after rent and bills each month?"
  Options:
    A → "Under $100"
    B → "$100–$300"
    C → "$300–$600"
    D → "More than $600"

RESULTS:

  If Q1=A (no emergency fund):
    Headline: "Build a basic emergency buffer first — then HSA."
    Body: "Without any emergency savings, an unexpected expense
    could force you to pull money out of your HSA early (triggering
    taxes and a 20% penalty). Aim for $500–$1,000 as a starter
    buffer, then start contributing to your HSA."
    [If Q2=A]: append: "One exception: capture your employer's
    HSA contribution if it's automatic — that's free money that
    arrives regardless."
    Next step: "I'm ready to start my HSA →" (Task Simplifier: open_hsa)

  If Q1=B AND Q2=A:
    Headline: "Capture the employer match — it beats almost everything."
    Body: "You have a basic safety net, and your employer is offering
    free money. Contribute at least enough to get the full employer
    match. That's a 100% instant return — better than any savings
    rate or debt payoff."
    Next step: "Set up contributions →" (Task Simplifier: set_contribution)

  If Q1=B AND Q2=B:
    Headline: "Split it: build your cushion and contribute a small amount."
    Body: "With 1 month saved and no employer match, a balanced
    approach works: put most of your extra toward getting to 2 months
    of savings, and contribute a small amount to HSA ($25–$50/month)
    to start the account."
    Next step: "How much should I contribute? →" (Task Simplifier: set_contribution)

  If Q1=C OR Q1=D:
    Headline: "You have enough cushion — HSA contributions make sense now."
    Body: "With 2+ months of emergency savings, you're in a good
    position to prioritize your HSA. The tax savings are real and
    the money never expires."
    [If Q2=A]: append: "Start by maxing your employer match, then
    decide how much more you want to contribute."
    [If Q3=A]: append: "Even $25/month is a meaningful start
    given your budget."
    Next step: "Help me decide how much →" (Task Simplifier: set_contribution)

---

#### Scenario B2 — "Should I pay off debt or contribute to HSA?"
(HSA vs Student Loans / Credit Card Debt)

QUESTION 1:
  "What kind of debt are you thinking about?"
  Options:
    A → "Student loans"
    B → "Credit card debt"
    C → "Both"
    D → "Other (car loan, personal loan, etc.)"

QUESTION 2:
  "Roughly what's the interest rate on that debt?"
  Options:
    A → "Under 5%"
    B → "5%–10%"
    C → "10%–20%"
    D → "Over 20% (likely credit card)"
    E → "I don't know"

QUESTION 3:
  "Does your employer contribute to your HSA?"
  Options:
    A → "Yes"
    B → "No"
    C → "Not sure"

RESULTS:

  Base rule (show for ALL results at top):
    "Regardless of your debt: if your employer matches HSA
    contributions, capture that match first. It's a 100% instant
    return — better than paying down any loan."

  If Q2=A (under 5%) AND Q3=A:
    Headline: "HSA first (after capturing the employer match)."
    Body: "Your debt rate is low enough that the HSA's triple
    tax advantage — potentially saving 25–30% on contributions —
    likely beats the guaranteed savings from paying down low-interest
    debt early."
    Next step: "Set up my HSA contributions →" (Task Simplifier: set_contribution)

  If Q2=A (under 5%) AND Q3=B:
    Headline: "HSA is still likely the better move."
    Body: "Even without an employer match, the tax savings on HSA
    contributions often exceed the cost of low-interest debt.
    Consider contributing up to the IRS limit, or split the difference."

  If Q2=B (5–10%):
    Headline: "It's close — splitting is a reasonable approach."
    Body: "At 5–10% interest, the math is roughly equal. A common
    strategy: put 50% toward debt and 50% toward HSA contributions.
    That way you make progress on both without overthinking it."

  If Q2=C (10–20%):
    Headline: "Pay down the high-interest debt first, after your employer match."
    Body: "A guaranteed 10–20% 'return' from paying off this debt
    likely beats the HSA's tax benefit. Minimum HSA contribution
    to keep the account active is fine; put the rest toward debt."

  If Q2=D (over 20%, credit card):
    Headline: "Credit card debt first — this is the clearest case."
    Body: "20%+ interest is very hard to beat with any tax advantage.
    Get this paid down first. Keep your HSA active with the minimum
    contribution (or employer match only), then redirect to HSA
    once the card is paid off."

  If Q2=E (don't know):
    Headline: "First — find your interest rate. It changes the answer."
    Body: "Check your loan servicer app or your credit card statement.
    The interest rate (APR) is usually listed on the first page.
    Under 7% → probably favor HSA. Over 15% → probably favor debt."

---

#### Scenario B3 — "How much should I contribute to my HSA?"

QUESTION 1:
  "What's your coverage type?"
  Options:
    A → "Just me (self-only)"
    B → "Me + family"

QUESTION 2:
  "Does your employer contribute to your HSA?"
  Options:
    A → "Yes — $1 to $500/year"
    B → "Yes — $500 to $1,500/year"
    C → "Yes — more than $1,500/year"
    D → "No employer contribution"

QUESTION 3:
  "How much do you have left after rent and bills each month?"
  Options:
    A → "Under $100"
    B → "$100–$300"
    C → "$300–$600"
    D → "More than $600"

RESULTS:
  (Note: 2025 IRS limits — Individual: $4,300 / Family: $8,750.
   Update these values each fall when IRS announces new limits.)

  If Q3=A (under $100/month):
    Headline: "Start small — even $10–$25/month counts."
    Body: "On a tight budget, the goal is just to open and activate
    the account. Any contribution gets you the tax benefit and
    keeps the account growing. [If Q2=A/B/C: Your employer is
    already adding money — you don't need to contribute much yourself.]"

  If Q3=B ($100–$300) AND Q2=D:
    Headline: "Aim for $50–$100/month as a starting point."
    Body: "That's $600–$1,200/year — meaningful tax savings and a
    growing balance without straining your budget. You can always
    increase it later."

  If Q3=B ($100–$300) AND Q2=A or B:
    Headline: "Contribute enough to maximize the employer match, then decide the rest."
    Body: "Your employer is already doing some of the work. Contribute
    at least enough to get the full match, then add whatever your
    budget allows beyond that."

  If Q3=C ($300–$600) AND Q1=A:
    Headline: "A target of $150–$250/month gets you to a strong annual balance."
    Body: "That's $1,800–$3,000/year — well on your way toward
    the $4,300 individual limit. Adjust based on your expected
    medical expenses for the year."

  If Q3=D (more than $600) AND Q1=A:
    Headline: "Consider maxing out — the 2025 limit is $4,300 for individuals."
    Body: "That's about $358/month. Maxing the HSA gives you
    the full triple-tax benefit. If your employer contributes, subtract
    that from your target. Any amount above that limit
    stays in your paycheck."

  If Q3=D AND Q1=B:
    Headline: "Consider maxing out — the 2025 family limit is $8,750."
    Body: "That's about $729/month. With a family plan, healthcare
    costs tend to be less predictable, so a larger HSA buffer
    is especially valuable."

---

### GROUP C: Using HSA + Long-Term Planning

#### Scenario C1 — "Can I use my HSA for glasses / therapy / dental?"

QUESTION 1:
  "What kind of expense are you thinking about?"
  Options:
    A → "Mental health / therapy / counseling"
    B → "Dental work"
    C → "Glasses, contacts, or eye care"
    D → "Prescription or OTC medication"
    E → "Something else"

RESULTS:
  If A: Route directly to qualified_expenses_mental_health topic
    + Task Simplifier: use_for_therapy

  If B: Route to qualified_expenses_dental_vision topic
    + Task Simplifier: use_for_dental_vision

  If C: Route to qualified_expenses_dental_vision topic
    + Task Simplifier: use_for_dental_vision

  If D: Route to qualified_expenses_otc topic
    Small note: "Almost all prescriptions qualify. Many OTC items
    do too since 2020."

  If E: Show a soft message:
    "Most medical, dental, and mental health expenses qualify.
    The general rule: if it prevents or treats a physical or mental
    condition, it's likely covered. When in doubt, save your receipt."
    Link to full qualified_expenses topic.

---

#### Scenario C2 — "Should I spend my HSA now or save it for later?"

QUESTION 1:
  "How would you describe your current health expenses?"
  Options:
    A → "I rarely use healthcare — maybe once a year"
    B → "I have regular, predictable expenses (prescriptions, therapy, etc.)"
    C → "I had a big unexpected expense recently"
    D → "I'm not sure what to expect"

QUESTION 2:
  "Can you cover your medical expenses out of pocket right now?"
  Options:
    A → "Yes — I could pay and not touch my HSA"
    B → "Sometimes — depends on the expense"
    C → "No — I need the HSA to cover current costs"

RESULTS:

  If Q1=A AND Q2=A:
    Headline: "Let it grow — this is the ideal investing situation."
    Body: "If you're healthy and can pay expenses out of pocket,
    leaving your HSA untouched and invested is the most powerful
    thing you can do. The tax-free compounding over 10–30 years
    can be substantial."
    Next step: "Start investing my HSA →" (Task Simplifier: start_investing)

  If Q1=B AND Q2=A:
    Headline: "Pay out of pocket now and keep your receipts."
    Body: "For regular, predictable expenses you can afford, paying
    out of pocket and letting the HSA grow is smarter long-term.
    Keep every receipt — you can reimburse yourself years later
    with no deadline."
    Next step: "Set up recordkeeping →" (Task Simplifier: setup_recordkeeping)

  If Q1=B AND Q2=B:
    Headline: "Use HSA for larger expenses, pay out of pocket for small ones."
    Body: "A practical split: cover routine small expenses yourself,
    use the HSA card for anything over $50–$100. This keeps your
    balance growing while making sure you're not stressed about
    current costs."

  If Q2=C:
    Headline: "Use it — that's what it's for."
    Body: "If you need the HSA to cover current medical costs,
    use it. There's no benefit in letting it sit if you're going
    into debt or skipping care to avoid spending it."
    Next step: "Handle a medical bill →" (Task Simplifier: surprise_medical_bill)

---

#### Scenario C3 — "I heard you can invest HSA money — is that risky?"

QUESTION 1:
  "What's your current HSA cash balance (roughly)?"
  Options:
    A → "Under $1,000"
    B → "$1,000–$3,000"
    C → "Over $3,000"
    D → "I don't know"

QUESTION 2:
  "When do you think you might need this money?"
  Options:
    A → "Within the next year (upcoming expense or uncertain)"
    B → "Probably 1–5 years from now"
    C → "Long-term — retirement or far future"

QUESTION 3:
  "How do you feel about investment risk?"
  Options:
    A → "I'd rather keep it safe in cash"
    B → "Some risk is okay if there's long-term gain"
    C → "I'm comfortable with market risk"

RESULTS:

  If Q1=A:
    Headline: "Not yet — you haven't hit the investing threshold."
    Body: "Most HSA providers require a minimum cash balance of
    $1,000–$2,000 before you can invest. Keep contributing and
    you'll get there soon."
    Next step: "Contribute more →" (Task Simplifier: set_contribution)

  If Q1=B OR C AND Q2=A:
    Headline: "Keep it in cash for now — you may need it soon."
    Body: "Investing makes sense for money you won't need in the
    near term. If you might have upcoming medical expenses, keep
    that portion in cash so it's available without waiting for
    funds to liquidate."

  If Q1=B OR C AND Q2=B OR C AND Q3=A:
    Headline: "You could invest a portion while keeping a cash buffer."
    Body: "A common approach: keep 1–2 months of expected medical
    costs in cash, and invest the rest. That way you have liquidity
    for near-term expenses and growth potential for the rest."
    Next step: "Start investing →" (Task Simplifier: start_investing)

  If Q1=C AND Q2=C AND Q3=B OR C:
    Headline: "Investing your HSA is one of the best moves available to you."
    Body: "For long-term savings you won't need soon, investing in
    a low-cost index fund or target-date fund means tax-free growth
    for decades. $3,000/year invested at 7% grows to ~$306,000
    over 30 years — vs $90,000 in cash. The risk is real but
    manageable for a long time horizon."
    Next step: "Start investing →" (Task Simplifier: start_investing)

---

### GROUP C (continued): Long-Term Value

#### Scenario C4 — "I'm worried about future medical costs — how does an HSA help?"

No questions needed. Show a static informational result card:

  Headline: "An HSA is one of the best tools for exactly this worry."
  Body paragraph 1: "A married couple retiring today will need an
  estimated $366,000 for out-of-pocket medical costs in retirement
  (EBRI). An HSA invested over your working years grows entirely
  tax-free — and withdrawals for medical expenses are never taxed,
  even in retirement."
  Body paragraph 2: "Starting in your 20s or 30s means decades of
  tax-free compounding. Even small contributions now make a
  meaningful difference later."
  Next step: "Start investing my HSA →" (Task Simplifier: start_investing)
  Learn more: "HSA for retirement →" (links to retirement_planning topic)

---

### GROUP D: Emotional Support + Overwhelm

#### Scenario D1 — "I don't want to mess up my HSA decisions"

No questions. Show a static reassurance + structure card:

  Headline: "There's very little you can actually mess up here."
  Body: "The main rule is: use HSA funds for qualified medical
  expenses. Almost everything medical qualifies. If you're unsure,
  save your receipt — you can always look it up later. The only
  real penalty is using it for clearly non-medical purchases before
  65, and that's easy to avoid."
  Structured guide:
    Step 1: Check if your plan qualifies
    Step 2: Open the account (10 min online)
    Step 3: Set any contribution amount — even $25/month
    Step 4: Use it when you have a medical expense
    Step 5: Save receipts
  Note: "You can always adjust, change, or pause contributions.
  Nothing about this is permanent or irreversible."
  Next step: "Walk me through opening one →" (Task Simplifier: open_hsa)

---

#### Scenario D2 — "There's too much information. I don't know where to start."

No questions. Show a 3-option card (let user pick ONE thing):

  Headline: "Pick one. Just one."
  Subtext: "You don't have to understand all of it today. Which of
  these feels most relevant to where you are right now?"

  Option A: "I don't have an HSA yet and want to understand if it's for me"
    → routes to A1 flow

  Option B: "I have an HSA but I'm not sure I'm using it right"
    → routes to C2 flow

  Option C: "I need to do something specific but I'm not sure how to start"
    → links to Task Simplifier page

---

## Scenario D3 — "I have an HSA but I rarely think about it"

QUESTION 1:
  "What feels true about why you haven't engaged with it?"
  Options:
    A → "I don't know what I can actually use it for"
    B → "I forget it exists / never think about it"
    C → "I have a balance but don't know what to do with it"
    D → "I'm worried I'll do something wrong"

RESULTS:

  If A: Route to qualified_expenses hub topic
    "You can use it for a lot more than you probably think —
    dental, vision, therapy, OTC products, and more."

  If B: Route to Task Simplifier: setup_recordkeeping
    "The easiest re-entry point: set up a receipt folder so
    you're ready next time you have a medical expense. Takes 5 min."

  If C: Route to start_investing flow (C3)
    "If you have a balance sitting in cash, investing it is
    probably the single highest-impact thing you can do with it."

  If D: Route to D1 (reassurance flow)

---

## Technical Notes for Cursor

### State management
Track: current_scenario_id, current_question_index, answers{}
On each button click: store answer, advance question index.
On final answer: look up result from hardcoded RESULTS dict.
No async, no API calls for any of the above.

### Result screen structure (render the same component every time)
```
<ResultCard>
  <Headline />           ← bold, 1 sentence
  <Body />               ← 2–3 sentences, plain language
  <EmployerNote />       ← conditional, only if employer match is relevant
  <NextStepButton />     ← links to Task Simplifier with task pre-loaded
  <LearnMoreButton />    ← links to HSA Guide topic node
  <StartOverButton />    ← returns to scenario entry cards
</ResultCard>
```

### Applying user mode (from cursor_prompt_user_modes.md)
Read `hsa_user_mode` from localStorage.

If mode = "neutral":
  - Remove gentle_note lines from result cards
  - Remove reassurance sentences (marked [SUPPORTIVE ONLY] in results)
  - Keep all factual content and next step buttons

If mode = "supportive":
  - Show all content including gentle notes
  - On GROUP D scenarios: prepend a single normalizing line before
    the headline, e.g. "A lot of people feel this way — and it makes
    sense given how confusing this system is."

### Anxiety trigger rules (apply regardless of mode)
  - Never show a "wrong answer" state
  - Never say "you should have" or "you missed out"
  - If user hasn't answered employer match and it's relevant: default
    to "no employer contribution" assumption, don't ask again
  - All result headlines are neutral or positive in framing
  - Never show peer comparison ("other users your age have...")

### Navigation between pages
  - "Next step →" buttons that link to Task Simplifier should pass
    a task_id query param, e.g. /task-simplifier?task=open_hsa
    so the Task Simplifier page pre-loads the correct task
  - "Learn more →" buttons should pass a topic_id query param,
    e.g. /hsa-guide?topic=qualified_expenses

### Progress indicator
Show a simple step counter at the top of each flow:
  "Question 1 of 3" — plain text, no progress bar
  (Progress bars can trigger anxiety if they show incompleteness)
  On result screen: hide the counter entirely

### Back button
Every question screen shows a "← Back" text link (not a button)
in the top left. Returns to previous question with answer preserved.
Never lose the user's previous answers on back navigation.

### Mobile
All question options render as full-width stacked buttons on mobile.
Result cards are single column. No horizontal scrolling anywhere.
```
