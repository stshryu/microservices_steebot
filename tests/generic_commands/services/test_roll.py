from django.test import TestCase

from generic_commands.services import roll
from errors import errors
import success
from tests import test_helper


class TestRoll(TestCase):
    def test_happy_path(self):
        # Arrange
        input_data = {
            'lower_bound': 10,
            'upper_bound': 100
        }
        request = test_helper.api_factory_helper('post', input_data)

        # Act
        value = roll.Roll()
        result = value.perform_roll(request)
        unpacked_result = result.unpack()
        roll_value = unpacked_result.value

        # Assert
        self.assertIsInstance(result, success.Success)
        self.assertIsInstance(unpacked_result, roll.Roll)
        self.assertTrue(input_data['lower_bound'] <= roll_value <= input_data['upper_bound'])

    def test_valid_lower_and_upper_bound(self):
        # Arrange
        input_data = {
            'lower_bound': 100,
            'upper_bound': 10
        }
        request = test_helper.api_factory_helper('post', input_data)

        # Act
        value = roll.Roll()
        result = value.perform_roll(request)

        # Assert
        self.assertIsInstance(result, errors.InvalidInputs)

