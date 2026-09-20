from agents import Agent

from tools.file_tools import list_project_files


def create_file_agent(model):

    return Agent(
        name="File Agent",

        instructions="""
        You are a File Management Specialist.

        You can help the user inspect files in the
        current project.

        Use list_project_files when the user asks
        what files are available.

        Do not claim that you created, deleted, or modified
        files because you do not have tools for those actions.

        Be clear about what you can and cannot do.
        """,

        model=model,

        tools=[
            list_project_files
        ],
    )