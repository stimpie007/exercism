def classify(number: int) -> str:
    """
    Classify the given number according to Nicomachus classification.

    :param:
    number: int

    :return:
    classification: str
    """
    if type(number) is not int or number <= 0:
        raise ValueError("Not a natural number.")

    aliquots = [i for i in range(1, number) if number % i == 0]

    if sum(aliquots) == number:
        return "perfect"
    elif sum(aliquots) > number:
        return "abundant"
    elif sum(aliquots) < number:
        return "deficient"
