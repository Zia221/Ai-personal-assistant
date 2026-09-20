import asyncio

from backend.assistant import run_assistant
from backend.session import create_session


async def main():

    session = create_session(
        "backend_test"
    )

    result = await run_assistant(
        "Calculate 25 multiplied by 4.",
        session,
    )

    print("\nAssistant:")
    print(result.final_output)

    print(
        "\nHandled by:",
        result.last_agent.name,
    )


if __name__ == "__main__":
    asyncio.run(main())