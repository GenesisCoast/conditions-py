# import unittest
import pytest

from src.errors.argument_error import ArgumentError
from src.validators.boolean_validator import BooleanValidator


def test_is_true_throws_error_on_false():
    """
    Tests if the `is_true()` validator method throws an `ArgumentError`
    when the supplied value is False.
    """
    # Arrange
    value = False
    validator = BooleanValidator(value, "value")

    # with assert_raises(ArgumentException):
    # Assert
    # with assert_raises(ArgumentError):
    with pytest.raises(ArgumentError):
        # Act
        validator.is_true()


def test_is_true_does_not_throw_error_on_true():
    """
    Tests if the `is_true()` validator method does not throw an `ArgumentError`
    when the supplied value is True.
    """
    # Arrange
    value = True
    validator = BooleanValidator(value, "value")

    # Act
    try:
        validator.is_true()
    # Assert
    except ArgumentError:
        pytest.fail()


def test_is_false_throws_argument_error_on_true():
    """
    Tests if the `is_false()` validator method throws an `ArgumentError`
    when the supplied value is True.
    """
    # Arrange
    value = True
    validator = BooleanValidator(value, "value")

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_false()


def test_is_false_does_not_throw_error_on_false():
    """
    Tests if the `is_false()` validator method does not throw an `ArgumentError`
    when the supplied value is False.
    """
    # Arrange
    value = False
    validator = BooleanValidator(value, "value")

    # Act
    try:
        validator.is_false()
    # Asset
    except ArgumentError:
        pytest.fail()