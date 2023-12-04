"""
Caroline Su
A01369603
"""
from unittest import TestCase
from event import check_reach_level_3


class Test(TestCase):
    def test_character_reach_level_3(self):
        my_char = {'Name': 'Joy', 'HP': 10, 'Max HP': 10, 'EX': 0, 'Level': 3}
        actual = check_reach_level_3(my_char)
        self.assertTrue(actual)

    def test_character_not_reach_level_3(self):
        my_char = {'Name': 'Joy', 'HP': 10, 'Max HP': 10, 'EX': 0, 'Level': 2}
        actual = check_reach_level_3(my_char)
        self.assertFalse(actual)
