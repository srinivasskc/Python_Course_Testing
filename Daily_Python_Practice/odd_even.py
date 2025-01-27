"""
Is Even or Odd Program
"""

def is_even(number):
    '''
    Returns modulus value zero (Even) when number mod 2 is 0
    '''
    return number % 2 == 0

def is_odd(number):
    '''
    Returns modulus value One (Odd) when number mod 2 is 1
    '''
    return number % 2 == 1


assert is_even(2) is True
assert is_even(3) is False
assert is_odd(3) is True
assert is_odd(2) is False

# Negative is not considered only values are considered
assert is_odd(-2) is False
assert is_even(-2) is True

# Fractional Numbers are considered as False.
assert is_even(34.5) is False
assert is_odd(34.5) is False
# assert is_odd(34.5) is True

# Zero Number is considered as Even
assert is_odd(0) == False
assert is_even(0) == True
