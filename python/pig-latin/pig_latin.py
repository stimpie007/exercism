VOWELS = "aeiou"


def translate(text: str) -> str:
    """
    Translate text in Pig Latin

    :param:
    text: str

    :return:
    pig_latin: str
    """
    return " ".join(translate_word(word) for word in text.split(" "))


def translate_word(word: str) -> str:
    """
    Translate a word to Pig Latin

    :param:
    word: str

    :return:
    orderd_word: str
    """
    return reorder_word(word) + "ay"


def reorder_word(word: str) -> str:
    """
    Reorder the word according to Pig Latin rules

    :param:
    word: str

    :return:
    orderd_word: str
    """
    if word[0] in VOWELS or word[:2] in ("yt", "xr"):
        return word
    elif word[:2] == "qu":
        return word[2:] + word[:2]
    else:
        # Place the first consonant to the end and call us recursively!
        return reorder_word(word[1:] + word[0])
