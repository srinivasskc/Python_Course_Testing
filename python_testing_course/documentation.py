# Explicitly specifying data types
def add_int_numbers(a: int,b: int) -> int:
    """
    Add two numbers and return the result
    This function takes two integers as input and returns their sum.
    a = first number
    b = second number
    """
    return a + b

RESULT = add_int_numbers(5, 10)
print(f"The sum of two numbers is: {RESULT}")

print("-----")
# Explicitly specifying data types
def add_float_numbers(a: float,b: float) -> float:
    """
    Add two numbers and return the result
    This function takes two integers as input and returns their sum.
    a = first number
    b = second number
    """
    return int(a + b)

RESULT = add_float_numbers(5.0, 10.5)
print(f"The sum of two numbers is: {RESULT}")
