def rows(letter):
    a = ord(letter) - 65
    res = []
    for i in range(a + 1):
        if i == 0:
            res.append(" " * (a) + 'A' + " " * (a))
        else:
            res.append(" " * (a - i) + chr(i + 65) + " " * (i * 2 - 1) + chr(i + 65) + " " * (a - i))
    return res + res[0:-1][::-1]
