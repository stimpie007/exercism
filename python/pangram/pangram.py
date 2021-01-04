from string import ascii_lowercase


def is_pangram(sentence):
    """
    Check if the sentence given is a pangram

    :param
    sentence: string

    :return:
    True or False: bool
    """
    alphabet = set(ascii_lowercase)
    return alphabet.issubset(sentence.lower())
