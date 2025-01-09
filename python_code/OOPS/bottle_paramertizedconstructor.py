#OOPS

class Bottle:
    '''
    This is a Bottle Class.
    '''
    # Static Variables - Properties
    brand="Bisleri"

    # Parameterized Constructor - Object Properties are initialized.
    def __init__(self,color,capacity,height,rate):
        # Instance Variables.
        self.color=color
        self.capacity=capacity
        self.height=height
        self.rate=rate
        print('Constructor is called')

    def get_bottle_info(self):
        '''
        This is get_bottle_info method.
        '''
        return 'Bottle Color: ' + self.color + '\n' + 'Bottle Capacity: ' + str(self.capacity) + '\n' + 'Bottle Height: ' + str(self.height) + '\n' + 'Bottle Rate: ' + str(self.rate)
    

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



print(Bottle.brand)

# Creating an Object of Bottle Class. i.e Bottle()
# Initializing the instance variable for the Object i.e bottle1.

print("\n")

# color,capacity,height,rate:
bottle1 = Bottle("green",1,10,20)
print("Bottle 1 Memory Location: ", bottle1)
print(bottle1.color)
print(bottle1.capacity)
print (bottle1.height)
print(bottle1.rate)
print("\n")

bottle2 = Bottle("blue",2,20,40)
print("Bottle 2 Memory Location: ", bottle2)
print(bottle2.color, bottle2.capacity, bottle2.height, bottle2.rate, sep="\n")

print("\n")

bottle3 = Bottle("red",3,30,70)
print("Bottle 3 Memory Location: ", bottle3)
print(bottle3.color)
print(bottle3.capacity)
print(bottle3.height)
print(bottle3.rate)

print("\n")



print("Calling Bottle 1 Methods")
bottle1.wash()
bottle1.set_cap()
bottle1.fill()
bottle1.close()

print("\n")
print("Calling Bottle 2 Methods")

bottle2.wash()
bottle2.set_cap()
bottle2.fill()
bottle2.close()

print("\n")
print("Calling Bottle 3 Methods")

bottle3.wash()
bottle3.set_cap()
bottle3.fill()
bottle3.close()


print("\n")
# Calling method using Instance Variable.
print(bottle1.get_bottle_info())

print("\n")
# Calling method using Class Name.
print(Bottle.get_bottle_info(bottle2))
