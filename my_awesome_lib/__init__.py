"""
my_awesome_lib

Prosta biblioteka z funkcjami do pracy z danymi,
tekstem oraz prostymi obliczeniami matematycznymi.
"""

from .data_utils import load_json, save_json, flatten_list
from .math_tools import add, multiply, average
from .text_processing import count_words, remove_punctuation, is_palindrome

__all__ = [
    "load_json",
    "save_json",
    "flatten_list",
    "add",
    "multiply",
    "average",
    "count_words",
    "remove_punctuation",
    "is_palindrome",
]
