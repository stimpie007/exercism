DIGITS_GRID = [
    " _     _  _     _  _  _  _  _ ",
    "| |  | _| _||_||_ |_   ||_||_|",
    "|_|  ||_  _|  | _||_|  ||_| _|",
    "                              "
]

def split(number):
    columns = zip(*number)
    args = [columns] * 3
    for digit in zip(*args):
        yield tuple(''.join(row) for row in zip(*digit))


def convert_line(number):
    digits = {d: str(i) for i, d in enumerate(split(DIGITS_GRID))}
    for digit in split(number):
        yield digits.get(digit, '?')


def convert_grid(grid):
    args = [iter(grid)] * 4
    for number in zip(*args):
        yield ''.join(convert_line(number))


def convert(grid):
    if len(grid) % 4 or any(len(line) % 3 for line in grid):
        raise ValueError(f'invalid size for input.')

    return ','.join(convert_grid(grid))
