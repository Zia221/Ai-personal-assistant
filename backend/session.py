import os

from agents import SQLiteSession


def create_session(session_id: str = "personal_assistant"):

    os.makedirs("data", exist_ok=True)

    return SQLiteSession(
        session_id,
        "data/conversations.db",
    )