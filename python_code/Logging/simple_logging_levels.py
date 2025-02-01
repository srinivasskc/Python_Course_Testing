"""
Logging Levels
5 - CRITICAL
4 - ERROR
3 - WARNING
2 - INFO
1 - DEBBUG
"""

import logging

def setup_logging():
    """
    Setup
    """
    logging.basicConfig(filename="F:/Career/udemy-course/python_course_testing/python_code/Logging/warn.log",level=logging.WARNING)
    # If no file found, this will create the file.

    print("==This is Logging Module Demo===")
    logging.debug("This is debug message")
    logging.info('This is info message')
    logging.warning("This is warning message")
    logging.error("This is error message")
    logging.critical("This is critical message")

setup_logging()

# As the basicConfig is with logging.WARNING, the logs will print only for WARNING and Above Levels.
