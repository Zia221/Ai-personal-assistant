import streamlit as st

from ui.components import render_page_header


def render_research_page():

    render_page_header(
        "🔬 Research",
        "Explore topics using your Research Agent.",
    )

    st.markdown(
        """
        <div class="welcome-card">

            <div class="welcome-icon">
                🔬
            </div>

            <div class="welcome-title">
                Research Workspace
            </div>

            <div class="welcome-text">
                Ask the Research Agent to investigate
                and explain complex topics.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.info(
        "Go to Chat and ask a research question."
    )