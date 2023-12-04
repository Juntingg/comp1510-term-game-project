"""
Caroline Su
A01369603
"""
import io
from unittest import TestCase
from unittest.mock import patch
from event import hole_movement


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_too_far_in_one_direction_message(self, mock_output):
        expect = "It seems like you are going too far? Maybe try the opposite direction...\n"\
                 "It's still pitch black. Keep moving forward...\n"
        test_distance = [60, 60]
        hole_movement(test_distance, "S")
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(the_game_printed_this, expect)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_within_scope_message(self, mock_output):
        expect = "It's still pitch black. Keep moving forward...\n"
        test_distance = [30, 30]
        hole_movement(test_distance, "S")
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(the_game_printed_this, expect)

    def test_move_south(self):
        expect = [40, 30]
        test_distance = [30, 30]
        hole_movement(test_distance, "S")
        self.assertEqual(test_distance, expect)

    def test_move_north(self):
        expect = [20, 30]
        test_distance = [30, 30]
        hole_movement(test_distance, "N")
        self.assertEqual(test_distance, expect)

    def test_move_west(self):
        expect = [30, 20]
        test_distance = [30, 30]
        hole_movement(test_distance, "W")
        self.assertEqual(test_distance, expect)

    def test_move_east(self):
        expect = [30, 40]
        test_distance = [30, 30]
        hole_movement(test_distance, "E")
        self.assertEqual(test_distance, expect)
