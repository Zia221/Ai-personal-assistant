from agents import Agent

from tools.time_tools import get_current_datetime


def create_time_agent(model):

    return Agent(
        name="Time Agent",

        instructions="""
        You are the Time Specialist.

        Your job is to provide the current date and time.

        Always use get_current_datetime when the user
        asks for the current date or time.

        Never guess the current time.

        Give the result clearly.
        """,

        model=model,

        tools=[
            get_current_datetime
        ],
    )