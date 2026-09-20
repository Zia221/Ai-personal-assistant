import os

from dotenv import load_dotenv

from agents import (
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
)


# -----------------------------------------
# Load local .env file
# -----------------------------------------

load_dotenv()


# -----------------------------------------
# Create Gemini model
# -----------------------------------------

def create_model():

    gemini_api_key = os.getenv("GEMINI_API_KEY")

    if not gemini_api_key:
        raise ValueError(
            "GEMINI_API_KEY is not set."
        )

    external_client = AsyncOpenAI(
        api_key=gemini_api_key,
        base_url=(
            "https://generativelanguage.googleapis.com/"
            "v1beta/openai/"
        ),
    )

    model = OpenAIChatCompletionsModel(
        model="gemini-2.5-flash",
        openai_client=external_client,
    )

    # Gemini through external provider
    # does not use OpenAI tracing here.
    set_tracing_disabled(True)

    return model