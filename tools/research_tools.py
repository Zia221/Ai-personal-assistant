from agents import function_tool


@function_tool
def research_topic(topic: str) -> str:
    """Provide basic research guidance for a topic."""

    return f"""
Research topic: {topic}

Research checklist:

1. Define the topic.
2. Identify the main concepts.
3. Find reliable sources.
4. Compare different explanations.
5. Summarize the important findings.
6. Clearly separate facts from opinions.
"""