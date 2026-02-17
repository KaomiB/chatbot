# HSA Chatbot — Q&A Architecture (Implementation-Ready)
## Version 1.0 | Generated from hsa_chatbot_quote_library.md

> **Sources referenced throughout:**
> - [A] HealthEquity HSA Guidebook (HealthEquity)
> - [B] HSAs For Dummies, Optum Financial Special Edition (Wiley / Optum, 2021)
> - [C] WageWorks Definitive Guide to HSAs (WageWorks, 2016)
> - [D] Generational HSA Divide (research document)
> - [E] Behavioral Architecture of Financial Avoidance (research document)
> - [F] HSA Bank Health and Wealth Index (research document)

---

## FIRST-TIME USER FLOW (Default Sequence)

```
what_is_hsa → triple_tax → eligibility → hdhp_basics
  → qualified_expenses → contribution_limits → investment
    → hsa_vs_other → portability → young_adults → retirement_planning
```

**Skeptic / "I'm healthy, why do I need this?" entry path:**
```
young_adults → qualified_expenses_mental_health → triple_tax → portability
```

**"I already have an HSA" entry path:**
```
contribution_limits → investment → funding_strategy → recordkeeping
```

---

## TOPIC NODES — FULL FORMAT

---

## topic_id: what_is_hsa
display_label: "What is an HSA?"
suggested_questions:
  - "What is an HSA?"
  - "What's an HSA?"
  - "Explain HSA to me"
  - "What does HSA stand for?"
  - "I've never heard of an HSA"
  - "What is a health savings account?"
next_suggested_topics: [triple_tax, eligibility, portability]

answer: |
  A Health Savings Account (HSA) is a special savings account where you
  set money aside — before taxes — to pay for healthcare expenses. The
  simplest way to think about it: it's like a 401(k), but for healthcare
  instead of retirement.

  You and your employer can both contribute to your HSA, and you use
  those funds tax-free to pay for a wide range of qualified medical
  expenses — doctor visits, prescriptions, dental work, vision care,
  mental health therapy, and much more. You decide what to spend, what
  to save, and how to invest it.

  The biggest thing that separates an HSA from other health accounts:
  the money never expires. There is no "use it or lose it" rule. Your
  balance rolls over every single year and keeps growing — whether you
  need it next month or in retirement decades from now.

citations:
  - "HealthEquity HSA Guidebook, p. 25"
  - "HSAs For Dummies, Optum Financial Special Edition, Introduction, p. 1"
  - "WageWorks Guide to HSAs, p. 8"

---

## topic_id: triple_tax
display_label: "Triple Tax Advantage"
suggested_questions:
  - "What is the triple tax advantage?"
  - "How does an HSA save me money on taxes?"
  - "Is an HSA tax-free?"
  - "What are the tax benefits of an HSA?"
  - "Why is an HSA better than other accounts?"
  - "How do HSA taxes work?"
next_suggested_topics: [eligibility, contribution_limits, hsa_vs_other]

answer: |
  The HSA's "triple tax advantage" is what makes it the most powerful
  savings vehicle in the U.S. tax code. No other account gives you all
  three of these benefits at once.

  Benefit 1 — Contributions go in tax-free. Whether you, your employer,
  or a family member contributes, you pay no federal income tax on those
  dollars. If contributions come through payroll, you also skip Social
  Security and Medicare taxes (FICA) — a bonus that 401(k)s do not
  offer. For someone in the 22% tax bracket, the effective savings on
  a payroll HSA contribution can exceed 30%.

  Benefit 2 — Your money grows tax-free. Any interest or investment
  earnings in your HSA accumulate without being taxed year by year, as
  long as you use the money for qualified medical expenses.

  Benefit 3 — Withdrawals are tax-free. When you spend HSA funds on
  qualified medical expenses, you owe zero federal tax — at any age,
  at any time.

  Only 6% of working Americans aged 18 to 34 can correctly identify all
  three of these benefits. Knowing this puts you well ahead of your peers.

citations:
  - "HealthEquity HSA Guidebook, Introduction, p. 5"
  - "HealthEquity HSA Guidebook, pp. 25–26"
  - "WageWorks Guide to HSAs, p. 15"
  - "Generational HSA Divide research document"

---

## topic_id: eligibility
display_label: "Am I eligible?"
suggested_questions:
  - "Am I eligible for an HSA?"
  - "Who can open an HSA?"
  - "Can I have an HSA?"
  - "Do I qualify for an HSA?"
  - "What do I need to open an HSA?"
  - "Can I get an HSA on my parent's plan?"
next_suggested_topics: [hdhp_basics, contribution_limits, misconceptions]

answer: |
  To be eligible to open and contribute to an HSA, three main IRS rules
  apply.

  Rule 1: You must be enrolled in an HSA-qualified health plan —
  commonly called a High-Deductible Health Plan (HDHP). These plans
  generally have lower monthly premiums but higher deductibles. They can
  be employer-sponsored or purchased through an ACA exchange (bronze and
  catastrophic level plans often qualify).

  Rule 2: You cannot have certain other coverage. Specifically, you
  cannot have a standard Health FSA through your employer, be enrolled
  in Medicare, or be claimed as a dependent on someone else's tax return
  for HSA contribution purposes.

  Rule 3: No other disqualifying health coverage. If you have access to
  a spouse's plan or supplemental coverage that pays expenses before
  your HDHP deductible is met, that may disqualify you — check with
  your HR or plan provider.

  If you are currently on a parent's plan, whether you can open an HSA
  depends on whether that specific plan is HSA-qualified. Once you are
  no longer eligible, you stop contributing — but all existing funds
  remain yours to use on qualified expenses indefinitely.

citations:
  - "HealthEquity HSA Guidebook, pp. 6–7"
  - "WageWorks Guide to HSAs, p. 8"

---

## topic_id: hdhp_basics
display_label: "What is an HDHP?"
suggested_questions:
  - "What is a high-deductible health plan?"
  - "What is an HDHP?"
  - "What kind of health plan do I need for an HSA?"
  - "Does my health plan qualify for an HSA?"
  - "What's the difference between an HDHP and regular insurance?"
next_suggested_topics: [eligibility, contribution_limits, qualified_expenses]

answer: |
  An HSA-qualified health plan — often called a High-Deductible Health
  Plan (HDHP) — is insurance that typically comes with lower monthly
  premiums than traditional plans, but a higher deductible (the amount
  you pay out-of-pocket before insurance starts covering costs).

  The government sets specific minimum deductible thresholds and maximum
  out-of-pocket limits that a plan must meet to be HSA-eligible. These
  numbers adjust slightly each year. Your HR department or insurance
  provider can confirm whether your specific plan qualifies.

  A common worry is losing your doctor. In most cases, HSA-qualified
  plans use the same healthcare networks as traditional coverage.
  Whether you stay in-network or use an out-of-network provider, you
  can pay whatever you owe directly from your HSA.

  Choosing an HSA-qualified plan may change how you think about
  healthcare spending — but it does not mean compromising the quality
  of care you receive.

citations:
  - "HealthEquity HSA Guidebook, pp. 6, 8"
  - "WageWorks Guide to HSAs, p. 15"

---

## topic_id: qualified_expenses
display_label: "What can I spend it on?"
suggested_questions:
  - "What can I use my HSA for?"
  - "What are qualified medical expenses?"
  - "What can I spend HSA money on?"
  - "Can I use my HSA for prescriptions?"
  - "What counts as a medical expense for HSA?"
  - "Can I use my HSA for dental?"
next_suggested_topics:
  - qualified_expenses_mental_health
  - qualified_expenses_dental_vision
  - qualified_expenses_otc
  - qualified_expenses_premiums
  - qualified_expenses_family

answer: |
  HSA funds can be used for a very wide range of qualified medical
  expenses — far more than most people realize. The IRS defines a
  qualified medical expense as money paid primarily to prevent or treat
  a physical or mental illness.

  Qualified expenses include: doctor and specialist visits, copays and
  coinsurance, hospital stays, prescription drugs, dental care, vision
  care, mental health therapy, hearing aids, and many over-the-counter
  (OTC) products and medications. You can also use HSA funds for your
  spouse and tax dependents, even if they are not on your health plan.

  Items that do NOT qualify include general wellness purchases like
  vitamins (unless prescribed for a specific diagnosed condition), gym
  memberships, or cosmetic-only procedures like teeth whitening.

  Explore the sub-topics below to learn what's covered in specific
  categories.

citations:
  - "HSAs For Dummies, Optum Financial Special Edition, p. 24"
  - "HealthEquity HSA Guidebook, p. 183"
  - "WageWorks Guide to HSAs, p. 67"
  - "HSAs For Dummies, Optum Financial Special Edition, p. 27"

---

## topic_id: qualified_expenses_mental_health
display_label: "Mental health & therapy"
suggested_questions:
  - "Can I use my HSA for therapy?"
  - "Does HSA cover mental health?"
  - "Can I pay for counseling with my HSA?"
  - "Is therapy an eligible HSA expense?"
  - "Can I use my HSA for a psychiatrist?"
next_suggested_topics: [qualified_expenses_otc, triple_tax, young_adults]

answer: |
  Yes — mental health services are qualified medical expenses. Therapy
  sessions, psychiatric care, counseling, and prescription medications
  for mental health conditions can all be paid with HSA funds tax-free.

  This is a point many young adults miss. Gen Z and Millennials report
  high utilization of behavioral and mental health services — yet 46%
  of Gen Z respondents in one study said they would cut mental health
  spending first if their budget tightened. Using an HSA to cover these
  costs means you're paying with pre-tax dollars, effectively getting
  a 22–30% discount (depending on your tax bracket) on care you may
  already be accessing.

  When younger adults understand that HSAs cover mental health therapy
  alongside physical healthcare, their engagement with HSAs increases
  significantly.

citations:
  - "HSAs For Dummies, Optum Financial Special Edition, p. 24"
  - "Generational HSA Divide research document"

---

## topic_id: qualified_expenses_dental_vision
display_label: "Dental & vision"
suggested_questions:
  - "Can I use my HSA for dental?"
  - "Does HSA cover glasses or contacts?"
  - "Can I pay for LASIK with my HSA?"
  - "Is orthodontia covered by HSA?"
  - "Can HSA pay for an eye exam?"
next_suggested_topics: [qualified_expenses_otc, qualified_expenses_premiums, complementary_accounts]

answer: |
  Both dental and vision care are covered HSA expenses — which catches
  many people by surprise, since most health insurance plans do not
  cover them.

  Dental: Checkups, cleanings, fillings, extractions, braces,
  orthodontia, implants, and dentures are all qualified. The exception:
  purely cosmetic procedures like teeth whitening are not eligible.

  Vision: Eye exams, prescription glasses (including frames and
  lenses), contact lenses, contact lens solution, prescription
  sunglasses, and laser eye surgery (such as LASIK or PRK) are all
  eligible. OTC reading glasses count too.

  Since dental and vision costs are often predictable, some people pair
  a Limited Purpose FSA (LPFSA) alongside their HSA specifically to
  cover these expenses — allowing HSA funds to stay invested and
  growing for larger future needs.

citations:
  - "WageWorks Guide to HSAs, p. 67"
  - "HSAs For Dummies, Optum Financial Special Edition, p. 27"
  - "HealthEquity HSA Guidebook, p. 53"

---

## topic_id: qualified_expenses_otc
display_label: "OTC products & prescriptions"
suggested_questions:
  - "Can I buy OTC medicine with my HSA?"
  - "Does HSA cover Tylenol or Advil?"
  - "Can I use my HSA for sunscreen?"
  - "What over-the-counter items are HSA eligible?"
  - "Are menstrual products covered by an HSA?"
  - "Can I buy bandages with my HSA?"
next_suggested_topics: [qualified_expenses_dental_vision, recordkeeping]

answer: |
  Since 2020, a wide range of over-the-counter (OTC) medications and
  products became HSA-eligible without needing a prescription — thanks
  to the CARES Act.

  Eligible OTC items include: allergy medications, pain relievers (like
  Tylenol and Advil), cold and flu treatments, cough syrup, sleep aids,
  stomach remedies, anti-fungal and anti-itch treatments, first-aid
  supplies (bandages, hydrogen peroxide, alcohol wipes), contact lens
  solution, sunscreen with SPF 15 or above, and menstrual care products
  (pads, tampons, cups, liners, etc.).

  Prescription drugs also qualify — generic or brand-name. If you take
  an expensive medication, ask about generic alternatives or check
  whether the manufacturer offers a discount program.

  Note: General toiletries like soap and shampoo do not qualify. Vitamins
  are only eligible if specifically prescribed to treat a diagnosed
  condition (and a letter of medical necessity from your provider may
  be required).

citations:
  - "HealthEquity HSA Guidebook, p. 101"
  - "HSAs For Dummies, Optum Financial Special Edition, pp. 25–26"

---

## topic_id: qualified_expenses_premiums
display_label: "Insurance premiums (exceptions)"
suggested_questions:
  - "Can I use my HSA to pay insurance premiums?"
  - "Can I pay COBRA with my HSA?"
  - "Can my HSA pay for Medicare premiums?"
  - "Can I pay for long-term care with my HSA?"
  - "What insurance can I pay with my HSA?"
next_suggested_topics: [age_65_medicare, portability, qualified_expenses]

answer: |
  Generally, you cannot use HSA funds to pay health insurance premiums.
  But there are important exceptions that can be a real lifeline.

  Premiums you CAN pay with your HSA:
  - COBRA continuation coverage after leaving a job
  - Health coverage while receiving federal or state unemployment
    compensation
  - Qualified long-term care insurance (subject to age-based IRS limits)
  - Medicare Parts A, B, C, and D premiums — but only once you turn 65
  - Retiree health plan premiums (but NOT Medigap/Medicare supplement
    policies)

  If you lose your job, your HSA can cover COBRA premiums tax-free
  while you figure out your next coverage step. This safety net is
  something most young adults don't know exists until they need it.

citations:
  - "HealthEquity HSA Guidebook, pp. 183–184"
  - "HSAs For Dummies, Optum Financial Special Edition, p. 26"
  - "WageWorks Guide to HSAs, p. 67"

---

## topic_id: qualified_expenses_family
display_label: "Paying for family members"
suggested_questions:
  - "Can I use my HSA for my spouse?"
  - "Can I use my HSA for my kids?"
  - "Can I pay for my family's medical bills with my HSA?"
  - "Does HSA cover dependents?"
  - "Can I use HSA for my partner's expenses?"
next_suggested_topics: [contribution_limits, qualified_expenses]

answer: |
  Yes — you can use your HSA to pay qualified medical expenses for your
  spouse and any tax dependents, even if they are not enrolled in your
  HSA-qualified health plan.

  A dependent is generally someone you can claim on your tax return:
  children, stepchildren, and in some cases other qualifying relatives.
  In divorce situations, either parent can use their own HSA to pay a
  child's qualified expenses — even if only one parent claims the child
  as a tax dependent.

  The same rules that define eligible expenses for you apply equally
  to your covered family members. You get the same tax-free benefit
  regardless of whose name is on the medical bill.

citations:
  - "HSAs For Dummies, Optum Financial Special Edition, p. 27"

---

## topic_id: contribution_limits
display_label: "Contribution limits"
suggested_questions:
  - "How much can I put in my HSA?"
  - "What are the HSA contribution limits?"
  - "Is there a max for HSA contributions?"
  - "How much can I contribute to an HSA per year?"
  - "Can my employer also contribute to my HSA?"
  - "What happens if I contribute too much to my HSA?"
next_suggested_topics: [funding_strategy, investment, triple_tax]

answer: |
  The IRS sets annual limits on how much can go into your HSA — from
  all sources combined (you, your employer, family members, anyone).
  These limits adjust each year based on inflation.

  For 2025, the limits are:
  - Self-only coverage: $4,300
  - Family coverage: $8,750
  - Catch-up contribution if you are 55 or older: an extra $1,000

  No matter who contributes, the combined total from all sources cannot
  exceed the annual limit. Only your own contributions and your
  employer's contributions receive the direct tax benefit at the time
  of contribution. Contributions from others (like family members) can
  be claimed as an above-the-line deduction on your tax return.

  If you exceed the limit — even because of an employer contribution —
  you will owe a 6% excise tax on the excess. If you open your HSA
  mid-year, you can still contribute the full year's maximum using the
  "last-month rule," but you must remain eligible through the end of
  the following year or face taxes and a 10% penalty on any overage.

citations:
  - "HealthEquity HSA Guidebook, p. 38"
  - "HealthEquity HSA Guidebook, pp. 77–79, 96"
  - "HSAs For Dummies, Optum Financial Special Edition, p. 13"
  > Note: WageWorks Guide cites 2016 limits; HealthEquity Guidebook
  > reflects current 2025 limits. Always verify with IRS.gov or your
  > HSA provider, as limits adjust annually.

---

## topic_id: investment
display_label: "Investing my HSA"
suggested_questions:
  - "Can I invest my HSA?"
  - "How do I invest my HSA money?"
  - "Does my HSA earn interest?"
  - "Can my HSA grow like a retirement account?"
  - "What investment options does an HSA have?"
  - "Should I invest my HSA?"
next_suggested_topics: [hsa_vs_other, funding_strategy, retirement_planning]

answer: |
  Yes — and this is the most underused HSA feature. You can invest your
  HSA balance in stocks, bonds, mutual funds, and certificates of
  deposit, similar to an IRA or 401(k). Your investment earnings grow
  entirely tax-free.

  Most HSA administrators allow investing once your cash balance reaches
  a minimum threshold — typically $1,000 to $2,000. Any amount above
  that threshold can be moved into investment options. If you need funds
  for a medical expense, you can move money back to cash at any time
  with no tax penalty.

  The math is compelling: saving $3,000 per year for 30 years without
  investing accumulates to about $90,000. Invested at a 7% average
  annual return, that same $3,000 per year grows to approximately
  $306,000 — over $200,000 more, all tax-free for qualified expenses.

  Despite this potential, only 9–15% of HSA holders invest their funds;
  most accounts sit in cash. If you can afford to pay current medical
  expenses out of pocket, letting your HSA balance grow invested is one
  of the most powerful financial moves available to young adults.

citations:
  - "HealthEquity HSA Guidebook, pp. 66, 127–129"
  - "HSAs For Dummies, Optum Financial Special Edition, p. 20"
  - "WageWorks Guide to HSAs, p. 64"
  - "Behavioral Architecture of Financial Avoidance research document"

---

## topic_id: hsa_vs_other
display_label: "HSA vs 401(k), FSA & IRA"
suggested_questions:
  - "How is an HSA different from a 401k?"
  - "What's the difference between HSA and FSA?"
  - "HSA vs FSA — which is better?"
  - "How does an HSA compare to an IRA?"
  - "Is an HSA better than a 401k?"
  - "Should I choose an HSA or an FSA?"
next_suggested_topics: [triple_tax, complementary_accounts, misconceptions]

answer: |
  The HSA is the only account in the U.S. that combines all three tax
  benefits: tax-free contributions, tax-free growth, and tax-free
  withdrawals for qualified expenses. Every other account offers only
  one or two of those.

  HSA vs 401(k): Both allow pre-tax contributions. But 401(k)
  withdrawals are taxed as income in retirement. HSA withdrawals for
  qualified medical expenses are never taxed. Additionally, HSA
  payroll contributions skip FICA taxes (Social Security and Medicare)
  — a benefit 401(k) contributions do not get.

  HSA vs Traditional IRA: IRAs reduce your taxable income now but are
  taxed on withdrawal. HSA withdrawals for qualified expenses are tax-
  free at any time. High earners may also lose IRA deductibility above
  certain income thresholds — HSAs have no income limit.

  HSA vs FSA: The FSA's critical drawback is the "use it or lose it"
  rule — unspent FSA funds generally expire at year-end. HSA funds
  roll over indefinitely. Confusing these two accounts is one of the
  most common barriers to HSA adoption among young adults.

citations:
  - "HealthEquity HSA Guidebook, pp. 5–6, 29"
  - "WageWorks Guide to HSAs, p. 15"
  - "Behavioral Architecture of Financial Avoidance research document"

---

## topic_id: portability
display_label: "It's yours — forever"
suggested_questions:
  - "What happens to my HSA if I change jobs?"
  - "Do I lose my HSA if I leave my employer?"
  - "Is my HSA portable?"
  - "Who owns my HSA?"
  - "What happens to HSA money I don't use?"
  - "Does my HSA expire?"
next_suggested_topics: [investment, age_65_medicare, what_is_hsa]

answer: |
  Your HSA belongs to you — not your employer, not your insurance
  company. It stays with you when you change jobs, change health plans,
  move, or get married. Think of it the same way as a 401(k): it's
  yours.

  Your HSA balance rolls over automatically every year. There is no
  deadline and no "use it or lose it" pressure. If you don't spend the
  money this year, it stays in your account and keeps growing.

  If you lose HSA eligibility — for example, by switching to a
  non-qualifying health plan — you stop being able to make new
  contributions. But every dollar already in the account remains yours,
  and you can keep spending it on qualified medical expenses for as
  long as you need.

  When you pass away, your HSA becomes part of your estate. If your
  spouse is your named beneficiary, they can inherit the account as
  their own HSA — tax-free.

citations:
  - "HealthEquity HSA Guidebook, p. 6"
  - "HSAs For Dummies, Optum Financial Special Edition, p. 42"
  - "WageWorks Guide to HSAs, p. 75"

---

## topic_id: funding_strategy
display_label: "How should I fund my HSA?"
suggested_questions:
  - "How should I contribute to my HSA?"
  - "Should I max out my HSA?"
  - "How do I get the most from my HSA?"
  - "Should I contribute to my HSA or 401k first?"
  - "How much should I put in my HSA?"
  - "My employer contributes to my HSA — what should I do?"
next_suggested_topics: [investment, contribution_limits, complementary_accounts]

answer: |
  A good starting rule: always contribute at least enough to capture any
  employer match or employer contribution your plan offers. That is free
  money — do not leave it on the table.

  After capturing your employer's contribution, consider contributing up
  to the full IRS annual maximum. Because HSAs offer more tax advantages
  than 401(k)s — including the FICA exemption on payroll contributions
  — many financial planners suggest maxing your HSA before adding extra
  to a 401(k) beyond any employer match.

  If your budget allows, consider paying current medical expenses out
  of pocket and letting your entire HSA balance grow invested. You can
  reimburse yourself for old expenses at any time — even years later —
  as long as the expense occurred after your HSA was opened. This
  strategy maximizes your invested balance and compounds your tax-free
  growth.

  If money is tight, even small regular contributions add up. HSA funds
  never expire, and every pre-tax dollar saved reduces your tax bill
  now and grows your balance for later.

citations:
  - "HealthEquity HSA Guidebook, pp. 118–119"
  - "HealthEquity HSA Guidebook, p. 49"

---

## topic_id: young_adults
display_label: "Why does this matter for me?"
suggested_questions:
  - "I'm young and healthy — why do I need an HSA?"
  - "Why should I care about an HSA?"
  - "I never go to the doctor. Should I get an HSA?"
  - "What's in it for me as a young person?"
  - "Is an HSA worth it if I don't have many medical expenses?"
  - "I'm just starting out — is an HSA for me?"
next_suggested_topics:
  - qualified_expenses_mental_health
  - triple_tax
  - investment
  - misconceptions

answer: |
  The "I'm healthy, I don't need this" mindset is the most common reason
  young adults miss out on one of the best financial tools available to
  them. Research confirms it: only 6% of working Americans aged 18 to
  34 can correctly describe all three HSA tax benefits.

  Here's the reframe: being young is actually the best time to open an
  HSA. If you rarely need healthcare, your money just stays in the
  account and grows — potentially for decades, entirely tax-free. The
  less you spend now, the more you accumulate for later.

  And young adults use healthcare more than the "invincible" image
  suggests. Gen Z and Millennials are among the highest users of mental
  health and behavioral health services. HSAs cover therapy,
  prescriptions, and many other expenses you might already be paying
  for out of pocket.

  The most common moment young adults realize HSA value is when they
  age off a parent's health plan at 26 — or face a surprise medical
  bill. Starting before either of those moments means you'll have a
  funded account ready when you actually need it.

citations:
  - "Generational HSA Divide research document"
  - "Behavioral Architecture of Financial Avoidance research document"
  - "HSA Bank Health and Wealth Index research document"

---

## topic_id: age_65_medicare
display_label: "HSA at age 65 & Medicare"
suggested_questions:
  - "What happens to my HSA when I turn 65?"
  - "Can I use my HSA in retirement?"
  - "Does Medicare affect my HSA?"
  - "Can I use my HSA to pay Medicare premiums?"
  - "What happens to my HSA when I enroll in Medicare?"
next_suggested_topics: [retirement_planning, portability, investment]

answer: |
  At age 65, your HSA becomes even more flexible. You can still use it
  tax-free for any qualified medical expense. But you can now also use
  it for non-medical expenses without penalty — you'll just pay ordinary
  income tax on those withdrawals, the same as a traditional IRA.

  Once you enroll in Medicare, you can no longer make new HSA
  contributions. But your existing balance remains available. You can
  use it to pay Medicare premiums for Parts A, B, C (Medicare
  Advantage), and D (prescription drugs) — as well as copays and
  coinsurance. The one exception: HSA funds cannot pay for a Medigap
  (Medicare supplement) policy.

  If you delay Medicare past 65 and keep an HSA-qualified health plan,
  you can keep contributing — including the $1,000 catch-up
  contribution — for as long as you remain eligible.

  For married couples where both spouses are 55 or older, each can
  make their own $1,000 catch-up contribution. Each spouse must have
  their own separate HSA account for this to work.

citations:
  - "HealthEquity HSA Guidebook, pp. 77–78"
  - "WageWorks Guide to HSAs, p. 75"

---

## topic_id: retirement_planning
display_label: "HSA for retirement"
suggested_questions:
  - "Can I use my HSA for retirement?"
  - "How does an HSA help with retirement savings?"
  - "Should I use my HSA as a retirement account?"
  - "How much will I need for healthcare in retirement?"
  - "Is an HSA a good long-term savings tool?"
next_suggested_topics: [investment, age_65_medicare, hsa_vs_other]

answer: |
  Retirement healthcare costs are one of the biggest financial risks
  most people underestimate. According to the Employee Benefit Research
  Institute (EBRI), a married couple with average prescription drug
  needs will need approximately $366,000 to cover out-of-pocket medical
  expenses in retirement.

  An HSA is uniquely positioned to address this. Unlike a 401(k) or
  IRA, HSA withdrawals for healthcare are never taxed — even in
  retirement. If you invest your HSA contributions throughout your
  working years, those funds can grow substantially, entirely tax-free.

  Young people just starting their careers have the greatest advantage:
  decades of tax-free compounding ahead of them. Even modest regular
  contributions, invested over time, can make a significant difference.
  It is never too early — or too late — to start.

  After age 65, HSA funds can also be used penalty-free for non-medical
  expenses (taxed as ordinary income), giving you a flexible additional
  reserve alongside your 401(k) and Social Security.

citations:
  - "HealthEquity HSA Guidebook, pp. 8–9, 118"

---

## topic_id: recordkeeping
display_label: "Receipts & recordkeeping"
suggested_questions:
  - "Do I need to save receipts for my HSA?"
  - "How do I track my HSA spending?"
  - "What records do I need to keep for my HSA?"
  - "Can I get audited on my HSA?"
  - "How do I reimburse myself from my HSA?"
next_suggested_topics: [qualified_expenses, contribution_limits]

answer: |
  Treat your HSA records the way you would any financial account —
  savings, investment, or credit card. Keep documentation showing what
  you spent and why it was a qualified expense.

  Always save itemized receipts and any Explanation of Benefits (EOB)
  notices from your health plan. If you paid for a medical expense out
  of pocket and want to reimburse yourself from your HSA later — even
  years later — those receipts make it possible. There is no IRS
  deadline on reimbursement, as long as the expense occurred after your
  HSA was opened.

  If the IRS ever questions your HSA withdrawals, your receipts are your
  defense. Without them, a qualified withdrawal could be treated as
  non-qualified — triggering income tax plus a 20% penalty.

  Most HSA providers have an online portal or app where you can track
  transactions and store receipts digitally. Build the habit early and
  it takes almost no time.

citations:
  - "HSAs For Dummies, Optum Financial Special Edition, p. 20"
  - "HealthEquity HSA Guidebook, p. 130"

---

## topic_id: complementary_accounts
display_label: "HSA + FSA/HRA together"
suggested_questions:
  - "Can I have both an HSA and an FSA?"
  - "What is a limited purpose FSA?"
  - "Can my employer give me an HRA if I have an HSA?"
  - "What is an HSA-compatible FSA?"
  - "How do I pair my HSA with other benefits?"
next_suggested_topics: [hsa_vs_other, qualified_expenses_dental_vision, funding_strategy]

answer: |
  In most cases, having a standard Health FSA or general-purpose HRA
  alongside an HSA will disqualify you from contributing to the HSA.
  However, there are HSA-compatible versions designed to work together.

  A Limited Purpose FSA (LPFSA) covers only dental and vision expenses.
  Because it doesn't cover general medical expenses, it doesn't
  disqualify your HSA. Using both lets you pay predictable dental and
  vision costs from the LPFSA (with its "use it or lose it" FSA funds)
  while keeping your HSA balance invested and growing for everything
  else.

  A Post-Deductible HRA is also compatible — it only reimburses medical
  expenses after you've met your HDHP's minimum deductible, so it
  doesn't interfere with HSA eligibility.

  The strategic advantage: pairing an LPFSA with a maxed-out HSA lets
  you protect more of your HSA balance for long-term investment, since
  dental and vision costs are covered elsewhere.

citations:
  - "WageWorks Guide to HSAs, p. 39"
  - "HealthEquity HSA Guidebook, pp. 53–54"

---

## topic_id: misconceptions
display_label: "Common HSA myths"
suggested_questions:
  - "Is an HSA complicated?"
  - "I've heard HSAs are confusing — is that true?"
  - "What do people get wrong about HSAs?"
  - "Are there myths about HSAs I should know?"
  - "I thought I had to spend my HSA money every year"
next_suggested_topics: [what_is_hsa, young_adults, triple_tax]

answer: |
  HSAs have a reputation for being complicated — but that reputation is
  mostly undeserved. As one guide puts it: "If you can open a savings
  account, you can handle an HSA."

  Myth 1: "It's use-it-or-lose-it." False. HSA funds roll over
  indefinitely. There is no deadline to spend the money.

  Myth 2: "It's only for sick people or big expenses." False. HSAs
  cover everyday costs like prescriptions, OTC medications, therapy,
  dental, and vision — things most people already pay for.

  Myth 3: "It's the same as an FSA." No. FSAs do have a use-it-or-
  lose-it rule. HSAs are permanent, portable accounts that you own.

  Myth 4: "I can't invest my HSA." False. Most HSAs let you invest in
  mutual funds, stocks, and more — and those earnings are entirely
  tax-free.

  Myth 5: "My employer controls it." False. You own your HSA. Your
  employer can contribute to it but has no control over how you use it.

  Despite these facts, 66% of HSA holders do not know how their funds
  are invested, and over 80% of lower-literacy holders don't know if
  their balance is in cash or market assets. Knowing even the basics
  puts you ahead of the majority of account holders.

citations:
  - "HSAs For Dummies, Optum Financial Special Edition, Introduction, p. 1"
  - "WageWorks Guide to HSAs, p. 75"
  - "Behavioral Architecture of Financial Avoidance research document"

---

## topic_id: non_qualified_withdrawals
display_label: "What if I spend it wrong?"
suggested_questions:
  - "What happens if I use my HSA for non-medical expenses?"
  - "What is the penalty for misusing my HSA?"
  - "Can I withdraw HSA money for anything I want?"
  - "What if I accidentally spend HSA money on something that doesn't qualify?"
  - "Is there a penalty for wrong HSA withdrawals?"
next_suggested_topics: [qualified_expenses, age_65_medicare, recordkeeping]

answer: |
  If you use HSA funds for a non-qualified expense before age 65, you
  will owe ordinary income tax on that amount plus a 20% penalty. That
  is steep — so knowing what qualifies matters.

  After age 65, the 20% penalty disappears. You can use HSA funds for
  any purpose — but non-medical withdrawals are still subject to
  ordinary income tax, just like a traditional 401(k).

  If you accidentally use your HSA for a non-qualified expense, some
  HSA administrators will allow you to return the funds before the tax
  filing deadline without penalty — check with your specific provider.

  You cannot deduct an expense on your taxes and also use HSA funds for
  the same expense. "Double-dipping" is not permitted by the IRS.

citations:
  - "HealthEquity HSA Guidebook, p. 101"
  - "WageWorks Guide to HSAs, p. 75"

---

## topic_id: opening_an_hsa
display_label: "How do I open an HSA?"
suggested_questions:
  - "How do I open an HSA?"
  - "Where can I get an HSA?"
  - "How do I start an HSA?"
  - "Can I open an HSA on my own?"
  - "Do I open my HSA through my employer?"
next_suggested_topics: [eligibility, contribution_limits, funding_strategy]

answer: |
  You can open an HSA through several channels depending on your
  situation.

  Through your employer: Most people enroll during open enrollment
  using their HR or benefits portal. If your employer offers an HSA-
  qualified health plan, they typically have a preferred HSA provider
  already set up, and contributions can come directly through payroll
  (with FICA tax savings).

  On your own: You can open an HSA independently at a bank, credit
  union, or HSA-specific administrator. This is common for self-
  employed individuals or people on marketplace plans. You contribute
  after-tax dollars and claim the deduction on your federal tax return.

  When comparing providers, look at: monthly fees and transaction fees,
  investment options and minimum balance requirements, ease of access
  (app, online portal), and whether automated investing is available.
  Lower fees compound into meaningfully more money over time.

  Your HSA custodian will have you complete a trust or custodial
  agreement (IRS Form 5305-B or 5305-C). Most providers allow this
  entirely online.

citations:
  - "HealthEquity HSA Guidebook, pp. 62–66"

---

## FULL TOPIC INDEX (Summary Table)

| topic_id | display_label | next_suggested_topics |
|---|---|---|
| what_is_hsa | What is an HSA? | triple_tax, eligibility, portability |
| triple_tax | Triple Tax Advantage | eligibility, contribution_limits, hsa_vs_other |
| eligibility | Am I eligible? | hdhp_basics, contribution_limits, misconceptions |
| hdhp_basics | What is an HDHP? | eligibility, contribution_limits, qualified_expenses |
| qualified_expenses | What can I spend it on? | qualified_expenses_mental_health, qualified_expenses_dental_vision, qualified_expenses_otc, qualified_expenses_premiums, qualified_expenses_family |
| qualified_expenses_mental_health | Mental health & therapy | qualified_expenses_otc, triple_tax, young_adults |
| qualified_expenses_dental_vision | Dental & vision | qualified_expenses_otc, qualified_expenses_premiums, complementary_accounts |
| qualified_expenses_otc | OTC products & prescriptions | qualified_expenses_dental_vision, recordkeeping |
| qualified_expenses_premiums | Insurance premiums (exceptions) | age_65_medicare, portability, qualified_expenses |
| qualified_expenses_family | Paying for family members | contribution_limits, qualified_expenses |
| contribution_limits | Contribution limits | funding_strategy, investment, triple_tax |
| investment | Investing my HSA | hsa_vs_other, funding_strategy, retirement_planning |
| hsa_vs_other | HSA vs 401(k), FSA & IRA | triple_tax, complementary_accounts, misconceptions |
| portability | It's yours — forever | investment, age_65_medicare, what_is_hsa |
| funding_strategy | How should I fund my HSA? | investment, contribution_limits, complementary_accounts |
| young_adults | Why does this matter for me? | qualified_expenses_mental_health, triple_tax, investment, misconceptions |
| age_65_medicare | HSA at age 65 & Medicare | retirement_planning, portability, investment |
| retirement_planning | HSA for retirement | investment, age_65_medicare, hsa_vs_other |
| recordkeeping | Receipts & recordkeeping | qualified_expenses, contribution_limits |
| complementary_accounts | HSA + FSA/HRA together | hsa_vs_other, qualified_expenses_dental_vision, funding_strategy |
| misconceptions | Common HSA myths | what_is_hsa, young_adults, triple_tax |
| non_qualified_withdrawals | What if I spend it wrong? | qualified_expenses, age_65_medicare, recordkeeping |
| opening_an_hsa | How do I open an HSA? | eligibility, contribution_limits, funding_strategy |

---

## IMPLEMENTATION NOTES FOR content_script.py

### Node count
23 topic nodes total: 15 top-level + 5 qualified_expenses sub-nodes +
3 auxiliary nodes (non_qualified_withdrawals, opening_an_hsa, hdhp_basics)

### Free-text matching
Each node's `suggested_questions` list is the vocabulary for keyword
or fuzzy matching. For a scripted bot, run incoming text against all
`suggested_questions` across all nodes. Return the highest-scoring
topic_id. Recommended minimum: TF-IDF or simple Jaccard on tokens.

### Displaying citations
Store citations as a list of strings per node. Render below the answer:

  📚 Sources:
  • HealthEquity HSA Guidebook, p. 25
  • HSAs For Dummies, Optum Financial Special Edition, Introduction, p. 1

### "You might also ask…" follow-up buttons
After each answer renders, show buttons using the display_label of each
topic_id listed in that node's next_suggested_topics.

### Welcome / home screen default buttons
On first load, offer entry buttons for:
  what_is_hsa       → "What is an HSA?"
  young_adults      → "Why does this matter for me?"
  triple_tax        → "Triple Tax Advantage"
  misconceptions    → "Common HSA myths"
  qualified_expenses → "What can I spend it on?"

### Contribution limits maintenance
The WageWorks Guide (2016) contains outdated dollar figures. The
HealthEquity Guidebook reflects 2025 limits ($4,300 / $8,750 / +$1,000
catch-up). Update the `contribution_limits` answer annually each fall
when IRS announces the following year's limits. Flag this node in your
content script with a `requires_annual_update: true` field.

### qualified_expenses as a hub node
The `qualified_expenses` node is designed to function as a menu —
its answer ends with "Explore the sub-topics below." In the UI, render
its five sub-topic buttons immediately after the answer text, not just
in a "you might also ask" section. This parent-child pattern makes
the biggest topic browsable without overwhelming the user with one
very long answer.
