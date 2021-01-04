def is_armstrong_number(number):
    """
    Check if a number is an armstrong number

    :param
    number: int

    :return:
    bool
        [True, False]
    """
    # Pythonic way

    # numbers = list(str(number))
    # total = 0
    #
    # for digit in numbers:
    #     total += pow(int(digit), len(numbers))
    #
    # return True if total == number else False


    # Non-pythonic way

    # numbers = list(str(number))
    # armstrong = lambda digit: pow(int(digit), len(numbers))
    # total = sum(list(map(armstrong, numbers)))
    # return True if total == number else False


    # Short version

    return True if sum([int(digit)**len(list(str(number))) for digit in list(str(number))]) == number else False
