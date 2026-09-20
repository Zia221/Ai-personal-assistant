from agents import Agent

from tools.calculator_tools import (
    add_numbers,
    subtract_numbers,
    multiply_numbers,
    divide_numbers,
)


def create_math_agent(model):

    return Agent(
        name="Math Agent",

        instructions="""
        You are the Math Specialist.

        You handle mathematical questions and calculations.

        Use the calculator tools whenever you need to
        perform calculations.

        Available operations:

        - addition
        - subtraction
        - multiplication
        - division

        Explain calculations clearly.

        You are now directly responsible for the user's
        mathematical request.
        """,

        model=model,

        tools=[
            add_numbers,
            subtract_numbers,
            multiply_numbers,
            divide_numbers,
        ],
    )