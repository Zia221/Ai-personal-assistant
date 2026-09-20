import streamlit as st

from ui.components import render_page_header


def render_settings_page():

    render_page_header(
        "⚙️ Settings",
        "View your assistant configuration.",
    )

    st.markdown(
        '<div class="section-title">'
        'AI Configuration'
        '</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="metric-card">

                <div class="metric-label">
                    MODEL
                </div>

                <div class="metric-value">
                    Gemini 2.5 Flash
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:

        st.markdown(
            """
            <div class="metric-card">

                <div class="metric-label">
                    ARCHITECTURE
                </div>

                <div class="metric-value">
                    Multi-Agent
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="section-title">'
        'System Features'
        '</div>',
        unsafe_allow_html=True,
    )

    st.checkbox(
        "Guardrails",
        value=True,
        disabled=True,
    )

    st.checkbox(
        "Conversation Memory",
        value=True,
        disabled=True,
    )

    st.checkbox(
        "Agent Handoffs",
        value=True,
        disabled=True,
    )

    st.checkbox(
        "Tracing",
        value=True,
        disabled=True,
    )