import os
import json
import unittest
from my_awesome_lib.data_utils import load_json, save_json, flatten_list


class TestDataUtils(unittest.TestCase):
    """Testy dla modułu data_utils."""

    def setUp(self):
        self.test_file = "test_data.json"
        self.sample_data = {"name": "Karol", "age": 25}

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_load_json(self):
        """Sprawdza zapis i odczyt JSON."""
        save_json(self.test_file, self.sample_data)
        loaded = load_json(self.test_file)
        self.assertEqual(loaded, self.sample_data)

    def test_load_json_file_not_found(self):
        """Sprawdza reakcję na brak pliku."""
        with self.assertRaises(FileNotFoundError):
            load_json("nie_istnieje.json")

    def test_flatten_list(self):
        """Sprawdza spłaszczanie listy list."""
        nested = [[1, 2], [3, 4], [], [5]]
        self.assertEqual(flatten_list(nested), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()

