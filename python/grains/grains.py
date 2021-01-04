def square(number: int) -> int:
    """
    Get the amount of grains up to given square

    :param:
    number: int

    :return:
    grains: int
    """
    if number <= 0 or 64 < number:
        raise ValueError("Number {} is not between 1 and 64".format(number))

    return 1 << (number - 1)  # Bitwise left shift for pow(2, number -1)


def total() -> int:
    """
    Get the total amount of grains

    :return:
    total_grains: int
    """
    return (1 << 64) - 1  # Bitwise left shift for pow(2, 64) -1
