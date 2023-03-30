import random
from errors import errors


class Roll(object):
    """
    Takes two integers (lower and upper bound) and finds a random integer between those bounds

    inputs:
    {
        lower_bound: int
        upper_bound: int
    }
    """

    VALIDATED_FIELDS = ['lower_bound', 'upper_bound']

    def __init__(self, non_validated_data):
        result = self.validate(non_validated_data)
        match result:
            case errors.InvalidInputs():
                self.error = result
            case errors.MissingInput():
                self.error = result
            case _:
                self.lower_bound = result['lower_bound']
                self.upper_bound = result['upper_bound']
                self.value = random.randint(self.lower_bound, self.upper_bound)

    def validate(self, non_validated_data):
        missing_keys = list(filter(lambda key: (key not in non_validated_data), self.VALIDATED_FIELDS))
        if len(missing_keys) > 0:
            return errors.InvalidInputs(missing_keys, 'Input value(s) are missing')
        if non_validated_data['lower_bound'] > non_validated_data['upper_bound']:
            return errors.InvalidInputs(['lower_bound'], 'Lower bound must not be higher than upper bound.')
        return non_validated_data
