from pathlib import Path

from agents import function_tool


MEMORY_FILE = Path("data/memory.txt")


@function_tool
def remember_fact(fact: str) -> str:
    """Save an important personal fact about the user."""

    MEMORY_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with MEMORY_FILE.open(
        "a",
        encoding="utf-8",
    ) as file:

        file.write(fact + "\n")

    return "I will remember that."


@function_tool
def recall_facts() -> str:
    """Read personal facts remembered about the user."""

    if not MEMORY_FILE.exists():
        return "I don't have any saved memories yet."

    memories = MEMORY_FILE.read_text(
        encoding="utf-8"
    )

    if not memories.strip():
        return "I don't have any saved memories yet."

    return memories