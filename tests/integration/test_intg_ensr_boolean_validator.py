import pytest
from src.condition import Condition
from src.errors.argument_error import ArgumentError


@pytest.mark.parametrize(
    'value',
    [
        (True),
        (False),
    ]
)
def test_intg_ensr_prnt_get_value_returns_value(value):
    """
    Tests if the parent `get_value()` ensures validator method returns the value saved in the validator.
    """
	# Act
    actual = Condition.ensures_bool(value, 'value').get_value()

    # Assert
    assert actual == value
    assert actual is value
    assert type(actual) == type(value)


def test_intg_ensr_is_true_throws_error_on_false():
    """
    Tests the `is_true()` ensures validator method through `Condition.ensures_bool()` to see if it,
	throws an `ArgumentError` when the supplied value is False.
    """
    # Arrange
    value = False

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.ensures_bool(value, 'value').is_true()


def test_intg_ensr_is_true_accepts_true():
    """
    Tests the `is_true()` ensures validator method through `Condition.ensures_bool()` to see if it,
	does not throw an `ArgumentError` when the supplied value is True.
    """
    # Arrange
    value = True

    # Act
    try:
        Condition.ensures_bool(value, 'value').is_true()
    # Assert
    except ArgumentError:
        pytest.fail()


def test_intg_ensr_is_false_throws_argument_error_on_true():
    """
    Tests the `is_false()` ensures validator method through `Condition.ensures_bool()` to see if it,
	throws an `ArgumentError` when the supplied value is True.
    """
    # Arrange
    value = True

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.ensures_bool(value, 'value').is_false()


def test_intg_ensr_is_false_accepts_false():
    """
    Tests the `is_false()` ensures validator method through `Condition.ensures_bool()` to see if it,
	does not throw an `ArgumentError` when the supplied value is False.
    """
    # Arrange
    value = False

    # Act
    try:
        Condition.ensures_bool(value, 'value').is_false()
    # Asset
    except ArgumentError:
        pytest.fail()