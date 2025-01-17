#OOPS

# First Class is derived from the parent called "Object".
class Bottle(object):
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



    # # Destructor is called when objects are destroyed.
    # # Python handles the descructor automatically.No need to call it explicitly.
    # def __del__(self):
    #     print('Destructor is called')

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
print(bottle2.color)
print(bottle2.capacity)
print(bottle2.height)
print(bottle2.rate)

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


print("=====Child Class Creation=====")

# Inheritance
# Child Class is inheriting the properties and methods of Parent Class.

class SteelBottle(Bottle):
    '''
    This is a SteelBottle Class.
    '''
    # Static Variables - Properties
    brand="Milton"
    material="Steel"

    # Sending data from chold class to parent class
    def __init__(self,color,capacity,height,rate):
        '''
        Child Class Constructor
        Sending data from chold class to parent class.
        '''
        Bottle.__init__(self,color,capacity,height,rate)

        # When we give Super(), no need to give self.
        super().__init__(color,capacity,height,rate)    
        print('SteelBottle Child Constructor is called')


    def drink_morning_water(self):
        '''
        This is drinkMorningWater method.
        '''
        print("Drinking Morning Water")

print(SteelBottle.brand)
print(SteelBottle.material)



steelBottle1 = SteelBottle(capacity=1,color="silver",height=10,rate=100)
print(steelBottle1.color)
steelBottle1.wash()
steelBottle1.set_cap()
steelBottle1.fill()
steelBottle1.drink_morning_water()
steelBottle1.close()

print("\n")

# To Know the Parent Class of the Child Class

print("=====Parent Class of Child Class=====")

print(SteelBottle.__bases__)
print(Bottle.__bases__)
print(steelBottle1.__class__.__bases__)
print(bottle1.__class__.__bases__)
print(bottle2.__class__.__bases__)
print(bottle3.__class__.__bases__) 
