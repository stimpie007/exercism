from itertools import cycle
from random import choices
from string import ascii_lowercase

letter_indices = {letter: index for index, letter in enumerate(ascii_lowercase)}


class Cipher(object):
    def __init__(self, key=None):
        if key is None:
            key = ''.join(choices(ascii_lowercase, k=256))
        if set(key).difference(ascii_lowercase):
            raise ValueError
        self.key = key

    def _matchup(self, phrase):
        return zip(cycle(self.key), filter(str.isalpha, phrase.lower()))

    def encode(self, phrase):
        return ''.join(
            ascii_lowercase[(letter_indices[p] + letter_indices[k]) % 26]
            for k, p in self._matchup(phrase)
        )

    def decode(self, phrase):
        return ''.join(
            ascii_lowercase[(letter_indices[p] - letter_indices[k]) % 26]
            for k, p in self._matchup(phrase)
        )
