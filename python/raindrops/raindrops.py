def convert(number):
    sounds = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong'
    }
    sound = ''

    for keys in sounds:
        if not number % keys:
            sound += sounds.get(keys, '')

    return sound if sound else str(number)
