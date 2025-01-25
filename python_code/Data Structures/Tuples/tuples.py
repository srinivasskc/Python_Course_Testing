# Tuple Data Type
# Tuple - Immutable Data Type and is represented by ()
# Tuple Value cannot be added, removed or changed.

# List Declaration
print("====Lists - Mutable Data Type====")
num_list = [5,8,2,1,7,8]
print(num_list)
print(num_list.count(8))
print(num_list.index(8))

print("\n")
# Tuple Declaration
print("====Tuple - Immutable Data Type====")
num_tuple=(5,8,2,1,7,8)
print(num_tuple)

# Tuple Methods
print("Count of Value in the Tuple: ",num_tuple.count(7))
print("Index Value is: ",num_tuple.index(7))

# Can we modify the value.
# num_tuple[0]=10
# print(num_tuple)
# TypeError: 'tuple' object does not support item assignment

coordinates = (12.9367333,77.5719128)
print(coordinates)
print(coordinates[0])  # Latitude
print(coordinates[1])  # Longitude

# coordinates[0]=12.9367334
# print(coordinates)
# TypeError: 'tuple' object does not support item assignment
