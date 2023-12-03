"""
Caroline Su
A01369603
"""
from unittest import TestCase
from character import move_character


class Test(TestCase):
    def test_move_north(self):
        expect = {'X-coordinate': 2, 'Y-coordinate': 0, 'HP': 10, 'Max HP': 10, 'EX': 0, 'Level': 1, 'key': False}
        character = {'X-coordinate': 2, 'Y-coordinate': 1, 'HP': 10, 'Max HP': 10, 'EX': 0, 'Level': 1, 'key': False}
        direction = "N"
        move_character(character, direction)
        self.assertEqual(expect, character)

    def test_move_south(self):
        expect = {'X-coordinate': 3, 'Y-coordinate': 4, 'HP': 7, 'Max HP': 10, 'EX': 3, 'Level': 1, 'key': False}
        character = {'X-coordinate': 3, 'Y-coordinate': 3, 'HP': 7, 'Max HP': 10, 'EX': 3, 'Level': 1, 'key': False}
        direction = "S"
        move_character(character, direction)
        self.assertEqual(expect, character)

    def test_move_west(self):
        expect = {'X-coordinate': 0, 'Y-coordinate': 3, 'HP': 5, 'Max HP': 10, 'EX': 0, 'Level': 1, 'key': False}
        character = {'X-coordinate': 1, 'Y-coordinate': 3, 'HP': 5, 'Max HP': 10, 'EX': 0, 'Level': 1, 'key': False}
        direction = "W"
        move_character(character, direction)
        self.assertEqual(expect, character)

    def test_move_east(self):
        expect = {'X-coordinate': 4, 'Y-coordinate': 1, 'HP': 10, 'Max HP': 10, 'EX': 0, 'Level': 1, 'key': True}
        character = {'X-coordinate': 3, 'Y-coordinate': 1, 'HP': 10, 'Max HP': 10, 'EX': 0, 'Level': 1, 'key': True}
        direction = "E"
        move_character(character, direction)
        self.assertEqual(expect, character)
