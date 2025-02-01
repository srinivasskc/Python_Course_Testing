"""
Simple logs to console and file
"""

import logging

# Setup function

def setup_logging():
    """
    Setup logging to file and console.
    """
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.DEBUG,
        handlers=[
            logging.FileHandler("F:/Career/udemy-course/python_course_testing/python_code/Logging/allLogs.log"),
            logging.StreamHandler() 
        ]
    )

# Calling Setup Logging
setup_logging()

# demo

def demo_log_levels():
    logging.info("This is info log level message")
    logging.debug("This is debug log level message")
    logging.warning("This is warning log level message")
    logging.error("This is error log level message")
    logging.critical("This is critical log level message")
    logging.exception("This is exception log level message")

# Calling demo method
demo_log_levels()
    