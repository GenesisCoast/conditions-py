import pytest
from src.condition import Condition
from src.errors.argument_error import ArgumentError


def test_intg_is_true_throws_error_on_false():
    """
    Tests the `is_true()` validator method through `Condition.requires()` to see if it,
	throws an `ArgumentError` when the supplied value is False.
    """
    # Arrange
    value = False

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires(value, 'value').is_true()


def test_intg_is_true_accepts_true():
    """
    Tests the `is_true()` validator method through `Condition.requires()` to see if it,
	does not throw an `ArgumentError` when the supplied value is True.
    """
    # Arrange
    value = True

    # Act
    try:
        Condition.requires(value, 'value').is_true()
    # Assert
    except ArgumentError:
        pytest.fail()


def test_intg_is_false_throws_argument_error_on_true():
    """
    Tests the `is_false()` validator method through `Condition.requires()` to see if it,
	throws an `ArgumentError` when the supplied value is True.
    """
    # Arrange
    value = True

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires(value, 'value').is_false()


def test_intg_is_false_accepts_false():
    """
    Tests the `is_false()` validator method through `Condition.requires()` to see if it,
	does not throw an `ArgumentError` when the supplied value is False.
    """
    # Arrange
    value = False

    # Act
    try:
        Condition.requires(value, 'value').is_false()
    # Asset
    except ArgumentError:
        pytest.fail()