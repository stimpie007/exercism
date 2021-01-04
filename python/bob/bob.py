def response(hey_bob: str) -> str:
    """
    Response of Bob

    :param
    hey_bob: string

    :return:
    response: string
    """
    ask = hey_bob.replace(' ', '')

    if ask.endswith('?') and ask.isupper():
        return "Calm down, I know what I'm doing!"
    elif ask.endswith('?'):
        return "Sure."
    elif ask.isupper():
        return "Whoa, chill out!"
    elif not ask.strip():
        return "Fine. Be that way!"
    else:
        return "Whatever."
