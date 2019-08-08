import pytest
from tests.unit.type_example import TypeExample
from tests.unit.type_example import TypeExample2
from tests.unit.type_example import TypeEqualityExample
from src.errors.argument_error import ArgumentError
from src.errors.argument_null_error import ArgumentNullError
from src.validators.object_validator import ObjectValidator


def test_prnt_get_value_returns_value():
    """
    Tests if the parent `get_value()` method returns the value saved in the validator.
    """
    # Arrange
    obj = type('type', (object,), {})()
    validator = ObjectValidator(obj, 'obj')

    # Act
    actual = validator.get_value()

    # Assert
    assert actual == obj
    assert actual is obj
    assert type(actual) == type(obj)


def test_is_of_type_name_accepts_equivalent_type():
    """
    Tests that the `is_of_type_name()` method does not throw an ArgumentError
    when it is supplied with a type that is of the specified type.
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


def test_is_of_type_name_accepts_the_same_type():
    """
    Tests that the `is_of_type_name()` method does not throw an ArgumentError
    when it is supplied with a type that is the same type instance.
    """
    # Arrange
    type_name = type('type', (object,), {})()
    validator = ObjectValidator(type, 'actual')

    # Act
    try:
        validator.is_of_type_name(type_name)
    # Assert
    except ArgumentError:
        pytest.fail(f'Type `{type_name.__class__.__name__}` should match type `{type_name.__class__.__name__}`, but an error occurred.')


def test_is_of_type_name_throws_error_on_different_type():
    """
    Tests that the `is_of_type_name()` method throws an ArgumentError
    when it is supplied with a type that is not of the specified type.
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
    Tests that the `is_of_type_name()` method throws a TypeError
    when it is supplied with a type that is not initialized.
    """
    # Arrange
    obj = TypeExample()
    validator = ObjectValidator(obj, 'obj')

    # Assert
    with pytest.raises(TypeError):
        # Act
        validator.is_of_type_name(TypeExample)


def test_is_of_type_name_returns_validator_self():
    """
    Tests if the `is_of_type()` validator method returns itself after the validation is performed,
    so that additional validations can be performed.
    """
    # Arrange
    actual = type('type', (object,), {})()
    expected = type('type', (object,), {})()
    validator = ObjectValidator(actual, 'actual')

    # Act
    validator_returned = validator.is_of_type_name(expected)

    # Assert
    assert validator_returned is validator


def test_is_not_of_type_name_accepts_different_type():
    """
    Tests that the `is_not_of_type_name()` method does not throw an ArgumentError
    when it is supplied with a type that is not the same as the supplied type.
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


def test_is_not_of_type_name_throws_error_on_the_same_type():
    """
    Tests that the `is_not_of_type_name()` method throws an ArgumentError
    when it is supplied with a type that is the same type instance.
    """
    # Arrange
    type_name = type('type', (object,), {})()
    validator = ObjectValidator(type, 'actual')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_not_of_type_name(type_name)


def test_is_not_of_type_name_throws_error_on_equivalent_type():
    """
    Tests that the `is_not_of_type_name()` method throws an ArgumentError
    when it is supplied with a type that is equivalent to the specified type.
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
    Tests that the `is_not_of_type_name()` method throws a TypeError
    when it is supplied with a type that is not initialized.
    """
    # Arrange
    obj = TypeExample()
    validator = ObjectValidator(obj, 'obj')

    # Assert
    with pytest.raises(TypeError):
        # Act
        validator.is_not_of_type_name(TypeExample2)


def test_is_not_of_type_name_returns_validator_self():
    """
    Tests if the `is_not_of_type_name()` validator method returns itself after the validation is performed,
    so that additional validations can be performed.
    """
    # Arrange
    actual = type('actual', (object,), {})()
    expected = type('expected', (object,), {})()
    validator = ObjectValidator(actual, 'actual')

    # Act
    validator_returned = validator.is_not_of_type_name(expected)

    # Assert
    assert validator_returned is validator


def test_is_of_type_accepts_equivalent_type():
    """
    Tests that the `is_of_type()` method does not throw an ArgumentError
    when it is supplied with a type that is equivalent to the specified type.
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
    Tests that the `is_of_type()` method throws an ArgumentError
    when it is supplied with a type that is different to the specified type.
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
    Tests that the `is_of_type()` method does not throw a TypeError
    when it is supplied with a type that is initialized rather than a class type.
    """
    # Arrange
    actual = type('type', (object,), {})()
    expected = type('type', (object,), {})()
    validator = ObjectValidator(actual, 'actual')

    # Assert
    with pytest.raises(TypeError):
        # Act
        validator.is_of_type(expected)


def test_is_of_type_returns_validator_self():
    """
    Tests if the `is_of_type()` validator method returns itself after the validation is performed,
    so that additional validations can be performed.
    """
    # Arrange
    obj = TypeExample()
    validator = ObjectValidator(obj, 'obj')

    # Act
    validator_returned = validator.is_of_type(TypeExample)

    # Assert
    assert validator_returned is validator


def test_is_not_of_type_accepts_different_type():
    """
    Tests that the `is_not_of_type()` method does not throw an ArgumentError
    when it is supplied with a type that is different to the specified class type.
    """
    # Arrange
    obj = TypeExample()
    validator = ObjectValidator(obj, 'obj')

    # Act
    try:
        validator.is_not_of_type(TypeExample2)
    # Assert
    except ArgumentError:
        pytest.fail(f'Type `{obj.__class__.__name__}` should match type `{TypeExample.__name__}`, but an error occurred.')


def test_is_not_of_type_throws_error_on_equivalent_type():
    """
    Tests that the `is_not_of_type()` method throws an ArgumentError
    when it is supplied with a type that is the same as the specified class type.
    """
    # Arrange
    obj = TypeExample()
    validator = ObjectValidator(obj, 'obj')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_not_of_type(TypeExample)


def test_is_not_of_type_throws_error_on_no_supplied_type_class():
    """
    Tests that the `is_not_of_type()` method throws a TypeError
    when it is supplied with a type that is initialized rather than a class type.
    """
    # Arrange
    actual = type('actual', (object,), {})()
    expected = type('expected', (object,), {})()
    validator = ObjectValidator(actual, 'actual')

    # Assert
    with pytest.raises(TypeError):
        # Act
        validator.is_not_of_type(expected)


def test_is_not_of_type_returns_validator_self():
    """
    Tests if the `is_not_of_type()` validator method returns itself after the validation is performed,
    so that additional validations can be performed.
    """
    # Arrange
    obj = TypeExample()
    validator = ObjectValidator(obj, 'obj')

    # Act
    validator_returned = validator.is_not_of_type(TypeExample2)

    # Assert
    assert validator_returned is validator


def test_is_null_accepts_null_value():
    """
    Tests that the `is_null()` method does not throw an ArgumentNullError
    when it is supplied with a type that is None (Null).
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
    Tests that the `is_null()` method throws an ArgumentNullError
    when it is supplied with a type that is not None (Null).
    """
    # Arrange
    type = TypeExample()
    validator = ObjectValidator(type, 'type')

    # Assert
    with pytest.raises(ArgumentNullError):
        # Act
        validator.is_null()


def test_is_null_returns_validator_self():
    """
    Tests if the `is_true()` validator method returns itself after the validation is performed,
    so that additional validations can be performed.
    """
    # Arrange
    type = None
    validator = ObjectValidator(type, 'type')

    # Act
    validator_returned = validator.is_null()

    # Assert
    assert validator_returned is validator


def test_is_not_null_accepts_not_null_value():
    """
    Tests that the `is_not_null()` method does not throw an ArgumentNullError
    when it is supplied with a type that is not None (Null).
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
    Tests that the `is_not_null()` method throws an ArgumentNullError
    when it is supplied with a type that is None (Null).
    """
    # Arrange
    type = None
    validator = ObjectValidator(type, 'type')

    # Assert
    with pytest.raises(ArgumentNullError):
        # Act
        validator.is_not_null()


def test_is_not_null_returns_validator_self():
    """
    Tests if the `is_not_null()` validator method returns itself after the validation is performed,
    so that additional validations can be performed.
    """
    # Arrange
    type = TypeExample()
    validator = ObjectValidator(type, 'type')

    # Act
    validator_returned = validator.is_not_null()

    # Assert
    assert validator_returned is validator


def test_is_equal_to_accepts_identical_object():
    """
    Tests that the `is_equal_to()` method does not throw an ArgumentError
    when the object is identical to the supplied object.
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
    Tests that the `is_equal_to()` method throws an ArgumentError
    when the object is not identical to the supplied object.
    """
    # Arrange
    actual = TypeExample()
    expected = TypeExample2()
    validator = ObjectValidator(actual, 'actual')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_equal_to(expected)


def test_is_equal_returns_validator_self():
    """
    Tests if the `is_equal_to()` validator method returns itself after the validation is performed,
    so that additional validations can be performed.
    """
    actual = TypeExample()
    expected = TypeExample()
    validator = ObjectValidator(actual, 'actual')

    # Act
    validator_returned = validator.is_equal_to(expected)

    # Assert
    assert validator_returned is validator


def test_is_not_equal_to_accepts_non_identical_object_class():
    """
    Tests that the `is_not_equal_to()` method does not throw an ArgumentError
    when the object is not identical to the supplied object.
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


def test_is_not_equal_throws_error_on_identical_object():
    """
    Tests that the `is_not_equal_to()` method throws an ArgumentError
    when the object is identical to the supplied object.
    """
    # Arrange
    actual = TypeExample()
    expected = TypeExample()
    validator = ObjectValidator(actual, 'actual')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_not_equal_to(expected)


def test_is_not_equal_returns_validator_self():
    """
    Tests if the `is_true()` validator method returns itself after the validation is performed,
    so that additional validations can be performed.
    """
    # Arrange
    actual = TypeExample()
    expected = TypeExample2()
    validator = ObjectValidator(actual, 'actual')

    # Act
    validator_returned = validator.is_not_equal_to(expected)

    # Assert
    assert validator_returned is validator


def test_is_equal_using_eq_accepts_equal_objects():
    """
    Tests that the `is_equal_to_using_eq()` method does not throw an ArgumentError
    when the object is equal to the supplied object using the `__eq__()` method.
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
    Tests that the `is_equal_to_using_eq()` method throws an ArgumentError
    when the object is not equal to the supplied object using the `__eq__()` method.
    """
    # Arrange
    actual = TypeEqualityExample(10)
    expected = TypeEqualityExample(11)
    validator = ObjectValidator(actual, 'actual')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_equal_to_using_eq(expected)


def test_is_equal_using_eq_returns_validator_self():
    """
    Tests if the `is_equal_to_using_eq()` validator method returns itself after the validation is performed,
    so that additional validations can be performed.
    """
    # Arrange
    actual = TypeEqualityExample(10)
    expected = TypeEqualityExample(10)
    validator = ObjectValidator(actual, 'actual')

    # Act
    validator_returned = validator.is_equal_to_using_eq(expected)

    # Assert
    assert validator_returned is validator


def test_is_not_equal_using_ne_accepts_unequal_objects():
    """
    Tests that the `is_not_equal_to_using_eq()` method throws an ArgumentError
    when the object is not equal to the supplied object using the `__ne__()` method.
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


def test_is_not_equal_using_ne_should_throw_on_equal_objects():
    """
    Tests that the `is_not_equal_to_using_ne()` method throws an ArgumentError
    when the object is equal to the supplied object using the `__ne__()` method.
    """
    # Arrange
    actual = TypeEqualityExample(10)
    expected = TypeEqualityExample(10)
    validator = ObjectValidator(actual, 'actual')

    # Assert
    with pytest.raises(ArgumentError):
        # Act
        validator.is_not_equal_to_using_ne(expected)


def test_is_not_equal_using_ne_returns_validator_self():
    """
    Tests if the `is_not_equal_to_using_ne()` validator method returns itself after the validation is performed,
    so that additional validations can be performed.
    """
    # Arrange
    actual = TypeEqualityExample(10)
    expected = TypeEqualityExample(11)
    validator = ObjectValidator(actual, 'actual')

    # Act
    validator_returned = validator.is_not_equal_to_using_ne(expected)

    # Assert
    assert validator_returned is validator