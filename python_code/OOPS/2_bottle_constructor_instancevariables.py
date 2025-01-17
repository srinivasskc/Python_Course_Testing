#OOPS

class Bottle:
    '''
    This is a Bottle Class.
    '''
    # Static Variables - Properties
    brand="Bisleri"

    # Default Constructor
    def __init__(self):
        print('Constructor is called')


    # Behaviors / Methods
    def wash(self):
        '''
        This is wash method.
        '''
        print("Washing the bottle")

    def set_cap(self):
        '''
        This is setCap method.
        '''
        print("Setting the cap")

    def fill(self):
        '''
        This IS fill method.
        '''
        print("Filling the bottle")

    def close(self):
        '''
        This is close method.
        '''
        print("Closing the bottle")


# Creating an Object of Bottle Class. i.e Bottle()
# Initializing the instance variable for the Object i.e bottle1.
bottle1 = Bottle()
print(bottle1)

print(Bottle.brand)

bottle1.wash()
bottle1.set_cap()
bottle1.fill()
bottle1.close()

