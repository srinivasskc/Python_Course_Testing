"""
Convert the Python Object to JSON Formatted String.
"""


import json

print("===Get the JSON Python Object===")
json_data = [{"title": "Learn JSON", "completed": False}]

print(json_data)
print(type(json_data))

print("\n")

print("===Convert to JSON String===")

json_string = json.dumps(json_data)
print(json_string)
print(type(json_string))
