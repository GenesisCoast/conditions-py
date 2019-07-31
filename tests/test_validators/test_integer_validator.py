import pytest

from src.errors.argument_error import ArgumentError
from src.errors.argument_out_of_range_error import ArgumentOutOfRangeError
from src.validators.integer_validator import IntegerValidator


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
        (2500, 2000, 3000)
    ]
)
def test_is_in_range_accepts_valid_range(
    value: int,
    min_value: int,
    max_value: int
):
    """

    """
    # Arrange
    validator = IntegerValidator(value, 'value')

    # Act
    try:
        validator.is_in_range(min_value, max_value)
    # Assert
    except ArgumentOutOfRangeError:
        pytest.fail(f'{value} should have been accepted in the range `{min_value}-{max_value}`, but instead an error occurred.')



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
        (4000, 2000, 3000)
    ]
)
def test_is_in_range_throws_error_on_invalid_range(
    value: int,
    min_value: int,
    max_value: int
):
    """

    """
    # Arrange
    validator = IntegerValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentOutOfRangeError):
        # Act
        validator.is_in_range(min_value, max_value)


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
        (4000, 2000, 3000)
    ]
)
def test_is_not_in_range_accepts_valid_range(
    value: int,
    min_value: int,
    max_value: int
):
    """

    """
    # Arrange
    validator = IntegerValidator(value, 'value')

    # Act
    try:
        validator.is_not_in_range(min_value, max_value)
    # Assert
    except ArgumentOutOfRangeError:
        pytest.fail(f'{value} should not have been accepted in the range `{min_value}-{max_value}`, but no error occurred.')


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
        (2500, 2000, 3000)
    ]
)
def test_is_not_in_range_throws_error_on_invalid_range(
    value: int,
    min_value: int,
    max_value: int
):
    """

    """
    # Arrange
    validator = IntegerValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentOutOfRangeError):
        # Act
        validator.is_not_in_range(min_value, max_value)


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
        (20000, 10000)
    ]
)
def test_is_greater_than_accepts_greater_than_value(
    value: int,
    min_value: int
):
    """

    """
    # Arrange
    validator = IntegerValidator(value, "value")

    # Act
    try:
        validator.is_greater_than(min_value)
    # Assert
    except ArgumentOutOfRangeError:
        pytest.fail()


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
        (2500, 10000)
    ]
)
def test_is_greater_than_throws_error_on_less_than_value(
    value: int,
    min_value: int
):
    """

    """
    # Arrange
    validator = IntegerValidator(value, "value")

    # Assert
    with pytest.raises(ArgumentOutOfRangeError):
        # Act
        validator.is_greater_than(min_value)


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
        (2500, 2500)
    ]
)
def test_is_greater_than_throws_error_on_equal_value(
    value: int,
    min_value: int
):
    """

    """
    # Arrange
    validator = IntegerValidator(value, "value")

    # Assert
    with pytest.raises(ArgumentOutOfRangeError):
        # Act
        validator.is_greater_than(min_value)


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
        (20000, 10000)
    ]
)
def test_is_greater_or_equal_accepts_greater_than_value(
    value: int,
    min_value: int
):
    """

    """
    # Arrange
    validator = IntegerValidator(value, "value")

    # Act
    try:
        validator.is_greater_or_equal(min_value)
    # Assert
    except ArgumentOutOfRangeError:
        pytest.fail()


@pytest.mark.parametrize(
    'value,min_value',
    [
        (3, 3),
        (4, 4),
        (12, 12),
        (15, 15),
        (700, 700),
        (900, 900),
        (8350, 8350),
        (10000, 10000)
    ]
)
def test_is_greater_or_equal_accepts_equal_value(
    value: int,
    min_value: int
):
    """

    """
    # Arrange
    validator = IntegerValidator(value, "value")

    # Act
    try:
        validator.is_greater_or_equal(min_value)
    # Assert
    except ArgumentOutOfRangeError:
        pytest.fail()


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
        (2500, 10000)
    ]
)
def test_is_greater_or_equal_throws_error_on_less_than_value(
    value: int,
    min_value: int
):
    """

    """
    # Arrange
    validator = IntegerValidator(value, "value")

    # Assert
    with pytest.raises(ArgumentOutOfRangeError):
        # Act
        validator.is_greater_or_equal(min_value)



@pytest.mark.parametrize(
    'value,max_value',
    [
        (2, 3),
        (3, 4),
        (11, 12),
        (10, 15),
        (653, 700),
        (657, 900),
        (3478, 7000),
        (8765, 10000)
    ]
)
def test_is_less_than_accepts_less_than_value(
    value: int,
    max_value: int
):
    """

    """
    # Arrange
    validator = IntegerValidator(value, "value")

    # Act
    try:
        validator.is_less_than(max_value)
    # Assert
    except ArgumentOutOfRangeError:
        pytest.fail()


@pytest.mark.parametrize(
    'value,max_value',
    [
        (5, 3),
        (7, 4),
        (20, 12),
        (50, 15),
        (894, 700),
        (1024, 900),
        (10000, 7000),
        (50000, 10000)
    ]
)
def test_is_less_than_throws_error_on_greater_than_value(
    value: int,
    max_value: int
):
    """

    """
    # Arrange
    validator = IntegerValidator(value, "value")

    # Assert
    with pytest.raises(ArgumentOutOfRangeError):
        # Act
        validator.is_less_than(max_value)


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
        (2500, 2500)
    ]
)
def test_is_less_than_throws_error_on_equal_value(
    value: int,
    max_value: int
):
    """

    """
    # Arrange
    validator = IntegerValidator(value, "value")

    # Assert
    with pytest.raises(ArgumentOutOfRangeError):
        # Act
        validator.is_less_than(max_value)


@pytest.mark.parametrize(
    'value,max_value',
    [
        (2, 3),
        (3, 4),
        (11, 12),
        (10, 15),
        (653, 700),
        (657, 900),
        (3478, 7000),
        (8765, 10000)
    ]
)
def test_is_less_or_equal_accepts_less_than_value(
    value: int,
    max_value: int
):
    """

    """
    # Arrange
    validator = IntegerValidator(value, "value")

    # Act
    try:
        validator.is_less_or_equal(max_value)
    # Assert
    except ArgumentOutOfRangeError:
        pytest.fail()


@pytest.mark.parametrize(
    'value,max_value',
    [
        (3, 3),
        (4, 4),
        (12, 12),
        (15, 15),
        (700, 700),
        (900, 900),
        (8350, 8350),
        (10000, 10000)
    ]
)
def test_is_less_or_equal_accepts_equal_value(
    value: int,
    max_value: int
):
    """

    """
    # Arrange
    validator = IntegerValidator(value, "value")

    # Act
    try:
        validator.is_less_or_equal(max_value)
    # Assert
    except ArgumentOutOfRangeError:
        pytest.fail()


@pytest.mark.parametrize(
    'value,max_value',
    [
        (5, 3),
        (7, 4),
        (20, 12),
        (50, 15),
        (894, 700),
        (1024, 900),
        (10000, 7000),
        (50000, 10000)
    ]
)
def test_is_less_or_equal_throws_error_on_greater_than_value(
    value: int,
    max_value: int
):
    """

    """
    # Arrange
    validator = IntegerValidator(value, "value")

    # Assert
    with pytest.raises(ArgumentOutOfRangeError):
        # Act
        validator.is_less_or_equal(max_value)