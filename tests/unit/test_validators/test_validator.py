import pytest
from src.validators.validator import Validator


@pytest.mark.parametrize(
    'value,argument_name',
    [
        (True, 'boolean_value'),
        (1456, 'number_value'),
        (45.76, 'float_value'),
        ('this_is_a_value', 'string_value')
    ]
)
def test_constructor_initializes_validator(value, argument_name):
    """
    Tests that the base validator initializes the validator with the correct value.
    """
    # Arrange / Act
    validator = Validator(value, argument_name)

    # Assert
    assert isinstance(validator, Validator)
    assert validator.value == value
    assert validator.argument_name == argument_name


@pytest.mark.parametrize(
    'value,argument_name',
    [
        (True, 'boolean_value'),
        (1456, 'number_value'),
        (45.76, 'float_value'),
        ('this_is_a_value', 'string_value')
    ]
)
def test_get_value_returns_value(value, argument_name):
    """
    Tests if the `get_value()` method returns the value saved in the validator.
    """
    # Arrange
    validator = Validator(value, argument_name)

    # Act
    actual = validator.get_value()

    # Assert
    assert actual == value
    assert actual is value
    assert type(actual) == type(value)