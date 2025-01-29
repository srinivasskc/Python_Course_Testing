"""
Reading a JSON File.
"""

with open(
    "F:/Career/udemy-course/python_course_testing/python_code/JSON File Handling/todo.json",
    "r",
    encoding="UTF-8",
) as file:
    print(file.read())
    print(type(file.read()))
# This program will read the file and display the output as string format.
