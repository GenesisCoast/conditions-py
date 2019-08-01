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

    """
    # Act
    validator = Condition.requires(value, 'value')

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

    """
    # Act
    validator = Condition.requires(value, 'value')

    # Assert
    assert isinstance(validator, NumberValidator)


def test_requires_returns_object_validator():
    """

    """
    # Arrange
    obj = TypeExample()

    # Act
    validator = Condition.requires(obj, 'obj')

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

    """
    # Act
    validator = Condition.requires(value, 'value')

    # Assert
    assert isinstance(validator, StringValidator)