"""
Moduł text_processing zawiera funkcje do prostego przetwarzania tekstu.
"""

import string


def count_words(text: str) -> int:
    """
    Zlicza słowa w tekście.

    :param text: Tekst wejściowy.
    :return: Liczba słów.
    """
    if not text.strip():
        return 0
    return len(text.split())


def remove_punctuation(text: str) -> str:
    """
    Usuwa znaki interpunkcyjne z tekstu.

    :param text: Tekst wejściowy.
    :return: Tekst bez znaków interpunkcyjnych.
    """
    table = str.maketrans("", "", string.punctuation)
    return text.translate(table)


def is_palindrome(text: str) -> bool:
    """
    Sprawdza, czy tekst jest palindromem (ignoruje spacje i wielkość liter).

    :param text: Tekst wejściowy.
    :return: True, jeśli tekst jest palindromem, False w przeciwnym razie.
    """
    cleaned = "".join(ch.lower() for ch in text if not ch.isspace())
    return cleaned == cleaned[::-1]
