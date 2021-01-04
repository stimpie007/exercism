class BufferFullException(Exception):
    def __init__(self):
        raise BufferError("Buffer is full.")


class BufferEmptyException(Exception):
    def __init__(self):
        raise BufferError("Buffer is empty.")


class CircularBuffer:
    """
    Data structure that uses a single, fixed-size buffer as if it were connected end-to-end.
    """

    def __init__(self, capacity: int):
        self.buffer = list()
        self.capacity = capacity

    def read(self) -> str:
        """
        Read item from buffer

        :return:
        buffer: int
        """
        try:
            return self.buffer.pop(0)
        except BufferEmptyException:
            return BufferEmptyException()

    def write(self, data: str):
        """
        Write to buffer

        :param:
        data: str
        """
        if len(self.buffer) < self.capacity:
            self.buffer.append(data)
        else:
            raise BufferFullException()

    def overwrite(self, data: str):
        """
        Overwrite buffer value

        :param:
        data: str
        """
        if len(self.buffer) == self.capacity:
            self.buffer.pop(0)
        self.write(data)

    def clear(self):
        """
        Clear the buffer
        """
        self.buffer.clear()
