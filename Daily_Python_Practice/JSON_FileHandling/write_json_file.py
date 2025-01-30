"""
Write the following list of todos to a JSON file called my_tasks.json.
"""

import json

todos = [
    {"title": "Complete Python Course", "completed": False},
    {"title": "Review Project Requirements", "completed": True}
]


with open("F:/Career/udemy-course/python_course_testing/Daily_Python_Practice/JSON_FileHandling/my_tasks.json","w",encoding="UTF-8") as file_Write:
    json.dump(todos,file_Write,indent=4)
