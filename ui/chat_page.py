import asyncio
import textwrap
import streamlit as st

from backend.assistant import run_assistant

from ui.components import (
    render_page_header,
    render_agent_badge,
)


def render_chat_page():

    render_page_header(
        "AI Personal Assistant",
        "Your intelligent multi-agent workspace.",
    )

    # -----------------------------------------
    # Welcome screen
    # -----------------------------------------

    if not st.session_state.messages:

        st.markdown(
    textwrap.dedent(
        """
        <div class="welcome-card">

            <div class="welcome-icon">
                🤖
            </div>

            <div class="welcome-title">
                How can I help you?
            </div>

            <div class="welcome-text">
                Ask me to calculate, remember,
                manage tasks, research,
                code, inspect files, and more.
            </div>

        </div>
        """
    ),
    unsafe_allow_html=True,
)
    # -----------------------------------------
    # Chat history
    # -----------------------------------------

    for message in st.session_state.messages:

        role = message["role"]

        with st.chat_message(role):

            if role == "assistant":

                agent_name = message.get(
                    "agent",
                    "AI Assistant",
                )

                render_agent_badge(
                    agent_name
                )

            st.markdown(
                message["content"]
            )

    # -----------------------------------------
    # Input
    # -----------------------------------------

    user_input = st.chat_input(
        "Ask your assistant anything..."
    )

    if not user_input:
        return

    # -----------------------------------------
    # User message
    # -----------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input,
        }
    )

    with st.chat_message("user"):

        st.markdown(user_input)

    # -----------------------------------------
    # Assistant
    # -----------------------------------------

    with st.chat_message("assistant"):

        with st.spinner(
            "Thinking..."
        ):

            try:

                result = asyncio.run(
                    run_assistant(
                        user_input,
                        st.session_state.agent_session,
                    )
                )

                response = str(
                    result.final_output
                )

                agent_name = (
                    result.last_agent.name
                )

                render_agent_badge(
                    agent_name
                )

                st.markdown(response)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response,
                        "agent": agent_name,
                    }
                )

            except Exception as e:

                st.error(
                    "Something went wrong."
                )

                st.caption(
                    str(e)
                )