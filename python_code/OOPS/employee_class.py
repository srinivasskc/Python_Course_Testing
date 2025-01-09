'''
Creating a Class.
Class will allow to create our own data types using a class.
Built In Data Types: Int, Float, Str, Bool, list.

This is a placeholder class. 
Class Name starts with Capital Letter and with Colon
If we want to create a class with empty, we write "pass"

Student() is the object of Student Class.
Both Names should be same.
student1 and student2 are instance variables assigned with Student object.
'''

class Student:
    '''
    This is student's class information
    '''
    pass




student1 = Student()
student2 = Student()

print(student1)
print(student2)

# This prints the memory location of student1 and student2
print(isinstance(student1,Student))
print(isinstance(student2,Student))

