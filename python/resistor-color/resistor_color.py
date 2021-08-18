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


def color_code(color: str) -> int:
    """
    Get a resistor code for the given color

    Args:
        color: str
            Color to check resistor number

    Returns:
        resistor: int
            Resistor number for given color
    """
    return COLORS[color]


def colors() -> list:
    """
    Get a list of colors

    Returns:
        colors: list
            Colors to choose from
    """
    return list(COLORS)
