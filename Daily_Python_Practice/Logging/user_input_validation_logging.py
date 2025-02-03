"""
Validate User Input with Logging
"""

import logging

def check_age_input(age):
    """
    This method is with logging
    """
    try:
        age = int(age)
        print(age)
        if age < 0:
            logging.warning("Age cannot be negative")
        else:
            logging.info("You have entered valid age: %d", age)
    except ValueError:
        logging.error("You have entered invalid age input literal")

def setup_logging():
    """
    This is setup of logging.
    By default, logging appends to the log file (filemode='a'). To overwrite it on every run, set filemode='w'.
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("F:/Career/udemy-course/python_course_testing/Daily_Python_Practice/Logging/age_log.log",mode="w"),
            logging.StreamHandler()
        ]
    )

setup_logging()

# Calling the functions
check_age_input(-5)
check_age_input(15)
check_age_input(18)
check_age_input('abc')
check_age_input(5.0)


