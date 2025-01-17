# Public Access Modifier Encapsulation

class Bottle:
    '''
    This is Bottle Class
    '''
    def __init__(self,color,capacity,height,rate):
        # Public Static Variables.
        self.color = color
        self.capacity = capacity
        self.height = height
        self.rate = rate

    def wash(self):
        '''
        This is Wash Method
        '''
        print("Washing the bottle")
    
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
print(b1.color)
print(b1.capacity)
print(b1.height)
print(b1.rate)
b1.wash()
b1.set_cap()
b1.fill()
b1.close()
