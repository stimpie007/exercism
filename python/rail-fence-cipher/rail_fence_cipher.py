from itertools import cycle


def encode(message: str, rails: int) -> str:
    """
    Encode a given message

    :params:
    message: str
    rails: int

    :return:
    encoded_message: str
    """
    p = fence_pattern(rails)
    return ''.join(sorted(message, key=lambda i: next(p)))


def decode(encoded_message: str, rails: int) -> str:
    """
    Decode a given message

    :params:
    encoded_message: str
    rails: int

    :return:
    decoded_message: str
    """
    p = fence_pattern(rails)
    indexes = sorted(range(len(encoded_message)), key=lambda i: next(p))
    result = [''] * len(encoded_message)
    for i, c in zip(indexes, encoded_message):
        result[i] = c
    return ''.join(result)


def fence_pattern(n: int) -> cycle:
    """
    Zigzag pattern
    :param:
    n: int

    :return:
    pattern: itertools.cycle
    """
    r = list(range(n))
    return cycle(r + r[-2:0:-1])
