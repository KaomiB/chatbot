"""
Task Breakdown Assistant — break a task into steps.
HSA scenarios are hardcoded (task_library.py); custom tasks use OpenAI via LangChain.
"""
import warnings

# LangChain still uses Pydantic v1 internally; suppress warning on Python 3.14+
warnings.filterwarnings(
    "ignore",
    message=".*Pydantic V1.*isn't compatible with Python 3.14.*",
    category=UserWarning,
    module="langchain_core",
)

import streamlit as st
from langchain_openai import ChatOpenAI

from task_library import flatten_steps, get_task_by_id, get_task_labels


def generate_breakdown(task: str, complexity: str, api_key: str) -> str:
    depth = {"Simple": "3-5 steps", "Medium": "5-8 steps", "Complex": "8-12 steps"}
    prompt = f"""Break down this task into {depth[complexity]}:
Task: {task}

Format as a numbered list with clear, actionable steps.
Each step should be specific and achievable.
Add estimated time for each step in (XX mins) format.
"""
    model = ChatOpenAI(temperature=0.7, api_key=api_key)
    response = model.invoke(prompt)
    return response.content if hasattr(response, "content") else str(response)


st.set_page_config(page_title="Task Breaker", page_icon="🧙‍♂️")
st.title("🧙‍♂️ Task Breakdown Assistant")

# ─── Preload from Trade-Off Tool ──────────────────────────────────────────
preload_id = st.session_state.pop("task_breaker_preload_task_id", None)
if preload_id:
    for tid, lbl in get_task_labels():
        if tid == preload_id:
            st.session_state.scenario_select = lbl
            break

# ─── HSA scenarios (hardcoded, no API) ─────────────────────────────────────
st.subheader("Pick an HSA scenario")
scenario_labels = ["— Pick a scenario —"] + [lbl for _, lbl in get_task_labels()]
selected_label = st.selectbox(
    "Choose a task to get step-by-step guidance",
    options=scenario_labels,
    key="scenario_select",
)
selected_id = None if selected_label == "— Pick a scenario —" else next(
    (tid for tid, lbl in get_task_labels() if lbl == selected_label), None
)

if selected_id:
    task_obj = get_task_by_id(selected_id)
    if task_obj:
        level = st.radio(
            "How much detail?",
            options=["gentle", "medium", "detailed"],
            format_func=lambda x: {
                "gentle": "Standard — moderate detail",
                "medium": "Overview — fewer steps, grouped",
                "detailed": "Step-by-step — every action listed",
            }[x],
            horizontal=True,
            key="scenario_level",
        )
        steps_list = task_obj["steps"].get(level) or task_obj["steps"].get("medium") or []
        flat_steps = flatten_steps(steps_list)
        st.caption("Track your progress")
        for i, step_line in enumerate(flat_steps):
            st.checkbox(step_line, key=f"scenario_{selected_id}_{level}_{i}")

st.divider()
st.subheader("Or break down a custom task")
st.caption("Uses AI to turn any task into steps. Requires OpenAI API key in secrets.")

if "OPENAI_API_KEY" not in st.secrets:
    st.error(
        "**OpenAI API key not found.** Add it in `.streamlit/secrets.toml` for custom breakdowns.\n\n"
        "HSA scenarios above work without a key."
    )
else:
    # Create the main task input form (custom task + API)
    with st.form("task_form"):
        task = st.text_area(
            "What's the main task you want to break down?",
            placeholder="e.g. Plan my HSA contributions for the year",
        )

        complexity = st.select_slider(
            "Task Complexity",
            options=["Simple", "Medium", "Complex"],
            value="Medium",
        )

        submitted = st.form_submit_button("Break Down Task")

    if submitted and task.strip():
        with st.status("Breaking down your task..."):
            breakdown = generate_breakdown(task.strip(), complexity, st.secrets["OPENAI_API_KEY"])
            st.session_state["task_breakdown"] = breakdown
            st.write(breakdown)
    elif submitted:
        st.warning("Please enter a task to break down.", icon="⚠️")

    # Show last custom breakdown and checkboxes on every run so they don't disappear when you click a checkbox
    if st.session_state.get("task_breakdown"):
        st.divider()
        st.markdown(st.session_state["task_breakdown"])
        st.subheader("Track Your Progress")
        breakdown = st.session_state["task_breakdown"]
        steps = [s.strip() for s in breakdown.split("\n") if s.strip()]
        for i, step in enumerate(steps):
            st.checkbox(step, key=f"task_step_{i}")

st.caption("**Next:** Explore HSA topics → **HSA topics** · Ask in your own words → **AI Chat** (sidebar).")

# Sidebar: preferences + tips
with st.sidebar:
    if selected_id:
        task_obj_sb = get_task_by_id(selected_id)
        if task_obj_sb and task_obj_sb.get("gentle_note"):
            show_notes = st.checkbox(
                "Show supportive note for this scenario",
                key="task_breaker_show_notes",
            )
            if show_notes:
                st.info(task_obj_sb["gentle_note"])
            st.divider()
    st.markdown("""
    ### Tips for Better Breakdowns
    - Be specific about your end goal
    - Include context and constraints
    - Think about dependencies
    """)
