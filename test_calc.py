import unittest
import Calc as calc
import security_check as sc
#  https://docs.python.org/3.10/library/unittest.html#unittest.TestCase.assertEqual


class CalculatorTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(4, calc.addition(3, 1))  # add assertion here

    def test_subtraction(self):
        self.assertEqual(5, calc.subtraction(10,5))

    def test_division(self):
        self.assertEqual(2, calc.division(10,5))

    def test_multiplication(self):
        self.assertEqual(50, calc.multiplication(10,5))

    def test_security(self):
        self.assertEqual(False, sc.main())


if __name__ == '__main__':
    unittest.main()
