import logging

LOGGER_NAME = "GothicArchitect"

logger = logging.getLogger(LOGGER_NAME)

if not logger.handlers:
    handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "[%(name)s] %(levelname)s: %(message)s"
    )

    handler.setFormatter(formatter)

    logger.addHandler(handler)

logger.setLevel(logging.INFO)