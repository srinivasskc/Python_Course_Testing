"""
Exercise 2: Add two numbers using a method

Task:
Create a class Calculator
Add a method add_numbers(self, a, b) that returns the sum
"""

class Calculator:
    def add_numbers(self,a,b):
        """Method to add two numbers."""
        return a + b

# Example usage:
my_calculator = Calculator()
result = my_calculator.add_numbers(5, 3)
print(f"The sum of 5 and 3 is: {result}")
