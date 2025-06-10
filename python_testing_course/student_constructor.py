class Student:
    def __init__(self,name, age=None, grade=None):
        self.name = name
        self.age = age
        self.grade = grade


my_student1  = Student("Srinivas")
# Python automatically adds provides a default constructor (__init__) method to the class.

my_student2 = Student("Kadiyala", 25, 'A')
# Providing all values including the optional value.

my_student3 = Student("Vasishta", grade="Sr")
# Provided grade="Sr", if we didnt provide grade = , it would consider sr for Age and not for grade.

my_student4 = Student("Srinivas", 36)
# Now 25 is considered as age.

my_student5 = Student("Srinivas", age=36, grade='A')
# Providing age and grade as keyword arguments.




