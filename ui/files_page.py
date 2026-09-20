from pathlib import Path

import streamlit as st

from ui.components import render_page_header


def render_files_page():

    render_page_header(
        "📁 Files",
        "Files available inside your project.",
    )

    root = Path(".")

    files = []

    for path in root.rglob("*"):

        if not path.is_file():
            continue

        if any(
            part.startswith(".")
            for part in path.parts
        ):
            continue

        if "__pycache__" in path.parts:
            continue

        files.append(path)

    files = sorted(files)

    if not files:

        st.info(
            "No files found."
        )

        return

    for file in files:

        st.markdown(
            f"""
            <div class="dashboard-card">
                📄 {file}
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")