import json

# Read data from Source File.

with open(
    "F:/Career/udemy-course/python_course_testing/python_code/JSON File Handling/source.json",
    "r",
    encoding="UTF-8",
) as source_file:
    source_data = json.load(source_file)

# Writing data to Destination File.

with open(
    "F:/Career/udemy-course/python_course_testing/python_code/JSON File Handling/destination.json",
    "w",
    encoding="UTF-8",
) as destination_file:
    json.dump(source_data,destination_file,indent=4)

print("Data Successfully Imported")