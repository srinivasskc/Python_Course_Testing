"""
Unit testing
"""

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    '''
    This is unit test case for Employee Program
    '''

    @classmethod
    def setUpClass(cls):
        print('Setup Class')

    @classmethod
    def tearDownClass(cls):
        print('Tear Down Class')


    def setUp(self):
        '''
        Setup method will run its code before every single test.
        '''
        print('\n')
        print('setup')
        self.emp1 = Employee('Srinivas','Kadiyala', 20000)
        self.emp2 = Employee('Rajesh','Khanna',50000)

    def tearDown(self):
        '''
        TearDown method will run its code after every single test.
        '''
        print('teardown')
        pass


    def test_email(self):
        '''
        Testing the email.
        '''
        print('test email')    
        self.assertEqual(self.emp1.email,'Srinivas.Kadiyala@email.com')
        self.assertEqual(self.emp2.email,'Rajesh.Khanna@email.com')

        self.emp1.first = 'Vasishta'
        self.emp2.first = 'Dimple'

        self.assertEqual(self.emp1.email,'Vasishta.Kadiyala@email.com')
        self.assertEqual(self.emp2.email,'Dimple.Khanna@email.com')

        

    print('\n')

    def test_fullname(self):
        '''
        Testing the Full Name.
        '''
        print('test fullname')
        self.assertEqual(self.emp1.fullname,'Srinivas Kadiyala')
        self.assertEqual(self.emp2.fullname,'Rajesh Khanna')

        self.emp1.first = 'Vasishta'
        self.emp2.first = 'Vinod'

        self.assertEqual(self.emp1.fullname,'Vasishta Kadiyala')
        self.assertEqual(self.emp2.fullname,'Vinod Khanna')

    def test_add_bonus(self):
        '''
        Testing the Add Bonus.
        '''
        print('test add bonus\n')
        self.emp1.add_bonus()
        self.emp2.add_bonus()

        self.assertEqual(self.emp1.salary,21000)
        self.assertEqual(self.emp2.salary,52500)


# Loads the test cases from test class using Test Loader to Suite.
suite = unittest.TestLoader().loadTestsFromTestCase(TestEmployee)

unittest.TextTestRunner(verbosity=2).run(suite)

