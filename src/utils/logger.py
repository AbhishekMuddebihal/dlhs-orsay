import logging
import os

def get_logger():
    """
    Configures logger that logs to files.
    """
    logger = logging.getLogger('my_logger')

    logger.setLevel(logging.DEBUG)  # Can be set to DEBUG, INFO, WARNING, ERROR, CRITICAL

    log_filepath = os.path.join(os.path.dirname(__file__), '../../output/logs.txt')
    file_handler = logging.FileHandler(log_filepath)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger