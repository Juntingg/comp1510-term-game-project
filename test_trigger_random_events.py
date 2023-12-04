"""
Caroline Su
A01369603
"""
import io
from unittest import TestCase
from unittest.mock import patch
from event import trigger_random_events


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_trigger_wolf_event(self, mock_output):
        actual = "You move forward.\n"\
                 "🐺 A wolf attack you. HP - 1\n"
        my_char = {'Name': 'Bob', 'X-coordinate': 1, 'Y-coordinate': 0, 'HP': 15, 'Max HP': 20, 'EX': 30,
                   'Level': 3}
        my_board = {(0, 0): 'begin', (0, 1): 'wolf', (1, 0): 'wolf', (1, 1): 'castle'}
        trigger_random_events(my_board, my_char)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(the_game_printed_this, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_trigger_mushroom_event(self, mock_output):
        actual = "You move forward.\n" \
                 "🍄 You pick up a mushroom and eat it. You feel you are full of energy! HP + 1\n"
        my_char = {'Name': 'Bob', 'X-coordinate': 1, 'Y-coordinate': 0, 'HP': 15, 'Max HP': 20, 'EX': 30,
                   'Level': 3}
        my_board = {(0, 0): 'begin', (0, 1): 'wolf', (1, 0): 'mushroom', (1, 1): 'castle'}
        trigger_random_events(my_board, my_char)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(the_game_printed_this, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_trigger_nothing_event(self, mock_output):
        actual = "You move forward.\n" \
                 "🍂 After a gust of wind passed by, the surroundings became even quieter. Nothing happened.\n"
        my_char = {'Name': 'Bob', 'X-coordinate': 1, 'Y-coordinate': 0, 'HP': 15, 'Max HP': 20, 'EX': 30,
                   'Level': 3}
        my_board = {(0, 0): 'begin', (0, 1): 'wolf', (1, 0): 'nothing', (1, 1): 'castle'}
        trigger_random_events(my_board, my_char)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(the_game_printed_this, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_trigger_traveled_event(self, mock_output):
        actual = "You move forward.\n" \
                 "👣 You notice faint footprints on the ground. You have been here not long ago.\n"
        my_char = {'Name': 'Bob', 'X-coordinate': 1, 'Y-coordinate': 0, 'HP': 15, 'Max HP': 20, 'EX': 30,
                   'Level': 3}
        my_board = {(0, 0): 'begin', (0, 1): 'wolf', (1, 0): 'traveled', (1, 1): 'castle'}
        trigger_random_events(my_board, my_char)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(the_game_printed_this, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_trigger_castle_event(self, mock_output):
        actual = "You move forward.\n" \
                 "A gruesome castle stands in front of you...\n"\
                 "🔒 But you have not get the key or reach level 3 to enter the castle. Please explore more!\n"
        my_char = {'Name': 'Bob', 'X-coordinate': 1, 'Y-coordinate': 1, 'HP': 15, 'Max HP': 20, 'EX': 30,
                   'Level': 2}
        my_board = {(0, 0): 'begin', (0, 1): 'nothing', (1, 0): 'traveled', (1, 1): 'castle'}
        trigger_random_events(my_board, my_char)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(the_game_printed_this, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_trigger_wooden_chest_event(self, mock_output):
        actual = "You move forward.\n" \
                 "🌈 You find a wooden chest in a pile of soil! EX + 1\n"
        my_char = {'Name': 'Bob', 'X-coordinate': 1, 'Y-coordinate': 0, 'HP': 15, 'Max HP': 20, 'EX': 30,
                   'Level': 3}
        my_board = {(0, 0): 'begin', (0, 1): 'wolf', (1, 0): 'wooden chest', (1, 1): 'castle'}
        trigger_random_events(my_board, my_char)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(the_game_printed_this, actual)
