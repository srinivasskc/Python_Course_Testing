'''
Built In Functions: print(), input()

Custom Functions:
def function_name() - defining the function.

function names should be lower case. 
if more than 1 word, underscore is used as a separator.

To call the function, we need to call it separately by function name after the definition of the function.

'''


def greeting_the_teacher():
    ''''
    This is my first function in python
    '''
    print("\t This is inside the function")
    print("\t Hello, Good Morning Teacher!")
    print("\t Happy New Year")


print("This is outside the function")
print("Start the Function call.")
greeting_the_teacher()
print("End of the function call")