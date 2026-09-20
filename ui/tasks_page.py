from pathlib import Path

import streamlit as st

from ui.components import render_page_header


TASK_FILE = Path(
    "data/tasks.txt"
)


def render_tasks_page():

    render_page_header(
        "✅ Tasks",
        "Your personal task list.",
    )

    if not TASK_FILE.exists():

        st.info(
            "No tasks found."
        )

        return

    tasks = TASK_FILE.read_text(
        encoding="utf-8"
    ).splitlines()

    tasks = [
        task.strip()
        for task in tasks
        if task.strip()
    ]

    if not tasks:

        st.info(
            "No tasks found."
        )

        return

    for index, task in enumerate(
        tasks,
        start=1,
    ):

        st.markdown(
            f"""
            <div class="dashboard-card">
                <b>{index}.</b>
                {task}
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")