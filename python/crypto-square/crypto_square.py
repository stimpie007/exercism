from math import sqrt, ceil


def cipher_text(plain_text: str) -> str:
    """
    Make a secret message

    :param
    plain_text: str

    :return:
    secret_message = str
    """
    text = "".join(char for char in plain_text.lower() if char.isalnum())

    if (text_len := len(text)) <= 1:
        return text

    ceil_size = ceil(sqrt(text_len))
    rectangle = [text[i: i + ceil_size].ljust(ceil_size) for i in range(0, text_len, ceil_size)]

    return " ".join("".join(row[i] for row in rectangle) for i in range(ceil_size))
