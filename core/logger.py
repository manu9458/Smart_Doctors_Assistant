import logging
from logging.handlers import RotatingFileHandler

def get_logger():
    logger = logging.getLogger("doctor_app")

    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    handler = RotatingFileHandler("app.log", maxBytes=5_000_000, backupCount=3)
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    handler.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setFormatter(formatter)

    logger.addHandler(handler)
    logger.addHandler(console)
    return logger
