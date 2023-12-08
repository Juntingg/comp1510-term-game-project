"""
Caroline Su
A01369603
"""
import io
from unittest import TestCase
from unittest.mock import patch
from event import handle_counter


class Test(TestCase):
    def test_counter_20(self):
        actual = handle_counter(20)
        expect = False
        self.assertEqual(actual, expect)

    def test_counter_40(self):
        result = handle_counter(40)
        expect = True
        self.assertEqual(result, expect)

    def test_counter_other(self):
        result = handle_counter(30)
        expect = False
        self.assertEqual(result, expect)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_counter_20_print_message(self, mock_output):
        expect = "You feel a little uncomfortable, and the darkness makes you feel disoriented.\n"\
                 "But you have no choice but to move forward...\n"
        handle_counter(20)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(expect, the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_counter_40_print_message(self, mock_output):
        expect = "It seems like you've been wandering around in the cave for too long, feeling exhausted.\n"\
                 "Just as you were starting to feel a bit desperate, it's as if the gods heard your plea...\n"\
                 "A mysterious force transports you out of the cave, leaving a key quietly resting in your hand.\n"\
                 "Your unwavering persistence appears to have caught the attention of the divine.\n"\
                 "After a burst of white light, there is something lied in your hand.\n"
        handle_counter(40)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(expect, the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_counter_other_print_message(self, mock_output):
        expect = ""
        handle_counter(30)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(expect, the_game_printed_this)
