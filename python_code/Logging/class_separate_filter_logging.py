"""
This is logging to different files for each level.
"""
import logging


# class LevelFilter inherits from logging.Filter
class LevelFilter(logging.Filter):
    """A filter to log only a specific level."""
    def __init__(self, level):
        super().__init__() # Calling the base class constructor.
        self.level = level

    def filter(self, record):
        """
        filter() defines whether a log record should be allowed through filter
        record is object created by logging module. it has below attributes
            record.levelno, record.msg, record.name
        here, record.levelno is compared with self.level specified level.
        If its mateched, then processed else not processed.
        """
        return record.levelno == self.level 



def setup_logging():
    """
    Create a new logger instance to capture all logs.
    """
    
    # Custom Logger.
    logger = logging.getLogger()
    breakpoint()
    # Returns <RootLogger root (WARNING)>.
    # logger.setLevel(logging.DEBUG)
    # print(logger)
    # Returns <RootLogger root (DEBUG)>

    # Define Log Format
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # Create File Handlers for different Log Levels.
    debug_handler = logging.FileHandler("F:/Career/udemy-course/python_course_testing/python_code/Logging/debug.log",mode="w")
    debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(formatter)
    debug_handler.addFilter(LevelFilter(logging.DEBUG))


    info_handler = logging.FileHandler("F:/Career/udemy-course/python_course_testing/python_code/Logging/info.log",mode="w")
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(formatter)
    info_handler.addFilter(LevelFilter(logging.INFO))



    warning_handler = logging.FileHandler("F:/Career/udemy-course/python_course_testing/python_code/Logging/warning.log",mode="w")
    warning_handler.setLevel(logging.WARNING)
    warning_handler.setFormatter(formatter)
    warning_handler.addFilter(LevelFilter(logging.WARNING))

    error_handler = logging.FileHandler("F:/Career/udemy-course/python_course_testing/python_code/Logging/error.log",mode="w")
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)
    error_handler.addFilter(LevelFilter(logging.ERROR))

    
    critical_handler = logging.FileHandler("F:/Career/udemy-course/python_course_testing/python_code/Logging/critical.log",mode="w")
    critical_handler.setLevel(logging.CRITICAL)
    critical_handler.setFormatter(formatter)
    critical_handler.addFilter(LevelFilter(logging.CRITICAL))



    # Stream Handler for console output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Assign the handlers to Custom Logger
    logger.addHandler(debug_handler)
    logger.addHandler(info_handler)
    logger.addHandler(warning_handler)
    logger.addHandler(error_handler)
    logger.addHandler(critical_handler)
    logger.addHandler(console_handler)


setup_logging()

# Testing the log levels.
logging.debug("This is a DEBUG message — for fine-grained details.")
logging.info("This is an INFO message — general information.")
logging.warning("This is a WARNING message — caution required.")
logging.error("This is an ERROR message — action needed.")
logging.critical("This is a CRITICAL message — immediate attention required.")
