"""
Calculations
"""

def add(a,b):
    """
    This is addition function
    """
    return a+b


def sub(a,b):
    """
    This is subraction Function
    """
    return a-b

def multi(a,b):
    """
    This is multiplication function
    """
    return a * b

def div(a,b):
    """
    This is division function
    """
    if b ==0:
        raise ZeroDivisionError("Cannot Divide by zero")
    return a/b

def mod(a,b):
    """
    This is modulus function
    """
    return a%b

def floor_div(a,b):
    """
    This is floor division function means no decimal.
    """
    if b ==0:
        raise ZeroDivisionError("Cannot Divide by zero")
    return a//b


print(add(10,20))
# print(div(5,0))
