import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-3, -4), -7)
    
    def test_subtract(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(-4, 7), -11)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(10, 4), 40)
        self.assertEqual(self.calc.multiply(-4, 7), -28)
        self.assertEqual(self.calc.multiply(-4, -7), 28)
        self.assertEqual(self.calc.multiply(0, 2), 0)

    def test_division(self):
        """Test the division method."""
        self.assertAlmostEqual(self.calc.divide(10, 5), 2)
        self.assertAlmostEqual(self.calc.divide(5, 9), 0.555)
        self.assertAlmostEqual(self.calc.divide(5, 0), 0.0)