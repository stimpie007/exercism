def smallest(max_factor: int, min_factor=0) -> tuple:
    """
    Largest palindrome

    :params:
    max_factor: int
    min_factor: int [default=0]

    :return:
    largest_palindrome: tuple
    """
    return palindrome(min_factor, max_factor)


def largest(max_factor: int, min_factor=0) -> tuple:
    """
    Largest palindrome

    :params:
    max_factor: int
    min_factor: int [default=0]

    :return:
    largest_palindrome: tuple
    """
    return palindrome(min_factor, max_factor, smallest=False)


def palindrome(mn: int, mx: int, smallest=True) -> list:
    """
    Get the product of palindromes

    :params:
    mn: int
    mx: int
    smallest: bool

    :return:
    palindromes: list
    """
    args = (mn ** 2, mx ** 2 + 1) if smallest else (mx ** 2, mn ** 2 - 1, -1)

    for r in range(*args):
        s = str(r)
        if s == s[::-1] and any(mn <= r // j <= mx for j in range(mn, mx + 1) if r % j == 0):
            return r, ((i, r // i) for i in range(mn, mx + 1) if r % i == 0 and mn <= i <= r // i <= mx)
    else:
        raise ValueError('Could not calculate palindrome for these parameters')
