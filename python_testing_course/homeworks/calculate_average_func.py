"""
Create a function that calculates the average of a list of numbers.
"""

def calculate_average(numbers):
    """
    calculate_average calculates the average of a list of numbers.
    """
    total = 0
    for number in numbers:
        total += number
    
    average = total / len(numbers)
    return average

# Example usage:
numbers = [10, 20, 30, 40, 50]
average_result = calculate_average(numbers)
print(f"The average of the numbers {numbers} is: {average_result}")
