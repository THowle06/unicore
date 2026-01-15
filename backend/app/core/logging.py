import logging
from logging.config import dictConfig

from app.core.config import get_settings

def setup_logging() -> None:
    """
    Configure application-wide logging.
    """
    settings = get_settings()

    log_level = "DEBUG" if settings.env == "development" else "INFO"

    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": (
                        "%(asctime)s | %(levelname)s | "
                        "%(name)s | %(message)s"
                    ),
                },
            },
            "root": {
                "handlers": ["default"],
                "level": log_level,
            },
        }
    )

def get_logger(name: str) -> logging.Logger:
    """
    Retrieve a module-specific logger.
    """
    return logging.getLogger(name)