from django.test import TestCase

from generic_commands.services import flip
from errors import errors
import success
from tests import test_helper


class TestFlip(TestCase):
    def test_happy_path(self):
        # Arrange
        request = test_helper.api_factory_helper('get')

        # Act
        value = flip.Flip()
        result = value.perform_flip()
        unpacked_result = result.unpack()
        flip_value = unpacked_result.value

        # Assert
        self.assertIsInstance(result, success.Success)
        self.assertIsInstance(unpacked_result, flip.Flip)
        self.assertTrue(flip_value is 'HEADS' or 'TAILS')
