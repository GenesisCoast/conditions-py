from pytest import raises
from src.errors.argument_error import ArgumentError


def test_constructor_assigns_values():
    """

    """
    # Arrange
    message = 'This is my error message'
    value = 'test_value'
    argument_name = 'value'

    # Act
    with raises(ArgumentError) as excinfo:
        raise ArgumentError(
            message,
            value,
            argument_name
        )

    # Assert
    assert excinfo.value.args[0] == message
    assert excinfo.value.value == value
    assert excinfo.value.argument_name == argument_name