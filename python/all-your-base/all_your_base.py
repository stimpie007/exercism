def rebase(input_base, digits, output_base):
    if input_base < 2 or sum(filter(lambda x: x < 0 or x >= input_base, digits)) != 0 or output_base < 2:
        raise ValueError("wrong arguments")
    value = sum(map(lambda x: x[1] * input_base ** x[0], enumerate(reversed(digits))))
    output_digits = []
    while value > 0:
        output_digits.insert(0, value % output_base)
        value //= output_base
    return output_digits
