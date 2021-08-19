from typing import List

COLORS = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}


def value(colors: List[str]) -> int:
    """
    Get the resistor code for given color codes

    Args:
        colors: List[str]
            Colors look for resistor code

    Returns:
        resistor_code: int
            Color code for the given resistors
    """
    return int(str(COLORS[colors[0]]) + str(COLORS[colors[1]]))
