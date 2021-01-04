SUBLIST, SUPERLIST, EQUAL, UNEQUAL = range(4)


def sublist(list_one: list, list_two: list):
    """
    Check if the given lists are sublist, superlist, equal lists or is unequal from eachother.

    :param
    list_one: list
    list_two: list

    :return:
    list_type: bool
    """
    a = ','.join([str(element) for element in list_one])
    b = ','.join([str(element) for element in list_two])

    if a == b:
        return EQUAL
    elif a in b:
        return SUBLIST
    elif b in a:
        return SUPERLIST
    else:
        return UNEQUAL
