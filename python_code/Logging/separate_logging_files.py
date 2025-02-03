"""
This is logging to different files for each level.
"""
import logging


def setup_logging():
    """
    Create a new logger instance to capture all logs.
    """
    
    # Custom Logger.
    logger = logging.getLogger()
    # Returns <RootLogger root (WARNING)>.
    logger.setLevel(logging.DEBUG)
    # Returns <RootLogger root (DEBUG)>

    # Define Log Format
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # Create File Handlers for different Log Levels.
    debug_handler = logging.FileHandler("F:/Career/udemy-course/python_course_testing/python_code/Logging/debug.log",mode="w")
    debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(formatter)


    info_handler = logging.FileHandler("F:/Career/udemy-course/python_course_testing/python_code/Logging/info.log",mode="w")
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(formatter)


    warning_handler = logging.FileHandler("F:/Career/udemy-course/python_course_testing/python_code/Logging/warning.log",mode="w")
    warning_handler.setLevel(logging.WARNING)
    warning_handler.setFormatter(formatter)

    error_handler = logging.FileHandler("F:/Career/udemy-course/python_course_testing/python_code/Logging/error.log",mode="w")
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    # Stream Handler for console output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Assign the handlers to Custom Logger
    logger.addHandler(debug_handler)
    logger.addHandler(info_handler)
    logger.addHandler(warning_handler)
    logger.addHandler(error_handler)
    logger.addHandler(console_handler)



setup_logging()

# Testing the log levels.
logging.debug("This is a DEBUG message — for fine-grained details.")
logging.info("This is an INFO message — general information.")
logging.warning("This is a WARNING message — caution required.")
logging.error("This is an ERROR message — action needed.")
logging.critical("This is a CRITICAL message — immediate attention required.")
