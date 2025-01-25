# Way 1 - Create Sets using Function
women = set(['Radha', 'Sita', 'Gita','Sita','Radha'])

# Way 2 - Create Sets using Constructor
men = set(('Ram', 'Shyam', 'Gopal','Ram','Shyam'))

# Way 3 - Create Sets using literals
numbers = {1,1,2,2,3,3,4,5,6,6,7,8,9,9,10}

# Sets removes the duplicates
# Each time we run this program, the output/order will be different.
print(women)
print(men)
print(numbers)

# Set Index - TypeError: 'set' object does not support indexing
# print(numbers[0])


# Even Numbers
even_nums =  {0,2,4,6,8,10,12,14,16,18,20}
odd_nums = {1,3,5,7,9,11,13,15,17,19}
prime_nums = {2,3,5,7,11,13,17,19}

# Set Functions

## Union - Combines the elements of two sets
print(even_nums.union(odd_nums))
print(even_nums | odd_nums)

## Intersection - Common elements between two sets
print(even_nums.intersection(odd_nums))
print(even_nums & odd_nums)

print(even_nums.intersection(prime_nums))
print(even_nums & prime_nums)

print(odd_nums.intersection(prime_nums))
print(odd_nums & prime_nums)

# Difference - Elements in one set but not in the other set
# If we have A and B, then A-B is elements in A but not in B
print(even_nums.difference(odd_nums))
print(even_nums.difference(prime_nums))
print(prime_nums.difference(odd_nums))
print(odd_nums - prime_nums)


