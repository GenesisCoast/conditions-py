from typing import Type, Union
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


    def is_of_type(self, type: object) -> self:
        """
        Checks whether the Type of the given value is of `type` by comparing the `__name__` attribute.
        An exception is thrown otherwise.
        """
        if not self.value.__name__ == type.__name__:
            raise ArgumentError(
                f'The argument `{self.argument_name}` should be of type `{type.__name__}` but was `{self.value.__name__}`',
                self.value,
                self.argument_name
            )

        return self


    def is_not_of_type(self, type: object) -> self:
        """
        Checks whether the Type of the given value is not of `type` by comparing the `__name__` attribute.
        An exception is thrown otherwise.
        """
        if self.value.__name__ == type.__name__:
            raise ArgumentError(
                f'The argument `{self.argument_name}` should not be of type `{type.__name__}` but was `{self.value.__name__}`',
                self.value,
                self.argument_name
            )

        return self


    def is_of_type_instance(self, type) -> self:
        """
        Checks whether the Type of the given value is of `type` by comparing the types using `isinstance()`.
        An exception is thrown otherwise.
        """
        if not isinstance(self.value, type):
            raise ArgumentError(
                f'The argument `{self.argument_name}` should be of type `{type.__name__}` but was `{self.value.__name__}`',
                self.value,
                self.argument_name
            )

        return self


    def is_not_of_type_instance(self, type) -> self:
        """
        Checks whether the Type of the given value is of `type` by comparing the types using `isinstance()`.
        An exception is thrown otherwise.
        """
        if isinstance(self.value, type):
            raise ArgumentError(
                f'The argument `{self.argument_name}` should not be of type `{type.__name__}` but was `{self.value.__name__}`',
                self.value,
                self.argument_name
            )

        return self


    def is_null(self) -> self:
        """
        Checks whether the given value is None (Null). An exception is thrown otherwise.
        """
        if not self.value is None:
            raise ArgumentNullError(
                f'The argument `{self.argument_name}` should be None (Null).',
                self.value,
                self.argument_name
            )

        return self


    def is_not_null(self) -> self:
        """
        Checks whether the given value is None (Null). An exception is thrown otherwise.
        """
        if self.value is None:
            raise ArgumentNullError(
                f'The argument `{self.argument_name}` should not be None (Null).',
                self.value,
                self.argument_name
            )

        return self


    def is_equal_to(self, value: object) -> self:
        """

        """
        if not self.value is value:
            raise ArgumentError(
                f'The argument `{self.value.__name__}` should be equal to `{value.__name__}`',
                self.value,
                self.argument_name
            )

        return self


    def is_not_equal_to(self, value: object) -> self:
        """

        """
        if self.value is value:
            raise ArgumentError(
                f'The argument `{self.value.__name__}` should be equal to `{value.__name__}`',
                self.value,
                self.argument_name
            )

        return self