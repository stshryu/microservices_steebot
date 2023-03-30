from generic_commands.services import roll
from django.test import TestCase


class TestRoll(TestCase):

    def test_happy_path(self):
        test_dataset = [
            {'lower_bound': 0, 'upper_bound': 100}
        ]

        for test in test_dataset:
            value = roll.Roll(**test).get_value()
            self.assertIsInstance(value, int)

    def test_higher_lower_bound(self):
        test_dataset = [
            {'lower_bound': 100, 'upper_bound': 10}
        ]

        for test in test_dataset:
            value = roll.Roll(**test).get_value()
            self.assertIsInstance(value, int)