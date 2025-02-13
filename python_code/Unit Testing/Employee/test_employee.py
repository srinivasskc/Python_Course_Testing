"""
Unit testing
"""

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    '''
    This is unit test case for Employee Program
    '''
    def test_email(self):
        '''
        Testing the email.
        '''
        emp1 = Employee('Srinivas','Kadiyala', 20000)
        emp2 = Employee('Rajesh','Khanna',50000)

        self.assertEqual(emp1.email,'Srinivas.Kadiyala@email.com')
        self.assertEqual(emp2.email,'Rajesh.Khanna@email.com')

        emp1.first = 'Vasishta'
        emp2.first = 'Dimple'

        self.assertEqual(emp1.email,'Vasishta.Kadiyala@email.com')
        self.assertEqual(emp2.email,'Dimple.Khanna@email.com')


    def test_fullname(self):
        '''
        Testing the Full Name.
        '''
        emp1 = Employee('Srinivas','Kadiyala', 20000)
        emp2 = Employee('Rajesh','Khanna',50000)

        self.assertEqual(emp1.fullname,'Srinivas Kadiyala')
        self.assertEqual(emp2.fullname,'Rajesh Khanna')

        emp1.first = 'Vasishta'
        emp2.first = 'Vinod'

        self.assertEqual(emp1.fullname,'Vasishta Kadiyala')
        self.assertEqual(emp2.fullname,'Vinod Khanna')

    def test_add_bonus(self):
        '''
        Testing the Add Bonus.
        '''
        emp1 = Employee('Srinivas','Kadiyala', 20000)
        emp2 = Employee('Rajesh','Khanna',50000)

        emp1.add_bonus()
        emp2.add_bonus()

        self.assertEqual(emp1.salary,21000)
        self.assertEqual(emp2.salary,52500)


# Loads the test cases from test class using Test Loader to Suite.
suite = unittest.TestLoader().loadTestsFromTestCase(TestEmployee)

unittest.TextTestRunner(verbosity=2).run(suite)

