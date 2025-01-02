# String Methods
# String is Immutable, The string value which is series of characters within the quotes cannot be changed.
# But we can copy the string then modify the string or a value from the string

# Method depends on the object, but function does not depend on the object
# Method is dependent on object and function is independent on object


book = "Programming with Python"

print(book)

# length is a function
print(len(book))

# lower is a method
print(book.lower())
# upper is a method
print(book.upper())

# True or false, if the string is completely upper or lower case
print(book.islower())
print(book.isupper())


# Convert to Upper and check if it is upper
# This would print only if the result is upper or not
print(book.upper().isupper())

print(book.lower().islower())


# Find the letter in the string
# If we give any character which is part of the string, the result would be index value of the string
# This will fetch first occurrence of the "find character in the string"
print(book.find('i'))
print(book.find('y'))

# If we give any character which is not part of the string, the result would be -1
print(book.find('A'))


# Search Range of Characters
# This will print first occurrence of "P" in "Python"
print(book.find("Python"))
print(book.find('Py'))


# Replace String
print(book.replace("with Python", "in Python"))

