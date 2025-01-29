"""
# Importing the JSON module and storing as Dictionary
"""

import json

# Reading from JSON File.

with open(
    "F:/Career/udemy-course/python_course_testing/python_code/JSON File Handling/todo.json",
    "r",
    encoding="UTF-8",
) as file:
    todos = json.load(file)
    print(todos)
    print(type(todos))

# This loads the json file data to todo python object and stores as Dictionary.
