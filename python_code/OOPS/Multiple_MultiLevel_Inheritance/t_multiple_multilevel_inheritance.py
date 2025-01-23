
class Employee:
    '''
    Employee Class Information
    '''
    # Static Variables - Properties
    bonus=10000
    total_employee=0

    def __init__(self, name, emp_num, salary):
        """
        Constructor Method
        """
        self.name=name
        self.emp_num=emp_num
        self.salary=salary

    def get_employee_info(self):
        """
        Get Employee Details Method.
        """
        return "Employee Name: "+self.name+"\nEmployee Number: "+str(self.emp_num)+"\nEmployee Salary: "+str(self.salary)
    
    
    def bonus_to_employee(self):
        """
        Get Bonus to Employee Method.
        """
        salary_with_bonus=self.salary+self.bonus
        return "Employee Name: "+self.name+"\n Employee Salary with Bonus: "+str(salary_with_bonus)
    
    def _del__(self):
        """
        Destructor Method.
        """
        print("Destructor is called")


empl1 = Employee("Srinivas", 101, 10000)
empl2 = Employee("Kadiyala", 102, 20000)

print(empl1.get_employee_info())
print(empl2.get_employee_info())
print(empl1.bonus_to_employee())
print(empl2.bonus_to_employee())

# Child Class
class Developer(Employee):
    """
    Developer Class Information
    """
    def __init__(self, name, emp_num, salary, language):
        self.language=language
        # Calling Parent Class Constructor
        super().__init__(name, emp_num, salary)

    def develop_applications(self):
        """
        Developer Method
        """
        return "Employee Develops Applications"


print("\n")
# Is Sub Class -- Check if Developer class is sub class of Employee Class
print("Is Developer Sub Class of Employee: ",issubclass(Developer, Employee))

dev_emp1 = Developer("Suresh", 103, 15000, "Python")
dev_emp2 = Developer("Ramesh", 104, 25000, "Java")

print("\n")
print("Developer Class Information")
print("===========================")

print(dev_emp1.get_employee_info())
print(dev_emp2.get_employee_info())
print(dev_emp1.bonus_to_employee())
print(dev_emp2.bonus_to_employee())

print("Employee ",dev_emp1.name," is working on ",dev_emp1.language)
print("Employee ",dev_emp2.name," is working on ",dev_emp2.language)

print(dev_emp1.develop_applications())
print(dev_emp2.develop_applications())


class Tester(Employee):
    """
    Tester Class Information
    """
    def __init__(self, name, emp_num, salary, tool):
        self.tool=tool
        # Calling Parent Class Constructor
        Employee.__init__(self, name, emp_num, salary)

    def tester_applications(self):
        """
        Tester Method
        """
        return "Employee Tests Applications"
    

print("\n")
# Is Sub Class -- Check if Developer class is sub class of Employee Class
print("Is Tester Sub Class of Employee: ",issubclass(Tester, Employee))

test_emp1 = Tester("Vamsi", 105, 6000, "Postman")
test_emp2 = Tester("Krishna", 106, 8500, "Java")

print("\n")
print("Tester Class Information")
print("===========================")

print(test_emp1.get_employee_info())
print(test_emp2.get_employee_info())
print(test_emp1.bonus_to_employee())
print(test_emp2.bonus_to_employee())

print("Employee ",test_emp1.name," is working on ",test_emp1.tool)

print("Employee ",test_emp2.name," is working on ",test_emp2.tool)

print(test_emp1.tester_applications())
print(test_emp2.tester_applications())



class AutomationTester(Tester,Developer):
    """
    Automation Tester Class Information
    """
    def __init__(self, name, emp_num, salary, language,tool):
        # Calling Parent Class Constructor
        Developer.__init__(self,name, emp_num, salary,language)
        super().__init__(name, emp_num, salary,tool)
   
    def automation_tester(self):
        """
        Automation Tester Method
        """
        return "Employee Automates Testing"


print("\n")
print("===Method Resolution Order===")
# Method Resolution Order.
print("AutomationTester.mro():",AutomationTester.mro())
print("Tester.mro():",Tester.mro())
print("Developer.mro():",Developer.mro())

print("\n")

print("===calling parent and child methods from child===")
auteng1 = AutomationTester("Srinivas", 107, 20000, "Python","Selenium")


print("Automation Srinivas: ",auteng1.develop_applications())
print("Automation Srinivas: ",auteng1.tester_applications())
print("Automation Srinivas: ",auteng1.automation_tester())


print("\n")

# Method Resolution Order using Help
print(help(AutomationTester))
