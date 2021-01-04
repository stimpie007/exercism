def is_paired(input_string: str) -> bool:
    """
    Check if brackets are matching and correct order of opening and closing.

    :param:
    input_string: str

    :return:
    stack: bool
    """
    pairs = {'{': '}', '[': ']', '(': ')'}
    stack = []

    for char in input_string:
        if char in pairs.keys():
            stack.append(char)
        elif char in pairs.values():
            if not stack or char != pairs[stack.pop()]:
                return False

    return not stack
