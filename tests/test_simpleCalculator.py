import unittest
import src.simpleCalculator

class MyTestCase(unittest.TestCase):

    def test_add(self):
        assert src.simpleCalculator.add(7, 3) == 10
        assert src.simpleCalculator.add(7, 4) == 11

    def test_sub(self):
        assert src.simpleCalculator.substract(7, 3) == 4
        assert src.simpleCalculator.substract(14, 3) == 11

class MyTestCase2(unittest.TestCase):

    def test_multiply(self):
        assert src.simpleCalculator.multiply(3,3) == 9
        assert src.simpleCalculator.multiply(12,2) == 24

    def test_sub(self):
        assert src.simpleCalculator.substract(7, 3) == 4
        assert src.simpleCalculator.substract(14, 3) == 11

# How to write Unit test cases
# AAA Model
# Arrange - Setting up of all the prereq required for the test to run
# Act - Run the actual code under test
# Assert - Verify weather code is indeed running as expected

# Example of AAA Unit test

def sum(a,b):
    return a+b
class Sumtest(unittest.TestCase):
    def test_sumtest(self):
        #Arrange
        a= 10
        b= 20
        #ACT
        result = sum(a,b)
        #Assert
        self.assertEqual(result, a+b)
        self.assertEqual(result, b+a)

# unitest framework provides functional called setup() which will be called
# for each and every test function written in a test class.
#similarly we can also use tearDown() function

class Sumtest2(unittest.TestCase):
    def setUp(self):
        print("setUp called")
        self.a = 10
        self.b = 20
        self.c = 0

    def tearDown(self):
        print("tearDown called")
        self.a = 0
        self.b = 0

    def test_sumtest(self):
        #Arrange is already done in Setup
        #Act
        result = sum(self.a,self.b)
        #Assert
        self.assertEqual(result, self.a + self.b +self.c)

    def test_sentest_rev(self):
        #Arrange is already done in Setup
        #Act
        result = sum(self.b,self.a)
        #Assert
        self.assertEqual(result, self.a + self.b)

#define a class
class CalculatorTest(unittest.TestCase):

    # test case for checking non prime nums
    def test_nonprime(self):
        self.assertEqual(src.simpleCalculator.prime(12), False)

    # test case to check prime nums
    def test_prime(self):
        self.assertEqual(src.simpleCalculator.prime(19), True)

    # test case to check invalid input
    def test_invalid(self):
        self.assertEqual(src.simpleCalculator.prime(-1), False)

if __name__ == '__main__':
    unittest.main()
