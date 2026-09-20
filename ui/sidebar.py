import streamlit as st

from ui.components import (
    render_brand,
    render_status,
)


def render_sidebar():

    with st.sidebar:

        render_brand()

        render_status()

        st.divider()

        st.caption("WORKSPACE")

        if st.button(
            "💬  Chat",
            use_container_width=True,
        ):
            st.session_state.page = "Chat"

        if st.button(
            "🧠  Memory",
            use_container_width=True,
        ):
            st.session_state.page = "Memory"

        if st.button(
            "✅  Tasks",
            use_container_width=True,
        ):
            st.session_state.page = "Tasks"

        if st.button(
            "🔬  Research",
            use_container_width=True,
        ):
            st.session_state.page = "Research"

        if st.button(
            "📁  Files",
            use_container_width=True,
        ):
            st.session_state.page = "Files"

        if st.button(
            "📊  Activity",
            use_container_width=True,
        ):
            st.session_state.page = "Activity"

        if st.button(
            "⚙️  Settings",
            use_container_width=True,
        ):
            st.session_state.page = "Settings"

        st.divider()

        st.caption("SYSTEM")

        st.write("🟢 Gemini Connected")
        st.write("🛡️ Guardrails")
        st.write("🔗 Multi-Agent")
        st.write("🧠 Memory")

        st.divider()

        st.caption(
            "AI Personal Assistant"
        )

        st.caption(
            "Powered by Gemini + Agents SDK"
        )