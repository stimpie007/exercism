from typing import List


def is_divisible(current: int, primes: int) -> bool:
    """
    Check if given number is divisible by the primes

    :param:
    current: int
    primes: List[int]

    :return:
    divisible: bool
    """
    return any(current % p == 0 for p in primes if current >= p ** 2)


def prime_range(number: int) -> List[int]:
    """
    Return a range of primary numbers from given input amount

    :param:
    number: int

    :return:
    primes: List[int]
    """
    primes = []
    current = 2
    while len(primes) < number:
        if not is_divisible(current, primes):
            primes.append(current)
        current += 1
    return primes


def prime(number: int) -> int:
    """
    Return the nth  prime number

    :param:
    number: int

    :return:
    prime: int
    """
    if 0 < number:
        return prime_range(number)[-1]
    else:
        raise ValueError(f"{number} cannot be smaller then 1.")
