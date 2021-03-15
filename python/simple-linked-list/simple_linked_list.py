class Node:
    def __init__(self, value):
        pass

    def value(self):
        pass

    def next(self):
        pass


class LinkedList:
    def __init__(self, values=[]):
        self.values = values
        self._value = None

    def __len__(self):
        return len(self.values)

    def head(self):
        if not self.values:
            raise EmptyListException()
        self._value = self.values[-1]
        return self

    def value(self):
        return self._value

    def push(self, value):
        pass

    def pop(self):
        pass

    def reversed(self):
        pass


class EmptyListException(Exception):
    # raise ValueError("Pretty empty list eh.")
    pass
