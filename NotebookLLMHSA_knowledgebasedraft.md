# NotebookLLM HSA Knowledge Base & Scenarios for Chatbot Training

## 1. Core Definitions & Eligibility
*Use this section when users ask "What is this?" or "Can I get one?"*

*   **Definition:** A Health Savings Account (HSA) is a tax-exempt trust or custodial account used to pay for qualified medical expenses. It must be paired with an HSA-qualified High Deductible Health Plan (HDHP). Unlike Flexible Spending Accounts (FSAs), HSA funds roll over year-to-year and never expire.
*   **The "Triple Tax" Advantage:**
    1.  **Tax-Free Contributions:** Money goes in pre-tax (via payroll) or is tax-deductible (if you contribute directly).
    2.  **Tax-Free Growth:** Interest and investment earnings in the account are not taxed.
    3.  **Tax-Free Withdrawals:** Money taken out for qualified medical expenses is never taxed.
*   **Eligibility Requirements:**
    *   Must be covered by a qualified HDHP on the first day of the month.
    *   **No other health coverage:** You cannot be covered by a spouse’s non-HDHP or a general-purpose FSA (unless it is a "limited purpose" FSA for dental/vision).
    *   **No Medicare:** You cannot be enrolled in Medicare.
    *   **Not a Dependent:** You cannot be claimed as a dependent on someone else's tax return.

## 2. 2026 Rules & Limits (The Numbers)
*Use for specific fact-checking queries.*

| Category | 2026 Limit | Notes |
| :--- | :--- | :--- |
| **Individual Contribution Limit** | **$4,400** | For those with self-only HDHP coverage. |
| **Family Contribution Limit** | **$8,750** | For those with family HDHP coverage. |
| **Catch-Up Contribution** | **$1,000** | Additional amount allowed for those age 55+. |
| **Min. Deductible (Self)** | $1,700 | Plan must have at least this deductible to qualify. |
| **Min. Deductible (Family)** | $3,400 | Plan must have at least this deductible to qualify. |
| **Max Out-of-Pocket (Self)** | $8,500 | The most a plan can require you to pay in a year. |
| **Max Out-of-Pocket (Family)** | $17,000 | The most a plan can require you to pay in a year. |

*   **Contribution Deadline:** You can contribute for a tax year up until the tax filing deadline (usually April 15) of the *following* year.
*   **Rollovers:** There is no "use-it-or-lose-it" rule. The money is yours forever, even if you change jobs or retire.

## 3. Qualified Expenses (Spending)
*Use when users ask "Can I buy X with my HSA?"*

*   **Allowed (Tax-Free):**
    *   Doctor visits, hospital stays, surgery.
    *   Dental work (cleanings, fillings, braces).
    *   Vision care (exams, glasses, contacts, Lasik).
    *   Prescription drugs.
    *   **Over-the-Counter (OTC):** Pain relievers, cold meds, allergy meds, menstrual care products (pads/tampons/cups).
    *   **Mental Health:** Therapy sessions, psychiatric care.
*   **Not Allowed (Taxable + 20% Penalty):**
    *   General health items (vitamins, gym memberships) unless prescribed for a specific condition.
    *   Cosmetic surgery.
    *   **Insurance Premiums:** Generally **NO**, with four exceptions:
        1.  COBRA premiums.
        2.  Premiums while receiving unemployment benefits.
        3.  Long-term care insurance.
        4.  Medicare premiums (Part A, B, D, and HMO) *after* age 65 (but NOT Medigap).

## 4. Chatbot Persona & Behavioral Strategy
*Based on "The Cognitive Architecture of Financial Resilience" and "Human-AI Emotional Synergy".*

*   **The "Curious Student" Tone:** Do not lecture. Ask guiding questions to reduce cognitive load.
    *   *Bad:* "You must contribute $3,000 to maximize your tax yield."
    *   *Good:* "That sounds like a busy month. Do you think you could set aside $50 for future health costs, or is cash tight right now?"
*   **Bandwidth Check:** If the user seems stressed (mentions debt, rent, panic), switch to "Support Mode." Hide complex investment graphs. Focus on immediate next steps.
*   **Visualizing Trade-offs:** Help users see the future.
    *   *Concept:* "The $100 you spend on takeout today could be $600 in tax-free health money when you retire if invested."

## 5. Key Scenarios for Young Adults
*Use these to illustrate concepts in a relatable way.*

### Scenario A: The "Adult Child" Loophole (The Secret Weapon)
*Context:* A 24-year-old is covered by their parents' family HDHP but has a job and files their own taxes.
*   **The Myth:** They think they can't have an HSA because they are on their parents' insurance.
*   **The Fact:** Because they are *not* a tax dependent, they can open their **own** HSA.
*   **The Superpower:** Because they are covered by a "family" plan (the parents'), they can contribute the **full family maximum ($8,750 in 2026)** to their own account, *in addition* to whatever the parents contribute to theirs.

### Scenario B: The "Healthy Saver" vs. The 401(k)
*Context:* User has limited funds and is deciding between 401(k) and HSA.
*   **The Strategy:**
    1.  Contribute to 401(k) only up to the employer match (don't leave free money on the table).
    2.  Max out the HSA next. Why? Because the HSA is **triple-tax advantaged** (better than 401(k)) and acts as a retirement account after age 65.
    3.  Go back to 401(k) or IRA with remaining funds.

### Scenario C: The "Shoebox" Strategy (Advanced)
*Context:* User has an HSA but can afford to pay a $200 medical bill with cash from their checking account.
*   **The Strategy:** Pay with cash now. Save the receipt (digital "shoebox"). Let the $200 stay in the HSA and invest it in the stock market.
*   **The Payoff:** In 20 years, that $200 might grow to $800 tax-free. The user can "reimburse" themselves for that old $200 bill anytime in the future tax-free, keeping the investment growth.

### Scenario D: The "Invincible" Skeptic
*Context:* A 22-year-old thinks, "I'm never sick, why do I want a high deductible?"
*   **The Reality Check:** Gen Z is the most likely generation to cut mental health services due to cost.
*   **The Chatbot Response:** "It's great you're healthy! But did you know HSA funds can pay for therapy, contact lenses, or dental cleanings? Plus, if you don't use it this year, it turns into a retirement savings account that moves with you if you change jobs."
