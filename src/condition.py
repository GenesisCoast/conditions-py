from typing import TypeVar, Generic
from src.validators.validator import Validator
from src.validators.string_validator import StringValidator
from src.validators.object_validator import ObjectValidator
from src.validators.boolean_validator import BooleanValidator
from src.validators.integer_validator import IntegerValidator


TValidator = TypeVar('TValidator', StringValidator, ObjectValidator, IntegerValidator)


class Condition(Generic[TValidator]):
    """
    Base condition class to create the validator which corresponds to the value type.
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
        elif type(value) is bool:
            return BooleanValidator(value, argument_name)
        else:
            return ObjectValidator(value, argument_name)