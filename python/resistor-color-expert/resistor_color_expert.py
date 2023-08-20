# Encoding      Tolerance
# - Black: 0    Grey - 0.05%
# - Brown: 1    Violet - 0.1%
# - Red: 2      Blue - 0.25%
# - Orange: 3   Green - 0.5%
# - Yellow: 4   Brown - 1%
# - Green: 5    Red - 2%
# - Blue: 6     Gold - 5%
# - Violet: 7   Silver - 10%
# - Grey: 8
# - White: 9
import enum

ENCODING = {
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

TOLERANCES = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10
}


class SIZE_UNIT(enum.Enum):
    ohms = 1
    kiloohms = 2
    megaohms = 3


def convert_unit(size_in_bytes, unit):
    """ Convert the size from bytes to other units like kiloohms or megaohms"""
    if unit == SIZE_UNIT.kiloohms:
        return size_in_bytes / 1000
    elif unit == SIZE_UNIT.megaohms:
        return size_in_bytes / (1000 * 1000)
    else:
        return size_in_bytes


def resistor_label(colors):
    # (["orange", "orange", "black", "red"]), "33 ohms ±2%")
    # ["blue", "grey", "brown", "violet"]), "680 ohms ±0.1%")
    color1 = ENCODING[colors[0]]
    color2 = ENCODING[colors[1]]
    band = str(color1) + str(color2)

    multiplier = ENCODING[colors[2]] + len(band)
    ohms = convert_unit(band.ljust(multiplier, '0'))

    tolerance = TOLERANCES[colors[3]]

    return f"{band} {ohms} ±{tolerance}%"
