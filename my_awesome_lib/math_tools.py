"""
Moduł math_tools zawiera proste funkcje matematyczne.
"""

from typing import List


def add(a: float, b: float) -> float:
    """
    Zwraca sumę dwóch liczb.

    :param a: Pierwsza liczba.
    :param b: Druga liczba.
    :return: Suma a + b.
    """
    return a + b


def multiply(a: float, b: float) -> float:
    """
    Zwraca iloczyn dwóch liczb.

    :param a: Pierwsza liczba.
    :param b: Druga liczba.
    :return: Iloczyn a * b.
    """
    return a * b


def average(numbers: List[float]) -> float:
    """
    Zwraca średnią arytmetyczną z listy liczb.

    :param numbers: Lista liczb.
    :return: Średnia arytmetyczna.
    :raises ValueError: Jeśli lista jest pusta.
    """
    if not numbers:
        raise ValueError("Lista liczb nie może być pusta")
    return sum(numbers) / len(numbers)
