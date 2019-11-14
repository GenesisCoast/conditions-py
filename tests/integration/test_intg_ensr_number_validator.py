import pytest
from typing import TypeVar
from src.condition import Condition
from src.errors.argument_error import ArgumentError
from src.errors.argument_out_of_range_error import ArgumentOutOfRangeError


number = TypeVar('number', int, float)


@pytest.mark.parametrize(
    'value',
    [
        (2),
        (3),
        (11),
        (12),
        (650),
        (700),
        (2000),
        (2500),
        (2.30),
        (3.5),
        (11.1),
        (12.56),
        (650),
        (700),
        (2000.6547),
        (2500.7869)
    ]
)
def test_intg_ensr_prnt_get_value_returns_value(value):
    """
    Tests if the parent `get_value()` ensures validator method returns the value saved in the validator.
    """
    # Act
    actual = Condition.ensures_num(value, 'value').get_value()

    # Assert
    assert actual == value
    assert actual is value
    assert type(actual) == type(value)


@pytest.mark.parametrize(
    'value,min_value,max_value',
    [
        (2, 2, 3),
        (3, 2, 3),
        (11, 11, 12),
        (12, 11, 12),
        (650, 600, 700),
        (700, 600, 700),
        (2000, 2000, 3000),
        (2500, 2000, 3000),
        (2.30, 2.25, 3.5),
        (3.5, 2, 3.75),
        (11.1, 11, 12.95),
        (12.56, 11, 12.66),
        (650, 600, 700.89),
        (700, 600.65, 700),
        (2000.6547, 2000, 3000.987),
        (2500.7869, 2000.1111, 3000.7893)
    ]
)
def test_intg_ensr_is_in_range_accepts_valid_range(
    value: number,
    min_value: number,
    max_value: number
):
    """
    Tests the `is_in_range()` ensures validator method through `Condition.ensures_num()` to see if it,
    does not throw an ArgumentOutOfRangeError when it is suppied with a value that is within
    the supplied range.
    """
    # Act
    try:
        Condition.ensures_num(value, 'value').is_in_range(min_value, max_value)
    # Assert
    except ArgumentOutOfRangeError:
        pytest.fail(f'`{value}` should have been accepted in the range `{min_value}-{max_value}`, but instead an error occurred.')


@pytest.mark.parametrize(
    'value,min_value,max_value',
    [
        (1, 2, 3),
        (9, 2, 3),
        (10, 11, 12),
        (15, 11, 12),
        (500, 600, 700),
        (800, 600, 700),
        (1000, 2000, 3000),
        (4000, 2000, 3000),
        (2.30, 2.35, 3.5),
        (3.5, 3.6, 3.75),
        (11.1, 11.2, 12.95),
        (11.56, 11.57, 12.66),
        (500, 600, 700.89),
        (600, 600.65, 700),
        (2000, 2000.6578, 3000.987),
        (2000.1111, 2000.7869, 3000.7893)
    ]
)
def test_intg_ensr_is_in_range_throws_error_on_invalid_range(
    value: number,
    min_value: number,
    max_value: number
):
    """
    Tests the `is_in_range()` ensures validator method through `Condition.ensures_num()` to see if it,
    throws an ArgumentOutOfRangeError when it is supplied with a value not in the supplied range.
    """
    # Assert
    with pytest.raises(ArgumentOutOfRangeError):
        # Act
        Condition.ensures_num(value, 'value').is_in_range(min_value, max_value)


@pytest.mark.parametrize(
    'value,min_value,max_value',
    [
        (1, 2, 3),
        (9, 2, 3),
        (10, 11, 12),
        (15, 11, 12),
        (500, 600, 700),
        (800, 600, 700),
        (1000, 2000, 3000),
        (4000, 2000, 3000),
        (2.30, 2.35, 3.5),
        (3.5, 3.6, 3.75),
        (11.1, 11.2, 12.95),
        (11.56, 11.57, 12.66),
        (500, 600, 700.89),
        (600, 600.65, 700),
        (2000, 2000.6578, 3000.987),
        (2000.1111, 2000.7869, 3000.7893)
    ]
)
def test_intg_ensr_is_not_in_range_accepts_valid_range(
    value: number,
    min_value: number,
    max_value: number
):
    """
    Tests the `is_not_in_range()` ensures validator method through `Condition.ensures_num()` to see if it,
    does not throw an ArgumentOutOfRangeError when it is supplied with a value not in the
    supplied range.
    """
    # Act
    try:
        Condition.ensures_num(value, 'value').is_not_in_range(min_value, max_value)
    # Assert
    except ArgumentOutOfRangeError:
        pytest.fail(f'`{value}` should not have been accepted in the range `{min_value}-{max_value}`, but no error occurred.')


@pytest.mark.parametrize(
    'value,min_value,max_value',
    [
        (2, 2, 3),
        (3, 2, 3),
        (11, 11, 12),
        (12, 11, 12),
        (650, 600, 700),
        (700, 600, 700),
        (2000, 2000, 3000),
        (2500, 2000, 3000),
        (2.30, 2.25, 3.5),
        (3.5, 2, 3.75),
        (11.1, 11, 12.95),
        (12.56, 11, 12.66),
        (650, 600, 700.89),
        (700, 600.65, 700),
        (2000.6547, 2000, 3000.987),
        (2500.7869, 2000.1111, 3000.7893)
    ]
)
def test_intg_ensr_is_not_in_range_throws_error_on_invalid_range(
    value: number,
    min_value: number,
    max_value: number
):
    """
    Tests the `is_not_in_range()` ensures validator method through `Condition.ensures_num()` to see if it,
    throws an ArgumentOutOfRangeError when it is supplied with a value in the supplied range.
    """
    # Assert
    with pytest.raises(ArgumentOutOfRangeError):
        # Act
        Condition.ensures_num(value, 'value').is_not_in_range(min_value, max_value)


@pytest.mark.parametrize(
    'value,min_value',
    [
        (4, 3),
        (5, 4),
        (15, 12),
        (20, 15),
        (750, 700),
        (901, 900),
        (8350, 7000),
        (20000, 10000),
        (2.30, 2.25),
        (3.5, 2),
        (11.1, 11),
        (12.56, 11),
        (650, 600),
        (700, 600.65),
        (2000.6547, 2000),
        (2500.7869, 2000.1111)
    ]
)
def test_intg_ensr_is_greater_than_accepts_greater_than_value(
    value: number,
    min_value: number
):
    """
    Tests the `is_greater_than()` ensures validator method through `Condition.ensures_num()` to see if it,
    does not throw an ArgumentOutOfRangeError when it is supplied with a value that is
    greater than the minimum value.
    """
    # Act
    try:
        Condition.ensures_num(value, 'value').is_greater_than(min_value)
    # Assert
    except ArgumentOutOfRangeError:
        pytest.fail(f'`{value}` should be greater than `{min_value}`, but instead an error occurred.')


@pytest.mark.parametrize(
    'value,min_value',
    [
        (2, 3),
        (3, 4),
        (11, 12),
        (12, 15),
        (650, 700),
        (700, 900),
        (2000, 7000),
        (2500, 10000),
        (2.30, 3.5),
        (3.5, 3.75),
        (11.1, 12.95),
        (12.56, 12.66),
        (650, 700.89),
        (700, 700),
        (2000.6547, 3000.987),
        (2500.7869, 3000.7893)
    ]
)
def test_intg_ensr_is_greater_than_throws_error_on_less_than_value(
    value: number,
    min_value: number
):
    """
    Tests the `is_greater_than()` ensures validator method through `Condition.ensures_num()` to see if it,
    throws an ArgumentOutOfRangeError when it is supplied with a value that is less than
    the minimum value.
    """
    # Assert
    with pytest.raises(ArgumentOutOfRangeError):
        # Act
        Condition.ensures_num(value, 'value').is_greater_than(min_value)


@pytest.mark.parametrize(
    'value,min_value',
    [
        (2, 2),
        (3, 3),
        (11, 11),
        (12, 12),
        (650, 650),
        (700, 700),
        (2000, 2000),
        (2500, 2500),
        (2.30, 2.30),
        (3.5, 3.5),
        (11.1, 11.1),
        (12.56, 12.56),
        (650.3, 650.3),
        (600.65, 600.65),
        (2000.6547, 2000.6547),
        (2500.7869, 2500.7869)
    ]
)
def test_intg_ensr_is_greater_than_throws_error_on_equal_value(
    value: number,
    min_value: number
):
    """
    Tests the `is_greater_than()` ensures validator method through `Condition.ensures_num()` to see if it,
    throws an ArgumentOutOfRangeError when it is supplied with a value that is equal
    to the minimum value.
    """
    # Assert
    with pytest.raises(ArgumentOutOfRangeError):
        # Act
        Condition.ensures_num(value, 'value').is_greater_than(min_value)


@pytest.mark.parametrize(
    'value,min_value',
    [
        (4, 3),
        (5, 4),
        (15, 12),
        (20, 15),
        (750, 700),
        (901, 900),
        (8350, 7000),
        (20000, 10000),
        (2.30, 2.25),
        (3.5, 2),
        (11.1, 11),
        (12.56, 11),
        (650, 600),
        (700, 600.65),
        (2000.6547, 2000),
        (2500.7869, 2000.1111)
    ]
)
def test_intg_ensr_is_greater_or_equal_accepts_greater_than_value(
    value: number,
    min_value: number
):
    """
    Tests the `is_greater_or_equal()` ensures validator method through `Condition.ensures_num()` to see if it,
    does not throw an ArgumentOutOfRangeError when it is supplied with a value that is greater
    than the minimum value.
    """
    # Act
    try:
        Condition.ensures_num(value, 'value').is_greater_or_equal(min_value)
    # Assert
    except ArgumentOutOfRangeError:
        pytest.fail(f'`{value}` should be greater or equal to `{min_value}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,min_value',
    [
        (2, 2),
        (3, 3),
        (11, 11),
        (12, 12),
        (650, 650),
        (700, 700),
        (2000, 2000),
        (2500, 2500),
        (2.30, 2.30),
        (3.5, 3.5),
        (11.1, 11.1),
        (12.56, 12.56),
        (650.3, 650.3),
        (600.65, 600.65),
        (2000.6547, 2000.6547),
        (2500.7869, 2500.7869)
    ]
)
def test_intg_ensr_is_greater_or_equal_accepts_equal_value(
    value: number,
    min_value: number
):
    """
    Tests the `is_greater_or_equal()` ensures validator method through `Condition.ensures_num()` to see if it,
    does not throw an ArgumentOutOfRangeError when it is supplied with a value that is
    equal to the minimum value.
    """
    # Act
    try:
        Condition.ensures_num(value, 'value').is_greater_or_equal(min_value)
    # Assert
    except ArgumentOutOfRangeError:
        pytest.fail(f'`{value}` should be greater than or equal to `{min_value}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,min_value',
    [
        (2, 3),
        (3, 4),
        (11, 12),
        (12, 15),
        (650, 700),
        (700, 900),
        (2000, 7000),
        (2500, 10000),
        (2.30, 3.5),
        (3.5, 3.75),
        (11.1, 12.95),
        (12.56, 12.66),
        (650, 700.89),
        (700, 700.1),
        (2000.6547, 3000.987),
        (2500.7869, 3000.7893)
    ]
)
def test_intg_ensr_is_greater_or_equal_throws_error_on_less_than_value(
    value: number,
    min_value: number
):
    """
    Tests the `is_greater_or_equal()` ensures validator method through `Condition.ensures_num()` to see if it,
    throws an ArgumentOutOfRangeError when it is supplied with a value that is less than the
    minimum value.
    """
    # Assert
    with pytest.raises(ArgumentOutOfRangeError):
        # Act
        Condition.ensures_num(value, 'value').is_greater_or_equal(min_value)


@pytest.mark.parametrize(
    'value,max_value',
    [
        (2, 3),
        (3, 4),
        (11, 12),
        (12, 15),
        (650, 700),
        (700, 900),
        (2000, 7000),
        (2500, 10000),
        (2.30, 3.5),
        (3.5, 3.75),
        (11.1, 12.95),
        (12.56, 12.66),
        (650, 700.89),
        (700, 700.1),
        (2000.6547, 3000.987),
        (2500.7869, 3000.7893)
    ]
)
def test_intg_ensr_is_less_than_accepts_less_than_value(
    value: number,
    max_value: number
):
    """
    Tests the `is_less_than()` ensures validator method through `Condition.ensures_num()` to see if it,
    does not throw an ArgumentOutOfRangeError when it is supplied with a value that is
    less than the maximum value.
    """
    # Act
    try:
        Condition.ensures_num(value, 'value').is_less_than(max_value)
    # Assert
    except ArgumentOutOfRangeError:
        pytest.fail(f'`{value}` should be less than `{max_value}`, but instead an error occurred.')


@pytest.mark.parametrize(
    'value,max_value',
    [
        (4, 3),
        (5, 4),
        (15, 12),
        (20, 15),
        (750, 700),
        (901, 900),
        (8350, 7000),
        (20000, 10000),
        (2.30, 2.25),
        (3.5, 2),
        (11.1, 11),
        (12.56, 11),
        (650, 600),
        (700, 600.65),
        (2000.6547, 2000),
        (2500.7869, 2000.1111)
    ]
)
def test_intg_ensr_is_less_than_throws_error_on_greater_than_value(
    value: number,
    max_value: number
):
    """
    Tests the `is_less_than()` ensures validator method through `Condition.ensures_num()` to see if it,
    throws an ArgumentOutOfRangeError when it is supplied with a value that is greater
    than the maximum value.
    """
    # Assert
    with pytest.raises(ArgumentOutOfRangeError):
        # Act
        Condition.ensures_num(value, 'value').is_less_than(max_value)


@pytest.mark.parametrize(
    'value,max_value',
    [
        (2, 2),
        (3, 3),
        (11, 11),
        (12, 12),
        (650, 650),
        (700, 700),
        (2000, 2000),
        (2500, 2500),
        (2.30, 2.30),
        (3.5, 3.5),
        (11.1, 11.1),
        (12.56, 12.56),
        (650.3, 650.3),
        (600.65, 600.65),
        (2000.6547, 2000.6547),
        (2500.7869, 2500.7869)
    ]
)
def test_intg_ensr_is_less_than_throws_error_on_equal_value(
    value: number,
    max_value: number
):
    """
    Tests the `is_less_than()` ensures validator method through `Condition.ensures_num()` to see if it,
    throws an ArgumentOutOfRangeError when it is supplied with a value that is equal
    to the maximum value.
    """
    # Assert
    with pytest.raises(ArgumentOutOfRangeError):
        # Act
        Condition.ensures_num(value, 'value').is_less_than(max_value)


@pytest.mark.parametrize(
    'value,max_value',
    [
        (2, 3),
        (3, 4),
        (11, 12),
        (12, 15),
        (650, 700),
        (700, 900),
        (2000, 7000),
        (2500, 10000),
        (2.30, 3.5),
        (3.5, 3.75),
        (11.1, 12.95),
        (12.56, 12.66),
        (650, 700.89),
        (700, 700.1),
        (2000.6547, 3000.987),
        (2500.7869, 3000.7893)
    ]
)
def test_intg_ensr_is_less_or_equal_accepts_less_than_value(
    value: number,
    max_value: number
):
    """
    Tests the `is_less_or_equal()` ensures validator method through `Condition.ensures_num()` to see if it,
    does not throw an ArgumentOutOfRangeError when it is supplied with a value that is less
    than the maximum value.
    """
    # Act
    try:
        Condition.ensures_num(value, 'value').is_less_or_equal(max_value)
    # Assert
    except ArgumentOutOfRangeError:
        pytest.fail(f'`{value}` should be less than or equal to `{max_value}`, but instead an error occurred.')


@pytest.mark.parametrize(
    'value,max_value',
    [
        (2, 2),
        (3, 3),
        (11, 11),
        (12, 12),
        (650, 650),
        (700, 700),
        (2000, 2000),
        (2500, 2500),
        (2.30, 2.30),
        (3.5, 3.5),
        (11.1, 11.1),
        (12.56, 12.56),
        (650.3, 650.3),
        (600.65, 600.65),
        (2000.6547, 2000.6547),
        (2500.7869, 2500.7869)
    ]
)
def test_intg_ensr_is_less_or_equal_accepts_equal_value(
    value: number,
    max_value: number
):
    """
    Tests the `is_less_or_equal()` ensures validator method through `Condition.ensures_num()` to see if it,
    does not throw an ArgumentOutOfRangeError when it is supplied with a value that is
    equal to the maximum value.
    """
    # Act
    try:
        Condition.ensures_num(value, 'value').is_less_or_equal(max_value)
    # Assert
    except ArgumentOutOfRangeError:
        pytest.fail()


@pytest.mark.parametrize(
    'value,max_value',
    [
        (4, 3),
        (5, 4),
        (15, 12),
        (20, 15),
        (750, 700),
        (901, 900),
        (8350, 7000),
        (20000, 10000),
        (2.30, 2.25),
        (3.5, 2),
        (11.1, 11),
        (12.56, 11),
        (650, 600),
        (700, 600.65),
        (2000.6547, 2000),
        (2500.7869, 2000.1111)
    ]
)
def test_intg_ensr_is_less_or_equal_throws_error_on_greater_than_value(
    value: number,
    max_value: number
):
    """
    Tests the `is_less_or_equal()` ensures validator method through `Condition.ensures_num()` to see if it,
    throws an ArgumentOutOfRangeError when it is supplied with a value that is greater than
    the maximum value.
    """
    # Assert
    with pytest.raises(ArgumentOutOfRangeError):
        # Act
        Condition.ensures_num(value, 'value').is_less_or_equal(max_value)


@pytest.mark.parametrize(
    'value,equal_to',
    [
        (2, 2),
        (3, 3),
        (11, 11),
        (12, 12),
        (650, 650),
        (700, 700),
        (2000, 2000),
        (2500, 2500),
        (2.30, 2.30),
        (3.5, 3.5),
        (11.1, 11.1),
        (12.56, 12.56),
        (650.3, 650.3),
        (600.65, 600.65),
        (2000.6547, 2000.6547),
        (2500.7869, 2500.7869)
    ]
)
def test_intg_ensr_is_equal_to_accepts_valid_value(
    value: number,
    equal_to: number
):
    """
    Tests the `is_equal()` ensures validator method through `Condition.ensures_num()` to see if it,
    does not throw an ArgumentOutOfRangeError when it is supplied with a value that is
    equal to the equal value.
    """
    # Act
    try:
        Condition.ensures_num(value, 'value').is_equal_to(equal_to)
    # Assert
    except ArgumentOutOfRangeError:
        pytest.fail()


@pytest.mark.parametrize(
    'value,not_equal_to',
    [
        (2, 3),
        (3, 4),
        (11, 12),
        (12, 15),
        (650, 700),
        (700, 900),
        (2000, 7000),
        (2500, 10000),
        (2.30, 3.5),
        (3.5, 3.75),
        (11.1, 12.95),
        (12.56, 12.66),
        (650, 700.89),
        (700, 700.1),
        (2000.6547, 3000.987),
        (2500.7869, 3000.7893)
    ]
)
def test_intg_ensr_is_equal_to_throws_error_on_invalid_value(
    value: number,
    not_equal_to: number
):
    """
    Tests the `is_equal()` ensures validator method through `Condition.ensures_num()` to see if it,
    throws an ArgumentOutOfRangeError when it is supplied with a value that is not
    equal to the equal value.
    """
    # Assert
    with pytest.raises(ArgumentOutOfRangeError):
        # Act
        Condition.ensures_num(value, 'value').is_equal_to(not_equal_to)


@pytest.mark.parametrize(
    'value,equal_to',
    [
        (2, 3),
        (3, 4),
        (11, 12),
        (12, 15),
        (650, 700),
        (700, 900),
        (2000, 7000),
        (2500, 10000),
        (2.30, 3.5),
        (3.5, 3.75),
        (11.1, 12.95),
        (12.56, 12.66),
        (650, 700.89),
        (700, 700.1),
        (2000.6547, 3000.987),
        (2500.7869, 3000.7893)
    ]
)
def test_intg_ensr_is_not_equal_to_accepts_valid_value(
    value: number,
    equal_to: number
):
    """
    Tests the `is_not_equal()` ensures validator method through `Condition.ensures_num()` to see if it,
    does not throw an ArgumentOutOfRangeError when it is supplied with a value that is
    not equal to the not equal value.
    """
    # Act
    try:
        Condition.ensures_num(value, 'value').is_not_equal_to(equal_to)
    # Assert
    except ArgumentOutOfRangeError:
        pytest.fail()


@pytest.mark.parametrize(
    'value,not_equal_to',
    [
        (2, 2),
        (3, 3),
        (11, 11),
        (12, 12),
        (650, 650),
        (700, 700),
        (2000, 2000),
        (2500, 2500),
        (2.30, 2.30),
        (3.5, 3.5),
        (11.1, 11.1),
        (12.56, 12.56),
        (650.3, 650.3),
        (600.65, 600.65),
        (2000.6547, 2000.6547),
        (2500.7869, 2500.7869)
    ]
)
def test_intg_ensr_is_not_equal_to_throws_error_on_invalid_value(
    value: number,
    not_equal_to: number
):
    """
    Tests the `is_not_equal()` ensures validator method through `Condition.ensures_num()` to see if it,
    throws an ArgumentOutOfRangeError when it is supplied with a value that is equal
    to the not equal value.
    """
    # Assert
    with pytest.raises(ArgumentOutOfRangeError):
        # Act
        Condition.ensures_num(value, 'value').is_not_equal_to(not_equal_to)


@pytest.mark.parametrize(
    'value',
    [
        (2),
        (3),
        (11),
        (12),
        (650),
        (700),
        (2000),
        (2500),
        (2.30),
        (3.5),
        (11.1),
        (12.56),
        (650.3),
        (600.65),
        (2000.6547),
        (2500.7869)
    ]
)
def test_intg_ensr_is_positive_accepts_positive_number(value: number):
    """
    Tests the `is_positive()` ensures validator method does not throw an ArgumentOutOfRangeError
    when the value is a positive number.
    """
    # Act
    try:
        Condition.ensures_num(value, 'value').is_positive()
    # Assert
    except ArgumentOutOfRangeError:
        pytest.fail()


@pytest.mark.parametrize(
    'value',
    [
        (-2),
        (-3),
        (-11),
        (-12),
        (-650),
        (-700),
        (-2000),
        (-2500),
        (-2.30),
        (-3.5),
        (-11.1),
        (-12.56),
        (-650.3),
        (-600.65),
        (-2000.6547),
        (-2500.7869)
    ]
)
def test_intg_ensr_is_positive_throws_error_on_negative_number(value: number):
    """
    Tests the `is_positive()` ensures validator method does not throw an ArgumentOutOfRangeError
    when the value is a negative number.
    """
    # Assert
    with pytest.raises(ArgumentOutOfRangeError):
        # Act
        Condition.ensures_num(value, 'value').is_positive()


@pytest.mark.parametrize(
    'value',
    [
        (-2),
        (-3),
        (-11),
        (-12),
        (-650),
        (-700),
        (-2000),
        (-2500),
        (-2.30),
        (-3.5),
        (-11.1),
        (-12.56),
        (-650.3),
        (-600.65),
        (-2000.6547),
        (-2500.7869)
    ]
)
def test_intg_ensr_is_negative_accepts_negative_number(value: number):
    """
    Tests the `is_negative()` ensures validator method does not throw an ArgumentOutOfRangeError
    when the value is a negative number.
    """
    # Act
    try:
        Condition.ensures_num(value, 'value').is_negative()
    # Assert
    except ArgumentOutOfRangeError:
        pytest.fail()


@pytest.mark.parametrize(
    'value',
    [
        (2),
        (3),
        (11),
        (12),
        (650),
        (700),
        (2000),
        (2500),
        (2.30),
        (3.5),
        (11.1),
        (12.56),
        (650.3),
        (600.65),
        (2000.6547),
        (2500.7869)
    ]
)
def test_intg_ensr_is_negative_throws_error_on_positive_number(value: number):
    """
    Tests the `is_negative()` ensures validator method does not throw an ArgumentOutOfRangeError
    when the value is a positive number.
    """
    # Assert
    with pytest.raises(ArgumentOutOfRangeError):
        # Act
        Condition.ensures_num(value, 'value').is_negative()