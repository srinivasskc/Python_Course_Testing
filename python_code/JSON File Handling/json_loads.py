"""
Parse JSON String to JSON Python Object. (List)
"""

import json

print("===Get the JSON String===")

JSON_STRING = '[{"title": "Learn JSON", "completed": false}]'

# String
print(JSON_STRING)
print(type(JSON_STRING))

print("\n")

print("===Convert to JSON Python Object===")

# Converting to List
json_data = json.loads(JSON_STRING)
print(json_data)
print(type(json_data))
