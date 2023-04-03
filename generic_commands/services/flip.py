import random

import success


class Flip(object):
    """
    Flips a coin between heads or tails and returns the outcome
    """
    VALID_OUTCOMES = ['HEADS', 'TAILS']

    def __init__(self):
        self.value = None

    def perform_flip(self):
        """
        Takes a flip request and processes it into a successful roll or an error

        Returns:
            errors.UnexpectedError -            When an unexpected error occurs while attempting the flip

            success.Success(object: Flip) -     When successful in flipping a coin, return self
        """
        flip = random.randint(0, 1)
        self.value = self.VALID_OUTCOMES[flip]
        return success.Success(self)

