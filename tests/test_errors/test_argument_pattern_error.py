from pytest import raises
from src.errors.argument_pattern_error import ArgumentPatternError


def test_constructor_assigns_values():
    """

    """
    # Arrange
    message = 'This is my error message'
    value = 'test_value'
    argument_name = 'value'
    pattern = r'[a-z0-9]+'

    # Act
    with raises(ArgumentPatternError) as excinfo:
        raise ArgumentPatternError(
            message,
            value,
            argument_name,
            pattern
        )

    # Assert
    assert excinfo.value.args[0] == message
    assert excinfo.value.value == value
    assert excinfo.value.argument_name == argument_name
    assert excinfo.value.pattern == pattern