"""
Caroline Su
A01369603
"""
from unittest import TestCase
from unittest.mock import patch
from battle import dodge_enemy_attack


class Test(TestCase):
    @patch("random.choice", return_value="R")
    def test_dodge_right(self, _):
        expect = "R"
        actual = dodge_enemy_attack()
        self.assertEqual(expect, actual)

    @patch("random.choice", return_value="L")
    def test_dodge_left(self, _):
        expect = "L"
        actual = dodge_enemy_attack()
        self.assertEqual(expect, actual)
