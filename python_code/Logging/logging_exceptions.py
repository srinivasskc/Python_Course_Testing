"""
logging exceptions
"""

import logging

logging.basicConfig(filename="F:/Career/udemy-course/python_course_testing/python_code/Logging/exception.log",level=logging.DEBUG)
logging.info("Start of Logging Exceptions")

# Program
try:
    x = int(input("Enter 1st number: "))
    y = int(input("Enter 2nd number: "))

    print(x/y)
except ZeroDivisionError as ex:
    print("division by zero is not possible")
    logging.exception(ex)
except ValueError as ex:
    print("Value Error occurred, No Value is entered")
    logging.exception(ex)

logging.info("End of Logging Exceptions")
