import json

class BaseError(Exception):
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

class UnexpectedError(BaseError):
    """
    Raise an unexpected error as our base error if something is uncaught
    """
    def __init__(self, message="UnexpectedError"):
        self.message = message

class InvalidDataInput(BaseError):
    """
    Raised when input data doesn't match the validation schema
    """
    def __init__(self, invalid_fields: dict):
        formatted_errors = [f"{key}: {value}" for key, value in invalid_fields.items()]
        self.message = '\n'.join(formatted_errors)

class UnauthorizedError(BaseError):
    """
    Raised when an issuer is unauthorized to perform some actions
    """
    def __init__(self, issuer: str, action: str):
        self.message = f"{issuer = } is not allowed to perfom {action = }"
