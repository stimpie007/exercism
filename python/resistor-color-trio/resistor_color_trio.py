from typing import List

COLORS = {
    "black": "0",
    "brown": "1",
    "red": "2",
    "orange": "3",
    "yellow": "4",
    "green": "5",
    "blue": "6",
    "violet": "7",
    "grey": "8",
    "white": "9"
}


def label(colors: List[str]) -> str:
    """
    Return the number of color code
    :param colors: List of strings
    :return: str
    """
    color_code = int(COLORS.get(colors[0]) + COLORS.get(colors[1])) * pow(10, int(COLORS.get(colors[2])))
    return f"{str(color_code)[:-3]} kiloohms" if color_code % 1e3 == 0 else f"{color_code} ohms"
