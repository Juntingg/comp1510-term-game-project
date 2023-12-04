"""
ADD A DOCSTRING
"""
import io
from unittest import TestCase
from unittest.mock import patch
from event import describe_user_state


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_user_state(self, mock_output):
        actual = "Your current location: (3,4)\n"\
                 "HP:15/20 EX:30 Level:3\n"
        my_char = {'Name': 'Bob', 'X-coordinate': 3, 'Y-coordinate': 4, 'HP': 15, 'Max HP': 20, 'EX': 30, 'Level': 3}
        describe_user_state(my_char)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(the_game_printed_this, actual)
