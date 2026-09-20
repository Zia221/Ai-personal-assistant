from agents import Agent

from tools.task_tools import (
    create_task,
    read_tasks,
)


def create_task_agent(model):

    return Agent(
        name="Task Agent",

        instructions="""
        You are the Task Management Specialist.

        You are responsible for managing the user's tasks.

        Use create_task when the user wants to create
        a new task.

        Use read_tasks when the user wants to see their tasks.

        Always use the tools instead of pretending that
        a task was created or retrieved.

        You are now directly responsible for handling
        the user's task-related conversation.

        Be clear and concise.
        """,

        model=model,

        tools=[
            create_task,
            read_tasks,
        ],
    )