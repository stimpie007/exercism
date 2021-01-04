def transform(legacy_data: dict) -> dict:
    """
    Transform current scrabble data to new format

    :param:
    legacy_data: dict

    :return:
    data: dict
    """
    return {letter.lower(): score for score, letters in legacy_data.items() for letter in letters}

    # data = dict()
    #
    # for score, letters in legacy_data.items():
    #     for letter in letters:
    #         data[letter.lower()] = score
    #
    # return data
