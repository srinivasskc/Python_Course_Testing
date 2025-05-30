"""
Create N Variable to store positive integer number
Calculate sum of all numbers that are multiples of 3 or 5 up to N (excluding N itself)
print the result
"""
N = int(input("Enter a positive integer number: "))

total_sum = 0

for i in range(0,N):
    if i % 3 == 0 or i % 5 == 0:
        total_sum += i

print(f"Sum of multiples of 3 or 5 up to {N} (excluding {N} itself) is: {total_sum}")

