"""
Read the following JSON data from a file called tasks.json and print the title of each task.
"""

import json

with open("F:/Career/udemy-course/python_course_testing/Daily_Python_Practice/JSON_FileHandling/read_tasks.json","r",encoding="UTF-8") as file:
    js_file = json.load(file)
    print(js_file)
    # print(type(js_file))
    for i in js_file:
        #print(i)
        print(i['title'])
