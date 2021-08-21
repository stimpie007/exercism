class StackUnderflowError(Exception):
    pass


def evaluate(input_data):
    intops = {
        '-': lambda x, y: y - x,
        '+': lambda x, y: y + x,
        '*': lambda x, y: y * x,
        '/': lambda x, y: y // x
    }
    stackops = {
        'DUP': lambda s: s + [s[-1]] if len(s) > 0 else None,
        'DROP': lambda s: s[:-1] if len(s) > 0 else None,
        'SWAP': lambda s: s[:-2] + [s[-1], s[-2]] if len(s) > 1 else None,
        'OVER': lambda s: s + [s[-2]] if len(s) > 1 else None
    }
    override = {}
    stack = []
    input_data = list(filter(None, input_data))
    while input_data:
        print('input data: ', input_data)
        input = [x for x in input_data[0].split(' ') if x != '']
        input_data = input_data[1:]
        if input[0] == ':' and input[-1] == ';':
            if input[1].isdigit():
                raise ValueError
            override[input[1].upper()] = ' '.join(input[2:-1]).upper()
            continue
        for data in input:
            if data.upper() in override:
                input_data.insert(0, override[data.upper()])
                break
            if data.isdigit():
                stack.append(int(data))
            elif data in intops:
                if len(stack) > 1:
                    stack.append(intops[data](stack.pop(), stack.pop()))
                else:
                    raise StackUnderflowError(input_data)
            elif data.upper() in stackops:
                if stackops[data.upper()](stack) is not None:
                    stack = stackops[data.upper()](stack)
                else:
                    raise StackUnderflowError(input_data)
            else:
                raise ValueError
    return stack
