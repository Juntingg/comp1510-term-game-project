"""
Caroline Su
A01369603
"""
import io
from unittest import TestCase
from unittest.mock import patch
from battle import dodge_attack


class Test(TestCase):

    @patch("random.choice", return_value="R")
    def test_succeed_to_dodge_attack(self, _):
        user_input = "R"
        expect_character = {'EX': 0, 'HP': 10, 'Max HP': 10}
        my_character = {'EX': 0, 'HP': 10, 'Max HP': 10}
        char_reduced_hp = 2
        dodge_attack(my_character, char_reduced_hp, user_input)
        self.assertEqual(expect_character, my_character)

    @patch("random.choice", return_value="L")
    def test_fail_to_dodge_attack(self, _):
        user_input = "R"
        expect_character = {'EX': 0, 'HP': 8, 'Max HP': 15}
        my_character = {'EX': 0, 'HP': 10, 'Max HP': 15}
        char_reduced_hp = 2
        dodge_attack(my_character, char_reduced_hp, user_input)
        self.assertEqual(expect_character, my_character)

    @patch("random.choice", return_value="R")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_succeed_to_dodge_attack_print_message(self, mock_output, _):
        expect = "👍 Nice! You dodge the attack!\n"
        user_input = "R"
        character = {'EX': 0, 'HP': 10, 'Max HP': 10}
        reduced_hp = 2
        dodge_attack(character, reduced_hp, user_input)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(expect, the_game_printed_this)

    @patch("random.choice", return_value="L")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fail_to_dodge_attack_print_message(self, mock_output, _):
        expect = "💥 Oh no! You did not dodge the attack! HP - 2\n"
        user_input = "R"
        character = {'EX': 0, 'HP': 10, 'Max HP': 10}
        reduced_hp = 2
        dodge_attack(character, reduced_hp, user_input)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(expect, the_game_printed_this)
