import pytest
from modules import find_next_perfect_square


def describe_find_next_square():
    def should_raise_error_when_not_integer():
        """🧪 should error when the input is not an integer"""
        with pytest.raises(ValueError, match="❗️ Input is not an integer"):
            find_next_perfect_square.find_next_square("blah")

    def should_give_negative_1_when_input_is_5():
        """🧪 should give -1 when the input is 5"""
        assert find_next_perfect_square.find_next_square(5) == -1

    def should_give_144_when_input_is_121():
        """🧪 should give 144 when the input is 121"""
        assert find_next_perfect_square.find_next_square(121) == 144

    def should_give_negative_1_when_input_is_122():
        """🧪 should give -1 when the input is 122"""
        assert find_next_perfect_square.find_next_square(122) == -1

    def should_give_676_when_input_is_625():
        """🧪 should give 676 when the input is 625"""
        assert find_next_perfect_square.find_next_square(625) == 676
