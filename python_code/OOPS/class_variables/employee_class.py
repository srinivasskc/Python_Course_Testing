class Employee:
    '''
    Employee Information
    '''

    # Static Variable
    bonus=10000

    def __init__(self,name,age,salary):
        '''
        This is a Parameterized Constructor.
        '''
        # Instance Variables
        self.name=name
        self.age=age
        self.salary=salary

    def get_employee_info(self):
        '''
        This is get_employee_info method.
        '''
        return 'Employee Name: ' + self.name + '\n' + 'Employee Age: ' + str(self.age) + '\n' + 'Employee Salary: ' + str(self.salary)
    

    def add_bonus_to_salary(self):
        '''
        This is add_bonus_to_salary method.
        '''
        salary_bonus=int(self.salary+Employee.bonus)
        return 'Employee Name: ' + self.name + '\n' + 'Employee Salary with Bonus: ' + str(salary_bonus) + '\n'
    
    

emp1 = Employee('John',25,25000)
emp2 = Employee('Smith',30,30000)

# Accessing the class variables.
print("Employee Bonus: ",Employee.bonus)
Employee.bonus=20000  # Changing the class variable value of bonus
print("Employee1 details with bonus: ",emp1.name,emp1.salary,emp1.bonus)
print("Employee2 details with bonus: ",emp2.name,emp2.salary,emp2.bonus)

# Dictionary: empl1 and empl2.
print("Employee 1 Dictionary: ",emp1.__dict__)
print("Employee 2 Dictionary: ",emp2.__dict__)

emp1.add_bonus_to_salary()

# Bonus values for emp1 and emp2 are coming from class variable. And we can change for emp2 as well.
emp2.bonus=30000
print("After bonus updated to emp2: ",emp2.name,emp2.salary,emp2.bonus)
print("Employee 2 Dictionary: ",emp2.__dict__)

emp2.add_bonus_to_salary()
