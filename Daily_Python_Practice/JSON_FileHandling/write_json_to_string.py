"""
Convert the following Python object to a JSON string using json.dumps().
"""

import json

new_task = {"title": "Finish Exercise", "completed": False}
print(new_task)
print(type(new_task))

str_json = json.dumps(new_task)
print(str_json)
print(type(str_json))
