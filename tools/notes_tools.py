from pathlib import Path

from agents import function_tool


NOTES_FILE = Path("data/notes.txt")


@function_tool
def save_note(note: str) -> str:
    """Save a note for the user."""

    NOTES_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with NOTES_FILE.open(
        "a",
        encoding="utf-8",
    ) as file:

        file.write(note + "\n")

    return "Note saved successfully."


@function_tool
def read_notes() -> str:
    """Read all saved notes."""

    if not NOTES_FILE.exists():
        return "There are no saved notes."

    notes = NOTES_FILE.read_text(
        encoding="utf-8"
    )

    if not notes.strip():
        return "There are no saved notes."

    return notes