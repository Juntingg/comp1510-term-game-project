"""
Caroline Su
A01369603
"""
from unittest import TestCase
from character import is_arrived_castle


class Test(TestCase):
    def test_character_arrive_castle(self):
        character = {'X-coordinate': 4, 'Y-coordinate': 4, 'HP': 10, 'Max HP': 10, 'EX': 0, 'Level': 1, 'key': False}
        rows = 5
        columns = 5
        actual = is_arrived_castle(character, rows, columns)
        self.assertTrue(actual)

    def test_character_not_arrive_castle(self):
        character = {'X-coordinate': 2, 'Y-coordinate': 2, 'HP': 10, 'Max HP': 10, 'EX': 0, 'Level': 1, 'key': False}
        rows = 5
        columns = 5
        actual = is_arrived_castle(character, rows, columns)
        self.assertFalse(actual)
