# This will return "None", as number + number is an expression and not a print statement like earlier.

def add_numbers(number):
    '''
    add two numbers. number is passed as argument to the parameter.
    '''
    number + number

print(add_numbers(10))



# This will return value.
def add_num(number):
    '''
    add two numbers. number is passed as argument to the parameter.
    '''
    return number + number

print(add_num(10))


# This will return value.
def add_two_nums(number1,number2):
    '''
    add two numbers. number is passed as argument to the parameter.
    '''
    total=number1 + number2
    return total

print(add_two_nums(10,20))

# This will return value.
def add_two_num(number1,number2):
    '''
    add two numbers. number is passed as argument to the parameter.
    '''
    total=number1 + number2
    print("Total is : ", end="")
    # end="" is used to end with no new line.
    return total
    # print("Total is : ") - If we add the print statmenet after return statement, code is not reachable

results=add_two_num(10,20)
print(results)

