'''
Enter the age of the person
If the age of the person is 18 and above, the person is eligible to vote.
If the age of the person is less than 18, the person is not eligible to vote.
'''

name = input("Enter your name: ")

age = int(input("Enter your age " + name + ": "))

print(age)


# If Statement
if age >= 18:
    print("Your age is above 18")
    print("You are eligible to vote")
print("Have an Awesome Day")

# If Else Statement
if age >= 18:
    print("Your age is above 18")
    print("You are eligible to vote")
else:
    print("You are not eligible to Vote.")
    print("Please come back when you are 18 or older")
print("Have a good day!")

# Ternary Statement - Shortcut to If Else Statement

outcome = True if age>=18 else False
print("Can you Vote?: " + str(outcome) + "\n")




