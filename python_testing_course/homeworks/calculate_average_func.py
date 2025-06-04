"""
Create a function that calculates the average of a list of numbers.
"""

def calculate_average(num_list):
    """
    calculate_average calculates the average of a list of numbers.
    """
    total = 0
    for number in num_list:
        total += number
    
    average = total / len(num_list)
    return average

# Example usage:
numbers = [10, 20, 30, 40, 50]
AVERAGE_RESULT = calculate_average(numbers)
print(f"The average of the numbers {numbers} is: {AVERAGE_RESULT}")
