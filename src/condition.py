from typing import TypeVar, Generic
from validators.validator import Validator
from validators.string_validator import StringValidator
from validators.object_validator import ObjectValidator
from validators.integer_validator import IntegerValidator

Condition().requires('test', 'test').is_not_null()


TValidator = TypeVar('TValidator', StringValidator, ObjectValidator, IntegerValidator)


class Condition(Generic[TValidator]):
    """

    """

    @staticmethod
    def requires(value: object, argument_name: str) -> TValidator:
        """
        Initializes the conditions framework with the correct value_type validator.
        """
        if type(value) is str:
            return StringValidator(value, argument_name)
        elif type(value) is int:
            return IntegerValidator(value, argument_name)
        else:
            return ObjectValidator(value, argument_name)