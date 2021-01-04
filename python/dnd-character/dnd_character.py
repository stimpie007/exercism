import math
from random import randint, choice
from typing import List

ABILITIES = [
    "charisma",
    "wisdom",
    "intelligence",
    "constitution",
    "dexterity",
    "strength"
]


def round_decimals_down(number: int, decimals=0) -> int:
    """
    Returns a value rounded down to a specific number of decimal places.

    :params
    number: int
    decimals: int [default=0]

    :returns
    round_down_number: int
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more")
    elif decimals == 0:
        return math.floor(number)

    factor = 10 ** decimals
    return math.floor(number * factor) / factor


def modifier(mod: int) -> int:
    """
    Returns character constitution modifier

    :param
    mod: int

    :return
    modifier: int
    """
    return round_decimals_down((mod - 10) / 2)


def roll_dice() -> List[int]:
    """
    Roll dice 4 times

    :return
    roll_list: List[int]
    """
    rolls = [randint(1, 6) for roll in range(4)]
    return sum(sorted(rolls)[-3:])


class Character:
    """
    Create a random generated character with several abilities and hitpoints.

    :attr
    charisma: int
    widsdom: int
    intelligence: int
    constitution: int
    dexterity: int
    strength: int
    hitpoints: int

    :method
    ability: int
        Return a random chosen character ability value
    """

    def __init__(self):
        self.charisma = roll_dice()
        self.wisdom = roll_dice()
        self.intelligence = roll_dice()
        self.constitution = roll_dice()
        self.dexterity = roll_dice()
        self.strength = roll_dice()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self) -> int:
        """
        Return a random chosen character ability value

        :return
        ability: int
        """
        return self.__getattribute__(choice(ABILITIES))
