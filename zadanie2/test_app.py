import unittest
from app import (
    is_valid_email,
    area_of_circle,
    filter_even,
    convert_date,
    is_palindrome
)

class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.sample_numbers = [1, 2, 3, 4, 5, 6]

    # --- TESTY EMAILA ---
    def test_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))

    def test_invalid_email_no_at(self):
        self.assertFalse(is_valid_email("testexample.com"))

    def test_invalid_email_no_domain(self):
        self.assertFalse(is_valid_email("test@"))

    # --- TESTY POLA KOŁA ---
    def test_area_of_circle(self):
        self.assertAlmostEqual(area_of_circle(2), 12.56636)

    def test_area_zero(self):
        self.assertEqual(area_of_circle(0), 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area_of_circle(-5)

    # --- TESTY FILTROWANIA PARZYSTYCH ---
    def test_filter_even(self):
        self.assertEqual(filter_even(self.sample_numbers), [2, 4, 6])

    def test_filter_even_empty(self):
        self.assertEqual(filter_even([]), [])

    def test_filter_even_mixed_types(self):
        self.assertEqual(filter_even([1, "a", 2, 3.5, 4]), [2, 4])

    # --- TESTY KONWERSJI DATY ---
    def test_convert_date(self):
        self.assertEqual(convert_date("2024-01-15"), "15.01.2024")

    def test_convert_date_invalid(self):
        with self.assertRaises(ValueError):
            convert_date("15-01-2024")

    def test_convert_date_wrong_format(self):
        with self.assertRaises(ValueError):
            convert_date("2024/01/15")

    # --- TESTY PALINDROMU ---
    def test_palindrome_simple(self):
        self.assertTrue(is_palindrome("level"))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("nurses run"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("python"))


if __name__ == "__main__":
    unittest.main()
