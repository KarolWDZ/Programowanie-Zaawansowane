my_awesome_lib to prosta biblioteka w języku Python, zawierająca funkcje do pracy z danymi, wykonywania podstawowych obliczeń matematycznych oraz przetwarzania tekstu. Projekt został przygotowany jako ćwiczenie z tworzenia własnych pakietów Python, organizacji modułów, dokumentowania kodu oraz pisania testów jednostkowych.

Struktura projektu:

my_awesome_lib/

folder my_awesome_lib zawiera pliki: init.py, data_utils.py, math_tools.py, text_processing.py

folder tests zawiera pliki: test_data_utils.py, test_math_tools.py, test_text_processing.py

plik README.md

Instalacja:

Aby zainstalować bibliotekę lokalnie w trybie developerskim, należy uruchomić polecenie:
pip install -e .

Uruchamianie testów:

Aby uruchomić wszystkie testy jednostkowe, należy wykonać polecenie:
python -m unittest discover -s tests

Przykłady użycia:

Przykład użycia funkcji is_palindrome z modułu text_processing:
from my_awesome_lib.text_processing import is_palindrome
is_palindrome("Kobyła ma mały bok")

Przykład użycia funkcji average z modułu math_tools:
from my_awesome_lib.math_tools import average
average([1, 2, 3, 4])

Przykład użycia funkcji flatten_list z modułu data_utils:
from my_awesome_lib.data_utils import flatten_list
flatten_list([[1, 2], [3, 4]])

Licencja, autor i wersja:

Autor: Karol Pilitowski
Wersja: 1.0
Licencja: MIT

Cel projektu:

Celem projektu jest stworzenie własnej biblioteki Python, organizacja kodu w moduły i pakiety, dokumentowanie funkcji za pomocą docstringów, pisanie testów jednostkowych oraz publikacja projektu na GitHubie.
