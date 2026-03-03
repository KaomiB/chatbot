"""
Trade-Off Tool / Scenario Explorer — personalized HSA guidance from 2–4 button questions.
All logic hardcoded in tradeoff_data.py; no API calls.
"""
import streamlit as st
from tradeoff_data import (
    ENTRY_CARDS,
    MORE_OPTIONS,
    SCENARIO_QUESTIONS,
    get_questions_for_display,
    get_result,
    should_show_question,
)

st.set_page_config(page_title="Trade-Off Tool", page_icon="⚖️")
st.title("Trade-Off Tool")
st.caption("Tell us what's going on — get a recommendation that fits your situation.")

# Session state for the flow
if "tradeoff_scenario_id" not in st.session_state:
    st.session_state.tradeoff_scenario_id = None
if "tradeoff_answers" not in st.session_state:
    st.session_state.tradeoff_answers = {}
if "tradeoff_q_index" not in st.session_state:
    st.session_state.tradeoff_q_index = 0

scenario_id = st.session_state.tradeoff_scenario_id
answers = st.session_state.tradeoff_answers
q_index = st.session_state.tradeoff_q_index

def start_over():
    st.session_state.tradeoff_scenario_id = None
    st.session_state.tradeoff_answers = {}
    st.session_state.tradeoff_q_index = 0
    st.rerun()

def go_to_result():
    st.session_state.tradeoff_q_index = 999  # signal: show result
    st.rerun()

# ─── Entry: no scenario selected ───────────────────────────────────────────
if scenario_id is None:
    st.subheader("Where are you right now?")
    for card in ENTRY_CARDS:
        with st.container():
            if st.button(f"{card['icon']} **{card['title']}**", key=f"entry_{card['id']}", use_container_width=True):
                st.session_state.tradeoff_scenario_id = card["scenario_id"]
                st.session_state.tradeoff_answers = {}
                st.session_state.tradeoff_q_index = 0
                st.rerun()

    with st.expander("More situations"):
        for opt in MORE_OPTIONS:
            if opt.get("link") == "task_breaker" and opt.get("task_id"):
                if st.button(opt["title"], key=f"more_{opt['id']}", use_container_width=True):
                    st.session_state.task_breaker_preload_task_id = opt["task_id"]
                    st.switch_page("pages/1_Task_Breaker.py")
            elif opt.get("id") == "D2":
                if st.button(opt["title"], key=f"more_{opt['id']}", use_container_width=True):
                    st.session_state.tradeoff_scenario_id = "D2"
                    st.session_state.tradeoff_answers = {}
                    st.session_state.tradeoff_q_index = 999
                    st.rerun()
            else:
                if st.button(opt["title"], key=f"more_{opt['id']}", use_container_width=True):
                    st.session_state.tradeoff_scenario_id = opt["id"]
                    st.session_state.tradeoff_answers = {}
                    st.session_state.tradeoff_q_index = 0
                    st.rerun()

    st.caption("**Next:** HSA topics · Task Breaker · AI Chat (sidebar).")
    st.stop()

# ─── Static result (no questions) ──────────────────────────────────────────
questions = SCENARIO_QUESTIONS.get(scenario_id, [])
if len(questions) == 0 and q_index == 0:
    # A1, C4, D1: show result immediately
    result = get_result(scenario_id, {})
    st.success(f"**{result['headline']}**")
    st.markdown(result["body"])
    col1, col2 = st.columns(2)
    with col1:
        if result.get("next_task_id"):
            if st.button(result.get("next_label", "Next step →"), key="res_next"):
                st.session_state.task_breaker_preload_task_id = result["next_task_id"]
                st.switch_page("pages/1_Task_Breaker.py")
        if result.get("next_goes_to"):
            if st.button(result.get("next_label", "Next step →"), key="res_next"):
                st.session_state.tradeoff_scenario_id = result["next_goes_to"]
                st.session_state.tradeoff_answers = {}
                st.session_state.tradeoff_q_index = 0
                st.rerun()
    with col2:
        if result.get("learn_more_topic_id"):
            if st.button("Learn more →", key="res_learn"):
                from content_script import get_topic_by_id
                t = get_topic_by_id(result["learn_more_topic_id"])
                if t:
                    st.session_state.pending_prompt = t.label
                st.switch_page("HSA_Topics.py")
    st.button("← Start over", on_click=start_over)
    st.stop()

# ─── D2: show 3 options (special result with buttons) ──────────────────────
if scenario_id == "D2" and q_index == 999:
    result = get_result("D2", {})
    st.info(f"**{result['headline']}**")
    st.markdown(result["body"])
    if st.button("I don't have an HSA yet and want to understand if it's for me", use_container_width=True, key="d2_a1"):
        st.session_state.tradeoff_scenario_id = "A1"
        st.session_state.tradeoff_answers = {}
        st.session_state.tradeoff_q_index = 0
        st.rerun()
    if st.button("I have an HSA but I'm not sure I'm using it right", use_container_width=True, key="d2_c2"):
        st.session_state.tradeoff_scenario_id = "C2"
        st.session_state.tradeoff_answers = {}
        st.session_state.tradeoff_q_index = 0
        st.rerun()
    if st.button("I need to do something specific but I'm not sure how to start", use_container_width=True, key="d2_tb"):
        st.switch_page("pages/1_Task_Breaker.py")
    st.button("← Start over", on_click=start_over)
    st.stop()

# ─── Question flow ─────────────────────────────────────────────────────────
questions_display = get_questions_for_display(scenario_id, answers)
at_result = q_index >= len(questions_display) or (scenario_id == "A2" and q_index == 1 and answers.get("0") in ("school", "parent"))

if at_result:
    result = get_result(scenario_id, answers)
    st.success(f"**{result['headline']}**")
    st.markdown(result["body"])
    c1, c2 = st.columns(2)
    with c1:
        if result.get("next_task_id"):
            if st.button("Next step →", key="res_next"):
                st.session_state.task_breaker_preload_task_id = result["next_task_id"]
                st.switch_page("pages/1_Task_Breaker.py")
    with c2:
        if result.get("learn_more_topic_id"):
            if st.button("Learn more →", key="res_learn"):
                from content_script import get_topic_by_id
                t = get_topic_by_id(result["learn_more_topic_id"])
                if t:
                    st.session_state.pending_prompt = t.label
                st.switch_page("HSA_Topics.py")
    st.button("← Start over", on_click=start_over)
    st.stop()

# Show current question
if not should_show_question(scenario_id, q_index, answers):
    go_to_result()
    st.stop()

q = questions_display[q_index]
st.caption(f"Question {q_index + 1} of {len(questions_display)}")
if st.button("← Back", key="back"):
    if q_index > 0:
        last_key = str(q_index - 1)
        if last_key in st.session_state.tradeoff_answers:
            del st.session_state.tradeoff_answers[last_key]
        st.session_state.tradeoff_q_index = q_index - 1
    else:
        start_over()
    st.rerun()

st.markdown(f"**{q['prompt']}**")
for opt in q["options"]:
    if st.button(opt["label"], key=f"q{q_index}_{opt['key']}", use_container_width=True):
        st.session_state.tradeoff_answers[str(q_index)] = opt["key"]
        # A2: after Q0 if school/parent, go to result; else next question
        if scenario_id == "A2" and q_index == 0 and opt["key"] in ("school", "parent"):
            st.session_state.tradeoff_q_index = 999
        else:
            st.session_state.tradeoff_q_index = q_index + 1
        st.rerun()

st.caption("**Next:** HSA topics · Task Breaker · AI Chat.")
