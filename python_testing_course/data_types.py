# Basic Data Types in Python
# Integer, Float, Complex

a = 5 #Integer
print(a)
a1 = -5 
print(a1)
a2 = 123456789012345678901234567890 #Large Integer
print(a2)


b = 5.3 #Float
print(b)
b1 = 5.5
print(b1)
b2 = 5.123456789012345678901234567890 #Large Float
print(b2)
b3 = -5.64
print(b3)

c = 5 + 2j #Complex
print(c)

# Type of Variables
print(f"a is {type(a)}")
print(f"a1 is {type(a1)}")
print(f"a2 is {type(a2)}")
print(f"b is {type(b)}")
print(f"b1 is {type(b1)}")
print(f"b2 is {type(b2)}")
print(f"b3 is {type(b3)}")
print(f"c is {type(c)}")

# Type Conversion
print(a)
a_float = float(a)  # Convert Integer to Float
print(f"a_float is {a_float} and its type is {type(a_float)}")

print(b)
b_int = int(b)  # Convert Float to Integer
print(f"b_int is {b_int} and its type is {type(b_int)}")
