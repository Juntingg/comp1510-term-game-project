"""
Caroline Su
A01369603
"""
from unittest import TestCase
from unittest.mock import patch
from battle import there_is_an_attack


class Test(TestCase):
    @patch("random.randint", return_value=1)
    def test_random_number_1(self, _):
        actual = there_is_an_attack()
        self.assertTrue(actual)

    @patch("random.randint", return_value=2)
    def test_random_number_2(self, _):
        actual = there_is_an_attack()
        self.assertFalse(actual)

    @patch("random.randint", return_value=3)
    def test_random_number_3(self, _):
        actual = there_is_an_attack()
        self.assertFalse(actual)

    @patch("random.randint", return_value=4)
    def test_random_number_4(self, _):
        actual = there_is_an_attack()
        self.assertFalse(actual)

    @patch("random.randint", return_value=5)
    def test_random_number_5(self, _):
        actual = there_is_an_attack()
        self.assertFalse(actual)
