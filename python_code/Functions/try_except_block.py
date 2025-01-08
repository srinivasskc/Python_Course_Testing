'''
This is a try except block.
'''
try:
    number = int(input("Enter the Number: "))
    value = 100/number
    print(value)
except ZeroDivisionError:
    print("Entered value is invalid. Received ZeroDivisionError")
    print("Value cannot be 0")
except ValueError:
    print("Entered Value is Invalid")
except KeyboardInterrupt as keyInExcept: 
    print(keyInExcept)
    # CTRL + C
except EOFError as eoferror:
    print(EOFError)
    # CTRL+Z
except Exception as e: 
    # Catch all other exceptions
    print(f"An unexpected error occured {e}")
print("Thank you!!")
