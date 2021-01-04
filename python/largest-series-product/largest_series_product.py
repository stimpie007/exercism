from typing import Generator


def serie_product(serie: Generator):
    """
    Get the product of a series

    :param:
    serie: Generator

    :return:
    product: int
    """
    product = 1
    for char in serie:
        product *= int(char)
    return product


def largest_product(series: str, size: int) -> int:
    """
    Find the largest product size in the series

    :param:
    series: str
    size: int

    :return:
    product: int
    """
    if size < 0:
        raise ValueError('Size must be a natural number.')

    # Generate all combinations based on the size
    combinations = (series[i:size + i] for i in range(0, len(series) - size + 1))

    # Generate a product for each combination
    products = (serie_product(combination) for combination in combinations)

    # Return the largest product
    return max(products)
