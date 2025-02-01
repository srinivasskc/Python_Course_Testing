"""
Logging to both console and file.
"""

import logging


# First write the setup of logging function.

def setup_logging():
    """
    Setup Logging
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s  - %(message)s",
        # asctime = ASCII Time.
        handlers=[
            logging.FileHandler("F:/Career/udemy-course/python_course_testing/python_code/Logging/app.log"),
            logging.StreamHandler()
        ]
    )

# Call the logging function
setup_logging()

# Sample Method
def add(a,b):
    """
    Add two numbers and store it in log a result.
    """
    result = a + b
    logging.info("Adding %s and %s gives %s", a, b, result)
    return result

# Calling Sample Method.
add(5,6)

