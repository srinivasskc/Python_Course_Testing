'''
Boolean Operators

> Identity Operators = Address of Object
is 
is not

> Membership Operators = Value
in
not in
'''


# Identity Operators
flowers1 = ["red","black", "blue"]
colors1  = ["red", "black", "blue"]

print(flowers1 == colors1)

print(id(flowers1))
print(id(colors1))

print(flowers1 is colors1)
print(flowers1 is not colors1)


print(id(flowers1[1]))
print(id(colors1[1]))
print(flowers1[1] is colors1[1])

# Membership Operators

print("red" in flowers1)
print("green" in flowers1)
print("green" not in flowers1)

