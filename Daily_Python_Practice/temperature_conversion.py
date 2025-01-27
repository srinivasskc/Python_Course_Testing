"""
Write a convertToFahrenheit() function with a degreesCelsius parameter. This
function returns the number of this temperature in degrees Fahrenheit. Then write a function named
convertToCelsius() with a degreesFahrenheit parameter and returns a number of this
temperature in degrees Celsius.

convertToCelsius(32) → 0.0
convertToFahrenheit(100) → 212

Fahrenheit = Celsius × (9 / 5) + 32
Celsius = (Fahrenheit - 32) × (5 / 9)
"""

def convert_to_fahrenheit(degrees_celsius):
    '''
    This is converting Celsius to Fahrenheit
    '''
    return degrees_celsius * (9/5) + 32

def convert_to_celsius(degrees_fahrenheit):
    '''
    This is converting Fahrenheit to Celsius
    '''
    return (degrees_fahrenheit - 32) * (5/9)

print(convert_to_fahrenheit(23))
print(convert_to_celsius(73.4))


# Test Cases:

# assert convert_to_celsius(73.4)==23  # This will throw an Assertion Error.
assert convert_to_celsius(73.4)==23.000000000000004
assert convert_to_fahrenheit(100) == 212
assert convert_to_fahrenheit(0) == 32

print(convert_to_fahrenheit(15))
print(convert_to_celsius(59.0))
assert convert_to_celsius(convert_to_fahrenheit(15)) == 15


print(convert_to_fahrenheit(42))
print(convert_to_celsius(107.60000000000001))
# Rounding errors cause a slight discrepancy:
assert convert_to_celsius(convert_to_fahrenheit(42)) == 42.00000000000001

# Exception Handling
try:

    assert convert_to_celsius(73.4)==23
    print("Test Passed")
except AssertionError:
    print("Test Failed")
    print("Expected Value: ",23.000000000000004)
