import pytest
from modules import find_next_perfect_square


def describe_find_next_square():
    def should_raise_error_when_not_integer():
        """🧪 should error when the input is not an integer"""
        with pytest.raises(ValueError, match="❗️ Input is not an integer"):
            find_next_perfect_square.find_next_square("blah")
