# Functions

print("-----")

def hello_world():
    """
    print "Hello, World!" using a function
    """
    print("Hello, World!")


hello_world()

print("-----")
print("Positional Arguments:")

def greet(name, age):
    """
    Print a greeting message with name and age
    """
    print(f"Hello, {name} you are {age} years old.")

greet("Srinivas", 36)

print("-----")
print("Arbitrary Arguments:")

def sum_numbers(*numbers):
    """
    Calculate the sum of arbitrary numbers
    """
    total = 0
    for number in numbers:
        total += number
    
    print(f"The sum of the numbers is: {total}")

sum_numbers(1, 2, 3, 4, 5)
sum_numbers(10, 20, 30)

print("-----")  

print("Positional and Keyword arguments with one default value:")

def display_info(name, age, city="Hyderabad"):
    """
    Display information about a person with a default city
    """
    print(f"Name: {name}, Age: {age}, City: {city}")

# Using positional arguments
display_info("Srinivas", 36)

# Using keyword arguments
display_info(name="John", age=30, city="New York")

print("-----")

print("Display List Fruits: ")

def display_fruits(fruits_list):
    """
    Display each fruit in the list
    """
    for fruit in fruits_list:
        print(fruit)
    
my_fruits = ["Apple", "Banana", "Mango", "Grapes"]

display_fruits(my_fruits)

print("-----")

print("Multiple Return Values:")

def multiply(a,b):
    """
    Multiply two numbers and return the result
    """
    result = a * b
    return result

multiply_result = multiply(1,3)
print(f"Multiplication Result: {multiply_result}")

print("-----")
print("Function with Return Value:")

def calculate(a, b):
    """
    Calculate the sum and product of two numbers
    """
    sum_result = a + b
    multiply_result = a * b
    difference_result = a - b
    return sum_result, multiply_result, difference_result

result_sum, result_mul, result_diff = calculate(5, 3)
print(f"Sum: {result_sum}, Product: {result_mul}, Difference: {result_diff}")

print("-----")


