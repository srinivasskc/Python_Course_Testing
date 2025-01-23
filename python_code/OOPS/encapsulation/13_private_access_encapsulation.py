# Private Access Modifier Encapsulation


# Private Variables can be called within the class and not child classes

class Bottle:
    '''
    This is Bottle Class
    '''
    def __init__(self,color,capacity,height,rate):
        
        # Private Static Variables represented with double underscore.
        self.__color = color

        # Public Static Variables.
        self.capacity = capacity
        self.height = height
        self.rate = rate

    def wash(self):
        '''
        This is Wash Method and printing the Private Static Variable within the class.
        '''
        print("Washing the bottle which is of color:", self.__color)
    
    def set_cap(self):
        '''
        This is setCap Method
        '''
        print("Setting the cap")
    
    def fill(self):
        '''
        This is Fill Method
        '''
        print("Filling the bottle")
    
    def close(self):
        '''
        This is Close Method
        '''
        print("Closing the bottle")

b1 = Bottle(capacity=1,color="red",height=10,rate=20)


# print(b1.__color)
# Private Variables cannot be accessed outside the class.

print(b1.capacity)
print(b1.height)
print(b1.rate)
b1.wash()
b1.set_cap()
b1.fill()
b1.close()

# Inheritance Class

class Bottle2(Bottle):
    '''
    This is Inheritance Class Bottle1 with Parent Class Bottle
    '''
    def wash1(self):
        '''
        This is wash1 method.
        '''
        print("Washing the bottle1 which is of color")

b2 = Bottle2(capacity=2,color="blue",height=20,rate=40)
b2.wash1()
b2.wash()
# print(b2.__color)
# Private Variables cannot be accessed outside the class and child classes.