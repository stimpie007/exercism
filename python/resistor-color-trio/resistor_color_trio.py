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


def label(colors: List[str]) -> str:
    """
    Return the number of color code

    :param colors: List of strings
    :return: str
    """
    color_one = COLORS.get(colors[0])
    color_two = COLORS.get(colors[1])
    color_three = pow(10, COLORS.get(colors[2]))

    color = int(str(color_one) + str(color_two)) * color_three

    if str(color)[-3:] == '000':
        return str(color)[:-3] + " kiloohms"
    else:
        return str(color) + " ohms"