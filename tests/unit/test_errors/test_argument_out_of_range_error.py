from pytest import raises
from src.errors.argument_out_of_range_error import ArgumentOutOfRangeError


def test_constructor_assigns_values():
    """

    """
    # Arrange
    message = 'This is my error message'
    value = 'test_value'
    argument_name = 'value'
    equal_to = 5,
    min_value = 1,
    max_value = 10

    # Act
    with raises(ArgumentOutOfRangeError) as excinfo:
        raise ArgumentOutOfRangeError(
            message,
            value,
            argument_name,
            equal_to,
            min_value,
            max_value
        )

    # Assert
    assert excinfo.value.args[0] == message
    assert excinfo.value.value == value
    assert excinfo.value.argument_name == argument_name
    assert excinfo.value.equal_to == equal_to
    assert excinfo.value.min_value == min_value
    assert excinfo.value.max_value == max_value