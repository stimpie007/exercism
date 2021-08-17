def input_validation(number):
    if number <= 0:
        raise ValueError(f"Input {number} is not a positive integer")


def steps(number):
    input_validation(number)

    amountofsteps = 0

    while not (number == 1):
        # odd
        if number % 2 != 0:
            number = (number * 3) + 1
        # even
        if number % 2 == 0:
            number = number / 2

        amountofsteps += 1

    return amountofsteps
