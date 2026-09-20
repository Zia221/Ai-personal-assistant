import os
import uuid

import streamlit as st


# -----------------------------------------
# Load secrets from Streamlit Cloud
# -----------------------------------------

try:
    if "GEMINI_API_KEY" in st.secrets:
        os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]
except FileNotFoundError:
    pass


# -----------------------------------------
# Backend and UI imports
# -----------------------------------------

from backend.session import create_session
from ui.styles import load_css
from ui.sidebar import render_sidebar
from ui.chat_page import render_chat_page
from ui.memory_page import render_memory_page
from ui.tasks_page import render_tasks_page
from ui.research_page import render_research_page
from ui.files_page import render_files_page
from ui.activity_page import render_activity_page
from ui.settings_page import render_settings_page


# -----------------------------------------
# Page configuration
# -----------------------------------------

st.set_page_config(
    page_title="AI Personal Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


# -----------------------------------------
# Load custom CSS
# -----------------------------------------

load_css()


# -----------------------------------------
# Initialize session state
# -----------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


if "page" not in st.session_state:
    st.session_state.page = "Chat"


# Create a unique conversation for each browser session
if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = (
        f"streamlit-{uuid.uuid4().hex}"
    )


if "agent_session" not in st.session_state:
    st.session_state.agent_session = create_session(
        st.session_state.conversation_id
    )


# -----------------------------------------
# Sidebar
# -----------------------------------------

render_sidebar()


# -----------------------------------------
# Page routing
# -----------------------------------------

if st.session_state.page == "Chat":

    render_chat_page()


elif st.session_state.page == "Memory":

    render_memory_page()


elif st.session_state.page == "Tasks":

    render_tasks_page()


elif st.session_state.page == "Research":

    render_research_page()


elif st.session_state.page == "Files":

    render_files_page()


elif st.session_state.page == "Activity":

    render_activity_page()


elif st.session_state.page == "Settings":

    render_settings_page()