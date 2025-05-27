empty_dict = {}
# Empty dictionary
print(empty_dict)

my_dict = {
    "first_name": "Srinivas",
    "last_name" : "Kadiyala",
    "age" : 36
}

print(my_dict)

print(my_dict["first_name"])

print(f'{my_dict["first_name"]} {my_dict["last_name"]} is {my_dict["age"]} years old.')

# Adding a new key-value pair to the dictionary
my_dict["city"] = "Hyderabad"
print(my_dict)

# Updating an existing key-value pair in the dictionary
my_dict["age"] = 37
print(my_dict)  

# Removing a key-value pair from the dictionary
del my_dict["age"]
print(my_dict)

print(my_dict.keys())  # Get all keys
print(my_dict.values())  # Get all values
print(my_dict.items())  # Get all key-value pairs

# Practical Application: Storing user information, organizing test results, storing configuration settings, etc.
