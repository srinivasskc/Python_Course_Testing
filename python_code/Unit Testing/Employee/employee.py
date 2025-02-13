"""
Employee Class.
"""
class Employee:
    """
    Employee Class
    """

    bonus = 1.05

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    @property
    def email(self):
        """
        Returns Email.
        """
        return f'{self.first}.{self.last}@email.com'
        
    @property    
    def fullname(self):
        """
        Returns Full Name.
        """
        return f'{self.first} {self.last}'

    
    def add_bonus(self):
        """
        Add bonus to salary
        """
        self.salary = int(self.salary * self.bonus)
