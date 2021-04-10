def encode(numbers):
    hex_list = []
    for n in range(len(numbers)):
        bi = str(bin(numbers[n])[2:])
        segment_indexes = [i for i in range(len(bi), 0, -7)][::-1]
        for i in segment_indexes:
            if i > len(bi) - 7:
                section = "0" + bi[i - 7:i]
            elif i > 7:
                section = "1" + bi[i - 7:i]
            else:
                section = "1" + "0" * (7 - i) + bi[:i]
            hex_list.append(int(section, 2))
            print(hex(int(section, 2)))
    return hex_list


def decode(bytes_):
    hex_list = []
    string = ""
    for n in range(len(bytes_)):
        section = bin(bytes_[n])
        if len(str(section)) == 10:
            section = section[3:]
            end_flag = False
        else:
            section = section[2:]
            end_flag = True
        if not end_flag and len(bytes_) - 1 - n == 0: raise ValueError("sign bit is 1 but no octet follows")
        section = "0" * (7 - len(section)) + section
        string += section
        if end_flag:
            number = int(string, 2)
            hex_list.append(number)
            string = ""
            print(hex(number))
    return hex_list
