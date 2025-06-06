
"""
Test file should start with test or end with test in file name.
"""

import unittest
import calc

class TestCalc(unittest.TestCase):
    """
    Created test class and importing unit test.
    """

    def test_add(self):
        """
        Test Case for Addition
        """
        result = calc.add(10,5)
        self.assertEqual(result,15)

        self.assertEqual(calc.add(10,5),14)
        self.assertEqual(calc.add(-1,5),4)
        self.assertEqual(calc.add(0,0),0)
        self.assertEqual(calc.add(-2,0),-2)
        self.assertEqual(calc.add(-2,2),0)
        
    
    def test_addition(self):
        """
        Test Case for Addition
        """
        result = calc.add(10,5)
        self.assertEqual(result,15)



    def test_sub(self):
        """
        Test Case for Subtraction
        """
        result = calc.sub(10,5)
        self.assertEqual(result,5)



    def test_multi(self):
        """
        Test Case for Multiplication
        """
        result = calc.multi(10,5)
        self.assertEqual(result,50)


    def test_div(self):
        """
        Test Case for Division
        """
        result = calc.div(10,2)
        self.assertEqual(result,5)

        self.assertEqual(calc.div(-2,2),-1)
        self.assertEqual(calc.div(10,2),5)

        # This is special method for exception check
        self.assertRaises(ZeroDivisionError,calc.div,10,0)
        
        # Context Manager way of method
        with self.assertRaises(ZeroDivisionError):
            calc.div(10,0)
    
    def test_mod(self):
        """
        Test Case for Modulus
        """
        result = calc.mod(10,5)
        self.assertEqual(result,0)

    def test_floordiv(self):
        """
        Test Case for Floor Division
        """
        self.assertEqual(calc.floor_div(5,2),2.5)

# Loads the test cases from test class using Test Loader to Suite.
suite = unittest.TestLoader().loadTestsFromTestCase(TestCalc)

unittest.TextTestRunner(verbosity=2).run(suite)
