import streamlit as st
import textwrap

def render_brand():

    st.markdown(
        textwrap.dedent(
            """
            <div class="brand">
                <div class="brand-icon">🤖</div>

                <div>
                    <div class="brand-title">
                        AI Assistant
                    </div>

                    <div class="brand-subtitle">
                        Intelligent Workspace
                    </div>
                </div>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )


def render_status():

    st.markdown(
        """
        <div class="status">
            <span class="status-dot"></span>
            Online
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_page_header(title, subtitle):

    html = textwrap.dedent(
        f"""
        <div class="page-header">
            <div class="page-title">
                {title}
            </div>

            <div class="page-subtitle">
                {subtitle}
            </div>
        </div>
        """
    ).strip()

    st.markdown(
        html,
        unsafe_allow_html=True,
    )

def render_agent_badge(agent_name):

    st.markdown(
        f"""
        <div class="agent-badge">
            🤖 {agent_name}
        </div>
        """,
        unsafe_allow_html=True,
    )