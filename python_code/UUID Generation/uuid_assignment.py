"""
Generate new unique uuid for todo list and assign to the json.
"""

import uuid
import json

def generate_unique_todo_id():
    """
    Generate Unique todo id and assign it to new todo items
    """
    return uuid.uuid4().hex

new_todo = {
        "title": "Generate UUID from a function again",
        "Status": True
            }


new_todo["id"] = generate_unique_todo_id()
print(new_todo)

# Open the JSON File. Read the File. and Append the above JSON new task to it.
with open("F:/Career/udemy-course/python_course_testing/python_code/UUID Generation/todo.json","r",encoding="UTF-8") as file:
    json_tasks = json.load(file)
    print(json_tasks)

json_tasks.append(new_todo)
print(json_tasks)

# Writing back to JSON File with write mode.
with open("F:/Career/udemy-course/python_course_testing/python_code/UUID Generation/todo.json","w",encoding="UTF-8") as file_write:
    # dump(from,to,indentation)
    json.dump(json_tasks,file_write,indent=4)
    print("Appended Successfully")

