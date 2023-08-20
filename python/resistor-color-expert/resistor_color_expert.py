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
colors = ["orange", "orange", "black", "red"]

def resistor_label(colors):
    # (["orange", "orange", "black", "red"]), "33 ohms ±2%")
    # ["blue", "grey", "brown", "violet"]), "680 ohms ±0.1%")
    color1 = ENCODING[colors[0]]
    color2 = ENCODING[colors[1]]
    band = str(color1) + str(color2)

    multiplier = ENCODING[colors[2]] + len(band)

    tolerance = TOLERANCES[colors[3]]

    return print(f"{band.ljust(multiplier, '0')} ohms ±{tolerance}%")