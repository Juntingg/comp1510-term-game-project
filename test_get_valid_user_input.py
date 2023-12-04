"""
Caroline Su
A01369603
"""
import io
from unittest import TestCase
from unittest.mock import patch
from event import get_valid_user_input


class Test(TestCase):
    @patch('builtins.input', return_value="STATE")
    def test_input_valid_uppercase_input(self, _):
        expect = "STATE"
        user_input = get_valid_user_input()
        self.assertEqual(user_input, expect)

    @patch('builtins.input', return_value="state")
    def test_input_valid_lowercase_input(self, _):
        expect = "STATE"
        user_input = get_valid_user_input()
        self.assertEqual(user_input, expect)

    @patch('builtins.input', return_value="   state   ")
    def test_input_valid_input_with_whitespace(self, _):
        expect = "STATE"
        user_input = get_valid_user_input()
        self.assertEqual(user_input, expect)

    @patch('builtins.input', side_effect=["hi", "state"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_invalid_input(self, mock_output, _):
        expect = "❌ That is not a valid input, try again!\n"
        get_valid_user_input()
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(the_game_printed_this, expect)
