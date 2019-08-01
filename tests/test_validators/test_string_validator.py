import pytest

from src.errors.argument_error import ArgumentError
from src.errors.argument_pattern_error import ArgumentPatternError
from src.errors.argument_null_error import ArgumentNullError
from src.validators.string_validator import StringValidator


EMPTY_STRING = ''
WHITESPACE_STRING = ' '


def test_is_null_accepts_null_value():
    """

    """
    # Arrange
    value = None
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.is_null()
    # Assert
    except ArgumentNullError:
        pytest.fail(f'`{value}` should have been None (Null), but an error occurred instead.')


def test_is_null_throws_error_on_whitespace_value():
    """

    """
    # Arrange
    value = WHITESPACE_STRING
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentNullError):
        # Act
        validator.is_null()


def test_is_null_throws_error_on_empty_value():
    """

    """
    # Arrange
    value = EMPTY_STRING
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentNullError):
        # Act
        validator.is_null()


@pytest.mark.parametrize(
    'value',
    [
        ('1234'),
        ('test'),
        ('this_is_my_value')
    ]
)
def test_is_null_throws_error_on_invalid_value(value: str):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentNullError):
        # Act
        validator.is_null()


def test_is_not_null_accepts_whitespace_value():
    """

    """
    # Arrange
    value = WHITESPACE_STRING
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.is_not_null()
    # Assert
    except ArgumentNullError:
        pytest.fail(f'`{value}` should not have been None (Null), but an error occurred instead.')


def test_is_not_null_accepts_empty_value():
    """

    """
    # Arrange
    value = EMPTY_STRING
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.is_not_null()
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
def test_is_not_null_accepts_valid_value(value: str):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.is_not_null()
    # Assert
    except ArgumentNullError:
        pytest.fail(f'`{value}` should not have been None (Null), but an error occurred instead.')


def test_is_not_null_throws_error_on_null_value():
    """

    """
    # Arrange
    value = None
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentNullError):
        # Act
        validator.is_not_null()


def test_is_null_or_empty_accepts_null_value():
    """

    """
    # Arrange
    value = None
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.is_null_or_empty()
    # Assert
    except ArgumentNullError:
        pytest.fail(f'`{value}` should have been None (Null) or empty, but an error occurred instead.')


def test_is_null_or_empty_accepts_empty_value():
    """

    """
    # Arrange
    value = EMPTY_STRING
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.is_null_or_empty()
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should have been None (Null) or empty, but an error occurred instead.')


def test_is_null_or_empty_throws_error_on_whitespace_value():
    """

    """
    # Arrange
    value = WHITESPACE_STRING
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_null_or_empty()


@pytest.mark.parametrize(
    'value',
    [
        ('1234'),
        ('test'),
        ('this_is_my_value')
    ]
)
def test_is_null_or_empty_throws_error_on_invalid_value(value: str):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_null_or_empty()


def test_is_not_null_or_empty_accepts_whitespace_value():
    """

    """
    # Arrange
    value = WHITESPACE_STRING
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.is_not_null_or_empty()
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
def test_is_not_null_or_empty_accepts_valid_value(value: str):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.is_not_null_or_empty()
    # Assert
    except (ArgumentError, ArgumentNullError):
        pytest.fail(f'`{value}` should not have been None (Null) or empty, but an error occurred instead.')


def test_is_not_null_or_empty_throw_error_on_null_value():
    """

    """
    # Arrange
    value = None
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_not_null_or_empty()


def test_is_not_null_or_empty_throw_error_on_empty_value():
    """

    """
    # Arrange
    value = EMPTY_STRING
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_not_null_or_empty()



def test_is_null_or_whitespace_accepts_null_value():
    """

    """
    # Arrange
    value = None
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.is_null_or_whitespace()
    # Assert
    except ArgumentNullError:
        pytest.fail(f'`{value}` should have been None (Null), empty or whitespace, but an error occurred instead.')


def test_is_null_or_whitespace_accepts_empty_value():
    """

    """
    # Arrange
    value = EMPTY_STRING
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.is_null_or_whitespace()
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should have been None (Null), empty or whitespace, but an error occurred instead.')


def test_is_null_or_whitespace_accepts_whitespace_value():
    """

    """
    # Arrange
    value = WHITESPACE_STRING
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.is_null_or_whitespace()
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
def test_is_null_or_whitespace_throws_error_on_invalid_value(value: str):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_null_or_whitespace()


@pytest.mark.parametrize(
    'value',
    [
        ('1234'),
        ('test'),
        ('this_is_my_value')
    ]
)
def test_is_not_null_or_whitespace_accepts_valid_value(value: str):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.is_not_null_or_whitespace()
    # Assert
    except (ArgumentError, ArgumentNullError):
        pytest.fail(f'`{value}` should not have been None (Null) or empty, but an error occurred instead.')


def test_is_not_null_or_whitespace_throws_error_on_whitespace_value():
    """

    """
    # Arrange
    value = WHITESPACE_STRING
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_not_null_or_whitespace()


def test_is_not_null_or_whitespace_throw_error_on_null_value():
    """

    """
    # Arrange
    value = None
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_not_null_or_whitespace()


def test_is_not_null_or_whitespace_throw_error_on_empty_value():
    """

    """
    # Arrange
    value = EMPTY_STRING
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_not_null_or_whitespace()


@pytest.mark.parametrize(
    'value,max_length',
    [
        ('1234', 5),
        ('test', 6),
        ('this_is_my_value', 20)
    ]
)
def test_is_shorter_than_accepts_shorted_length(value: str, max_length: int):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.is_shorter_than(max_length)
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
def test_is_shorter_than_throws_error_on_longer_length(value: str, max_length: int):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_shorter_than(max_length)


@pytest.mark.parametrize(
    'value,max_length',
    [
        ('1234', 4),
        ('test', 4),
        ('this_is_my_value', 16)
    ]
)
def test_is_shorter_than_throws_error_on_equal_length(value: str, max_length: int):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_shorter_than(max_length)


@pytest.mark.parametrize(
    'value,max_length',
    [
        ('1234', 5),
        ('test', 6),
        ('this_is_my_value', 20)
    ]
)
def test_is_shorter_or_equal_accepts_shorter_length(value: str, max_length: int):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.is_shorter_or_equal(max_length)
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
def test_is_shorter_or_equal_accepts_equal_length(value: str, max_length: int):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.is_shorter_or_equal(max_length)
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
def test_is_shorter_or_equal_throws_error_on_longer_length(value: str, max_length: int):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_shorter_or_equal(max_length)


@pytest.mark.parametrize(
    'value,min_length',
    [
        ('1234', 2),
        ('test', 1),
        ('this_is_my_value', 9)
    ]
)
def test_is_longer_than_accepts_longer_length(value: str, min_length: int):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.is_longer_than(min_length)
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
def test_is_longer_than_throws_error_on_equal_length(value: str, min_length: int):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_longer_than(min_length)


@pytest.mark.parametrize(
    'value,min_length',
    [
        ('1234', 4),
        ('test', 9),
        ('this_is_my_value', 50)
    ]
)
def test_is_longer_than_throws_error_on_shorter_length(value: str, min_length: int):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_longer_than(min_length)


@pytest.mark.parametrize(
    'value,min_length',
    [
        ('1234', 2),
        ('test', 1),
        ('this_is_my_value', 9)
    ]
)
def test_is_longer_or_equal_accepts_longer_length(value: str, min_length: int):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.is_longer_or_equal(min_length)
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
def test_is_longer_or_equal_accepts_equal_length(value: str, min_length: int):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.is_longer_or_equal(min_length)
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
def test_is_longer_or_equal_throws_error_on_shorter_length(value: str, min_length: int):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_longer_or_equal(min_length)


@pytest.mark.parametrize(
    'value,length',
    [
        ('1234', 4),
        ('test', 4),
        ('this_is_my_value', 16)
    ]
)
def test_has_length_accepts_equal_length(value: str, length: int):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.has_length(length)
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
def test_has_length_throws_error_on_notequal_length(value: str, length: int):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.has_length(length)


@pytest.mark.parametrize(
    'value,length',
    [
        ('1234', 4),
        ('test', 4),
        ('this_is_my_value', 16)
    ]
)
def test_does_not_have_length_throws_error_on_equal_length(value: str, length: int):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.does_not_have_length(length)


@pytest.mark.parametrize(
    'value,length',
    [
        ('1234', 7),
        ('test', 9),
        ('this_is_my_value', 50)
    ]
)
def test_does_not_have_length_accepts_notequal_length(value: str, length: int):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.does_not_have_length(length)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should not have the length `{length}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,starts_with',
    [
        ('1234', '1'),
        ('test', 'tes'),
        ('this_is_my_value', 'this_is_my')
    ]
)
def test_starts_with_accepts_valid_value(value: str, starts_with: str):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.starts_with(starts_with)
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
def test_starts_with_throws_error_on_invalid_value(value: str, starts_with: str):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.starts_with(starts_with)


@pytest.mark.parametrize(
    'value,starts_with',
    [
        ('1234', '1'),
        ('test', 'tes'),
        ('this_is_my_value', 'this_is_my')
    ]
)
def test_does_not_start_with_throws_error_on_invalid_value(value: str, starts_with: str):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.does_not_start_with(starts_with)


@pytest.mark.parametrize(
    'value,starts_with',
    [
        ('1234', 'test'),
        ('test', '1'),
        ('this_is_my_value', 'is_my')
    ]
)
def test_does_not_start_with_accepts_valid_value(value: str, starts_with: str):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.does_not_start_with(starts_with)
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
def test_ends_with_accepts_valid_value(value: str, ends_with: str):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.ends_with(ends_with)
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
def test_ends_with_throws_error_on_invalid_value(value: str, ends_with: str):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.ends_with(ends_with)


@pytest.mark.parametrize(
    'value,ends_with',
    [
        ('1234', '4'),
        ('test', 'est'),
        ('this_is_my_value', '_my_value')
    ]
)
def test_does_not_end_with_throws_error_on_invalid_value(value: str, ends_with: str):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.does_not_end_with(ends_with)


@pytest.mark.parametrize(
    'value,ends_with',
    [
        ('1234', 'test'),
        ('test', '1'),
        ('this_is_my_value', 'is_my')
    ]
)
def test_does_not_end_with_accepts_valid_value(value: str, ends_with: str):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.does_not_end_with(ends_with)
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
def test_contains_accepts_valid_value(value: str, contains: str):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.contains(contains)
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
def test_contains_throw_error_on_invalid_value(value: str, contains: str):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.contains(contains)


@pytest.mark.parametrize(
    'value,contains',
    [
        ('1234', '23'),
        ('test', 'es'),
        ('this_is_my_value', 'is_my')
    ]
)
def test_does_not_contain_throw_error_on_invalid_value(value: str, contains: str):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.does_not_contain(contains)


@pytest.mark.parametrize(
    'value,contains',
    [
        ('1234', 'test'),
        ('test', '1234'),
        ('this_is_my_value', '-')
    ]
)
def test_does_not_contain_accepts_valid_value(value: str, contains: str):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.does_not_contain(contains)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{value}` should not contain `{contains}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,pattern',
    [
        ('1234', r'\d+'),
        ('test', r'\w+'),
        ('this_is_my_value', r'[a-z_]+')
    ]
)
def test_is_regex_match_accepts_matching_pattern(value: str, pattern: str):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.is_regex_match(pattern)
    # Assert
    except ArgumentPatternError:
        pytest.fail(f'`{value}` should match the pattern `{pattern}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,pattern',
    [
        # ('test', r'\d+'),
        ('1234', r'\w+'),
        ('this-is-my-value', r'[a-z_]+')
    ]
)
def test_is_regex_match_throws_error_on_not_matching_pattern(value: str, pattern: str):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.is_regex_match(pattern)
    # Assert
    except ArgumentPatternError:
        pytest.fail(f'`{value}` should match the pattern `{pattern}`, but an error occurred.')



@pytest.mark.parametrize(
    'value,pattern',
    [
        # ('test', r'\d+'),
        ('1234', r'\w+'),
        ('this-is-my-value', r'[a-z_]+')
    ]
)
def test_is_not_regex_match_accepts_not_matching_pattern(value: str, pattern: str):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.is_not_regex_match(pattern)
    # Assert
    except ArgumentPatternError:
        pytest.fail(f'`{value}` should match the pattern `{pattern}`, but an error occurred.')


@pytest.mark.parametrize(
    'value,pattern',
    [
        ('1234', r'\d+'),
        ('test', r'\w+'),
        ('this_is_my_value', r'[a-z_]+')
    ]
)
def test_is_not_regex_match_throws_error_on_matching_pattern(value: str, pattern: str):
    """

    """
    # Arrange
    validator = StringValidator(value, 'value')

    # Act
    try:
        validator.is_not_regex_match(pattern)
    # Assert
    except ArgumentPatternError:
        pytest.fail(f'`{value}` should match the pattern `{pattern}`, but an error occurred.')