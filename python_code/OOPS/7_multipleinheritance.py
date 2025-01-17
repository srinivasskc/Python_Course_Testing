# Multiple Inheritance

class Class1:
    '''
    This is Class 1
    '''
    def join(self):
        '''
        This is Join Method
        '''
        print("Joining Class 1")

class Class2:
    '''
    This is Class 2
    '''
    def subscribe(self):
        '''
        This is Subscribe Method
        '''
        print("Subscribe Class 2")

class Class3(Class1, Class2):
    '''
    This is Class 3 inheriting Class1, Class2
    '''
    def like(self):
        '''
        This is Like Method
        '''
        print("Like Class 3")

class Class4(Class3):
    '''
    This is Class4 inheriting Class3. and Class3 is inheriting Class1, Class2
    '''
    def share(self):
        '''
        This is Share Method
        '''
        print("Share Class 4")

cls4 = Class4()
cls4.join()
cls4.subscribe()
cls4.like()
cls4.share()
