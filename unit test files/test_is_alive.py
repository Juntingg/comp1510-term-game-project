"""
Caroline Su
A01369603
"""
from unittest import TestCase
from battle import is_alive


class Test(TestCase):
    def test_positive_HP(self):
        new_character = {"X-coordinate": 1, "Y-coordinate": 1, "HP": 3}
        actual = is_alive(new_character)
        self.assertTrue(actual)

    def test_negative_HP(self):
        new_character = {"X-coordinate": 1, "Y-coordinate": 1, "HP": -2}
        actual = is_alive(new_character)
        self.assertFalse(actual)

    def test_zero_HP(self):
        new_character = {"X-coordinate": 1, "Y-coordinate": 1, "HP": 0}
        actual = is_alive(new_character)
        self.assertFalse(actual)
