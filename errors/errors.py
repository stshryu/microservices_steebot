import json


class BaseError(Exception):
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class InvalidInputs(BaseError):
    """Raised when the inputs are incorrect

    Attributes:
        input_var   -- input name which caused the error
        message     -- message sent back with exception
    """

    def __init__(self, input_var, message=None):
        self.input_var = input_var
        if message is None:
            self.message = "Error with input value: {}"\
                .format(', '.join(self.input_var))
        else:
            self.message = "Error with input value: {}. Error Message: {}"\
                .format(', '.join(self.input_var), message)


class MissingInput(BaseError):
    """
    Raised when expected inputs are missing

    Attributes:
        expected_inputs   -- list of inputs missing
        message             -- message sent back with exception
    """

    def __init__(self, expected_inputs, message=None):
        self.expected_inputs = expected_inputs
        if message is None:
            self.message = "Error, missing input value(s): {}"\
                .format(', '.join(self.expected_inputs))
        else:
            self.message = "Error, missing input value(S): {}. Error message: {}"\
                .format(', '.join(self.expected_inputs), message)
