"""
Caroline Su
A01369603
"""
import io
from unittest import TestCase
from unittest.mock import patch
from character import upgrade_character_level


class Test(TestCase):
    def test_upgrade_to_level_3(self):
        expect = {"Level": 3, "EX": 2, "HP": 20, "Max HP": 20}
        character = {"Level": 2, "EX": 17, "HP": 15, "Max HP": 15}
        upgrade_character_level(character)
        self.assertEqual(character, expect)

    def test_upgrade_to_level_2(self):
        expect = {"Level": 2, "EX": 7, "HP": 15, "Max HP": 15}
        character = {"Level": 1, "EX": 17, "HP": 7, "Max HP": 10}
        upgrade_character_level(character)
        self.assertEqual(character, expect)

    def test_EX_is_not_enough(self):
        expect = {"Level": 1, "EX": 5, "HP": 7, "Max HP": 10}
        character = {"Level": 1, "EX": 5, "HP": 7, "Max HP": 10}
        upgrade_character_level(character)
        self.assertEqual(character, expect)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_level_2_print_message(self, mock_output):
        expect = "🎊 Congratulation! You are Level 2 now! You feel more powerful than before!\n"\
                 "Your courage has earned the recognition of the gods. You are now fully healed. Current HP: 15/15\n"
        character = {"Level": 1, "EX": 17, "HP": 7, "Max HP": 10}
        upgrade_character_level(character)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(the_game_printed_this, expect)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_level_3_print_message(self, mock_output):
        expect = "🎊 Congratulation! You are Level 3 now! You feel more powerful than before!\n" \
                 "Your courage has earned the recognition of the gods. You are now fully healed. Current HP: 20/20\n"
        character = {"Level": 2, "EX": 20, "HP": 15, "Max HP": 15}
        upgrade_character_level(character)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(the_game_printed_this, expect)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_not_upgrade_message(self, mock_output):
        expect = ""
        character = {"Level": 1, "EX": 5, "HP": 7, "Max HP": 10}
        upgrade_character_level(character)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(the_game_printed_this, expect)
