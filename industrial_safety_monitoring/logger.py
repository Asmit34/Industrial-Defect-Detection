import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

# Create logs directory (relative to project root)
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)


def get_logger(name: str) -> logging.Logger:
    """
    Creates and returns a configured logger
    """

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate logs
    if logger.hasHandlers():
        return logger

    # Formatter
    formatter = logging.Formatter(
        "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s"
    )

    # File Handler (with rotation)
    file_handler = RotatingFileHandler(
        LOG_FILE_PATH, maxBytes=5 * 1024 * 1024, backupCount=5
    )
    file_handler.setFormatter(formatter)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger