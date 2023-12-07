"""
ADD A DOCSTRING
"""
from unittest import TestCase
from unittest.mock import patch
from event import trigger_hole_event


def main():
    pass


if __name__ == "__main__":
    main()


class Test(TestCase):
    @patch('builtins.input', side_effect=["N", "N", "W", "N", "N", "W", "N", "N", "W", "W",
                                          "N", "N", "W", "N", "N", "W", "N", "N", "W", "W",
                                          "N", "N", "W", "N", "N", "W", "N", "N", "W", "W",
                                          "N", "N", "W", "N", "N", "W", "N", "N", "W", "W"])
    def test_loop_through_40_time(self, _):
        my_char = {"key": False}
        trigger_hole_event(my_char)
        self.assertTrue(my_char["key"])

    @patch('builtins.input', side_effect=["N", "N", "N", "W", "W", "W"])
    def test_find_key(self, _):
        my_char = {"key": False}
        trigger_hole_event(my_char)
        self.assertTrue(my_char["key"])


