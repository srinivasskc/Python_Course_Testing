"""
Parse a JSON string using json.loads() and print the value of the "title" key.
"""

import json

json_string = '[{"title": "Learn JSON", "completed": false}]'

print("===Reads the String===")
print(json_string)
print(type(json_string))

print("\n")
print("===Parsing String to JSON==")

json_data = json.loads(json_string)
print(json_data)
print(type(json_data))

print("\n")
print("==Printing the Value of Title===")
print(json_data[0]['title'])
