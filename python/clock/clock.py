class Clock:
    def __init__(self, hour, minute):
        self.hour, self.min = divmod((hour * 60 + minute) % (24 * 60), 60)

    def __repr__(self):
        return f"{self.hour:02d}:{self.min:02d}"

    def __eq__(self, other):
        return self.hour == other.hour and self.min == other.min

    def __add__(self, minutes):
        return self.__class__(self.hour, self.min + minutes)

    def __sub__(self, minutes):
        return self.__class__(self.hour, self.min - minutes)
