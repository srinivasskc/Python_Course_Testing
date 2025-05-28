# Assignment Operators
x = 5
print(x)

y = x + 3
print(y)

z = y / 2
print(z)

# Add Assign operator
x += 10
print(x)

# Subtract Assign operator
x -= 2
print(x)

# Multiply Assign operator
x *= 3
print(x)

# Divide Assign operator
x /= 2
print(x)

# Modulus Assign operator
x %= 3
print(x)

# Exponent Assign operator
x **= 2
print(x)

# Floor Division Assign operator
x //= 2
print(x)

print("-----------------")

print("Comparison Operators")
# Comparison Operators
a = 10
b = 20
print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to

print("-----------------")
print("Logical Operators")
# Logical Operators
x = True
y = False
print(x and y)  # Logical AND
print(x or y)   # Logical OR
print(not x)    # Logical NOT
print(not y)    # Logical NOT

print("-----------------")

print("Membership Operators")
# Membership Operators
fruits = ['Apple', 'Banana', 'Cherry']
print('Banana' in fruits)  # True if 'Banana' is in the list
print('Mango' not in fruits)  # True if 'Mango' is not in the list

print("-----------------")
print("Identity Operators with Numbers")
# Identity Operators - Check if two variables point to the same object
a = 5
b = 5

print(a is b)  # True, because both point to the same object
print(a == b)  # True, because values are equal

print("Memory address of a:", id(a))
print("Memory address of b:", id(b))


print("-----------------")
print("Identity Operators with Lists")
list_a = [1, 2, 3]
list_b = [1, 2, 3]
print(list_a is list_b)  # False, because they are different objects in memory
print(list_a == list_b)  # True, because values are equal

print("Memory address of list_a:", id(list_a))
print("Memory address of list_b:", id(list_b))


print("-----------------")


list_c = list_a  # list_c points to the same object as list_a
print(list_a is list_c)  # True, because both point to the same object  
print("Memory address of list_c:", id(list_c))
print("Memory address of list_a:", id(list_a))

print("-----------------")

list_d = list_a.copy()  # Creates a shallow copy of list_a
print(list_a is list_d)  # False, because list_d is a new object
print(list_a == list_d)  # True, because values are equal
print("Memory address of list_d:", id(list_d))
print("Memory address of list_a:", id(list_a))
