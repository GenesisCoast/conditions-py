class TypeExample:
    pass


class TypeExample2:
    def __init__(self):
        self.value = 'TestExample2'


class TypeEqualityExample:
    def __init__(self, value: int = 10):
        self.value = value

    def __eq__(self, other: object):
        return self.value == other.value

    def __ne__(self, other: object):
        return self.value != other.value