import pytest

from tests.type_example import TypeExample
from tests.type_example import TypeExample2
from tests.type_example import TypeEqualityExample
from src.errors.argument_error import ArgumentError
from src.errors.argument_null_error import ArgumentNullError
from src.validators.object_validator import ObjectValidator


def test_is_of_type_name_accepts_equivalent_type():
    """

    """
    # Arrange
    actual = type('type', (object,), {})()
    expected = type('type', (object,), {})()
    validator = ObjectValidator(actual, 'actual')

    # Act
    try:
        validator.is_of_type_name(expected)
    # Assert
    except ArgumentError:
        pytest.fail(f'Type `{actual.__class__.__name__}` should match type `{expected.__class__.__name__}`, but an error occurred.')


def test_is_of_type_name_throws_error_on_different_type():
    """

    """
    # Arrange
    actual = type('actual', (object,), {})()
    expected = type('expected', (object,), {})()
    validator = ObjectValidator(actual, 'actual')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_of_type_name(expected)


def test_is_of_type_name_throws_error_on_no_supplied_initialized_object():
    """

    """
    # Arrange
    obj = TypeExample()
    validator = ObjectValidator(obj, 'obj')

    # Assert
    with pytest.raises(TypeError):
        # Act
        validator.is_of_type_name(TypeExample)


def test_is_not_of_type_name_accepts_equivalent_type():
    """

    """
    # Arrange
    actual = type('actual', (object,), {})()
    expected = type('expected', (object,), {})()
    validator = ObjectValidator(actual, 'actual')

    # Act
    try:
        validator.is_not_of_type_name(expected)
    # Assert
    except ArgumentError:
        pytest.fail(f'Type `{actual.__class__.__name__}` should match type `{expected.__class__.__name__}`, but an error occurred.')


def test_is_not_of_type_name_throws_error_on_different_type():
    """

    """
    # Arrange
    actual = type('type', (object,), {})()
    expected = type('type', (object,), {})()
    validator = ObjectValidator(actual, 'actual')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_not_of_type_name(expected)


def test_is_not_of_type_name_throws_error_on_no_supplied_initialized_object():
    """

    """
    # Arrange
    obj = TypeExample()
    validator = ObjectValidator(obj, 'obj')

    # Assert
    with pytest.raises(TypeError):
        # Act
        validator.is_not_of_type_name(TypeExample2)


def test_is_of_type_accepts_equivalent_type():
    """

    """
    # Arrange
    obj = TypeExample()
    validator = ObjectValidator(obj, 'obj')

    # Act
    try:
        validator.is_of_type(TypeExample)
    # Assert
    except ArgumentError:
        pytest.fail(f'Type `{obj.__class__.__name__}` should match type `{TypeExample.__name__}`, but an error occurred.')


def test_is_of_type_throws_error_on_different_type():
    """

    """
    # Arrange
    obj = TypeExample()
    validator = ObjectValidator(obj, 'obj')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_of_type(TypeExample2)


def test_is_of_type_throws_error_on_no_supplied_type_class():
    """

    """
    # Arrange
    actual = type('type', (object,), {})()
    expected = type('type', (object,), {})()
    validator = ObjectValidator(actual, 'actual')

    # Assert
    with pytest.raises(TypeError):
        # Act
        validator.is_of_type(expected)


def test_is_not_of_type_accepts_equivalent_type():
    """

    """
    # Arrange
    obj = TypeExample()
    validator = ObjectValidator(obj, 'obj')

    # Act
    try:
        validator.is_of_type(TypeExample)
    # Assert
    except ArgumentError:
        pytest.fail(f'Type `{obj.__class__.__name__}` should match type `{TypeExample.__name__}`, but an error occurred.')


def test_is_not_of_type_throws_error_on_different_type():
    """

    """
    # Arrange
    obj = TypeExample()
    validator = ObjectValidator(obj, 'obj')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_of_type(TypeExample2)


def test_is_not_of_type_throws_error_on_no_supplied_type_class():
    """

    """
    # Arrange
    actual = type('actual', (object,), {})()
    expected = type('expected', (object,), {})()
    validator = ObjectValidator(actual, 'actual')

    # Assert
    with pytest.raises(TypeError):
        # Act
        validator.is_not_of_type(expected)


def test_is_null_accepts_null_value():
    """

    """
    # Arrange
    type = None
    validator = ObjectValidator(type, 'type')

    # Act
    try:
        validator.is_null()
    # Assert
    except ArgumentNullError:
        pytest.fail(f'The object should have been None (Null), but an error occurred.')


def test_is_null_throws_error_on_not_null_value():
    """

    """
    # Arrange
    type = TypeExample()
    validator = ObjectValidator(type, 'type')

    # Assert
    with pytest.raises(ArgumentNullError):
        # Act
        validator.is_null()



def test_is_not_null_accepts_not_null_value():
    """

    """
    # Arrange
    type = TypeExample()
    validator = ObjectValidator(type, 'type')

    # Act
    try:
        validator.is_not_null()
    # Assert
    except ArgumentNullError:
        pytest.fail(f'The object should have been None (Null), but an error occurred.')


def test_is_not_null_throws_error_on_null_value():
    """

    """
    # Arrange
    type = None
    validator = ObjectValidator(type, 'type')

    # Assert
    with pytest.raises(ArgumentNullError):
        # Act
        validator.is_not_null()


def test_is_equal_to_accepts_identical_object():
    """

    """
    # Arrange
    actual = TypeExample()
    expected = TypeExample()
    validator = ObjectValidator(actual, 'actual')

    # Act
    try:
        validator.is_equal_to(expected)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{actual.__class__.__name__}` should be equal to `{expected.__class__.__name__}`, but an error occurred')


def test_is_equal_throws_error_on_non_identical_object():
    """

    """
    # Arrange
    actual = TypeExample()
    expected = TypeExample2()
    validator = ObjectValidator(actual, 'actual')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_equal_to(expected)


def test_is_not_equal_to_accepts_non_identical_object_class():
    """

    """
    # Arrange
    actual = TypeExample()
    expected = TypeExample2()
    validator = ObjectValidator(actual, 'actual')

    # Act
    try:
        validator.is_not_equal_to(expected)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{actual.__class__.__name__}` should be not equal to `{expected.__class__.__name__}`, but an error occurred')


def test_is_equal_throws_error_on_identical_object():
    """

    """
    # Arrange
    actual = TypeExample()
    expected = TypeExample()
    validator = ObjectValidator(actual, 'actual')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_not_equal_to(expected)


def test_is_equal_using_eq_accepts_equal_objects():
    """

    """
    # Arrange
    actual = TypeEqualityExample(10)
    expected = TypeEqualityExample(10)
    validator = ObjectValidator(actual, 'actual')

    # Act
    try:
        validator.is_equal_to_using_eq(expected)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{actual.__class__.__name__}` should be equal to `{expected.__class__.__name__}` when using the `__eq__()` function, but an error occurred')


def test_is_equal_using_eq_should_throw_on_unequal_objects():
    """

    """
    # Arrange
    actual = TypeEqualityExample(10)
    expected = TypeEqualityExample(11)
    validator = ObjectValidator(actual, 'actual')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_equal_to_using_eq(expected)


def test_is_not_equal_using_eq_accepts_unequal_objects():
    """

    """
    # Arrange
    actual = TypeEqualityExample(10)
    expected = TypeEqualityExample(11)
    validator = ObjectValidator(actual, 'actual')

    # Act
    try:
        validator.is_not_equal_to_using_ne(expected)
    # Assert
    except ArgumentError:
        pytest.fail(f'`{actual.__class__.__name__}` should be equal to `{expected.__class__.__name__}` when using the `__eq__()` function, but an error occurred')


def test_is_not_equal_using_eq_should_throw_on_equal_objects():
    """

    """
    # Arrange
    actual = TypeEqualityExample(10)
    expected = TypeEqualityExample(10)
    validator = ObjectValidator(actual, 'actual')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_not_equal_to_using_ne(expected)