class Encapsulation:
    def __init__(self):
        self.public = "I am public"
        self._protected = "I am protected" # Single Underscore
        self.__private = "I am private" # Double Underscore

    @property   
    def private(self):
        """
        This is getter method and accessing __private variable.
        """
        return self.__private
    
    @private.setter    
    def private(self, value):
        """
        This is setter method, if we want to change the value of private variable.
        """
        self.__private = value
    
my_encapsulation = Encapsulation()

print(my_encapsulation.public)
print(my_encapsulation._protected)
# print(my_encapsulation.__private)  # AttributeError: 'Encapsulation' object has no attribute '__private'

print(my_encapsulation.private)
my_encapsulation.private = "I am new private from object"
print(my_encapsulation.private)

