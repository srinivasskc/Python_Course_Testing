# Lists - Mutable Data Type

"""
Lists Value can be added, removed and changed.
"""

num_list = [5,8,2,1,7,8]

str_list = ['A','a','B','Apple','Ball','Cat','Dog']

boolean_list = [[0,'F'],[1,'T'],[-1,'Error']]

print(num_list)
print(str_list)
print(boolean_list)

# Length of the List
print(len(num_list))
print(len(str_list))
print(len(boolean_list))  #Does not count the nested lists count.

# Count Method - How many times an element is present in the list
print(num_list.count(8))
print(str_list.count('a'))
print(boolean_list.count('T'))  #Does not count the nested lists count.

# Accessing the list.
print(num_list[0])
print(str_list[6])

# Positive Flow
print(boolean_list[0])
print(boolean_list[1])
print(boolean_list[1][1])
print(boolean_list[2])


# Negative Flow
print(boolean_list[-1])
print(boolean_list[-2])
print(boolean_list[-3])


# Errors - List Index Out of Range
# print(num_list[6])
# Index starts at 0 and ends at n-1

print(num_list) 
print(num_list[0])
print(num_list[5])

# Errors - TypeError: list indices must be integers or slices, not float
# print(num_list[1.0])

print("\n")

# Slicing
print(num_list)
print(num_list[0:3]) # Slice starts at beginning of the list, but does not include the end index
print(num_list[0:])  # Slices till the end of the list
print(num_list[:5])  # Slice starts at the beginning of the list

print("\n")

# Updating the List
print(num_list)
num_list[5]=9
print(num_list)

print("\n")

print(str_list)
str_list[1]='elephant'
print(str_list)

print("\n")
# Adding to the List - Insert
print(num_list)
num_list.insert(1,6)
print(num_list)

print("\n")

# Adding to the end of the list - Append
print(str_list)
str_list.append('Fish')
print(str_list)


print("\n")
# Adding more than one item to the end of list - Extend
print(str_list)
str_list.extend(['Goat','Hen','Ink'])
print(str_list)
str_list_2 = ['Kite','Lion','Monkey']
str_list.extend(str_list_2)
print(str_list)

print("\n")
# Extending one word as multiple letters.
print(str_list)
str_list.extend('Jelly')
print(str_list)

print("\n")
# Appending the list to the list
str_list_3 = ['Nose','Owl','Parrot']
print(str_list)
str_list.append(str_list_3)
print(str_list)


# Removing Item from the list - Remove

# Single Letter
str_list.remove('J')
print(str_list)

print("\n")
# Removing Item from the list based on position of Item
print(str_list)
del str_list[1]
print(str_list)

print("\n")
# Removing the last item from the list - Pop Method.
print(str_list)
popped_str = str_list.pop()
print(str_list)
print(popped_str)

print("\n")
# Popping specific item from the list.
print(str_list)
popped_str_index = str_list.pop(0)
print(str_list)
print(popped_str_index)

print("\n")
# Sorting the List 
print(num_list)
num_list.sort()
print(num_list)

# Strings are sorted in ASCII'betical Order.
print("\n")
print(str_list)
str_list.sort()
print(str_list)

print("\n")
print(boolean_list)
boolean_list.sort()
print(boolean_list) 

# Sorting the String List in Alphabetical Order
print("\n")
print(str_list)
str_list.sort(key=str.lower)
print(str_list)
