from pydantic import BaseModel

from agents import (
    Agent,
    Runner,
    GuardrailFunctionOutput,
    RunContextWrapper,
)

from agents.decorators import (
    input_guardrail,
    output_guardrail,
)

from backend.config import create_model

from my_agents.math_agent import create_math_agent
from my_agents.task_agent import create_task_agent
from my_agents.memory_agent import create_memory_agent
from my_agents.general_agent import create_general_agent
from my_agents.coding_agent import create_coding_agent
from my_agents.research_agent import create_research_agent
from my_agents.time_agent import create_time_agent
from my_agents.file_agent import create_file_agent


# ============================================================
# MODEL
# ============================================================

model = create_model()


# ============================================================
# SPECIALIST AGENTS
# ============================================================

math_agent = create_math_agent(model)

task_agent = create_task_agent(model)

memory_agent = create_memory_agent(model)

general_agent = create_general_agent(model)

coding_agent = create_coding_agent(model)

research_agent = create_research_agent(
    model,
    coding_agent,
)

time_agent = create_time_agent(model)

file_agent = create_file_agent(model)


# ============================================================
# SAFETY SCHEMA
# ============================================================

class SafetyCheck(BaseModel):

    unsafe: bool

    reason: str


# ============================================================
# INPUT SAFETY CHECKER
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

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.unsafe,
    )


# ============================================================
# OUTPUT SAFETY CHECKER
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
# MAIN ASSISTANT
# ============================================================

assistant = Agent(

    name="Main Personal Assistant",

    instructions="""
    You are the main AI Personal Assistant.

    Your job is to understand the user's request and
    hand the conversation to the correct specialist.

    MATH:
    calculations and mathematical questions.

    TASK:
    creating and reading tasks.

    MEMORY:
    remembering and recalling personal information.

    GENERAL:
    general knowledge and normal questions.

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

    Let the specialist handle the conversation
    after the handoff.

    Be friendly, clear, and concise.
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
        safety_input_guardrail,
    ],

    output_guardrails=[
        safety_output_guardrail,
    ],
)


# ============================================================
# RUN ASSISTANT
# ============================================================

async def run_assistant(
    user_input: str,
    session,
):

    result = await Runner.run(
        assistant,
        user_input,
        session=session,
    )

    return result