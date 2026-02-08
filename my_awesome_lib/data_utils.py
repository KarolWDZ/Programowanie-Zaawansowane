"""
Moduł data_utils zawiera funkcje do pracy z danymi,
takimi jak pliki JSON oraz listy.
"""

import json
from typing import Any, List


def load_json(path: str) -> Any:
    """
    Wczytuje dane z pliku JSON.

    :param path: Ścieżka do pliku JSON.
    :return: Dane wczytane z pliku.
    :raises FileNotFoundError: Jeśli plik nie istnieje.
    :raises json.JSONDecodeError: Jeśli plik nie zawiera poprawnego JSON-a.
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: str, data: Any) -> None:
    """
    Zapisuje dane do pliku JSON.

    :param path: Ścieżka do pliku wyjściowego.
    :param data: Dane do zapisania (obiekt serializowalny do JSON).
    """
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def flatten_list(nested_list: List[list]) -> list:
    """
    Spłaszcza listę list do jednej listy.

    :param nested_list: Lista zawierająca listy.
    :return: Jedna lista z wszystkimi elementami.
    """
    result = []
    for sub in nested_list:
        result.extend(sub)
    return result
