import logging
from colorlog import ColoredFormatter


def init_logging() -> None:
    handler = logging.StreamHandler()
    handler.setFormatter(
        ColoredFormatter(
            fmt="%(log_color)s%(asctime)s %(levelname)s [%(module)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            log_colors={
                "DEBUG": "cyan",
                "INFO": "white",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "bold_red",
            },
        )
    )
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.propagate = False  # Prevent double logging
