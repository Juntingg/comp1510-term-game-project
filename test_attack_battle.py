"""
Caroline Su
A01369603
"""
import io
from unittest import TestCase
from unittest.mock import patch
from battle import attack_battle


class Test(TestCase):
    @patch('random.randint', return_value="🦇 bat")
    @patch('builtins.input', return_value="L")
    @patch("random.choice", return_value="L")
    def test_character_gain_EX(self, _, __, ___):
        expect = {'EX': 3, 'HP': 10, 'Max HP': 10}
        my_character = {'EX': 0, 'HP': 10, 'Max HP': 10}
        attack_battle(my_character)
        self.assertEqual(expect, my_character)

    @patch('random.choice', return_value="🦇 bat")
    @patch('builtins.input', return_value="L")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_bat_message(self, mock_output, _, __):
        expect = "❗Suddenly! A 🦇 bat emerges and launches an attack on you!\n"\
                 "Would you like to dodge to the right or to the left?(You have 50% chance to dodge the attack)\n"\
                 "💥 Oh no! You did not dodge the attack! HP - 2\n"\
                 "⚔️ You unleash a powerful strike and defeat the enemy! EX + 3\n"
        my_character = {'EX': 0, 'HP': 10, 'Max HP': 10}
        attack_battle(my_character)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(expect, the_game_printed_this)

    @patch('random.choice', return_value="🐻 bear")
    @patch('builtins.input', return_value="L")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_bear_message(self, mock_output, _, __):
        expect = "❗Suddenly! A 🐻 bear emerges and launches an attack on you!\n" \
                 "Would you like to dodge to the right or to the left?(You have 50% chance to dodge the attack)\n" \
                 "💥 Oh no! You did not dodge the attack! HP - 2\n" \
                 "⚔️ You unleash a powerful strike and defeat the enemy! EX + 3\n"
        my_character = {'EX': 0, 'HP': 10, 'Max HP': 10}
        attack_battle(my_character)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(expect, the_game_printed_this)

    @patch('random.choice', return_value="🐍 snake")
    @patch('builtins.input', return_value="L")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_snake_message(self, mock_output, _, __):
        expect = "❗Suddenly! A 🐍 snake emerges and launches an attack on you!\n" \
                 "Would you like to dodge to the right or to the left?(You have 50% chance to dodge the attack)\n" \
                 "💥 Oh no! You did not dodge the attack! HP - 2\n" \
                 "⚔️ You unleash a powerful strike and defeat the enemy! EX + 3\n"
        my_character = {'EX': 0, 'HP': 10, 'Max HP': 10}
        attack_battle(my_character)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(expect, the_game_printed_this)

    @patch('random.choice', return_value="🐗 boar")
    @patch('builtins.input', return_value="L")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_boar_message(self, mock_output, _, __):
        expect = "❗Suddenly! A 🐗 boar emerges and launches an attack on you!\n" \
                 "Would you like to dodge to the right or to the left?(You have 50% chance to dodge the attack)\n" \
                 "💥 Oh no! You did not dodge the attack! HP - 2\n" \
                 "⚔️ You unleash a powerful strike and defeat the enemy! EX + 3\n"
        my_character = {'EX': 0, 'HP': 10, 'Max HP': 10}
        attack_battle(my_character)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(expect, the_game_printed_this)
