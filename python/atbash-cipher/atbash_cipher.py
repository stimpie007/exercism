from string import ascii_letters, punctuation


def encode(plain_text: str):
    """
    Encipher given text using atbash cipher

    :param
    plain_text: str

    :return:
    cipher: str
    """
    trans = plain_text.maketrans(ascii_letters, ''.join(reversed(ascii_letters)))
    cipher = plain_text.translate(trans).lower().replace(' ', '')
    cipher = cipher.translate(str.maketrans('', '', punctuation))
    return ' '.join(cipher[i:i + 5] for i in range(0, len(cipher), 5))


def decode(ciphered_text: str):
    """
    Decipher given cipher using atbash cipher

    :param
    ciphered_text: str

    :return:
    text: str
    """
    trans = ciphered_text.maketrans(''.join(reversed(ascii_letters)), ascii_letters)
    text = ciphered_text.translate(trans).lower().replace(' ', '')
    return text.translate(str.maketrans('', '', punctuation))
