import unittest
from my_awesome_lib.math_tools import add, multiply, average


class TestMathTools(unittest.TestCase):
    """Testy dla modułu math_tools."""

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)

    def test_average_typical(self):
        self.assertAlmostEqual(average([1, 2, 3, 4]), 2.5)

    def test_average_single(self):
        self.assertEqual(average([10]), 10)

    def test_average_empty_list(self):
        with self.assertRaises(ValueError):
            average([])


if __name__ == "__main__":
    unittest.main()
