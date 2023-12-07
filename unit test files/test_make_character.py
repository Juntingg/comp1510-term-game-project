"""
Caroline Su
A01369603
"""
from unittest import TestCase
from character import make_character


class Test(TestCase):
    def test_make_new_character(self):
        expect = {'EX': 0, 'HP': 10, 'Level': 1, 'Max HP': 10, 'X-coordinate': 0, 'Y-coordinate': 0, 'key': False}
        actual = make_character()
        self.assertEqual(expect, actual)
