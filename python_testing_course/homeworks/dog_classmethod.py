"""
Exercise 4: Use a class method to count instances

Task:
Create a class Dog
Use a class variable count = 0
In the __init__ method, increase count each time a dog is created
Add a @classmethod called get_count() to print the count
"""

class Dog:
    count = 0  # Class variable to keep track of the number of Dog instances

    def __init__(self, name):
        """ Each time a Dog instance is created, increment the count. """
        self.name = name
        Dog.count = Dog.count + 1
        print(f"Dog created: {self.name}. Total dogs: {Dog.count}")
    
    @classmethod
    def get_count(cls):
        """ return the current count of Dog instances. """
        return cls.count

# Example usage:
my_dog1 = Dog("Sky")
my_dog2 = Dog("Buddy")

# Calling the class method to get the count of Dog instances
print(f"Total number of dogs: {Dog.get_count()}")
