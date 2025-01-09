#OOPS

class Bottle:
    '''
    This is a Bottle Class.
    '''
    # Static Variables - Properties
    id=1
    color="red"
    capacity=1
    height=10

    # Behaviors / Methods
    def wash(self):
        '''
        This is wash method.
        '''
        print(self)
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

print(bottle1.id)
print(bottle1.color)
print(bottle1.height)
print(bottle1.capacity)

bottle1.wash()
bottle1.set_cap()
bottle1.fill()
bottle1.close()

# Static Variables - Properties
print(Bottle.id)
print(Bottle.color)
print(Bottle.height)
print(Bottle.capacity)
