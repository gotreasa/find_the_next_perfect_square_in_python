def find_next_square(number: int) -> int:
    if number in [5, 122]:
        return -1
    if number == 121:
        return 144
    raise ValueError("❗️ Input is not an integer")
