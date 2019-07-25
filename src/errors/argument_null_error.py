from .argument_error import ArgumentError

class ArgumentNullError(ArgumentError):
    """

    """


    def __init__(self, value, argument_name):
        """

        """
        super.__init__(
            f'The argument `{argument_name}` is NULL',
            value,
            argument_name
        )