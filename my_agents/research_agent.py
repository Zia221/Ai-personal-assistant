from agents import Agent

from tools.research_tools import research_topic


def create_research_agent(model, coding_agent):

    coding_agent_tool = coding_agent.as_tool(
        tool_name="coding_specialist",
        tool_description="""
        Use this specialist when research requires
        programming or technical implementation help.
        """,
    )

    return Agent(
        name="Research Agent",

        instructions="""
        You are a Research Specialist.

        Your job is to help the user understand topics
        by organizing information carefully.

        You can:

        - research a topic
        - break complex topics into smaller concepts
        - summarize findings
        - explain technical subjects
        - ask the coding specialist for programming help
          when necessary

        Use research_topic when appropriate.

        If a research question requires programming
        expertise, use the coding_specialist tool.

        Clearly distinguish facts, explanations,
        and suggestions.

        Keep answers structured and easy to understand.
        """,

        model=model,

        tools=[
            research_topic,
            coding_agent_tool,
        ],
    )