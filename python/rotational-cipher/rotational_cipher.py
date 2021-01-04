from string import ascii_lowercase as lc, ascii_uppercase as uc


def rotate(text: str, key: int) -> str:
    """
    Rotate given string with key

    :param
    text: str
    key: int

    :return:
    Encoded string
    """
    lookup = str.maketrans(lc + uc, lc[key:] + lc[:key] + uc[key:] + uc[:key])
    return text.translate(lookup)
