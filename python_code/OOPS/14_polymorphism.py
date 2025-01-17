# Polymorphism
# Python does not support Method Overloading
# Python -> Class -> Two Methods with same name but different Parameters is not supported.

# Method Overriding: 
# Calling the same method name in Parent and Child Class.
# Output: Child Class return data will override Parent Class.

class Bottle:
    '''
    This is parent class Bottle.
    '''
    def __init__(self):
        pass

    def wash(self):
        '''
        This is wash method in Bottle Class
        '''
        print("Washing the bottle")
    
    def set_cap(self):
        '''
        This is set cap Method in Bottle Class
        '''
        print("Setting the cap")


class CopperBottle(Bottle):
    '''
    This is Copper Bottle Class
    '''
    def wash(self):
        print("Washing the Copper Bottle")
    
    def set_cap(self):
        print("Setting the cap for Copper Bottle")

b2 = CopperBottle()
b2.wash()
b2.set_cap()


