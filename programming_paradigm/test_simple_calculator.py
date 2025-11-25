import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with positive, negative and zero inputs."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-3, -4), -7)
        self.assertEqual(self.calc.add(10, 0), 10)
    
    def test_subtraction(self):
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
        """Test the division method, including float and division by zero."""
        self.assertEqual(self.calc.divide(10, 5), 2.0, places=4)
        self.assertAlmostEqual(self.calc.divide(5, 9), 5/9, places=4)
        # Test division by zero: returns None
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertAlmostEqual(self.calc.divide(12, 3), 4.0, places=4)

# Test runner Entry point
if __name__ == "__main__":
    unittest.main()