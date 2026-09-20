import os

from agents import function_tool


@function_tool
def list_project_files() -> str:
    """List safe files in the project directory."""

    allowed_files = []

    for filename in os.listdir("."):

        if os.path.isfile(filename):

            allowed_files.append(filename)

    if not allowed_files:

        return "No files found."

    return "\n".join(
        sorted(allowed_files)
    )