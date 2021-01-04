from typing import List

verses = {1: [' first ', "and a Partridge in a Pear Tree."],
          2: [' second ', "two Turtle Doves, "],
          3: [' third ', "three French Hens, "],
          4: [' fourth ', "four Calling Birds, "],
          5: [' fifth ', "five Gold Rings, "],
          6: [' sixth ', "six Geese-a-Laying, "],
          7: [' seventh ', "seven Swans-a-Swimming, "],
          8: [' eighth ', "eight Maids-a-Milking, "],
          9: [' ninth ', "nine Ladies Dancing, "],
          10: [' tenth ', "ten Lords-a-Leaping, "],
          11: [' eleventh ', "eleven Pipers Piping, "],
          12: [' twelfth ', "twelve Drummers Drumming, "]}


def recite_verse(verse_num: int) -> str:
    """
    Recite the verse

    :param
    verse_num: int

    :return:
    verse: str
    """
    output = f'On the{verses[verse_num][0]}day of Christmas my true love gave to me: '
    for i in range(verse_num, 0, -1):
        output += f'{verses[i][1]}'
    return output.replace('and ', '') if verse_num == 1 else output


def recite(start_verse: int, end_verse: int) -> List[str]:
    """
    Christmass carol

    :param
    start_verse: int
    end_verse: int

    :return:
    recite: List[str]
    """
    output = []
    for n in range(start_verse, end_verse + 1):
        output.append(recite_verse(n))
    return output
