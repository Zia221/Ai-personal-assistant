from pathlib import Path

import streamlit as st

from ui.components import render_page_header


MEMORY_FILE = Path(
    "data/memory.txt"
)


def render_memory_page():

    render_page_header(
        "🧠 Memory",
        "Personal information your assistant remembers.",
    )

    st.markdown(
        '<div class="section-title">'
        'Saved Memories'
        '</div>',
        unsafe_allow_html=True,
    )

    if not MEMORY_FILE.exists():

        st.info(
            "No memories have been saved yet."
        )

        return

    memories = MEMORY_FILE.read_text(
        encoding="utf-8"
    ).splitlines()

    memories = [
        memory.strip()
        for memory in memories
        if memory.strip()
    ]

    if not memories:

        st.info(
            "No memories have been saved yet."
        )

        return

    for memory in memories:

        st.markdown(
            f"""
            <div class="dashboard-card">
                🧠 {memory}
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")