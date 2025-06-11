class Parent:
    def greet(self, name=None):
        if name is None:
            return "Hello, Unknown Parent"
        else:
            return f"Hello, parent {name}"
        
class Child(Parent):
    def greet(self, name=None):
        if name is None:
            return "Hello, Who are you child?"
        else:
            return f"Hello, child {name}"


my_parent = Parent()
print(my_parent.greet())
print(my_parent.greet("Srinivas"))

my_child = Child()
print(my_child.greet())
print(my_child.greet("Vasishta"))
