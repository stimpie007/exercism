from random import choices, seed
from string import ascii_uppercase


def create_name() -> str:
    """
    Generate a name with 2 uppercase letters and 3 numbers

    :return:
    name: str
    """
    seed()
    digits = [str(digit) for digit in range(10)]
    return ''.join(choices(ascii_uppercase, k=2) + choices(digits, k=3))


class Robot:
    """
    A cool robot with a name
    """
    def __init__(self):
        """
        Create a name on initialisation
        """
        self.name = create_name()

    def reset(self):
        """
        Reset the name of the robot
        """
        self.name = create_name()
