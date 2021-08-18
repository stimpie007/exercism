#  Points
OUTER_CIRKLE = 1
MIDDLE_CIRKLE = 5
INNER_CIRKLE = 10


def score(x, y):
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
