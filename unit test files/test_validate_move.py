"""
Caroline Su
A01369603
"""
from unittest import TestCase
from game import validate_move


class Test(TestCase):
    def test_invalid_move_to_north(self):
        my_board = {(0, 0): 'begin', (1, 0): 'mushroom', (0, 1): 'mushroom', (1, 1): 'castle'}
        my_char = {"X-coordinate": 0, "Y-coordinate": 0}
        actual = validate_move(my_board, my_char, 'N')
        self.assertFalse(actual)

    def test_invalid_move_to_west(self):
        my_board = {(0, 0): 'begin', (1, 0): 'mushroom', (0, 1): 'mushroom', (1, 1): 'castle'}
        my_char = {"X-coordinate": 0, "Y-coordinate": 0}
        actual = validate_move(my_board, my_char, 'W')
        self.assertFalse(actual)

    def test_invalid_move_to_south(self):
        my_board = {(0, 0): 'begin', (1, 0): 'mushroom', (0, 1): 'mushroom', (1, 1): 'castle'}
        my_char = {"X-coordinate": 1, "Y-coordinate": 1}
        actual = validate_move(my_board, my_char, 'S')
        self.assertFalse(actual)

    def test_invalid_move_to_east(self):
        my_board = {(0, 0): 'begin', (1, 0): 'mushroom', (0, 1): 'mushroom', (1, 1): 'castle'}
        my_char = {"X-coordinate": 1, "Y-coordinate": 1}
        actual = validate_move(my_board, my_char, 'E')
        self.assertFalse(actual)

    def test_valid_move_to_east(self):
        my_board = {(0, 0): 'begin', (1, 0): 'mushroom', (0, 1): 'mushroom', (1, 1): 'castle'}
        my_char = {"X-coordinate": 0, "Y-coordinate": 0}
        actual = validate_move(my_board, my_char, 'E')
        self.assertTrue(actual)

    def test_valid_move_to_south(self):
        my_board = {(0, 0): 'begin', (1, 0): 'mushroom', (0, 1): 'mushroom', (1, 1): 'castle'}
        my_char = {"X-coordinate": 0, "Y-coordinate": 0}
        actual = validate_move(my_board, my_char, 'S')
        self.assertTrue(actual)

    def test_valid_move_to_north(self):
        my_board = {(0, 0): 'begin', (1, 0): 'mushroom', (0, 1): 'mushroom', (1, 1): 'castle'}
        my_char = {"X-coordinate": 1, "Y-coordinate": 1}
        actual = validate_move(my_board, my_char, 'N')
        self.assertTrue(actual)

    def test_valid_move_to_west(self):
        my_board = {(0, 0): 'begin', (1, 0): 'mushroom', (0, 1): 'mushroom', (1, 1): 'castle'}
        my_char = {"X-coordinate": 1, "Y-coordinate": 1}
        actual = validate_move(my_board, my_char, 'W')
        self.assertTrue(actual)
