from datetime import datetime

from agents import function_tool


@function_tool
def get_current_datetime() -> str:
    """Get the current date and time."""

    now = datetime.now()

    return now.strftime(
        "%Y-%m-%d %H:%M:%S"
    )