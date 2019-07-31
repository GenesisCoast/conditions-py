import re

class RegexHelper:
    """
    Defines regex helper methods.
    """

    @staticmethod
    def is_match(pattern: str, string: str, flag: int = 0) -> bool:
        """
        Returns `True` or `False` if a regex match has been found in the string.
        """
        if not re.match(pattern, string, flag):
            return True
        else:
            return False