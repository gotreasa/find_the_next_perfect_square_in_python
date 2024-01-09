import math


def find_next_square(number: int) -> int:
    if not isinstance(number, int):
        raise ValueError("❗️ Input is not an integer")
    square_root = math.sqrt(number)

    if square_root.is_integer():
        return (square_root + 1) ** 2
    return -1
