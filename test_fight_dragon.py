"""
Caroline Su
A01369603
"""
import io
from unittest import TestCase
from unittest.mock import patch
from battle import fight_dragon


class Test(TestCase):
    @patch('builtins.input', return_value="R")
    @patch("random.choice", return_value="L")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_die(self, mock_output, _, __):
        expect = "The dragon is furious and swiped at you with a mighty paw.\n"\
                 "Would you like to dodge to the right or to the left?(You have 50% chance to dodge the attack)\n"\
                 "💥 Oh no! You did not dodge the attack! HP - 5\n"\
                 "☠️ Sorry, you die! You lose the game.\n"
        my_character = {'EX': 0, 'HP': 0, 'Max HP': 15}
        fight_dragon(my_character)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(expect, the_game_printed_this)

    @patch('builtins.input', return_value="R")
    @patch("random.choice", return_value="R")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_during_the_battle(self, mock_output, _, __):
        expect = "The dragon is furious and swiped at you with a mighty paw.\n"\
                 "Would you like to dodge to the right or to the left?(You have 50% chance to dodge the attack)\n"\
                 "👍 Nice! You dodge the attack!\n"\
                 "⚔️ You gather all your focus and deliver a mighty strike aimed at the dragon.\n"\
                 "He lunges forward, its massive jaws opening wide as searing flames shoot forth.\n"\
                 "Would you like to dodge to the right or to the left?(You have 50% chance to dodge the attack)\n"\
                 "👍 Nice! You dodge the attack!\n"\
                 "⚔️ You gather all your focus and deliver a mighty strike aimed at the dragon.\n"\
                 "The dragon's colossal wings beat forcefully, creating gusts of wind\n"\
                 "Would you like to dodge to the right or to the left?(You have 50% chance to dodge the attack)\n"\
                 "👍 Nice! You dodge the attack!\n"\
                 "⚔️ You gather all your focus and deliver a mighty strike aimed at the dragon.\n"\
                 "You persistently battled and defeated the dragon. Finally, roaring in protest, the dragon fell.\n"\
                 "In a secluded corner, you discovered the treasure. You win the game!🎉🎉🎉\n"
        my_character = {'EX': 0, 'HP': 15, 'Max HP': 15}
        fight_dragon(my_character)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(expect, the_game_printed_this)
