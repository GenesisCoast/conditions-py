from .validator import Validator
from errors.argument_error import ArgumentError


class BooleanValidator(Validator):
    """
    Contains all the boolean validation conditions.
    """

    def is_true(self) -> self:
        """
        Checks whether the given value is `True`. An exception is thrown otherwise.
        """
        if not self.value == True:
            raise ArgumentError(
                f'The argument `{self.argument_name}` should be True but was `{self.value}`',
                self.value,
                self.argument_name
            )

        return self


    def is_false(self) -> self:
        """
        Checks whether the given value is `True`. An exception is thrown otherwise.
        """
        if not self.value == False:
            raise ArgumentError(
                f'The argument `{self.argument_name}` should be False but was `{self.value}`',
                self.value,
                self.argument_name
            )

        return self