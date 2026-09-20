import asyncio
import os

from pydantic import BaseModel

from agents import (
    Agent,
    Runner,
    SQLiteSession,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
    GuardrailFunctionOutput,
    RunContextWrapper,
)

from agents.decorators import input_guardrail, output_guardrail

from my_agents.time_agent import create_time_agent
from my_agents.file_agent import create_file_agent
from my_agents.math_agent import create_math_agent
from my_agents.task_agent import create_task_agent
from my_agents.memory_agent import create_memory_agent
from my_agents.general_agent import create_general_agent
from my_agents.coding_agent import create_coding_agent
from my_agents.research_agent import create_research_agent
from tracing.logger import log_info, log_error

# ============================================================
# GEMINI CONFIGURATION
# ============================================================

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError(
        "GEMINI_API_KEY is not set."
    )


external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


model = OpenAIChatCompletionsModel(
    model="gemini-3.1-pro-preview",
    openai_client=external_client,
)


set_tracing_disabled(True)


# ============================================================
# CREATE SPECIALIST AGENTS
# ============================================================

math_agent = create_math_agent(model)
time_agent = create_time_agent(model)

file_agent = create_file_agent(model)
task_agent = create_task_agent(model)

memory_agent = create_memory_agent(model)

general_agent = create_general_agent(model)

coding_agent = create_coding_agent(model)

research_agent = create_research_agent(
    model,
    coding_agent,
)


# ============================================================
# SAFETY SCHEMA
# ============================================================

class SafetyCheck(BaseModel):

    unsafe: bool

    reason: str


# ============================================================
# INPUT SAFETY AGENT
# ============================================================

input_checker = Agent(

    name="Input Safety Checker",

    instructions="""
    Analyze the user's request.

    Set unsafe=true only when the request is clearly
    dangerous, malicious, or inappropriate.

    Normal requests should be unsafe=false.

    Always provide a short reason.
    """,

    model=model,

    output_type=SafetyCheck,
)


# ============================================================
# INPUT GUARDRAIL
# ============================================================

@input_guardrail(
    name="Input Safety Guardrail",
    run_in_parallel=False,
)
async def safety_input_guardrail(
    ctx: RunContextWrapper,
    agent: Agent,
    input,
) -> GuardrailFunctionOutput:

    result = await Runner.run(
        input_checker,
        input,
        context=ctx.context,
    )
    log_info(
    f"Agent run completed: {result.final_output}"
)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.unsafe,
    )


# ============================================================
# OUTPUT SAFETY AGENT
# ============================================================

output_checker = Agent(

    name="Output Safety Checker",

    instructions="""
    Analyze the assistant's final response.

    Set unsafe=true if the response contains clearly
    dangerous or inappropriate content.

    Otherwise set unsafe=false.

    Always provide a short reason.
    """,

    model=model,

    output_type=SafetyCheck,
)


# ============================================================
# OUTPUT GUARDRAIL
# ============================================================

@output_guardrail
async def safety_output_guardrail(
    ctx: RunContextWrapper,
    agent: Agent,
    output,
) -> GuardrailFunctionOutput:

    result = await Runner.run(
        output_checker,
        str(output),
        context=ctx.context,
    )

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.unsafe,
    )


# ============================================================
# MAIN ROUTER AGENT
# ============================================================

assistant = Agent(

    name="Main Personal Assistant",

    instructions="""
    You are the main routing assistant.

    Route the user to the appropriate specialist.

    MATH:
    calculations and mathematical questions.

    TASK:
    creating and reading tasks.

    MEMORY:
    remembering and recalling personal information.

    GENERAL:
    general knowledge.

    CODING:
    programming, Python, debugging, APIs,
    and software development.

    RESEARCH:
    research and topic investigation.

    TIME:
    current date and time.

    FILE:
    inspecting project files.

    Use handoffs whenever a specialist clearly
    owns the request.
    """,

    model=model,

    handoffs=[
        math_agent,
        task_agent,
        memory_agent,
        general_agent,
        coding_agent,
        research_agent,
        time_agent,
        file_agent,
    ],

    input_guardrails=[
        safety_input_guardrail
    ],

    output_guardrails=[
        safety_output_guardrail
    ],
)


# ============================================================
# SESSION MEMORY
# ============================================================

session = SQLiteSession(
    "personal_assistant_phase7"
)


# ============================================================
# MAIN LOOP
# ============================================================

async def main():

    print("=" * 60)
    print("          AI PERSONAL ASSISTANT")
    print("=" * 60)

    print("\nPhase 7: Advanced Agent Orchestration")
    print("Handoffs Enabled")
    print("Agents as Tools Enabled")
    print("Guardrails Enabled")
    print("SQLite Memory Enabled")

    print("\nType 'exit' to stop.\n")


    while True:

        user_input = input("You: ")
        log_info(f"User input: {user_input}")

        if user_input.lower() == "exit":

            print("Assistant: Goodbye!")

            break


        try:
            log_info("Agent run started")
            result = await Runner.run(
            
                assistant,
                user_input,
                session=session,
            )


            print(
                "\nAssistant:",
                result.final_output
            )

            print()


        except Exception as e:

         log_error(
        f"Agent run failed: {str(e)}"
    )

    print(
        "\nAssistant: "
        "I couldn't process that request."
    )

    print(
        "Reason:",
        str(e)
    )

    print()


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    asyncio.run(main())