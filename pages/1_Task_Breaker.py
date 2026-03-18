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

from task_library import (
    TASK_SECTIONS,
    flatten_steps,
    get_task_by_id,
    get_task_labels,
    get_section_for_task_id,
)


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

# Sidebar supportive note: sticky-note look (yellow) + readable text
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] [data-testid="stAlert"] {
        color: #1A2028 !important;
        background-color: #FDFBD4 !important;
        border-radius: 0.5rem;
        border-left: 4px solid #E4B4C2;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    }
    [data-testid="stSidebar"] [data-testid="stAlert"] p {
        color: #1A2028 !important;
    }
    @media (prefers-color-scheme: dark) {
        [data-testid="stSidebar"] [data-testid="stAlert"] {
            color: #f0e6d2 !important;
            background-color: #3d3420 !important;
            border-left: 4px solid #c4a574;
            box-shadow: 0 1px 3px rgba(0,0,0,0.2);
        }
        [data-testid="stSidebar"] [data-testid="stAlert"] p {
            color: #f0e6d2 !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Task Breakdown Assistant")

# ─── Preload from Trade-Off Tool ──────────────────────────────────────────
preload_id = st.session_state.pop("task_breaker_preload_task_id", None)
if preload_id:
    preload_section = get_section_for_task_id(preload_id)
    if preload_section:
        st.session_state.task_breaker_section = preload_section
    for tid, lbl in get_task_labels():
        if tid == preload_id:
            st.session_state.scenario_select = lbl
            break

# ─── HSA scenarios (hardcoded, no API) ─────────────────────────────────────
st.subheader("Pick an HSA scenario")

section_options = ["— Pick a section —"] + list(TASK_SECTIONS)
selected_section = st.selectbox(
    "Section",
    options=section_options,
    key="task_breaker_section",
)
selected_section = None if selected_section == "— Pick a section —" else selected_section

if selected_section:
    scenario_labels = ["— Pick a scenario —"] + [lbl for _, lbl in get_task_labels(selected_section)]
    # Reset scenario if it belonged to a different section (e.g. user changed section)
    if st.session_state.get("scenario_select") and st.session_state["scenario_select"] not in scenario_labels:
        st.session_state["scenario_select"] = "— Pick a scenario —"
    selected_label = st.selectbox(
        "Scenario",
        options=scenario_labels,
        key="scenario_select",
    )
    selected_id = None if selected_label == "— Pick a scenario —" else next(
        (tid for tid, lbl in get_task_labels(selected_section) if lbl == selected_label), None
    )
else:
    selected_label = "— Pick a scenario —"
    selected_id = None

if selected_id:
    task_obj = get_task_by_id(selected_id)
    if task_obj:
        level = st.radio(
            "How much detail?",
            options=["gentle", "medium", "detailed"],
            format_func=lambda x: {
                "gentle": "Guided Walk Through (Standard)",
                "medium": "Quick Summary",
                "detailed": "Detailed Checklist",
            }[x],
            horizontal=True,
            key="scenario_level",
        )
        st.caption("Track your progress")
        use_detailed = level == "detailed" and task_obj.get("sections_detailed")
        sections_list = (task_obj["sections_detailed"] if use_detailed else task_obj.get("sections")) or task_obj.get("sections")
        if sections_list:
            show_items = level != "medium"  # Quick Summary = main steps only
            for sec_idx, sec in enumerate(sections_list):
                header = sec["title"]
                if sec.get("time"):
                    header += f" (Estimated time: {sec['time']})"
                if show_items:
                    weight = "bold"
                    st.markdown(
                        f'<p style="font-size: 1.15em; font-weight: {weight}; margin-bottom: 0.25em;">{header}</p>',
                        unsafe_allow_html=True,
                    )
                else:
                    st.checkbox(header, key=f"scenario_{selected_id}_summary_{sec_idx}")
                if show_items:
                    for i, item in enumerate(sec["items"]):
                        if isinstance(item, dict) and "text" in item and "sub" in item:
                            st.checkbox(item["text"], key=f"scenario_{selected_id}_sec_{sec_idx}_{i}")
                            sub_items_html = "".join(f"<li>{s}</li>" for s in item["sub"])
                            st.markdown(
                                f'<div style="margin-left: 0; margin-top: -1.15em; margin-bottom: 0.6em;"><ul style="margin: 0; padding-left: 1.5em; line-height: 1.4;">{sub_items_html}</ul></div>',
                                unsafe_allow_html=True,
                            )
                        else:
                            text = item if isinstance(item, str) else item.get("text", "")
                            st.checkbox(text.replace("\n", " "), key=f"scenario_{selected_id}_sec_{sec_idx}_{i}")
                if sec_idx < len(sections_list) - 1:
                    st.markdown('<div style="margin-bottom: 1.25em;"></div>', unsafe_allow_html=True)
        else:
            steps_list = task_obj["steps"].get(level) or task_obj["steps"].get("medium") or []
            flat_steps = flatten_steps(steps_list)
            for i, step_line in enumerate(flat_steps):
                st.checkbox(step_line, key=f"scenario_{selected_id}_{level}_{i}")

st.divider()
st.subheader("Break Down a Custom Task")
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

st.caption("**Next:** Explore HSA topics → **HSA topics** (ask in your own words there).")

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
