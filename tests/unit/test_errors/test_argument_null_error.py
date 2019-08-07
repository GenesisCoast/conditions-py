from pytest import raises
from src.errors.argument_null_error import ArgumentNullError


def test_constructor_assigns_values():
    """

    """
    # Arrange
    message = 'This is my error message'
    value = 'test_value'
    argument_name = 'value'

    # Act
    with raises(ArgumentNullError) as excinfo:
        raise ArgumentNullError(
            message,
            value,
            argument_name
        )

    # Assert
    assert excinfo.value.args[0] == message
    assert excinfo.value.value == value
    assert excinfo.value.argument_name == argument_name