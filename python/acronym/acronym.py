from re import findall


def abbreviate(words):
    words = words.replace("'", "").title()
    return ''.join(findall('[A-Z]', words))
