import pytest
from src.condition import Condition
from src.errors.argument_error import ArgumentError
from src.errors.argument_pattern_error import ArgumentPatternError
from src.errors.argument_null_error import ArgumentNullError


EMPTY_STRING = ''
WHITESPACE_STRING = ' '


@pytest.mark.parametrize(
    'value',
    [
        ('hello world'),
        ('test'),
        ('lorem ipsum!'),
        ('this_is_a_value')
    ]
)
def test_intg_rqr_prnt_get_value_returns_value(value):
    """
    Tests if the parent `get_value()` requires validator method returns the value saved in the validator.
    """
    # Act
    actual = Condition.requires_str(value, 'value').get_value()

    # Assert
    assert actual == value
    assert actual is value
    assert type(actual) == type(value)


def test_intg_rqr_is_null_accepts_null_value():
    """
    Tests the `is_null()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when it is supplied with a None
    (Null) value.
    """
    # Arrange
    value = None

    # Act
    try:
        Condition.requires_str(value, 'value').is_null()
    # Assert
    except ArgumentNullError:
        pytest.fail(f'`{value}` should have been None (Null), but an error occurred instead.')


def test_intg_rqr_is_null_throws_error_on_whitespace_value():
    """
    Tests the `is_null()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with a whitespace value.
    """
    # Arrange
    value = WHITESPACE_STRING

    # Assert
    with pytest.raises(ArgumentNullError):
        # Act
        Condition.requires_str(value, 'value').is_null()


def test_intg_rqr_is_null_throws_error_on_empty_value():
    """
    Tests the `is_null()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with an empty value.
    """
    # Arrange
    value = EMPTY_STRING

    # Assert
    with pytest.raises(ArgumentNullError):
        # Act
        Condition.requires_str(value, 'value').is_null()


@pytest.mark.parametrize(
    'value',
    [
        ('1234'),
        ('test'),
        ('this_is_my_value')
    ]
)
def test_intg_rqr_is_null_throws_error_on_invalid_value(value: str):
    """
    Tests the `is_null()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with an invalid value.
    """
    # Assert
    with pytest.raises(ArgumentNullError):
        # Act
        Condition.requires_str(value, 'value').is_null()


def test_intg_rqr_is_not_null_accepts_whitespace_value():
    """
    Tests the `is_not_null()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with a whitespace value.
    """
    # Arrange
    value = WHITESPACE_STRING

    # Act
    try:
        Condition.requires_str(value, 'value').is_not_null()
    # Assert
    except ArgumentNullError:
        pytest.fail(f'`{value}` should not have been None (Null), but an error occurred instead.')


def test_intg_rqr_is_not_null_accepts_empty_value():
    """
    Tests the `is_not_null()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with a empty value.
    """
    # Arrange
    value = EMPTY_STRING

    # Act
    try:
        Condition.requires_str(value, 'value').is_not_null()
    # Assert
    except ArgumentNullError:
        pytest.fail(f'`{value}` should not have been None (Null), but an error occurred instead.')


@pytest.mark.parametrize(
    'value',
    [
        ('1234'),
        ('test'),
        ('this_is_my_value')
    ]
)
def test_intg_rqr_is_not_null_accepts_valid_value(value: str):
    """
    Tests the `is_not_null()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with a valid value.
    """
    # Act
    try:
        Condition.requires_str(value, 'value').is_not_null()
    # Assert
    except ArgumentNullError:
        pytest.fail(f'`{value}` should not have been None (Null), but an error occurred instead.')


def test_intg_rqr_is_not_null_throws_error_on_null_value():
    """
    Tests the `is_not_null()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with a None (Null) value.
    """
    # Arrange
    value = None

    # Assert
    with pytest.raises(ArgumentNullError):
        # Act
        Condition.requires_str(value, 'value').is_not_null()


def test_intg_rqr_is_null_or_empty_accepts_null_value():
    """
    Tests the `is_null_or_empty()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when it is supplied with a None (Null) value.
    """
    # Arrange
    value = None

    # Act
    try:
        Condition.requires_str(value, 'value').is_null_or_empty()
    # Assert
    except ArgumentNullError:
        pytest.fail(f'`{value}` should have been None (Null) or empty, but an error occurred instead.')


def test_intg_rqr_is_null_or_empty_accepts_empty_value():
    """
    Tests the `is_null_or_empty()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with a empty value.
    """
    # Arrange
    value = EMPTY_STRING

    # Act
    try:
        Condition.requires_str(value, 'value').is_null_or_empty()
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should have been None (Null) or empty, but an error occurred instead.')


def test_intg_rqr_is_null_or_empty_throws_error_on_whitespace_value():
    """
    Tests the `is_null_or_empty()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with a whitespace value.
    """
    # Arrange
    value = WHITESPACE_STRING

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').is_null_or_empty()


@pytest.mark.parametrize(
    'value',
    [
        ('1234'),
        ('test'),
        ('this_is_my_value')
    ]
)
def test_intg_rqr_is_null_or_empty_throws_error_on_invalid_value(value: str):
    """
    Tests the `is_null_or_empty()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with an invalid value.
    """
    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').is_null_or_empty()


def test_intg_rqr_is_not_null_or_empty_accepts_whitespace_value():
    """
    Tests the `is_not_null_or_empty()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when it is supplied with a whitespace value.
    """
    # Arrange
    value = WHITESPACE_STRING

    # Act
    try:
        Condition.requires_str(value, 'value').is_not_null_or_empty()
    # Assert
    except (ArgumentError, ArgumentNullError):
        pytest.fail(f'`{value}` should not have been None (Null) or empty, but an error occurred instead.')


@pytest.mark.parametrize(
    'value',
    [
        ('1234'),
        ('test'),
        ('this_is_my_value')
    ]
)
def test_intg_rqr_is_not_null_or_empty_accepts_valid_value(value: str):
    """
    Tests the `is_not_null_or_empty()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when it is supplied with a valid value.
    """
    # Assert
    try:
        Condition.requires_str(value, 'value').is_not_null_or_empty()
    # Assert
    except (ArgumentError, ArgumentNullError):
        pytest.fail(f'`{value}` should not have been None (Null) or empty, but an error occurred instead.')


def test_intg_rqr_is_not_null_or_empty_throw_error_on_null_value():
    """
    Tests the `is_not_null_or_empty()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with a None (Null) value.
    """
    # Arrange
    value = None

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').is_not_null_or_empty()


def test_intg_rqr_is_not_null_or_empty_throw_error_on_empty_value():
    """
    Tests the `is_not_null_or_empty()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with a empty value.
    """
    # Arrange
    value = EMPTY_STRING

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').is_not_null_or_empty()


def test_intg_rqr_is_null_or_whitespace_accepts_null_value():
    """
    Tests the `is_not_null_or_whitespace()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when it is supplied with a None (Null) value.
    """
    # Arrange
    value = None

    # Act
    try:
        Condition.requires_str(value, 'value').is_null_or_whitespace()
    # Assert
    except ArgumentNullError:
        pytest.fail(f'`{value}` should have been None (Null), empty or whitespace, but an error occurred instead.')


def test_intg_rqr_is_null_or_whitespace_accepts_empty_value():
    """
    Tests the `is_not_null_or_whitespace()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when it is supplied with a empty value.
    """
    # Arrange
    value = EMPTY_STRING

    # Act
    try:
        Condition.requires_str(value, 'value').is_null_or_whitespace()
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should have been None (Null), empty or whitespace, but an error occurred instead.')


def test_intg_rqr_is_null_or_whitespace_accepts_whitespace_value():
    """
    Tests the `is_not_null_or_whitespace()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when it is supplied with a whitespace value.
    """
    # Arrange
    value = WHITESPACE_STRING

    # Act
    try:
        Condition.requires_str(value, 'value').is_null_or_whitespace()
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should have been None (Null), empty or whitespace, but an error occurred instead.')


@pytest.mark.parametrize(
    'value',
    [
        ('1234'),
        ('test'),
        ('this_is_my_value')
    ]
)
def test_intg_rqr_is_null_or_whitespace_throws_error_on_invalid_value(value: str):
    """
    Tests the `is_not_null_or_whitespace()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with an invalid value.
    """
    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').is_null_or_whitespace()


@pytest.mark.parametrize(
    'value',
    [
        ('1234'),
        ('test'),
        ('this_is_my_value')
    ]
)
def test_intg_rqr_is_not_null_or_whitespace_accepts_valid_value(value: str):
    """
    Tests the `is_not_null_or_whitespace()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when it is supplied with a valid value.
    """
    # Assert
    try:
        Condition.requires_str(value, 'value').is_not_null_or_whitespace()
    # Assert
    except (ArgumentError, ArgumentNullError):
        pytest.fail(f'`{value}` should not have been None (Null) or empty, but an error occurred instead.')


def test_intg_rqr_is_not_null_or_whitespace_throws_error_on_whitespace_value():
    """
    Tests the `is_not_null_or_whitespace()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with a whitespace value.
    """
    # Arrange
    value = WHITESPACE_STRING

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').is_not_null_or_whitespace()


def test_intg_rqr_is_not_null_or_whitespace_throw_error_on_null_value():
    """
    Tests the `is_not_null_or_whitespace()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with a None (Null) value.
    """
    # Arrange
    value = None

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').is_not_null_or_whitespace()


def test_intg_rqr_is_not_null_or_whitespace_throw_error_on_empty_value():
    """
    Tests the `is_not_null_or_whitespace()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with a whitespace value.
    """
    # Arrange
    value = EMPTY_STRING

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').is_not_null_or_whitespace()


@pytest.mark.parametrize(
    'value,max_length',
    [
        ('1234', 5),
        ('test', 6),
        ('this_is_my_value', 20)
    ]
)
def test_intg_rqr_is_shorter_than_accepts_shorter_length(value: str, max_length: int):
    """
    Tests the `is_shorter_than()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when it is supplied with a shorter length.
    """
    # Act
    try:
        Condition.requires_str(value, 'value').is_shorter_than(max_length)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should be shorter than `{max_length}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,max_length',
    [
        ('1234', 3),
        ('test', 1),
        ('this_is_my_value', 10)
    ]
)
def test_intg_rqr_is_shorter_than_throws_error_on_longer_length(value: str, max_length: int):
    """
    Tests the `is_shorter_than()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with a longer length.
    """
    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').is_shorter_than(max_length)


@pytest.mark.parametrize(
    'value,max_length',
    [
        ('1234', 4),
        ('test', 4),
        ('this_is_my_value', 16)
    ]
)
def test_intg_rqr_is_shorter_than_throws_error_on_equal_length(value: str, max_length: int):
    """
    Tests the `is_shorter_than()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with a equal length.
    """
    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').is_shorter_than(max_length)


@pytest.mark.parametrize(
    'value,max_length',
    [
        ('1234', 5),
        ('test', 6),
        ('this_is_my_value', 20)
    ]
)
def test_intg_rqr_is_shorter_or_equal_accepts_shorter_length(value: str, max_length: int):
    """
    Tests the `is_shorter_or_equal()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when it is supplied with a shorter length.
    """
    # Act
    try:
        Condition.requires_str(value, 'value').is_shorter_or_equal(max_length)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should be shorter or equal to `{max_length}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,max_length',
    [
        ('1234', 4),
        ('test', 4),
        ('this_is_my_value', 16)
    ]
)
def test_intg_rqr_is_shorter_or_equal_accepts_equal_length(value: str, max_length: int):
    """
    Tests the `is_shorter_or_equal()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when it is supplied with a equal length.
    """
    # Act
    try:
        Condition.requires_str(value, 'value').is_shorter_or_equal(max_length)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should be shorter or equal to `{max_length}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,max_length',
    [
        ('1234', 3),
        ('test', 1),
        ('this_is_my_value', 10)
    ]
)
def test_intg_rqr_is_shorter_or_equal_throws_error_on_longer_length(value: str, max_length: int):
    """
    Tests the `is_shorter_or_equal()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with a longer length.
    """
    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').is_shorter_or_equal(max_length)


@pytest.mark.parametrize(
    'value,min_length',
    [
        ('1234', 2),
        ('test', 1),
        ('this_is_my_value', 9)
    ]
)
def test_intg_rqr_is_longer_than_accepts_longer_length(value: str, min_length: int):
    """
    Tests the `is_longer_than()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when it is supplied with a longer length.
    """
    # Act
    try:
        Condition.requires_str(value, 'value').is_longer_than(min_length)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should be longer than `{min_length}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,min_length',
    [
        ('1234', 4),
        ('test', 4),
        ('this_is_my_value', 16)
    ]
)
def test_intg_rqr_is_longer_than_throws_error_on_equal_length(value: str, min_length: int):
    """
    Tests the `is_longer_than()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with a equal length.
    """
    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').is_longer_than(min_length)


@pytest.mark.parametrize(
    'value,min_length',
    [
        ('1234', 4),
        ('test', 9),
        ('this_is_my_value', 50)
    ]
)
def test_intg_rqr_is_longer_than_throws_error_on_shorter_length(value: str, min_length: int):
    """
    Tests the `is_longer_than()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with a shorter length.
    """
    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').is_longer_than(min_length)


@pytest.mark.parametrize(
    'value,min_length',
    [
        ('1234', 2),
        ('test', 1),
        ('this_is_my_value', 9)
    ]
)
def test_intg_rqr_is_longer_or_equal_accepts_longer_length(value: str, min_length: int):
    """
    Tests the `is_longer_or_equal()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when it is supplied with a longer length.
    """
    # Act
    try:
        Condition.requires_str(value, 'value').is_longer_or_equal(min_length)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should be longer or equal to `{min_length}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,min_length',
    [
        ('1234', 4),
        ('test', 4),
        ('this_is_my_value', 16)
    ]
)
def test_intg_rqr_is_longer_or_equal_accepts_equal_length(value: str, min_length: int):
    """
    Tests the `is_longer_or_equal()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when it is supplied with a equal length.
    """
    # Act
    try:
        Condition.requires_str(value, 'value').is_longer_or_equal(min_length)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should be longer or equal to `{min_length}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,min_length',
    [
        ('1234', 5),
        ('test', 9),
        ('this_is_my_value', 50)
    ]
)
def test_intg_rqr_is_longer_or_equal_throws_error_on_shorter_length(value: str, min_length: int):
    """
    Tests the `is_longer_or_equal()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with a shorter length.
    """
    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').is_longer_or_equal(min_length)


@pytest.mark.parametrize(
    'value,length',
    [
        ('1234', 4),
        ('test', 4),
        ('this_is_my_value', 16)
    ]
)
def test_intg_rqr_has_length_accepts_equal_length(value: str, length: int):
    """
    Tests the `has_length()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when it is supplied with a equal length.
    """
    # Act
    try:
        Condition.requires_str(value, 'value').has_length(length)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should have the length `{length}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,length',
    [
        ('1234', 7),
        ('test', 9),
        ('this_is_my_value', 50)
    ]
)
def test_intg_rqr_has_length_throws_error_on_notequal_length(value: str, length: int):
    """
    Tests the `has_length()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with a not equal length.
    """
    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').has_length(length)


@pytest.mark.parametrize(
    'value,length',
    [
        ('1234', 4),
        ('test', 4),
        ('this_is_my_value', 16)
    ]
)
def test_intg_rqr_does_not_have_length_throws_error_on_equal_length(value: str, length: int):
    """
    Tests the `does_not_have_length()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when it is supplied with a equal length.
    """
    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').does_not_have_length(length)


@pytest.mark.parametrize(
    'value,length',
    [
        ('1234', 7),
        ('test', 9),
        ('this_is_my_value', 50)
    ]
)
def test_intg_rqr_does_not_have_length_accepts_notequal_length(value: str, length: int):
    """
    Tests the `does_not_have_length()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when it is supplied with a not equal length.
    """
    # Act
    try:
        Condition.requires_str(value, 'value').does_not_have_length(length)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should not have the length `{length}`, but an error occurred.')


def test_intg_rqr_equals_accepts_equal_value():
    """
    Tests the `equals()` requires validator method does not throw an ArgumentError
    when the value is equal to the specified value.
    """
    # Arrange
    value = 'Hello World!'

    # Act
    try:
        Condition.requires_str(value, 'value').equals(value)
    # Assert
    except ArgumentError:
        pytest.fail()


def test_intg_rqr_equals_throws_error_on_notequal_value():
    """
    Tests the `equals()` requires validator method throws an ArgumentError
    when the value is not equal to the specified value.
    """
    # Arrange
    value = 'Hello World!'
    equals = 'Test'

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').equals(equals)


def test_intg_rqr_does_not_equal_accepts_notequal_value():
    """
    Tests the `equals()` requires validator method does not throw an ArgumentError
    when the value is equal to the specified value.
    """
    # Arrange
    value = 'Hello World!'
    not_equals = 'Test'

    # Act
    try:
        Condition.requires_str(value, 'value').does_not_equal(not_equals)
    # Assert
    except ArgumentError:
        pytest.fail()


def test_intg_rqr_does_not_equal_throws_error_on_equal_value():
    """
    Tests the `equals()` requires validator method throws an ArgumentError
    when the value is not equal to the specified value.
    """
    # Arrange
    value = 'Hello World!'

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').does_not_equal(value)


@pytest.mark.parametrize(
    'value,starts_with',
    [
        ('1234', '1'),
        ('test', 'tes'),
        ('this_is_my_value', 'this_is_my')
    ]
)
def test_intg_rqr_starts_with_accepts_valid_value(value: str, starts_with: str):
    """
    Tests the `starts_with()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when the value starts with the specified value.
    """
    # Act
    try:
        Condition.requires_str(value, 'value').starts_with(starts_with)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should start with `{starts_with}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,starts_with',
    [
        ('1234', 'test'),
        ('test', '1'),
        ('this_is_my_value', 'is_my')
    ]
)
def test_intg_rqr_starts_with_throws_error_on_invalid_value(value: str, starts_with: str):
    """
    Tests the `starts_with()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when the value does not start with the specified value.
    """
    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').starts_with(starts_with)


@pytest.mark.parametrize(
    'value,starts_with',
    [
        ('1234', '1'),
        ('test', 'tes'),
        ('this_is_my_value', 'this_is_my')
    ]
)
def test_intg_rqr_does_not_start_with_throws_error_on_invalid_value(value: str, starts_with: str):
    """
    Tests the `does_not_start_with()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when the value starts with the specified value.
    """
    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').does_not_start_with(starts_with)


@pytest.mark.parametrize(
    'value,starts_with',
    [
        ('1234', 'test'),
        ('test', '1'),
        ('this_is_my_value', 'is_my')
    ]
)
def test_intg_rqr_does_not_start_with_accepts_valid_value(value: str, starts_with: str):
    """
    Tests the `does_not_start_with()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when the value does not start with the specified value.
    """
    # Act
    try:
        Condition.requires_str(value, 'value').does_not_start_with(starts_with)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should not start with `{starts_with}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,ends_with',
    [
        ('1234', '4'),
        ('test', 'est'),
        ('this_is_my_value', '_my_value')
    ]
)
def test_intg_rqr_ends_with_accepts_valid_value(value: str, ends_with: str):
    """
    Tests the `ends_with()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when the value ends with the specified value.
    """
    # Act
    try:
        Condition.requires_str(value, 'value').ends_with(ends_with)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should end with `{ends_with}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,ends_with',
    [
        ('1234', 'test'),
        ('test', '1'),
        ('this_is_my_value', 'is_my')
    ]
)
def test_intg_rqr_ends_with_throws_error_on_invalid_value(value: str, ends_with: str):
    """
    Tests the `ends_with()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when the value does not end with the specified value.
    """
    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').ends_with(ends_with)


@pytest.mark.parametrize(
    'value,ends_with',
    [
        ('1234', '4'),
        ('test', 'est'),
        ('this_is_my_value', '_my_value')
    ]
)
def test_intg_rqr_does_not_end_with_throws_error_on_invalid_value(value: str, ends_with: str):
    """
    Tests the `does_not_end_with()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when the value ends with the specified value.
    """
    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').does_not_end_with(ends_with)


@pytest.mark.parametrize(
    'value,ends_with',
    [
        ('1234', 'test'),
        ('test', '1'),
        ('this_is_my_value', 'is_my')
    ]
)
def test_intg_rqr_does_not_end_with_accepts_valid_value(value: str, ends_with: str):
    """
    Tests the `does_not_end_with()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when the value does not end with the specified value.
    """
    # Act
    try:
        Condition.requires_str(value, 'value').does_not_end_with(ends_with)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should not end with `{ends_with}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,contains',
    [
        ('1234', '23'),
        ('test', 'es'),
        ('this_is_my_value', 'is_my')
    ]
)
def test_intg_rqr_contains_accepts_valid_value(value: str, contains: str):
    """
    Tests the `contains()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when the value does contains specified value.
    """
    # Act
    try:
        Condition.requires_str(value, 'value').contains(contains)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should contain `{contains}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,contains',
    [
        ('1234', 'test'),
        ('test', '1234'),
        ('this_is_my_value', '-')
    ]
)
def test_intg_rqr_contains_throw_error_on_invalid_value(value: str, contains: str):
    """
    Tests the `contains()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when the value does not contain specified value.
    """
    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').contains(contains)


@pytest.mark.parametrize(
    'value,contains',
    [
        ('1234', '23'),
        ('test', 'es'),
        ('this_is_my_value', 'is_my')
    ]
)
def test_intg_rqr_does_not_contain_throw_error_on_invalid_value(value: str, contains: str):
    """
    Tests the `does_not_contain()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when the value contains specified value.
    """
    # Assert
    with pytest.raises(ArgumentError):
        # Act
        Condition.requires_str(value, 'value').does_not_contain(contains)


@pytest.mark.parametrize(
    'value,contains',
    [
        ('1234', 'test'),
        ('test', '1234'),
        ('this_is_my_value', '-')
    ]
)
def test_intg_rqr_does_not_contain_accepts_valid_value(value: str, contains: str):
    """
    Tests the `does_not_contain()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when the value does not contain specified value.
    """
    # Act
    try:
        Condition.requires_str(value, 'value').does_not_contain(contains)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should not contain `{contains}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,pattern',
    [
        ('1234', r'^\d+$'),
        ('test', r'^\w+$'),
        ('this_is_my_value', r'^[a-z_]+$')
    ]
)
def test_intg_rqr_is_regex_match_accepts_matching_pattern(value: str, pattern: str):
    """
    Tests the `is_regex_match()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when the value matches the specified pattern.
    """
    # Act
    try:
        Condition.requires_str(value, 'value').is_regex_match(pattern)
    # Assert
    except ArgumentPatternError:
        pytest.fail(f'`{value}` should match the pattern `{pattern}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,pattern',
    [
        ('test', r'^\d+$'),
        ('1234', r'^[a-z]+$'),
        ('this-is-my-value', r'^[a-z_]+$')
    ]
)
def test_intg_rqr_is_regex_match_throws_error_on_not_matching_pattern(value: str, pattern: str):
    """
    Tests the `is_regex_match()` through `Condition.requires_str()` to see if it,
    throws an ArgumentError when the value does not match the specified pattern.
    """
    # Act
    with pytest.raises(ArgumentPatternError):
		# Act
        Condition.requires_str(value, 'value').is_regex_match(pattern)


@pytest.mark.parametrize(
    'value,pattern',
    [
        ('test', r'^\d+$'),
        ('1234', r'^[a-z]+$'),
        ('this-is-my-value', r'^[a-z_]+$')
    ]
)
def test_intg_rqr_is_not_regex_match_accepts_not_matching_pattern(value: str, pattern: str):
    """
    Tests the `is_not_regex_match()` through `Condition.requires_str()` to see if it,
    does not throw an ArgumentError when the value does not match the specified pattern.
    """
    # Act
    try:
        Condition.requires_str(value, 'value').is_not_regex_match(pattern)
    # Assert
    except ArgumentPatternError:
        pytest.fail(f'`{value}` should match the pattern `{pattern}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,pattern',
    [
        ('1234', r'^\d+$'),
        ('test', r'^\w+$'),
        ('this_is_my_value', r'^[a-z_]+$')
    ]
)
def test_intg_rqr_is_not_regex_match_throws_error_on_matching_pattern(value: str, pattern: str):
    """
    Tests the `is_not_regex_match()` requires validator method through `Condition.requires_str()` to see if it,
    throws an ArgumentError when the value matches the specified pattern.
    """
    # Assert
    with pytest.raises(ArgumentPatternError):
		# Act
        Condition.requires_str(value, 'value').is_not_regex_match(pattern)


@pytest.mark.parametrize(
    'value,set',
    [
        ('test', ['test']),
        ('1234', ['1234', '5678', '9876']),
        ('this-is-my-value', ['this-is-my-value', 'testing', '1234'])
    ]
)
def test_intg_rqr_is_in_set_accepts_value_in_set(value: str, set: list):
    """
    Tests the `is_in_set()` requires validator method does not throw an ArgumentError when its value is present
    in the supplied set.
    """
    # Arrange
    validator = Condition.requires_str(value, 'value')

    # Act
    try:
        validator.is_in_set(set)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should be in the set `{set}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,set',
    [
        ('1234', ['test']),
        ('test', ['1234', '5678', '9876']),
        ('testing', ['this-is-MY-value', 'TESTING', '1234'])
    ]
)
def test_intg_rqr_is_in_set_throws_error_on_non_matching_set(value: str, set: list):
    """
    Tests the `is_in_set()` requires validator method throws an ArgumentError when its value is not present
    in the supplied set.
    """
    # Arrange
    validator = Condition.requires_str(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_in_set(set)


@pytest.mark.parametrize(
    'value,set',
    [
        ('1234', ['test']),
        ('test', ['1234', '5678', '9876']),
        ('testing', ['this-is-MY-value', 'TESTING', '1234'])
    ]
)
def test_intg_rqr_is_not_in_set_accepts_value_not_in_set(value: str, set: list):
    """
    Tests the `is_not_in_set()` requires validator method accepts when its value is not present
    in the supplied set.
    """
    # Arrange
    validator = Condition.requires_str(value, 'value')

    # Act
    try:
        validator.is_not_in_set(set)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should be in the set `{set}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,set',
    [
        ('test', ['test']),
        ('1234', ['1234', '5678', '9876']),
        ('this-is-my-value', ['this-is-my-value', 'testing', '1234'])
    ]
)
def test_intg_rqr_is_not_in_set_throws_error_on_matching_set(value: str, set: list):
    """
    Tests the `is_not_in_set()` requires validator method throws an ArgumentError when its value is present
    in the supplied set.
    """
    # Arrange
    validator = Condition.requires_str(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_not_in_set(set)


@pytest.mark.parametrize(
    'value,set',
    [
        ('test', ['tESt']),
        ('1234', ['1234', '5678', '9876']),
        ('this-is-my-value', ['this-is-MY-value', 'testing', '1234'])
    ]
)
def test_intg_rqr_is_in_set_case_insensitive_accepts_value_in_set(value: str, set: list):
    """
    Tests the `is_in_set_case_insensitive()` requires validator method does not throw an ArgumentError when its value is present
    in the supplied set, case insensitive.
    """
    # Arrange
    validator = Condition.requires_str(value, 'value')

    # Act
    try:
        validator.is_in_set_case_insensitive(set)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should be in the set `{set}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,set',
    [
        ('1234', ['test']),
        ('test', ['1234', '5678', '9876']),
        ('testing1234', ['this-is-MY-value', 'TESTING', '1234'])
    ]
)
def test_intg_rqr_is_in_set_case_insensitive_throws_error_on_non_matching_set(value: str, set: list):
    """
    Tests the `is_in_set_case_insensitive()` requires validator method throws an ArgumentError when its value is not present
    in the supplied set, case insensitive.
    """
    # Arrange
    validator = Condition.requires_str(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_in_set_case_insensitive(set)


@pytest.mark.parametrize(
    'value,set',
    [
        ('1234', ['test']),
        ('test', ['1234', '5678', '9876']),
        ('testing1234', ['this-is-MY-value', 'TESTING', '1234'])
    ]
)
def test_intg_rqr_is_not_in_set_case_insensitive_accepts_value_not_in_set(value: str, set: list):
    """
    Tests the `is_not_in_set_case_insensitive()` requires validator method accepts when its value is not present
    in the supplied set, case insensitive.
    """
    # Arrange
    validator = Condition.requires_str(value, 'value')

    # Act
    try:
        validator.is_not_in_set_case_insensitive(set)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should be in the set `{set}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,set',
    [
        ('test', ['tESt']),
        ('1234', ['1234', '5678', '9876']),
        ('this-is-my-value', ['this-is-my-value', 'testing', '1234'])
    ]
)
def test_intg_rqr_is_not_in_set_case_insensitive_throws_error_on_matching_set(value: str, set: list):
    """
    Tests the `is_not_in_set_case_insensitive()` requires validator method throws an ArgumentError when its value is present
    in the supplied set, case insensitive.
    """
    # Arrange
    validator = Condition.requires_str(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_not_in_set_case_insensitive(set)