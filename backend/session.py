from agents import SQLiteSession


def create_session(session_id: str = "personal_assistant"):
    """
    Create a persistent SQLite conversation session.
    """

    return SQLiteSession(
        session_id,
        "data/conversations.db",
    )