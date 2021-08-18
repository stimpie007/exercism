#  Points
OUTER_CIRKLE = 1
MIDDLE_CIRKLE = 5
INNER_CIRKLE = 10


def score(x: int, y: int) -> int:
    """
    Calculate the score of the dart throw.

    Args:
        x: int
            x-coordinate of the throw
        y: int
            y-coordinate of the throw

    Returns:
        points: int
            Awarded points in regards to where the dart landed

    Raises:
        exception: Exception
            Raised when you're shot is completely off or not an integer.
    """
    radius = (x ** 2 + y ** 2) ** 0.5

    if radius > 10:
        return 0
    elif 10 >= radius > 5:
        return OUTER_CIRKLE
    elif 5 >= radius > 1:
        return MIDDLE_CIRKLE
    elif 1 >= radius:
        return INNER_CIRKLE
    else:
        raise Exception("You threw the dart at one eyed Pete.")
