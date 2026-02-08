import re
from datetime import datetime


def is_valid_email(email):
    """
    Sprawdza poprawność adresu e-mail.
    Zwraca True dla poprawnych adresów, False dla niepoprawnych.
    """
    if not isinstance(email, str):
        return False
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))


def area_of_circle(r):
    """
    Zwraca pole koła o promieniu r.
    Dla r < 0 rzuca ValueError.
    """
    if not isinstance(r, (int, float)):
        raise TypeError("Promień musi być liczbą")
    if r < 0:
        raise ValueError("Promień nie może być ujemny")
    return 3.14159 * r * r


def filter_even(numbers):
    """
    Zwraca listę liczb parzystych z podanej listy.
    Ignoruje elementy, które nie są liczbami całkowitymi.
    """
    if numbers is None:
        return []
    return [n for n in numbers if isinstance(n, int) and n % 2 == 0]


def convert_date(date_str):
    """
    Konwertuje format daty z YYYY-MM-DD na DD.MM.YYYY.
    Dla niepoprawnego formatu rzuca ValueError.
    """
    if not isinstance(date_str, str):
        raise TypeError("Data musi być napisem (str)")
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        return date.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Niepoprawny format daty, oczekiwano YYYY-MM-DD")


def is_palindrome(text):
    """
    Sprawdza, czy tekst jest palindromem.
    Ignoruje spacje i wielkość liter.
    """
    if not isinstance(text, str):
        return False
    cleaned = "".join(ch.lower() for ch in text if not ch.isspace())
    return cleaned == cleaned[::-1]
