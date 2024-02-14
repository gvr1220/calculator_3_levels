import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(Calculator.divide(6, 3), 2)

if __name__ == '__main__':
    unittest.main()
