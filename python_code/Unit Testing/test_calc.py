
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
        
    
    def test_add(self):
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
        result = calc.div(10,5)
        self.assertEqual(result,2)

    
    def test_mod(self):
        """
        Test Case for Modulus
        """
        result = calc.mod(10,5)
        self.assertEqual(result,0)


# Loads the test cases from test class using Test Loader to Suite.
suite = unittest.TestLoader().loadTestsFromTestCase(TestCalc)

unittest.TextTestRunner(verbosity=2).run(suite)
