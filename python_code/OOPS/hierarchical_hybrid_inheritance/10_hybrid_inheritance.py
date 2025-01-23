# Hybrid Inheritance
'''
This is a Hybrid Inheritance consists of Single, Multiple, Multi Level and Hierarchical Inheritance.
'''

class Class1:
    '''
    This is Class 1
    '''
    class_name = "1st Class"


    def join_class1(self):
        '''
        This is Join Method
        '''
        print("Joining Class 1")


cls1 = Class1()

cls1.join_class1()
print(Class1.class_name)

print("\n")

class Class2(Class1):
    '''
    This is Class 2 with Parent Child Inheritance with Class1
    '''
    class_name = "2nd Class"


    def join_class2(self):
        '''
        This is Join Method
        '''
        print("Joining Class 2")

class Class3(Class1):
    '''
    This is Class 3 with Hierarchical Inheritance with Class1
    '''
    class_name = "3rd Class"


    def join_class3(self):
        '''
        This is Join Method
        '''
        print("Joining Class 3")

class Class4(Class3):
    '''
    This is Class 4 with Multi Level Inheritance with Class3 
    '''
    class_name = "4th Class"


    def join_class4(self):
        '''
        This is Join Method
        '''
        print("Joining Class 4")

class Class5(Class2,Class3):
    '''
    This is Class 5 with Multiple Inheritance with Class2 and Class3
    '''
    class_name = "5th Class"


    def join_class5(self):
        '''
        This is Join Method
        '''
        print("Joining Class 5")

cls2 = Class2()
cls3 = Class3()
cls4 = Class4()
cls5 = Class5()

# Parent - Class1, Child - Class2
cls2.join_class1()
cls2.join_class2()
print(Class2.class_name)

print("\n")

# Hierarchical Inheritance - Parent - Class1, Child - Class3
cls3.join_class1()
cls3.join_class3()
print(Class3.class_name)

print("\n")

# Multi Level Inheritance - Parent - Class3, Child - Class4 and Parent of Class3 is Class1
cls4.join_class1()
cls4.join_class3()
cls4.join_class4() 
print(Class4.class_name)

print("\n")

# Multiple Inheritance - Parent - Class2, Class3, Child - Class5 and Parent of Class2 is Class1 and Parent of Class3 is Class1
cls5.join_class1()
cls5.join_class2()
cls5.join_class3()
cls5.join_class5()
print(Class5.class_name)
