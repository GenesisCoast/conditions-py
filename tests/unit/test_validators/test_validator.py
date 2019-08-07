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