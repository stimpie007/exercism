def primes(limit: int) -> list:
    """
    Get a list of prime numbers for the given limit using Sieve of Eratosthenes

    :param:
    limit: int

    :return:
    primes: list
    """
    multiples = []
    prime_numbers = []
    for i in range(2, limit + 1):
        for j in range(i * i, limit + 1, i):
            multiples.append(j)
        if i not in multiples:
            prime_numbers.append(i)
    return prime_numbers
