"""
Caroline Su
A01369603
"""
import io
from unittest import TestCase
from unittest.mock import patch
from event import get_valid_direction


class Test(TestCase):
    @patch('builtins.input', side_effect=["state", "w"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_input_state(self, mock_output, _):
        expect = "Your current location: (0,0)\n"\
                 "HP:10/10 EX:0 Level:2\n"
        my_char = {'Name': 'Bob', 'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 10, 'Max HP': 10, 'EX': 0, 'Level': 2}
        get_valid_direction(my_char)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(the_game_printed_this, expect)

    @patch('builtins.input', side_effect=["HELP", "w"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_input_help(self, mock_output, _):
        expect = "---------------------------------------------------------------------------------------\n"\
                  "You will control the character's movement direction using the four keys:\n"\
                  " 1.'N' for north direction\n"\
                  " 2.'S' for south direction\n"\
                  " 3.'E' for east direction\n"\
                  " 4.'W' for west direction\n"\
                  "You can also input 'state' to check your character's attributes or 'help' to get instruction.\n"\
                  "Tell you quietly: you can type 'hint' if you couldn't find the key!\n"\
                  "---------------------------------------------------------------------------------------\n"
        my_char = {'Name': 'Bob', 'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 10, 'Max HP': 10, 'EX': 0, 'Level': 2}
        get_valid_direction(my_char)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(the_game_printed_this, expect)

    @patch('builtins.input', side_effect=["hint", "w"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_input_hint(self, mock_output, _):
        expect = "Please check out the location: (1, 3)\n"
        my_char = {'Name': 'Bob', 'X-coordinate': 0, 'Y-coordinate': 0, 'hole': (1, 3)}
        get_valid_direction(my_char)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(the_game_printed_this, expect)

    @patch('builtins.input', side_effect=["hint", "w"])
    def test_get_valid_direction(self, _):
        expect = "W"
        my_char = {'Name': 'Bob', 'X-coordinate': 0, 'Y-coordinate': 0, 'hole': (1, 3)}
        actual = get_valid_direction(my_char)
        self.assertEqual(actual, expect)
