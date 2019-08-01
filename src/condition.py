from typing import TypeVar, Generic
from .validators.validator import Validator
from .validators.string_validator import StringValidator
from .validators.object_validator import ObjectValidator
from .validators.number_validator import NumberValidator
from .validators.boolean_validator import BooleanValidator


TValidator = TypeVar('TValidator', StringValidator, ObjectValidator, NumberValidator)


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
        elif type(value) is int or type(value) is float:
            return NumberValidator(value, argument_name)
        elif type(value) is bool:
            return BooleanValidator(value, argument_name)
        else:
            return ObjectValidator(value, argument_name)