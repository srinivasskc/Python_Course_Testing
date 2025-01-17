# Hierarchical Inheritance

class Class1:
    '''
    This is Class 1
    '''
    def join(self):
        '''
        This is Join Method
        '''
        print("Joining Class 1")

class Class2(Class1):
    '''
    This is Class 2 inheriting Class1
    '''
    def subscribe(self):
        '''
        This is Subscribe Method
        '''
        print("Subscribe Class 2")

class Class3(Class1):
    '''
    This is Class 3 inheriting Class1
    '''
    def like(self):
        '''
        This is Like Method
        '''
        print("Like Class 3")


cls2 = Class2()
cls2.join()
cls2.subscribe()

cls3 = Class3()
cls3.join()
cls3.like()
