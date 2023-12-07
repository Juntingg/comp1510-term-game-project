"""
Caroline Su
A01369603
"""
from unittest import TestCase
from unittest.mock import patch
from game import make_board


class Test(TestCase):
    @patch("random.choice", side_effect=["mushroom", "mushroom", "mushroom", "wolf", "wolf", "wolf",
                                         "wooden chest", "wooden chest", "wooden chest"])
    @patch("random.randint", return_value=1)
    @patch("random.randint", return_value=1)
    def test_3x3_board(self, _, __, ___):
        expect = {(0, 0): 'begin', (0, 1): 'mushroom', (0, 2): 'mushroom', (1, 0): 'wolf',
                  (1, 1): 'hole', (1, 2): 'wolf', (2, 0): 'wooden chest', (2, 1): 'wooden chest', (2, 2): 'castle'}
        rows = 3
        columns = 3
        my_character = {'EX': 0, 'HP': 0, 'Max HP': 15}
        new_board = make_board(rows, columns, my_character)
        self.assertEqual(expect, new_board)

    @patch("random.choice", side_effect=["mushroom", "mushroom", "mushroom", "wolf", "wolf", "wolf",
                                         "wooden chest", "wooden chest", "wooden chest"])
    @patch("random.randint", return_value=1)
    @patch("random.randint", return_value=1)
    def test_character_gain_hole_attribute(self, _, __, ___):
        expect_char = {'EX': 0, 'HP': 0, 'Max HP': 15, "hole": (1, 1)}
        rows = 3
        columns = 3
        my_character = {'EX': 0, 'HP': 0, 'Max HP': 15}
        make_board(rows, columns, my_character)
        self.assertEqual(expect_char, my_character)
