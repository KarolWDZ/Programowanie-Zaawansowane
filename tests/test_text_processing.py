import unittest
from my_awesome_lib.text_processing import (
    count_words,
    remove_punctuation,
    is_palindrome,
)


class TestTextProcessing(unittest.TestCase):
    """Testy dla modułu text_processing."""

    def test_count_words(self):
        self.assertEqual(count_words("To jest test"), 3)
        self.assertEqual(count_words("  "), 0)

    def test_remove_punctuation(self):
        text = "Hello, world! Jak się masz?"
        result = remove_punctuation(text)
        self.assertNotIn(",", result)
        self.assertNotIn("!", result)
        self.assertNotIn("?", result)

    def test_is_palindrome_true(self):
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("Race car"))
        self.assertTrue(is_palindrome("Kobyła ma mały bok"))

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("to nie jest palindrom"))


if __name__ == "__main__":
    unittest.main()
