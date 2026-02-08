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
        self.valid_emails = [
            "test@example.com",
            "user.name@domain.co",
            "user-name@sub.domain.org",
        ]
        self.invalid_emails = [
            "testexample.com",
            "user@",
            "@domain.com",
            "user@domain",
            "",
            None,
        ]
        self.sample_numbers = [1, 2, 3, 4, 5, 6, 0, -2, -3]
        self.palindromes = [
            "level",
            "Racecar",
            "nurses run",
            "Kobyła ma mały bok",
        ]
        self.not_palindromes = [
            "python",
            "hello",
            "palindrome",
        ]

    def test_valid_emails(self):
        for email in self.valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email))

    def test_invalid_emails(self):
        for email in self.invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))

    # --- TESTY POLA KOŁA ---
    def test_area_of_circle_positive(self):
        self.assertAlmostEqual(area_of_circle(2), 12.56636, places=5)

    def test_area_of_circle_zero(self):
        self.assertEqual(area_of_circle(0), 0)

    def test_area_of_circle_negative(self):
        with self.assertRaises(ValueError):
            area_of_circle(-1)

    def test_area_of_circle_wrong_type(self):
        with self.assertRaises(TypeError):
            area_of_circle("abc")

    def test_filter_even_typical(self):
        self.assertEqual(filter_even(self.sample_numbers), [2, 4, 6, 0, -2])

    def test_filter_even_empty_list(self):
        self.assertEqual(filter_even([]), [])

    def test_filter_even_none(self):
        self.assertEqual(filter_even(None), [])

    def test_filter_even_mixed_types(self):
        data = [1, "a", 2, 3.5, 4, None, True]
        self.assertEqual(filter_even(data), [2, 4])

    def test_convert_date_valid(self):
        self.assertEqual(convert_date("2024-01-15"), "15.01.2024")

    def test_convert_date_invalid_format(self):
        with self.assertRaises(ValueError):
            convert_date("15-01-2024")

    def test_convert_date_wrong_type(self):
        with self.assertRaises(TypeError):
            convert_date(20240115)

    def test_palindromes(self):
        for text in self.palindromes:
            with self.subTest(text=text):
                self.assertTrue(is_palindrome(text))

    def test_not_palindromes(self):
        for text in self.not_palindromes:
            with self.subTest(text=text):
                self.assertFalse(is_palindrome(text))

    def test_palindrome_wrong_type(self):
        self.assertFalse(is_palindrome(12345))


if __name__ == "__main__":
    unittest.main()
