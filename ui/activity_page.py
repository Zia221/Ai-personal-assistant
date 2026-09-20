from pathlib import Path

import streamlit as st

from ui.components import render_page_header


LOG_FILE = Path(
    "logs/assistant.log"
)


def render_activity_page():

    render_page_header(
        "📊 Activity",
        "Monitor recent assistant activity.",
    )

    if not LOG_FILE.exists():

        st.info(
            "No activity has been recorded yet."
        )

        return

    logs = LOG_FILE.read_text(
        encoding="utf-8"
    )

    if not logs.strip():

        st.info(
            "No activity has been recorded yet."
        )

        return

    st.code(
        logs,
        language="text",
    )