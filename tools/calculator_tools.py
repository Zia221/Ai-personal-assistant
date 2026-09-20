from agents import function_tool


@function_tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@function_tool
def subtract_numbers(a: int, b: int) -> int:
    """Subtract the second number from the first number."""
    return a - b


@function_tool
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


@function_tool
def divide_numbers(a: float, b: float) -> float:
    """Divide the first number by the second number."""

    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b