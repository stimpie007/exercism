from itertools import groupby
from re import sub


def decode(string: str) -> str:
    """
    Decode a run length code

    :param
    string: str

    :return:
    result: str
    """
    return sub(r'(\d+)(\D)', lambda x: x.group(2) * int(x.group(1)), string)


def encode(string: str) -> str:
    """
        Encode a long string

        :param
        string: str

        :return:
        result: str
        """
    return sub(r'(.)\1+', lambda x: str(len(x.group(0))) + x.group(1), string)
