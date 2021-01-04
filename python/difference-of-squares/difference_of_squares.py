def square_of_sum(number: int) -> int:
    """
    Square the total of each number starting 0.
    Example: (1 + 2 + ... + 10)² = 55² = 3025.

    :param
    number: int

    :return:
    square_of_sum: int
    """
    return pow(sum(range(number + 1)), 2)


def sum_of_squares(number: int) -> int:
    """
    Square of each number added together starting 0.
    Example: 1² + 2² + ... + 10² = 385.

    :param
    number: int

    :return:
    sum_of_squares: int
    """
    return sum([pow(num, 2) for num in range(number + 1)])


def difference_of_squares(number: int) -> int:
    """
    Difference between square_of_sum and sum_of_squares.

    :param
    number: int

    :return:
    difference_of_squares: int
    """
    return square_of_sum(number) - sum_of_squares(number)
