import logging
import os

def setup_logger(name: str, log_file: str, level=logging.INFO):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Clear the log file at each start
    with open(log_file, "w"):
        pass

    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.handlers.clear()
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
