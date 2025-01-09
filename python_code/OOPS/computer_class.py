'''
Class contains variables and methods.
variables = attributes (properties)
methods = functions (behaviour)
'''


class Computer:
    '''
    This is a Computer Class.
    '''
    def config(self):
        '''
        This is the configuration of the computer.
        '''
        print("i5, 16GB, 1TB")


com1 = Computer()
com2 = Computer()
# print(type(com1))

# Class -> Object Methods -> Object
Computer.config(com1)
Computer.config(com2)

# Object -> Class Methods
com1.config()
com2.config()
