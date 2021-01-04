from typing import List


def sum_of_multiples(limit: int, multiples: List[int]) -> int:
    """
    Return the sum of all the unique multiples of particular numbers up to but not including that number.

    :param:
    limit: int
    multiples: list

    :return:
    sum_of_multiples: int
    # """
    return sum({
        x
        for multiple in multiples if multiple != 0
        for x in range(multiple, limit, multiple)
    })
