"""
Create N Variable to store positive integer number
Calculate sum of all numbers that are multiples of 3 or 5 up to N (excluding N itself)
print the result
"""

N = int(input("Enter a positive integer number: "))

total_sum = 0

current_number = 1


while current_number < N:
    if current_number % 3 == 0 or current_number % 5 == 0:
        total_sum += current_number
    current_number += 1

print(f"Sum of multiples of 3 or 5 up to {N} (excluding {N} itself) is: {total_sum}")
