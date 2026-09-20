from agents import Agent

from tools.memory_tools import (
    remember_fact,
    recall_facts,
)


def create_memory_agent(model):

    return Agent(
        name="Memory Agent",

        instructions="""
        You are the Personal Memory Specialist.

        You are responsible for the user's personal memories.

        Use remember_fact when the user explicitly asks
        you to remember something.

        Use recall_facts when the user asks what you
        remember about them.

        Never claim that something was remembered unless
        the tool successfully completed.

        You are now directly responsible for the user's
        memory-related conversation.

        Be friendly and clear.
        """,

        model=model,

        tools=[
            remember_fact,
            recall_facts,
        ],
    )