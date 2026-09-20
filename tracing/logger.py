import logging
import os


# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)


logging.basicConfig(
    filename="logs/assistant.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


def log_info(message: str):
    """Write an informational message to the trace log."""
    logging.info(message)


def log_error(message: str):
    """Write an error message to the trace log."""
    logging.error(message)