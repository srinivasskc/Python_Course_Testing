"""
Your task list is stored in my_tasks.json, and you want to add a new task without breaking the JSON format.
"""
import json

new_task = {"title": "Debug JSON Handling", "completed": False}


with open("F:/Career/udemy-course/python_course_testing/Daily_Python_Practice/JSON_FileHandling/my_tasks.json","r",encoding="UTF-8",) as file:
    tasks = json.load(file)
    print(tasks)

# Appending the new task with tasks.
tasks.append(new_task)
print(tasks)
#print(type(tasks))

with open("F:/Career/udemy-course/python_course_testing/Daily_Python_Practice/JSON_FileHandling/my_tasks.json","w",encoding="UTF-8",) as file:
    # Dumping the data from the tasks back to the file.
    json.dump(tasks,file,indent=4)
    print("Data Appended successfully")

