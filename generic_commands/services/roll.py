import random

import success
from errors import errors


class Roll(object):
    """
    Takes two integers (lower and upper bound) and finds a random integer between those bounds
    """

    # List of valid inputs for our validation functions
    VALID_INPUTS = ['lower_bound', 'upper_bound']

    def __init__(self):
        self.lower_bound = None
        self.upper_bound = None
        self.value = None

    def perform_roll(self, request):
        """
        Takes a roll request and processes it into a successful roll or an error

        Parameters:
            request: rest_framework.request.Request

        Returns:
            errors.InvalidInputs -          When one or more inputs are invalid

            errors.MissingInputs -          When one or more expected inputs are missing

            errors.UnexpectedError -        When none of the success/error cases match an expected outcome

            success.Success(object: Roll) - When successful in rolling, return self
        """
        non_validated_data = request.POST
        result = self.validate(non_validated_data)
        match result:
            case errors.InvalidInputs():
                return result
            case errors.MissingInputs():
                return result
            case success.Success():
                self.unpack_valid_data(result)
                return success.Success(self)
            case _:
                return errors.UnexpectedError()

    def validate(self, non_validated_data):
        """
        Takes non-validated data and returns successfully validated data or an error

        Parameters:
            non_validated_data: QuerySet
        Returns:
            errors.InvalidInputs -            When one or more inputs are not integers or are strings that cannot be
                                                converted to integers

            errors.InvalidInputs -            When lower_bound is larger than upper_bound

            errors.MissingInputs -            When one or more required inputs are missing

            success.Success(object: dict) -   When data is validated successfully return a Success() with the
                                                validated data object
        """
        invalid_data = dict(filter(self.invalid_dict_kv_pair, non_validated_data.items()))
        if invalid_data:
            return errors.InvalidInputs(invalid_data.keys(), 'Input value(s) are invalid')
        validated_data = self.convert_dict_values_to_int(non_validated_data)
        missing_keys = list(filter(lambda key: (key not in validated_data), self.VALID_INPUTS))
        if len(missing_keys) > 0:
            return errors.MissingInputs(missing_keys, 'Input value(s) are missing')
        if validated_data['lower_bound'] > validated_data['upper_bound']:
            return errors.InvalidInputs(['lower_bound'], 'Lower bound must not be higher than upper bound.')
        return success.Success(validated_data)

    def unpack_valid_data(self, result):
        """
        Takes a Success() and unpacks the nested data

        Parameters:
            result: object
        """
        valid_data = result.unpack()
        self.lower_bound = valid_data['lower_bound']
        self.upper_bound = valid_data['upper_bound']
        self.value = random.randint(self.lower_bound, self.upper_bound)

    @staticmethod
    def convert_dict_values_to_int(non_validated_data):
        """
        Converts all values in a dict() into an int() and returns a new dict() with the same keys and values

        Parameters:
            non_validated_data: object
        Returns:
            validated_data -    dict
        """
        validated_data = {}
        for key, value in non_validated_data.items():
            validated_data[key] = int(value)
        return validated_data

    @staticmethod
    def invalid_dict_kv_pair(kv_pair):
        """
        Checks if a key value pair has a value that is not an integer, or cannot be converted to one

        Parameters:
            kv_pair: Tuple()
        Returns:
            True -      If a key-value pair value cannot be converted to an int

            False -     If a key-value pair value can be converted to an int (or is already an int)
        """
        val = kv_pair[1]
        if val is None:
            return True
        elif type(val) == int:
            return False
        elif val.isdigit():
            return False
        else:
            return True
