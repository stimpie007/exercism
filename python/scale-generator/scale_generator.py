"""
Exercism solution for "scale-generator"
"""
from dataclasses import dataclass, field
from typing import List

SHARP_SCALE = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
FLAT_SCALE = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
FLAT_TONICS = {"Bb", "Db", "Eb", "F", "Gb", "Ab", "bb", "c", "d", "eb", "f", "g"}
INTERVALS = {"m": 1, "M": 2, "A": 3}
NOTES = 12

Chromatic = List[str]


@dataclass
class Scale:
    """
    Simple implementation of a musical scale.
    """

    tonic: str
    scale: Chromatic = field(repr=False, compare=False)

    def __init__(self, tonic: str) -> None:
        scale = FLAT_SCALE if tonic in FLAT_TONICS else SHARP_SCALE
        self.tonic = tonic.title()
        index = scale.index(self.tonic)
        self.scale = scale[index:] + scale[:index]

    def chromatic(self) -> Chromatic:
        """
        Return the chromatic scale for this tonic.
        """
        return self.scale[:]

    def interval(self, interval: str) -> Chromatic:
        """
        Return the scale for this tonic and interval.
        """
        steps = [INTERVALS[i] for i in interval]
        if sum(steps) != NOTES:
            raise ValueError("Interval will not result in a full scale!")
        index = self.scale.index(self.tonic)
        pitches = [self.tonic]
        for step in steps[:-1]:
            index += step
            pitches.append(self.scale[index % NOTES])
        return pitches
