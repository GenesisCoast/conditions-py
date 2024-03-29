import pytest
from typing import TypeVar
from .type_example import TypeExample
from src.condition import Condition
from src.validators.boolean_validator import BooleanValidator
from src.validators.number_validator import NumberValidator
from src.validators.object_validator import ObjectValidator
from src.validators.string_validator import StringValidator


number = TypeVar('number', int, float)


@pytest.mark.parametrize(
    'value',
    [
        (True),
        (False)
    ]
)
def test_requires_returns_boolean_validator(value: bool):
    """
    Tests if the `Condition.requires()` method returns the validator that is appropriate to
    the boolean datatype.
    """
    # Act
    validator = Condition.requires_bool(value, 'value')

    # Assert
    assert isinstance(validator, BooleanValidator)


@pytest.mark.parametrize(
    'value',
    [
        (1234),
        (7589724),
        (787.3762),
        (80188.76)
    ]
)
def test_requires_returns_number_validator(value: number):
    """
    Tests if the `Condition.requires()` method returns the validator that is appropriate to
    the number (float, int) datatype.
    """
    # Act
    validator = Condition.requires_num(value, 'value')

    # Assert
    assert isinstance(validator, NumberValidator)


def test_requires_returns_object_validator():
    """
    Tests if the `Condition.requires()` method returns the validator that is appropriate to
    the object datatype.
    """
    # Arrange
    obj = TypeExample()

    # Act
    validator = Condition.requires_obj(obj, 'obj')

    # Assert
    assert isinstance(validator, ObjectValidator)


@pytest.mark.parametrize(
    'value',
    [
        ('test'),
        ('this_is_my_value')
    ]
)
def test_requires_returns_string_validator(value: str):
    """
    Tests if the `Condition.requires_str()` method returns the validator that is appropriate to
    the string datatype.
    """
    # Act
    validator = Condition.requires_str(value, 'value')

    # Assert
    assert isinstance(validator, StringValidator)


@pytest.mark.parametrize(
    'value',
    [
        (True),
        (False)
    ]
)
def test_ensures_returns_boolean_validator(value: bool):
    """
    Tests if the `Condition.ensures()` method returns the validator that is appropriate to
    the boolean datatype.
    """
    # Act
    validator = Condition.ensures_bool(value, 'value')

    # Assert
    assert isinstance(validator, BooleanValidator)


@pytest.mark.parametrize(
    'value',
    [
        (1234),
        (7589724),
        (787.3762),
        (80188.76)
    ]
)
def test_ensures_returns_number_validator(value: number):
    """
    Tests if the `Condition.ensures()` method returns the validator that is appropriate to
    the number (float, int) datatype.
    """
    # Act
    validator = Condition.ensures_num(value, 'value')

    # Assert
    assert isinstance(validator, NumberValidator)


def test_ensures_returns_object_validator():
    """
    Tests if the `Condition.ensures()` method returns the validator that is appropriate to
    the object datatype.
    """
    # Arrange
    obj = TypeExample()

    # Act
    validator = Condition.ensures_obj(obj, 'obj')

    # Assert
    assert isinstance(validator, ObjectValidator)


@pytest.mark.parametrize(
    'value',
    [
        ('test'),
        ('this_is_my_value')
    ]
)
def test_ensures_returns_string_validator(value: str):
    """
    Tests if the `Condition.ensures_str()` method returns the validator that is appropriate to
    the string datatype.
    """
    # Act
    validator = Condition.ensures_str(value, 'value')

    # Assert
    assert isinstance(validator, StringValidator)