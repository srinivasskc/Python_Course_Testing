"""
# Tuples are immutable, create a collection of items that cannot be changed.
# Attempting to change an element in a tuple will raise an error.
# In Test Automation, we used to store selenium locators in tuples.
#  we often use tuples to store fixed data that should not change.
"""


# Empty lists and tuples
empty_list = []
empty_tuple = ()

print(empty_list)
print(empty_tuple)

# Lists and Tuples with Mixed Data Types
my_list = [1,2, "apple", 3.14, True, 's', 4+5j]
my_tuple = (1, 2, "apple", 3.14, True, 's', 4+5j)
print(my_list)
print(my_tuple)

# Accessing data
print(my_list[0])
print(my_tuple[3])

# Slicing the list and tuples
sliced_list = my_list[0:3]  #Start, End-1
print(sliced_list)

sliced_tuple = my_tuple[0:3]
print(sliced_tuple)

# Assiging the list with new value.
my_list[2] = "Banana"
print(my_list)

# Length of the list and tuple
print(len(my_list))
print(f"Length of my_list is {len(my_list)}")
print(f"Length of my_tuple is {len(my_tuple)}")

# Appending to the list : Adding one more element to the end of the list
my_list.append(10)
print(my_list)

# Extending the list : Adding multiple elements to the end of the list
my_list.extend([5, 'Pear', 'Grapes'])
print(my_list)


# Inserting an element at a specific position in the list
my_list.insert(1, "Mango")
print(my_list)

# Adding duplicate elements to the list
my_list.append("Banana")
print(my_list)

# Counting occurrences of an element in the list
banana_count = my_list.count("Banana")
print(banana_count)

# Index of an element in the list - Index of the first occurrence.
banana_index = my_list.index("Banana")
print(banana_index)



empty_tuple = ()
print(empty_tuple)
my_tuple = (1, 2, "apple", 3.14, True, 's', 4+5j)
print(my_tuple)

print(my_tuple[0])  # Accessing first element
print(my_tuple[2])  # Accessing fourth element
print(my_tuple[0:3])  # Slicing the tuple to get first three elements

print(len(my_tuple))  # Length of the tuple

apple_count = my_tuple.count("apple")  # Count occurrences of "apple"
print(apple_count)

apple_index = my_tuple.index("apple")  # Index of the first occurrence of "apple"
print(apple_index)

# Attempting to change an element in a tuple will raise an error.
# my_tuple[2] = "Banana"  # Uncommenting this line will raise a TypeError
# print(my_tuple)