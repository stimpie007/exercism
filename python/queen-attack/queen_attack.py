def validate_input(row: int, column: int):
    """
    Validate if given input matches our criteria

    :params:
    row: int
    column: int
    """
    if row < 0 or column < 0:
        raise ValueError("Position cannot be negative.")
    if row >= 8 or column >= 8:
        raise ValueError("The board is 0 - 7 squares. Given position is out of bounds.")


class Queen:
    def __init__(self, row: int, column: int):
        """
        Queen object that holds x and y position.

        :params:
        row: int
        column: int
        """
        validate_input(row, column)
        self.row = row
        self.column = column

    def can_attack(self, another_queen) -> bool:
        """
        Check if we can attack the other opponent

        :param:
        another_queen: Queen object

        :return:
        can_attack: bool
        """
        if (self.row, self.column) == (another_queen.row, another_queen.column):
            raise ValueError("Opponent is on the same position.")

        def horizontally(row):
            return self.row == row

        def vertically(column):
            return self.column == column

        def diagonally(row, column):
            candidates = set()

            for i in range(0, 8):
                candidates.update([
                    (self.row + i, self.column + i),
                    (self.row + i, self.column - i),
                    (self.row - i, self.column + i),
                    (self.row - i, self.column - i)
                ])

            return True if (row, column) in candidates else False

        return horizontally(another_queen.row) or \
               vertically(another_queen.column) or \
               diagonally(another_queen.row, another_queen.column)
