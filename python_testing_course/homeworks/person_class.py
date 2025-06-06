"""
Exercise 1: Create a method that greets a user

Task:
Create a class called Person.

The class should have an __init__ method that takes name as a parameter.

Add a method called greet() that prints:
"Hello, my name is <name>"
"""
class Person:
    def __init__(self,name):
        self.name = name

    def greet(self):
        """Method to greet the user."""
        print(f"Hello, my name is {self.name}.")


# Example usage:
my_person = Person("Srinivas")
my_person.greet()
