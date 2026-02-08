import re
from datetime import datetime

def is_valid_email(email):
    """Sprawdza poprawność adresu e-mail."""
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))


def area_of_circle(r):
    """Zwraca pole koła o promieniu r."""
    if r < 0:
        raise ValueError("Promień nie może być ujemny")
    return 3.14159 * r * r


def filter_even(numbers):
    """Zwraca listę liczb parzystych."""
    return [n for n in numbers if isinstance(n, int) and n % 2 == 0]


def convert_date(date_str):
    """Konwertuje format YYYY-MM-DD na DD.MM.YYYY."""
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        return date.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Niepoprawny format daty")


def is_palindrome(text):
    """Sprawdza, czy tekst jest palindromem."""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
