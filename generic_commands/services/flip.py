import random

import success


class Flip(object):
    VALID_OUTCOMES = ['HEADS', 'TAILS']

    def __init__(self):
        self.value = None

    def perform_flip(self):
        flip = random.randint(0, 1)
        self.value = self.VALID_OUTCOMES[flip]
        return success.Success(self)

