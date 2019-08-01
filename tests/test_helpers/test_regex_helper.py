import pytest
from src.helpers.regex_helper import RegexHelper


@pytest.mark.parametrize(
    'value,pattern',
    [
        ('test', r'\w+'),
        ('this_is_my_value', r'[a-z_]+')
    ]
)
def test_is_match_returns_true_on_matching_pattern(value: str, pattern: str):
    """

    """
    # Act
    result = RegexHelper.is_match(pattern, value)

    # Assert
    assert result == True


@pytest.mark.parametrize(
    'value,pattern',
    [
        ('1234', r'[a-z]+'),
        ('this-is-my-value', r'[0-9_]+')
    ]
)
def test_is_match_returns_false_on_non_matching_pattern(value: str, pattern: str):
    """

    """
    # Act
    result = RegexHelper.is_match(pattern, value)

    # Assert
    assert result == False