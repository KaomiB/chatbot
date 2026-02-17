// ============================================================
// HSA TASK BREAKER — Hardcoded Task Library
// Copy this object into your frontend JS / React component.
// Zero API calls. Fuzzy-match user input to task_id via keywords.
// ============================================================

export const TASK_LIBRARY = {

  // ──────────────────────────────────────────────────────────
  // TASK 1: Open an HSA for the first time
  // ──────────────────────────────────────────────────────────
  open_hsa: {
    id: "open_hsa",
    label: "Open an HSA for the first time",
    match_keywords: ["open", "start", "set up", "create", "get an hsa", "new hsa", "how do i open", "sign up"],
    gentle_note: "This looks like a lot of steps written out, but each one is tiny. You don't have to do them all today.",
    steps: {
      gentle: [
        {
          text: "Check if your health plan says 'HSA-eligible', 'HDHP', or 'High-Deductible' anywhere in the name or plan documents.",
          time: "~5 min",
          sub_steps: [
            { text: "Find your insurance card or the email from HR when you enrolled.", time: "~2 min" },
            { text: "Look for the words 'HDHP', 'HSA-eligible', 'High-Deductible', or 'Bronze/Catastrophic' (if on a marketplace plan).", time: "~1 min" },
            { text: "If you can't find it, text or email your HR contact and ask: 'Is my current health plan HSA-eligible?'", time: "~2 min" }
          ]
        },
        {
          text: "Find out if your employer already has an HSA provider set up for you.",
          time: "~5 min",
          sub_steps: [
            { text: "Log into your employee benefits portal (the same place you enrolled in health insurance).", time: "~2 min" },
            { text: "Look for a section called 'HSA', 'Benefits Accounts', or 'HealthEquity / Optum / Fidelity'.", time: "~2 min" },
            { text: "If you see an HSA option, your employer has already done the hard part — you just need to activate it.", time: "~1 min" }
          ]
        },
        {
          text: "Open or activate your account — this usually takes about 10 minutes online.",
          time: "~10 min",
          sub_steps: [
            { text: "Click the 'Open HSA' or 'Enroll' button in your benefits portal, or go directly to your HSA provider's website.", time: "~2 min" },
            { text: "Have your Social Security Number and a photo ID ready — federal law requires identity verification (same as opening a bank account).", time: "~3 min" },
            { text: "Fill out the online form. You'll be asked for your name, address, date of birth, and SSN.", time: "~5 min" }
          ]
        },
        {
          text: "Set a contribution amount — even $10/month is a real start.",
          time: "~5 min",
          sub_steps: [
            { text: "In your payroll or benefits portal, find the HSA contribution field.", time: "~2 min" },
            { text: "Enter any amount — $25, $50, whatever feels manageable. You can change this anytime.", time: "~1 min" },
            { text: "If your employer contributes to your HSA, that money arrives automatically — you don't need to do anything extra for it.", time: "~1 min" }
          ]
        },
        {
          text: "Name a beneficiary (takes 2 minutes, easy to skip and regret later).",
          time: "~2 min",
          sub_steps: [
            { text: "In your HSA account settings, look for 'Beneficiary'.", time: "~1 min" },
            { text: "Enter the name and date of birth of whoever you'd want to inherit the account (a parent, partner, sibling, etc.).", time: "~1 min" }
          ]
        }
      ],
      medium: [
        {
          text: "Confirm your health plan is HSA-eligible by checking for 'HDHP' or 'HSA-eligible' on your insurance card, HR portal, or plan documents.",
          time: "~5 min",
          sub_steps: [
            { text: "Find your insurance card or HR enrollment email.", time: "~2 min" },
            { text: "Look for 'HDHP', 'HSA-eligible', or 'High-Deductible'. Not sure? Email HR: 'Is my plan HSA-eligible?'", time: "~3 min" }
          ]
        },
        {
          text: "Log into your employee benefits portal and find the HSA enrollment section.",
          time: "~5 min",
          sub_steps: [
            { text: "Go to your benefits portal (the same one used for health insurance enrollment).", time: "~2 min" },
            { text: "Look for 'HSA', 'Health Savings Account', or the name of a provider like HealthEquity, Optum, or Fidelity.", time: "~3 min" }
          ]
        },
        {
          text: "Complete the online enrollment form — you'll need your SSN and a photo ID.",
          time: "~10 min",
          sub_steps: [
            { text: "Gather your Social Security Number and driver's license or passport.", time: "~2 min" },
            { text: "Fill out name, address, date of birth, and SSN. Accept the custodial agreement (IRS Form 5305-B or C).", time: "~8 min" }
          ]
        },
        {
          text: "Set your payroll contribution amount — even a small amount counts.",
          time: "~5 min",
          sub_steps: [
            { text: "In your payroll portal, find the HSA contribution field.", time: "~2 min" },
            { text: "Enter your chosen monthly or per-paycheck amount. You can update this anytime during the year.", time: "~3 min" }
          ]
        },
        {
          text: "Add a beneficiary in your HSA account settings.",
          time: "~2 min"
        }
      ],
      detailed: [
        { text: "Find your insurance card or the enrollment email HR sent when you chose your health plan.", time: "~2 min" },
        { text: "Check the plan name for 'HDHP', 'High-Deductible', 'HSA-eligible', 'Bronze', or 'Catastrophic'.", time: "~2 min" },
        { text: "If you're not sure, send this exact message to HR: 'Quick question — is my current health plan HSA-eligible?'", time: "~2 min" },
        { text: "Log into your employee benefits or HR portal (the same site where you enrolled in health insurance).", time: "~3 min" },
        { text: "Navigate to the section for 'HSA', 'Spending Accounts', or your HSA provider name (common ones: HealthEquity, Optum, Fidelity, HSA Bank).", time: "~3 min" },
        { text: "Click 'Open HSA' or 'Enroll'. If you don't see this option, call HR or check your benefits handbook.", time: "~2 min" },
        { text: "Get your Social Security Number and a photo ID (driver's license or passport) — you'll need both for identity verification.", time: "~3 min" },
        { text: "Fill in your full legal name, current mailing address, date of birth, and SSN in the online form.", time: "~5 min" },
        { text: "Review and accept the custodial agreement (IRS Form 5305-B or 5305-C). This is standard — it makes the account legally yours.", time: "~2 min" },
        { text: "Go to your payroll portal and find the HSA contribution field. Enter any amount — even $10 per paycheck. You can change this later.", time: "~5 min" },
        { text: "Navigate to your HSA account settings and add a beneficiary — the person who inherits the account if something happens to you.", time: "~2 min" },
        { text: "Write down your HSA account number and provider name somewhere safe (a notes app is fine).", time: "~1 min" }
      ]
    }
  },

  // ──────────────────────────────────────────────────────────
  // TASK 2: Figure out if my health plan qualifies
  // ──────────────────────────────────────────────────────────
  check_eligibility: {
    id: "check_eligibility",
    label: "Figure out if my health plan qualifies for an HSA",
    match_keywords: ["eligible", "qualify", "qualifies", "hdhp", "high deductible", "my plan", "does my insurance", "can i get", "am i eligible", "my coverage"],
    gentle_note: "You only need to find one piece of paper (or one email) to figure this out. It's genuinely not hard once you know where to look.",
    steps: {
      gentle: [
        {
          text: "Find the name of your health insurance plan — it's on your insurance card or in your HR enrollment email.",
          time: "~3 min",
          sub_steps: [
            { text: "Check your wallet for your insurance card. The plan name is usually on the front.", time: "~1 min" },
            { text: "Or search your email inbox for 'benefits enrollment' or your insurance company's name.", time: "~2 min" }
          ]
        },
        {
          text: "Look for these words in the plan name or description: 'HDHP', 'High-Deductible', 'HSA-eligible', 'Consumer Choice', 'Bronze', or 'Catastrophic'.",
          time: "~2 min",
          sub_steps: [
            { text: "If any of those words appear: very likely yes, you qualify. Keep going.", time: "~1 min" },
            { text: "If the plan name says 'PPO', 'HMO', 'EPO', or 'Platinum/Gold': likely not HSA-eligible, but still worth a quick confirmation.", time: "~1 min" }
          ]
        },
        {
          text: "When in doubt, just ask HR directly — this is a totally normal question.",
          time: "~2 min",
          sub_steps: [
            { text: "Send this message: 'Hi — quick question, is my current health plan HSA-eligible?'", time: "~1 min" },
            { text: "That's it. HR gets this question all the time.", time: "~1 min" }
          ]
        }
      ],
      medium: [
        {
          text: "Find your insurance card or HR enrollment email and note the plan name.",
          time: "~3 min"
        },
        {
          text: "Search the plan name for: 'HDHP', 'High-Deductible', 'HSA-eligible', 'Consumer Choice', 'Bronze', or 'Catastrophic'.",
          time: "~2 min",
          sub_steps: [
            { text: "These words = likely eligible. 'PPO', 'HMO', 'Gold', 'Platinum' = likely not eligible.", time: "~1 min" }
          ]
        },
        {
          text: "If you're on a marketplace plan (not through an employer), check your plan summary for the annual deductible. For 2025, it must be at least $1,650 (individual) or $3,300 (family).",
          time: "~5 min"
        },
        {
          text: "Also confirm you're not enrolled in Medicare or claimed as a dependent on someone else's taxes — both disqualify you.",
          time: "~2 min"
        },
        {
          text: "Still unsure? Email HR: 'Is my current health plan HSA-eligible?' — that's the fastest answer.",
          time: "~2 min"
        }
      ],
      detailed: [
        { text: "Find your insurance card (in your wallet or on your insurance company's app).", time: "~2 min" },
        { text: "Note the full plan name shown on the card.", time: "~1 min" },
        { text: "Search your email inbox for 'open enrollment' or your insurer's name to find your plan documents.", time: "~3 min" },
        { text: "In the plan name or summary, look for: 'HDHP', 'High-Deductible Health Plan', 'HSA-eligible', 'Consumer Choice', 'Bronze', or 'Catastrophic'.", time: "~2 min" },
        { text: "If on a marketplace plan: find your annual deductible. It must be at least $1,650 (individual) or $3,300 (family) for 2025.", time: "~3 min" },
        { text: "Confirm you are not enrolled in Medicare Part A or B (enrolling in Medicare ends HSA eligibility).", time: "~1 min" },
        { text: "Confirm no one is claiming you as a dependent on their federal tax return.", time: "~1 min" },
        { text: "Confirm you don't have a general-purpose Health FSA from an employer (this disqualifies you — a Limited Purpose FSA is fine).", time: "~2 min" },
        { text: "If still unsure, send HR this message: 'Hi — is my current health plan HSA-eligible? I'd like to open an HSA.'", time: "~2 min" }
      ]
    }
  },

  // ──────────────────────────────────────────────────────────
  // TASK 3: Got off my parents' plan — what do I do now?
  // ──────────────────────────────────────────────────────────
  aged_off_parents_plan: {
    id: "aged_off_parents_plan",
    label: "I just aged off my parents' plan — figure out what to do",
    match_keywords: ["parents plan", "parent's plan", "turned 26", "age off", "aged off", "lost coverage", "no insurance", "off my parents"],
    gentle_note: "This is a genuinely stressful life transition and it's okay that it feels overwhelming. You have a 60-day window from when you lose coverage to enroll — so you have a little time.",
    steps: {
      gentle: [
        {
          text: "First, breathe — you have 60 days from losing coverage to enroll in a new plan. You are not in immediate crisis.",
          time: "~0 min"
        },
        {
          text: "Find out your exact last day of coverage on your parents' plan.",
          time: "~5 min",
          sub_steps: [
            { text: "Call the insurance number on the back of your current card, or ask your parent to check with their HR.", time: "~5 min" },
            { text: "Write down this date somewhere. It's your deadline countdown clock.", time: "~1 min" }
          ]
        },
        {
          text: "Check if your job offers health insurance — that's usually the simplest path.",
          time: "~5 min",
          sub_steps: [
            { text: "Email HR or check your benefits portal. Ask: 'Do you offer health insurance, and can I enroll now due to a qualifying life event?'", time: "~5 min" },
            { text: "Aging off a parent's plan counts as a qualifying life event — you don't have to wait for open enrollment.", time: "~1 min" }
          ]
        },
        {
          text: "If your job offers an HDHP option, look into it — this is what lets you open an HSA.",
          time: "~5 min",
          sub_steps: [
            { text: "Compare the HDHP to other plan options. Lower monthly premium, higher deductible.", time: "~5 min" },
            { text: "If healthy and rarely visit doctors, the HDHP often costs less total — especially with an employer HSA contribution.", time: "~1 min" }
          ]
        },
        {
          text: "No job coverage? Check healthcare.gov — you qualify for a special enrollment period.",
          time: "~10 min"
        }
      ],
      medium: [
        { text: "Find your exact last day of coverage on your parents' plan. Call the insurer or ask your parent to check with their HR.", time: "~5 min" },
        { text: "Check if your employer offers health insurance. Aging off a parent's plan is a qualifying life event — you can enroll outside open enrollment.", time: "~5 min" },
        { text: "If your employer offers plans, compare them. An HDHP (High-Deductible Health Plan) is what makes you eligible for an HSA.", time: "~10 min" },
        { text: "If no employer coverage: go to healthcare.gov and enter your info. You have 60 days from losing coverage to enroll.", time: "~15 min" },
        { text: "Once enrolled in an HSA-eligible plan, open your HSA account through your benefits portal or provider.", time: "~10 min" }
      ],
      detailed: [
        { text: "Call the insurance number on the back of your current card. Ask: 'What is my last day of coverage?'", time: "~5 min" },
        { text: "Write the date down — you have 60 days from that date to get new coverage.", time: "~1 min" },
        { text: "Email your employer's HR: 'I'm losing coverage on my parents' plan on [date]. Do you offer health insurance? Can I enroll now?'", time: "~5 min" },
        { text: "Review the plan options your employer provides. Look for any plan labeled 'HDHP', 'High-Deductible', or 'HSA-eligible'.", time: "~10 min" },
        { text: "Compare the HDHP to other plans: add up (monthly premium × 12) + deductible for each option to see true annual cost.", time: "~10 min" },
        { text: "If your employer contributes to the HSA, factor that into the comparison — it reduces your net cost.", time: "~5 min" },
        { text: "If no employer coverage is available, go to healthcare.gov and start a new application. Select your state.", time: "~10 min" },
        { text: "On healthcare.gov, select 'I lost health coverage' as your reason for enrolling.", time: "~2 min" },
        { text: "Browse Bronze or Catastrophic plans — these are often HSA-eligible and have lower premiums.", time: "~10 min" },
        { text: "Once enrolled in an HDHP, open your HSA through your benefits portal or a provider like Fidelity, HealthEquity, or Lively.", time: "~10 min" },
        { text: "Set a contribution amount — even $25/month gets your account started and your money growing tax-free.", time: "~5 min" }
      ]
    }
  },

  // ──────────────────────────────────────────────────────────
  // TASK 4: Start investing my HSA balance
  // ──────────────────────────────────────────────────────────
  start_investing: {
    id: "start_investing",
    label: "Start investing my HSA balance",
    match_keywords: ["invest", "investing", "grow my hsa", "stocks", "mutual fund", "investment", "make my hsa grow", "not just cash"],
    gentle_note: "Most people never do this step — and it's the one that could make the biggest difference over time. You don't need to know much about investing to start.",
    steps: {
      gentle: [
        {
          text: "Log into your HSA provider's website or app.",
          time: "~2 min",
          sub_steps: [
            { text: "If you're not sure who your provider is, check your HSA debit card or your benefits portal.", time: "~2 min" }
          ]
        },
        {
          text: "Check your current cash balance and find the 'Invest' or 'Investments' section.",
          time: "~3 min",
          sub_steps: [
            { text: "Look for tabs or links labeled 'Invest', 'Investment Options', or 'Grow My HSA'.", time: "~2 min" },
            { text: "Your provider will tell you the minimum cash balance required before you can invest — usually $1,000.", time: "~1 min" }
          ]
        },
        {
          text: "If you've hit the minimum, pick a simple starting option — a target-date fund or a broad index fund.",
          time: "~5 min",
          sub_steps: [
            { text: "Target-date funds (e.g. 'Target 2055') are the lowest-stress option — they automatically adjust as you age. Just pick the year closest to when you'd turn 65.", time: "~3 min" },
            { text: "Or pick a broad market index fund (like a 'Total Market' or 'S&P 500' fund). These tend to have low fees.", time: "~2 min" }
          ]
        },
        {
          text: "Set up automatic investing so you don't have to think about it again.",
          time: "~3 min",
          sub_steps: [
            { text: "Look for 'Auto-invest' or 'Automatic Transfer' in your account settings.", time: "~2 min" },
            { text: "Set it to automatically move any balance above your minimum threshold into your chosen fund.", time: "~1 min" }
          ]
        }
      ],
      medium: [
        { text: "Log into your HSA provider's app or website and navigate to the 'Investments' section.", time: "~3 min" },
        { text: "Check the minimum cash balance required to invest (usually $1,000–$2,000). Note your current balance.", time: "~2 min" },
        {
          text: "If eligible, choose an investment fund. Simplest options:",
          time: "~5 min",
          sub_steps: [
            { text: "Target-date fund: pick the year you'll turn 65. It manages itself.", time: "~2 min" },
            { text: "Index fund: 'Total Market' or 'S&P 500'. Low fees, broad diversification.", time: "~2 min" }
          ]
        },
        { text: "Check the fund's expense ratio — lower is better. Aim for under 0.20%.", time: "~3 min" },
        { text: "Enable auto-invest so any amount above your minimum threshold moves into the fund automatically.", time: "~3 min" }
      ],
      detailed: [
        { text: "Log into your HSA provider's website. (Find it on your HSA debit card or in your benefits portal.)", time: "~2 min" },
        { text: "Navigate to 'Investments', 'Invest', or 'Grow My HSA'.", time: "~2 min" },
        { text: "Note the minimum cash balance required to invest — usually $1,000 or $2,000.", time: "~1 min" },
        { text: "Check your current HSA cash balance. If you're below the minimum, note how far away you are.", time: "~2 min" },
        { text: "If you've hit the minimum: browse the available funds. Look for target-date funds or index funds.", time: "~5 min" },
        { text: "For each fund you're considering, check the expense ratio (the annual fee). Lower than 0.20% is good.", time: "~5 min" },
        { text: "If available, pick a target-date fund matching the year you'll turn 65 (e.g., 'Target 2055'). It automatically adjusts its risk level as you age.", time: "~3 min" },
        { text: "Alternatively, pick a 'Total Market Index' or 'S&P 500 Index' fund for simplicity and low fees.", time: "~3 min" },
        { text: "Enter the amount you want to move into investments initially — start with whatever's above your minimum threshold.", time: "~3 min" },
        { text: "Look for 'Auto-invest' or 'Automatic Transfer' settings. Enable it to automatically sweep any balance above the threshold into your chosen fund.", time: "~3 min" },
        { text: "Save your changes. Your money is now working tax-free.", time: "~1 min" },
        { text: "Set a calendar reminder to check your investment balance once per quarter — that's enough.", time: "~1 min" }
      ]
    }
  },

  // ──────────────────────────────────────────────────────────
  // TASK 5: Use my HSA to pay for therapy or mental health
  // ──────────────────────────────────────────────────────────
  use_for_therapy: {
    id: "use_for_therapy",
    label: "Use my HSA to pay for therapy or mental health care",
    match_keywords: ["therapy", "therapist", "counseling", "mental health", "psychiatrist", "psychologist", "counselor", "mental healthcare", "behavioral health"],
    gentle_note: "Using your HSA for therapy is one of the most direct ways it supports your whole health — not just physical. This is exactly what it's for.",
    steps: {
      gentle: [
        {
          text: "Confirm the service qualifies — therapy, counseling, psychiatry, and mental health prescriptions all do.",
          time: "~1 min"
        },
        {
          text: "Find out if your therapist accepts direct HSA card payment, or if you pay out of pocket and reimburse yourself.",
          time: "~5 min",
          sub_steps: [
            { text: "Ask your therapist or their billing department: 'Do you accept HSA/FSA cards as payment?'", time: "~3 min" },
            { text: "Most therapists do — you'd pay the same way you'd pay with a debit card.", time: "~1 min" }
          ]
        },
        {
          text: "Pay with your HSA debit card directly — done. Or if you paid out of pocket, request a receipt and reimburse yourself.",
          time: "~5 min",
          sub_steps: [
            { text: "To reimburse yourself: log into your HSA provider's app, find 'Reimburse Myself' or 'Distribute Funds', and enter the amount.", time: "~5 min" }
          ]
        },
        {
          text: "Save your receipt — a simple photo on your phone is enough.",
          time: "~1 min",
          sub_steps: [
            { text: "Create a folder called 'HSA Receipts' in your photos app or email and drop it there.", time: "~1 min" }
          ]
        }
      ],
      medium: [
        { text: "Confirm the expense qualifies: therapy, counseling, psychiatry visits, and mental health prescriptions all count as qualified HSA expenses.", time: "~1 min" },
        { text: "Ask your therapist: 'Do you accept HSA/FSA cards?' Most do — you'd pay with your HSA debit card like a regular card.", time: "~3 min" },
        { text: "If your therapist doesn't take cards or you already paid out of pocket: get an itemized receipt.", time: "~2 min" },
        { text: "Log into your HSA provider's website or app and find 'Reimburse Myself' or 'Request Distribution'. Enter the amount and upload the receipt.", time: "~5 min" },
        { text: "Save all receipts — photo in your camera roll, email folder, or Google Drive. You may need them if the IRS ever asks.", time: "~1 min" }
      ],
      detailed: [
        { text: "Confirm the service qualifies: therapy sessions, counseling, psychiatric appointments, mental health medications, and telehealth mental health visits are all qualified HSA expenses.", time: "~1 min" },
        { text: "Contact your therapist or their billing department. Ask: 'Do you accept HSA or FSA debit cards?'", time: "~3 min" },
        { text: "If yes: bring your HSA debit card to your next appointment and pay directly. You don't need to do anything else — the card handles it.", time: "~1 min" },
        { text: "If no, or if you already paid: request an itemized receipt. It should show: provider name, date of service, type of service, and amount paid.", time: "~5 min" },
        { text: "Log into your HSA provider's website or app.", time: "~2 min" },
        { text: "Navigate to 'Reimburse Myself', 'Withdraw Funds', or 'Pay Expense'.", time: "~2 min" },
        { text: "Enter the date of service, provider name, amount, and expense category (usually 'Medical / Mental Health').", time: "~3 min" },
        { text: "Upload a photo of your receipt when prompted (required by most providers).", time: "~2 min" },
        { text: "Submit. The reimbursement usually arrives in your checking account in 1–3 business days.", time: "~1 min" },
        { text: "Save the receipt permanently in a folder called 'HSA Receipts' — you can keep this folder in Google Drive, a notes app, or even just in your email.", time: "~1 min" }
      ]
    }
  },

  // ──────────────────────────────────────────────────────────
  // TASK 6: Handle a surprise medical bill
  // ──────────────────────────────────────────────────────────
  surprise_medical_bill: {
    id: "surprise_medical_bill",
    label: "Handle a surprise medical bill using my HSA",
    match_keywords: ["medical bill", "surprise bill", "unexpected bill", "got a bill", "owe", "hospital bill", "doctor bill", "can't pay", "emergency", "medical debt"],
    gentle_note: "Getting a medical bill you weren't expecting is stressful. This is exactly the situation your HSA is built for — let's take it one step at a time.",
    steps: {
      gentle: [
        {
          text: "Don't panic — you almost certainly have time. Medical bills are rarely due immediately.",
          time: "~0 min"
        },
        {
          text: "Check that the bill is accurate before you pay anything.",
          time: "~10 min",
          sub_steps: [
            { text: "Compare the bill to your Explanation of Benefits (EOB) — this is a letter or email from your insurance company explaining what they paid.", time: "~5 min" },
            { text: "If the numbers don't match, call the billing department and ask them to explain the charges.", time: "~5 min" }
          ]
        },
        {
          text: "Check your HSA balance — log into your HSA provider's app or website.",
          time: "~3 min"
        },
        {
          text: "If your HSA covers it: pay with your HSA debit card, or pay another way and reimburse yourself.",
          time: "~5 min",
          sub_steps: [
            { text: "HSA debit card: call the billing department and give them your card number, or pay online using it.", time: "~5 min" },
            { text: "Reimburse yourself: log into your HSA app, find 'Reimburse Myself', enter the amount, and submit.", time: "~5 min" }
          ]
        },
        {
          text: "Save the receipt and any payment confirmation.",
          time: "~2 min"
        }
      ],
      medium: [
        { text: "Don't pay immediately — first confirm the bill is correct by comparing it to your insurance Explanation of Benefits (EOB).", time: "~10 min" },
        { text: "If anything looks off, call the provider's billing department and ask for an itemized bill. Errors are common.", time: "~10 min" },
        { text: "Check your HSA balance in your provider's app.", time: "~3 min" },
        { text: "Confirm the expense is HSA-qualified (almost all medical services are — doctor visits, labs, hospital stays, prescriptions).", time: "~1 min" },
        { text: "Pay using your HSA debit card directly, or pay another way and log into your HSA to reimburse yourself.", time: "~10 min" },
        { text: "If the bill exceeds your HSA balance, ask the billing office about a payment plan — most will set one up with no interest.", time: "~5 min" },
        { text: "Save all receipts and the EOB together in a folder.", time: "~2 min" }
      ],
      detailed: [
        { text: "Take a breath. Most medical bills have at least 30 days before they're due, and many have 60–90 days.", time: "~1 min" },
        { text: "Find the Explanation of Benefits (EOB) from your insurance company. It usually arrives by mail or in your insurer's online portal within 2–4 weeks of a visit.", time: "~5 min" },
        { text: "Compare the EOB to the bill: the amounts should match what your insurer says you owe.", time: "~5 min" },
        { text: "If they don't match, or the bill lists services you don't recognize, call the billing department and say: 'Can I get an itemized bill and compare it to my EOB?'", time: "~10 min" },
        { text: "Ask if the provider has any financial assistance programs or sliding scale discounts — even many large hospitals have these.", time: "~5 min" },
        { text: "Log into your HSA provider's app or website and check your current balance.", time: "~3 min" },
        { text: "Confirm the expense is HSA-qualified. Doctor visits, hospital stays, lab work, imaging, procedures, and prescriptions are all qualified.", time: "~1 min" },
        { text: "Option A — Pay with HSA debit card: Call the billing number and give your HSA card number, or pay online.", time: "~5 min" },
        { text: "Option B — Reimburse yourself: Log into your HSA, find 'Reimburse Myself' or 'Distribute Funds', enter the amount and date of service.", time: "~5 min" },
        { text: "If the bill is more than your HSA balance: contact billing to set up an interest-free payment plan while you continue contributing to your HSA.", time: "~10 min" },
        { text: "Save the itemized bill and payment confirmation in your HSA receipts folder.", time: "~2 min" }
      ]
    }
  },

  // ──────────────────────────────────────────────────────────
  // TASK 7: Figure out my contribution amount / max out my HSA
  // ──────────────────────────────────────────────────────────
  set_contribution: {
    id: "set_contribution",
    label: "Figure out how much to contribute to my HSA",
    match_keywords: ["how much", "contribution", "contribute", "max out", "limit", "maximum", "how much should i put", "what's the limit", "increase my contribution"],
    gentle_note: "There's no 'right' answer here that works for everyone. Even a small regular contribution is genuinely worthwhile — it just needs to be whatever doesn't stress your budget.",
    steps: {
      gentle: [
        {
          text: "Check what the IRS limit is for this year.",
          time: "~2 min",
          sub_steps: [
            { text: "For 2025: $4,300 if you have individual (self-only) coverage. $8,750 if you have a family plan.", time: "~1 min" },
            { text: "If you're 55 or older, you can add $1,000 more on top of that.", time: "~1 min" }
          ]
        },
        {
          text: "Check if your employer contributes anything — that counts toward your limit but is free money.",
          time: "~5 min",
          sub_steps: [
            { text: "Check your benefits portal or pay stub for any employer HSA contribution.", time: "~5 min" },
            { text: "Subtract your employer's contribution from the annual limit to see how much room you have left.", time: "~1 min" }
          ]
        },
        {
          text: "Decide on a per-paycheck amount that won't strain your budget.",
          time: "~5 min",
          sub_steps: [
            { text: "Divide your target annual contribution by the number of paychecks per year (26 for biweekly, 24 for semi-monthly).", time: "~2 min" },
            { text: "Even $25 per paycheck adds up to $650/year — all tax-free.", time: "~1 min" }
          ]
        },
        {
          text: "Update your payroll contribution in your benefits portal.",
          time: "~5 min"
        }
      ],
      medium: [
        { text: "Look up the 2025 IRS limit: $4,300 (individual) or $8,750 (family). Add $1,000 if you're 55+.", time: "~2 min" },
        { text: "Check your pay stub or benefits portal to see how much your employer contributes. Subtract that from the limit.", time: "~5 min" },
        { text: "Decide your target: anywhere from capturing employer match only, to maxing out the full limit.", time: "~5 min" },
        { text: "Divide by pay periods to get your per-paycheck amount.", time: "~2 min" },
        { text: "Log into your payroll or benefits portal and update your HSA contribution amount.", time: "~5 min" },
        { text: "Note that you can change this anytime — you're not locked in.", time: "~1 min" }
      ],
      detailed: [
        { text: "Look up the current year's IRS HSA contribution limit. For 2025: $4,300 individual, $8,750 family.", time: "~2 min" },
        { text: "Check your pay stub or benefits portal to see if your employer contributes to your HSA and how much (monthly or annual amount).", time: "~5 min" },
        { text: "Calculate: IRS limit minus employer contribution = your maximum allowed contribution.", time: "~2 min" },
        { text: "Review your budget. Decide on a realistic target — options: (a) just the employer match (if any), (b) a fixed comfortable amount, (c) the full annual max.", time: "~10 min" },
        { text: "Divide your target by your number of pay periods (26 for biweekly, 24 for semi-monthly, 12 for monthly) to get your per-paycheck amount.", time: "~2 min" },
        { text: "Log into your payroll or HR benefits portal.", time: "~2 min" },
        { text: "Find the HSA contribution section and enter your per-paycheck amount.", time: "~3 min" },
        { text: "Save the change. It usually takes 1–2 pay periods to take effect.", time: "~1 min" },
        { text: "Set a calendar reminder for October to revisit — you can increase your contribution if you want to max out before year-end.", time: "~2 min" }
      ]
    }
  },

  // ──────────────────────────────────────────────────────────
  // TASK 8: Use my HSA for dental or vision
  // ──────────────────────────────────────────────────────────
  use_for_dental_vision: {
    id: "use_for_dental_vision",
    label: "Use my HSA for a dental or vision expense",
    match_keywords: ["dental", "dentist", "teeth", "glasses", "contacts", "vision", "eye exam", "braces", "orthodontist", "lasik", "optometrist"],
    gentle_note: "A lot of people don't realize HSAs cover dental and vision. This is genuinely one of the most useful day-to-day uses of the account.",
    steps: {
      gentle: [
        {
          text: "Confirm the expense qualifies — most dental and vision care does.",
          time: "~1 min",
          sub_steps: [
            { text: "Dental: checkups, cleanings, fillings, braces, extractions, implants ✓", time: "~0 min" },
            { text: "Vision: eye exams, glasses (frames + lenses), contacts, solution, LASIK ✓", time: "~0 min" },
            { text: "Does not qualify: teeth whitening (cosmetic only), non-prescription sunglasses", time: "~0 min" }
          ]
        },
        {
          text: "Ask your provider if they accept HSA/FSA cards — almost all dental and vision offices do.",
          time: "~2 min"
        },
        {
          text: "Pay with your HSA debit card at the appointment, or reimburse yourself afterward.",
          time: "~5 min",
          sub_steps: [
            { text: "HSA card: hand it over like a regular debit card.", time: "~1 min" },
            { text: "Reimburse yourself: log into your HSA app → 'Reimburse Myself' → enter amount and date.", time: "~5 min" }
          ]
        },
        {
          text: "Keep your receipt.",
          time: "~1 min"
        }
      ],
      medium: [
        { text: "Confirm the expense qualifies: dental cleanings, fillings, braces, implants, eye exams, glasses, contacts, LASIK all qualify. Cosmetic-only procedures (teeth whitening) don't.", time: "~1 min" },
        { text: "Ask your dental or vision office if they accept HSA/FSA cards. Almost all do.", time: "~2 min" },
        { text: "Pay with your HSA debit card directly at checkout, or pay by other means and reimburse yourself through your HSA app.", time: "~5 min" },
        { text: "Save your itemized receipt.", time: "~1 min" }
      ],
      detailed: [
        { text: "Confirm the specific expense is qualified. HSA-eligible: cleanings, fillings, extractions, crowns, root canals, braces, dentures, implants, eye exams, prescription glasses (frames and lenses), contact lenses, contact lens solution, reading glasses, LASIK.", time: "~2 min" },
        { text: "Not eligible: teeth whitening, non-prescription sunglasses, cosmetic enhancements.", time: "~1 min" },
        { text: "Call or check the provider's website to confirm they accept HSA/FSA cards.", time: "~3 min" },
        { text: "If yes: bring your HSA debit card and pay at the appointment. Done.", time: "~1 min" },
        { text: "If no, or if you already paid: request an itemized receipt from the provider.", time: "~3 min" },
        { text: "Log into your HSA provider's app or website.", time: "~2 min" },
        { text: "Go to 'Reimburse Myself' or 'Pay Expense'. Enter the provider name, date, amount, and category (Dental or Vision).", time: "~3 min" },
        { text: "Upload or attach a photo of your receipt.", time: "~2 min" },
        { text: "Submit. Reimbursement usually posts to your checking account in 1–3 business days.", time: "~1 min" },
        { text: "Save the receipt in your HSA receipts folder.", time: "~1 min" }
      ]
    }
  },

  // ──────────────────────────────────────────────────────────
  // TASK 9: Set up recordkeeping so I don't stress later
  // ──────────────────────────────────────────────────────────
  setup_recordkeeping: {
    id: "setup_recordkeeping",
    label: "Set up a simple system for keeping HSA receipts",
    match_keywords: ["receipts", "recordkeeping", "records", "organize", "keep track", "documentation", "irs", "audit", "filing", "receipts folder", "track my hsa"],
    gentle_note: "Setting this up once takes about 10 minutes and saves a lot of anxiety later. You'll never have to worry about losing a receipt again.",
    steps: {
      gentle: [
        {
          text: "Pick one place to store receipts — a phone folder, email label, or Google Drive folder.",
          time: "~3 min",
          sub_steps: [
            { text: "On your phone: create an album called 'HSA Receipts' in your photos app.", time: "~1 min" },
            { text: "In email: create a label or folder called 'HSA Receipts' and forward receipts there.", time: "~2 min" },
            { text: "Google Drive: create a folder called 'HSA Receipts' with subfolders by year.", time: "~2 min" }
          ]
        },
        {
          text: "Photograph or screenshot every receipt right after paying — it takes 10 seconds.",
          time: "~1 min"
        },
        {
          text: "That's it. No spreadsheet required.",
          time: "~0 min"
        }
      ],
      medium: [
        { text: "Choose a storage method: phone album, email folder, Google Drive, or your HSA provider's built-in receipt vault.", time: "~3 min" },
        { text: "Name it something you'll recognize: 'HSA Receipts 2025'.", time: "~1 min" },
        { text: "Check if your HSA provider's app has a receipt storage feature — many do, and it's the most convenient option.", time: "~3 min" },
        { text: "For past receipts: gather any you have and spend 15 minutes photographing and filing them now.", time: "~15 min" },
        { text: "From now on: photograph every HSA-related receipt within 24 hours of the expense.", time: "~1 min" }
      ],
      detailed: [
        { text: "Log into your HSA provider's app. Check whether it has a built-in 'Receipt Vault' or 'Document Storage' feature.", time: "~3 min" },
        { text: "If yes: this is your primary storage. Take a screenshot of where to find it so you remember.", time: "~1 min" },
        { text: "As a backup, create a Google Drive folder called 'HSA Receipts'. Inside it, create subfolders for each year: '2024', '2025', etc.", time: "~5 min" },
        { text: "For every receipt, your documentation should show: provider name, date of service, type of service, and amount paid. An itemized receipt or EOB covers this.", time: "~2 min" },
        { text: "Go through your phone's camera roll and email inbox for any past HSA-related receipts. Photograph or forward them to your storage folder now.", time: "~15 min" },
        { text: "Set a phone reminder for 'HSA receipt' that triggers once a week — it takes 30 seconds to file any receipts you've collected.", time: "~2 min" },
        { text: "Also save your HSA tax forms when they arrive: Form 1099-SA (withdrawals) and Form 5498-SA (contributions). These come in January/February.", time: "~2 min" },
        { text: "You don't need to submit receipts to the IRS — you just need to have them in case you're ever asked.", time: "~1 min" }
      ]
    }
  },

  // ──────────────────────────────────────────────────────────
  // TASK 10: Understand my HSA before open enrollment
  // ──────────────────────────────────────────────────────────
  open_enrollment_prep: {
    id: "open_enrollment_prep",
    label: "Understand my HSA options before open enrollment",
    match_keywords: ["open enrollment", "enrollment", "choosing a plan", "which plan", "compare plans", "hdhp vs ppo", "benefits selection", "pick my insurance"],
    gentle_note: "Open enrollment is one of those things that feels more overwhelming than it is. The goal here is just to get you enough information to make a confident choice — not a perfect one.",
    steps: {
      gentle: [
        {
          text: "Find out which plans your employer is offering this year.",
          time: "~5 min",
          sub_steps: [
            { text: "Log into your benefits portal or look for the open enrollment email from HR.", time: "~5 min" },
            { text: "List the plan options — you're looking for at least one labeled 'HDHP' or 'HSA-eligible'.", time: "~2 min" }
          ]
        },
        {
          text: "For each plan, find three numbers: monthly premium, deductible, and employer HSA contribution (if any).",
          time: "~10 min",
          sub_steps: [
            { text: "Monthly premium: what comes out of your paycheck.", time: "~0 min" },
            { text: "Deductible: what you pay out of pocket before insurance covers anything.", time: "~0 min" },
            { text: "Employer HSA contribution: free money your employer puts in your HSA — check the plan summary or HR materials.", time: "~0 min" }
          ]
        },
        {
          text: "Do a rough 'real cost' comparison.",
          time: "~5 min",
          sub_steps: [
            { text: "HDHP real cost = (monthly premium × 12) + expected medical spending − employer HSA contribution", time: "~3 min" },
            { text: "Traditional plan real cost = (monthly premium × 12) + expected copays + expected specialist visits", time: "~3 min" },
            { text: "The HDHP often wins if you're generally healthy and your employer contributes to the HSA.", time: "~1 min" }
          ]
        },
        {
          text: "Make your choice. You can revisit this next year.",
          time: "~5 min"
        }
      ],
      medium: [
        { text: "Find this year's plan options in your benefits portal or HR open enrollment email.", time: "~5 min" },
        { text: "For each plan, write down: monthly premium, annual deductible, out-of-pocket maximum, and whether it's HSA-eligible.", time: "~10 min" },
        { text: "Check if your employer contributes to the HSA and how much — this directly reduces the HDHP's effective cost.", time: "~5 min" },
        { text: "Estimate your likely medical spending for the year. If you're generally healthy, the HDHP often costs less total.", time: "~5 min" },
        { text: "Calculate rough totals: (annual premiums) + (expected out-of-pocket) − (employer HSA contribution) for each plan.", time: "~10 min" },
        { text: "Choose the plan. The HDHP + HSA is especially powerful if your employer contributes — that's free money you'd lose by picking a different plan.", time: "~5 min" }
      ],
      detailed: [
        { text: "Log into your benefits portal and download the plan comparison document for this year.", time: "~5 min" },
        { text: "For each plan option, record: plan type (HMO/PPO/HDHP), monthly premium, annual deductible, out-of-pocket maximum, and whether it's HSA-eligible.", time: "~10 min" },
        { text: "Check whether your employer contributes to the HSA, and how much. This is usually in the benefits guide or HR summary.", time: "~5 min" },
        { text: "Look up your medical usage last year: how many doctor visits, prescriptions, procedures, dental and vision costs.", time: "~5 min" },
        { text: "Estimate next year's expected medical costs as low/medium/high.", time: "~5 min" },
        { text: "For the HDHP option: calculate (annual premium) + (estimated medical spending, up to deductible) − (employer HSA contribution).", time: "~10 min" },
        { text: "For the traditional PPO option: calculate (annual premium) + (estimated copays and coinsurance).", time: "~10 min" },
        { text: "Compare totals. For most healthy young adults, the HDHP wins once the employer contribution is factored in.", time: "~5 min" },
        { text: "Confirm the HDHP uses the same doctor network as the PPO (usually yes — call your doctor's office to verify if unsure).", time: "~5 min" },
        { text: "Submit your plan selection in the benefits portal before the open enrollment deadline.", time: "~5 min" },
        { text: "If you chose the HDHP: immediately plan to open or activate your HSA.", time: "~1 min" }
      ]
    }
  }

};

// ============================================================
// MATCHING LOGIC — paste this alongside the task library
// ============================================================

/**
 * findTask(userInput)
 * Returns the best-matching task object, or null if no match.
 * Uses simple keyword scoring — no API needed.
 */
export function findTask(userInput) {
  const input = userInput.toLowerCase();
  let bestMatch = null;
  let bestScore = 0;

  for (const task of Object.values(TASK_LIBRARY)) {
    let score = 0;
    for (const keyword of task.match_keywords) {
      if (input.includes(keyword.toLowerCase())) {
        // Longer keyword matches score higher (more specific)
        score += keyword.split(" ").length;
      }
    }
    if (score > bestScore) {
      bestScore = score;
      bestMatch = task;
    }
  }

  // Return match only if at least one keyword matched
  return bestScore > 0 ? bestMatch : null;
}

/**
 * getSteps(task, level)
 * level: "gentle" | "medium" | "detailed"
 * Returns the step array for the given calm level.
 */
export function getSteps(task, level = "medium") {
  return task.steps[level] || task.steps.medium;
}

// ============================================================
// FALLBACK SYSTEM PROMPT for OpenAI (unmatched inputs only)
// Keep this under 200 tokens to minimize cost.
// ============================================================

export const FALLBACK_SYSTEM_PROMPT = `You are an HSA task assistant for young adults with financial anxiety.
When given a task related to health savings accounts (HSAs), break it into 3-6 calm, small, actionable steps.
Each step should take under 10 minutes to complete.
Use plain, friendly language — never clinical, urgent, or alarming.
Format: numbered list. Include a time estimate like "(~5 min)" after each step.
End with one gentle sentence reminding the user they can do just one step today.`;
