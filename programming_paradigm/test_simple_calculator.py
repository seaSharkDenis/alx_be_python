from simple_calculator import SimpleCalculator
import unittest

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test"""
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertRaises(TypeError, self.calc.add,'f', 0)
        self.assertRaises(TypeError, self.calc.add,' ', 34)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 10), 0)
        self.assertEqual(self.calc.subtract(0, 10), -10)
        self.assertRaises(TypeError, self.calc.subtract,'f', 0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(10, 53), 530)
        self.assertEqual(self.calc.multiply(256, 0), 0)
        self.assertEqual(self.calc.multiply(90, 5), 450)
        self.assertEqual(self.calc.multiply(6, "h"), "hhhhhh")

    def test_division(self):
        self.assertEqual(self.calc.divide(5, 1), 5)
        self.assertEqual(self.calc.divide(200, 10), 20)
        self.assertEqual(self.calc.divide(20, 5), 4)