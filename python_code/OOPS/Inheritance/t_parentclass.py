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