"""
Caroline Su
A01369603
"""
import io
from unittest import TestCase
from unittest.mock import patch
from battle import ask_dodge_direction


class Test(TestCase):
    @patch('builtins.input', return_value="R")
    def test_input_uppercase_R(self, _):
        expect = "R"
        user_input = ask_dodge_direction()
        self.assertEqual(user_input, expect)

    @patch('builtins.input', return_value="L")
    def test_input_uppercase_L(self, _):
        expect = "L"
        user_input = ask_dodge_direction()
        self.assertEqual(user_input, expect)

    @patch('builtins.input', return_value="l")
    def test_input_lowercase_l(self, _):
        expect = "L"
        user_input = ask_dodge_direction()
        self.assertEqual(user_input, expect)

    @patch('builtins.input', return_value="   l   ")
    def test_input_lowercase_l_with_white_space(self, _):
        expect = "L"
        user_input = ask_dodge_direction()
        self.assertEqual(user_input, expect)

    @patch('builtins.input', side_effect=["Somthing", "L"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_input(self, mock_output, _):
        expect = "Would you like to dodge to the right or to the left?(You have 50% chance to dodge the attack)\n"\
                 "❌ That is not a valid input. Please try again!\n"
        ask_dodge_direction()
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(the_game_printed_this, expect)
