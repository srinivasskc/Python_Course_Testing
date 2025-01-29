"""
Importing json data to json file.
"""

import json

new_todo = [
    {
        "userId": 2,
        "id": 2,
        "title": "Mahabharata",
        "completed": False
    },
    {
        "userId": 1,
        "id": 3,
        "title": "Lessons Learned in Software Testing",
        "completed": True
    }
]

# Write to JSON File.
with open(
    "F:/Career/udemy-course/python_course_testing/python_code/JSON File Handling/todo.json",
    "w",
    encoding="UTF-8",
) as file:
    json.dump(new_todo,file,indent=4)


# Append Data to Existing JSON File.

new_todo = [
    {
        "userId": 1,
        "id": 1,
        "title": "Ramayana",
        "completed": False
    }
]

with open(
    "F:/Career/udemy-course/python_course_testing/python_code/JSON File Handling/todo.json",
    "r",
    encoding="UTF-8",
) as file:
    todo_file = json.load(file)
    print(todo_file)

todo_file.extend(new_todo)

with open(
    "F:/Career/udemy-course/python_course_testing/python_code/JSON File Handling/todo.json",
    "w",
    encoding="UTF-8",
) as file:
    json.dump(todo_file,file,indent=4)
