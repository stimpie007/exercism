def is_isogram(string):
    string = string.lower()

    for char in string:
        if char not in ['-', ' '] and string.count(char) > 1:
            return False

    return True
