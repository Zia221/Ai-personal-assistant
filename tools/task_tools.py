from pathlib import Path

from agents import function_tool


TASK_FILE = Path("data/tasks.txt")


@function_tool
def create_task(task: str) -> str:
    """Add a new task to the user's task list."""

    TASK_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with TASK_FILE.open(
        "a",
        encoding="utf-8",
    ) as file:

        file.write(task + "\n")

    return f"Task added successfully: {task}"


@function_tool
def read_tasks() -> str:
    """Read all tasks from the user's task list."""

    if not TASK_FILE.exists():
        return "There are no tasks."

    tasks = TASK_FILE.read_text(
        encoding="utf-8"
    )

    if not tasks.strip():
        return "There are no tasks."

    return tasks