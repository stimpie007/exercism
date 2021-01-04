from typing import List


def flatten(iterable: list) -> List[int]:
    """
    Get all numbers from a give list

    :param:
    iterable: list

    :return:
    flattened_list: List[int]
    """
    flattened_list = list()

    for element in iterable:
        if isinstance(element, list):
            flattened_list = flattened_list + flatten(element)
        else:
            flattened_list.append(element)

    return list(filter(None.__ne__, flattened_list))
