from typing import List


def recite(start: int, take=1) -> List[str]:
    """
    Recite the lyrics

    :param:
    start: int
    take: int [default=1]

    :return:
    lyrics: List[str]
    """
    song = [verse(n) + [""] for n in range(start, start - take, -1)]
    return [line for v in song for line in v][:-1]


def verse(number: int) -> List[str]:
    """
    Create a verse from given number

    :param:
    number: int

    :return:
    verse: List[str]
    """
    return [
        f"{beer(number).capitalize()} on the wall, {beer(number)}.",
        (
            f"Take {'one' if number > 1 else 'it'} down and pass it around"
            if number else "Go to the store and buy some more"
        ) + f", {beer(number - 1)} on the wall."
    ]


def beer(number: int) -> str:
    """
    Check amount of beers and match words accordingly

    :param:
    number: int

    :return:
    lyric: str
    """
    return f"{'99' if number == -1 else number if number else 'no more'} bottle{'s' if number != 1 else ''} of beer"
