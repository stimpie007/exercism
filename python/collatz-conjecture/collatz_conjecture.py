def input_validation(number):
    if number <= 0:
        raise ValueError(f"Input {number} is not a positive integer")


def steps(number):
    input_validation(number)

    amountofsteps = 0

    while not (number == 1):
        if number % 2 == 0:  # even
            number = number / 2
        else:  # odd
            number = (number * 3) + 1

        amountofsteps += 1

    return amountofsteps
