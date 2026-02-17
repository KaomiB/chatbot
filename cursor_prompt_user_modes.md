# Cursor Prompt: User Mode / Tone Customization System

## What to build

Add a **user mode selector** to the app that customizes the emotional tone and
interface behavior across all pages (chatbot, FAQ/topics, task breaker, free
chat). The mode is chosen once on first visit (or in settings) and stored in
localStorage. It changes the SYSTEM PROMPT sent to OpenAI AND controls which
UI elements render.

This is based on real survey data from 19 young adult users. The three most
common preferences were:
  - 32% → "Matter-of-fact & neutral — just information, no emotional framing"
  - 26% → "Encouraging & supportive — celebrates small wins, offers reassurance"
  - 26% → "Let me switch between modes depending on my mood"

---

## Step 1: Mode picker UI

On first load (or via a visible "Change my mode" button in the nav/settings),
show a simple mode picker. Do NOT use a modal — render it inline as a card or
banner. Keep it brief and non-clinical.

Display these three options as clickable cards (not a dropdown):

### Card 1 — "Just the facts"
  Icon: 📋  
  Headline: "Just the facts"  
  Subtext: "Give me clear information. Skip the emotional framing."  
  mode_value: "neutral"

### Card 2 — "A little support"
  Icon: 🌱  
  Headline: "A little support"  
  Subtext: "I'd like encouragement alongside the information."  
  mode_value: "supportive"

### Card 3 — "I'll decide as I go"
  Icon: 🔄  
  Headline: "I'll decide as I go"  
  Subtext: "Show me a toggle I can flip anytime."  
  mode_value: "flexible"

Store the selected value in localStorage as `hsa_user_mode`.

For `flexible` mode, render a small persistent toggle in the top-right corner
of every page:
  "📋 Neutral ↔ 🌱 Supportive"
The toggle updates `hsa_user_mode` to either `neutral` or `supportive`
in real time. Default to `supportive` until toggled.

---

## Step 2: OpenAI system prompt — swap based on mode

In the free chat page (and anywhere else you call the OpenAI API), read
`hsa_user_mode` from localStorage and select the system prompt accordingly.

### NEUTRAL mode system prompt
```
You are a knowledgeable HSA assistant for young adults.
Your job: answer questions about Health Savings Accounts accurately and concisely.
Rules:
- Be direct and factual. No emotional framing, no pep talks, no affirmations.
- Keep answers to 3-5 sentences unless the user asks for more detail.
- If the user asks a procedural question, give numbered steps.
- End each answer with one concrete next action or follow-up question offer.
- Do not comment on how the user is feeling unless they bring it up first.
- Never use the words "should", "need to", or "must" in a pressuring way.
```

### SUPPORTIVE mode system prompt
```
You are a calm, knowledgeable HSA guide for young adults who often feel anxious
about finances. Your job is two things equally: give accurate HSA information,
AND help the person feel less stressed about it.
Rules:
- If someone expresses confusion or stress, briefly acknowledge it before
  answering: "That's genuinely confusing — here's the clearer version."
- Keep answers to 3-5 sentences unless asked for more. Lead with the answer,
  not the acknowledgment.
- If someone seems overwhelmed (asks multiple questions at once, says "I don't
  understand any of this"), respond to only ONE thing first and say:
  "Let's just focus on this piece first — we can cover the rest after."
- End every answer with ONE of: a reassurance they don't have to decide today,
  a small next step, or an invitation to ask a follow-up.
- Never make the person feel behind, wrong, or like they've made a mistake.
- Do NOT use hollow affirmations like "Great question!" or "You're doing amazing!"
  Instead, validate the substance: "That's a common point of confusion — here's why."
- Never use the words "should", "need to", or "must" in a pressuring way.
- If the user expresses negative self-talk ("I'm so bad at this"), do not
  affirm it and do not over-reassure. Redirect factually:
  "This system is genuinely confusing — let's just look at the actual rule."
```

### How to implement the swap (Python example)
```python
def get_system_prompt(mode: str) -> str:
    if mode == "neutral":
        return NEUTRAL_SYSTEM_PROMPT
    else:  # supportive or flexible defaults to supportive
        return SUPPORTIVE_SYSTEM_PROMPT
```

If you're reading mode from a cookie or session on the backend, pass it as a
query param or in the request body from the frontend. If you're doing it
purely frontend, just swap the string before sending to the API.

---

## Step 3: Keyword-triggered empathy injection (supportive mode only)

In supportive mode only, before sending user message to OpenAI, check for
emotional keywords. If matched, append a short instruction to the system prompt
dynamically. This costs ~10-15 extra tokens per triggered message.

```python
EMPATHY_INJECTIONS = {
    # key: trigger phrase → value: instruction to append to system prompt
    "stressed":         "The user expressed stress. Acknowledge it warmly in one sentence before your answer.",
    "overwhelmed":      "The user feels overwhelmed. Answer only the most essential thing. Then say it's okay to stop here.",
    "confused":         "The user is confused. Briefly normalize the confusion, then give the clearest version.",
    "scared":           "The user is anxious. Reassure them this is manageable before answering.",
    "don't understand": "The user feels lost. Simplify your answer to 2-3 sentences and offer to go simpler.",
    "too late":         "The user feels behind. Counter this gently — there is no 'too late' with HSAs.",
    "terrible with":    "The user is being self-critical. Redirect factually: this system is confusing, not them.",
    "can't afford":     "The user has a money constraint. Acknowledge the real constraint before offering options.",
    "stupid":           "The user used self-deprecating language. Briefly counter it and move to the answer.",
    "don't know where": "The user doesn't know where to start. Suggest ONE specific first step only.",
}

def inject_empathy(system_prompt: str, user_message: str, mode: str) -> str:
    if mode == "neutral":
        return system_prompt  # Never inject in neutral mode
    msg_lower = user_message.lower()
    injections = []
    for trigger, instruction in EMPATHY_INJECTIONS.items():
        if trigger in msg_lower:
            injections.append(instruction)
    if injections:
        system_prompt += "\n\nADDITIONAL INSTRUCTION FOR THIS MESSAGE:\n" + " ".join(injections)
    return system_prompt
```

---

## Step 4: UI component rendering — what changes per mode

Read `hsa_user_mode` wherever these components render and conditionally
show/hide them.

### Components that render in SUPPORTIVE mode only
- The gentle_note above task breaker checklists
  (e.g. "You don't have to do all of this today.")
- The "How are you feeling about HSAs?" entry check-in on the chatbot home
- "You're not behind" reframe text at the bottom of open_hsa and young_adults
  topic nodes
- The "It's okay to close this tab" note at the bottom of the FAQ page
- Empathy-prefixed sentences on hard topics (contribution limits, penalties,
  eligibility, HDHP comparison, investment)
  Example: "This sounds scarier than it is. The 20% penalty only applies in
  one specific situation — let's look at it clearly."
- "By the way — there's no right age to start this" line on late-start topics

### Components that render in BOTH modes
- Topic difficulty tags (🟢 Good starting point / 🟡 More detail / 🔵 When ready)
  — these reduce overwhelm through clarity, not emotional framing
- "One of the most asked questions" social norm badges on top topics
- Concrete next step at the end of every chatbot answer
- Sub-task breakdown button on task breaker steps
- The calm level slider (🌿 Gentle / 🌿🌿 Medium / 🌿🌿🌿 Detailed) on task breaker
  — in neutral mode, rename labels to "Fewer steps / Standard / Full detail"
    so they feel practical rather than emotional

### Components that NEVER render (neither mode)
- Hollow affirmations ("Great question!", "You're doing amazing!")
- Progress comparisons to peers ("Users like you saved X more")
- Urgency language ("Don't miss out", "Act before open enrollment closes")
- Loss framing as the primary message
  (survey data: only 2/19 preferred loss framing; 8/19 preferred gain framing)

---

## Step 5: Message framing — use survey-informed copy

When writing static copy for topic pages and chatbot answers, default to
**gain framing** (8/19 preferred) over loss framing (2/19 preferred).

Survey-validated message framing examples:

  PREFERRED (gain): "An HSA saves you around $1,800/year in taxes —
  that's real money back in your pocket."

  ALSO EFFECTIVE (reflective): "If you faced a $5,000 medical bill next year,
  how would you want past-you to have prepared?"

  AVOID (loss): "Without an HSA, you'll pay $1,800 more in taxes."

  FOR ANXIOUS USERS (permission-based): "Even $25/month is a meaningful start.
  You don't have to max it out."

When the chatbot detects a user is in the "overwhelmed" or "anxious" cluster
(keywords above), default to permission-based framing in that response only.
Otherwise default to gain framing.

---

## Step 6: Progress tracking — handle mixed reactions

Survey data: 9/19 motivated by progress tracking, 7/19 mixed (motivating when
ahead, discouraging when behind), 2/19 anxious if falling behind.

Implementation:
- Show progress indicators (e.g. "You've explored 4 of 23 topics") in BOTH modes
- In SUPPORTIVE mode: if user hasn't visited in a while, do NOT show a
  "you've been away" message or a "you're falling behind" nudge.
  Instead show: "Welcome back — pick up wherever you left like."
- In NEUTRAL mode: show progress counts plainly with no framing at all.
- Never show a red state, warning color, or negative indicator for
  "incomplete" progress. Use neutral grey for untouched items.

---

## Step 7: Survey-informed anxiety trigger avoidance

These UI patterns triggered anxiety in survey respondents. Avoid them
regardless of mode:

  ❌ Peer comparison framing: "Other users your age have saved X"
  ❌ Milestone shame: "You're behind where most 25-year-olds are"
  ❌ "Should/need/must" pressure language in any context
  ❌ Suggesting current choices are wrong: "You may have made a mistake by..."
  ❌ Ignoring real financial constraints (never assume user can afford to max out)

These are safe in both modes:
  ✅ Social norm normalization: "This is one of the most asked questions"
  ✅ Gain framing: "Here's what this unlocks for you"
  ✅ Permission-based: "You can start with any amount, any time"
  ✅ Externalizing difficulty: "This rule is genuinely confusing — here's the clear version"
  ✅ Reflective: "What would feel like a good outcome for you here?"

---

## Summary: What gets built

1. Mode picker card UI on first load (3 options: neutral / supportive / flexible)
2. localStorage persistence + real-time toggle for flexible mode
3. Two system prompts swapped based on mode at API call time
4. Python empathy injection function (supportive mode only, keyword-triggered)
5. Conditional rendering of ~8 emotional UI components based on mode
6. Calm level slider label swap (neutral mode = practical labels)
7. Progress tracking with no negative states in either mode
8. Copy review pass: replace all loss framing with gain framing as default
