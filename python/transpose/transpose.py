from itertools import zip_longest


def transpose(lines: str) -> str:
    """
    Transpose text input to a string matrix

    :param:
    lines: str

    :return:
    transposed_string: str
        A string is returned with new lines to make it look like a matrix.
    """
    # fill up empty space with an uncommon value '$'
    iterable = zip_longest(*lines.splitlines(), fillvalue='$')

    # replace '$' with spaces
    return '\n'.join(''.join(word).rstrip('$').replace('$', ' ') for word in iterable)
