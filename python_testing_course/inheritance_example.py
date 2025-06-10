class Parent:
    def __init__(self):
        """Initialize the Parent class."""
        print("Parent class initialized.")

    def speak(self):
        """Method for the Parent class to speak."""
        print("Parent is speaking.")


class Child(Parent):
    def __init__(self):
        super().__init__()  # Call the Parent class's __init__ method
        """Initialize the Child class."""
        print("Child class initialized.")
    
    def speak(self):
        """Method for the Child class to speak."""
        super().speak()  # Call the Parent class's speak method
        print("Child is speaking.")

# Example usage:
my_child = Child()
# This will print:
# Parent class initialized.
# Child class initialized.
# The Child class inherits from the Parent class, and when an instance of Child is created,

my_child.speak()
# Method Overriding in action:
# This will print child's method and not parent's method

