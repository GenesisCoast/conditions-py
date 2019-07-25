from .validator import Validator
from errors.argument_error import ArgumentError
from errors.argument_null_error import ArgumentNullError

class ObjectValidator(Validator):
    """
    Contains all the object validation conditions.
    """


    def __init__(self, value: object, argument_name: str):
        """
        Initializes the validator base class with the `value` and `argument_name`.
        """
        super.__init__(value, argument_name)