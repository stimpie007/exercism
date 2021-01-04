from typing import List


class Matrix:
    """
    Create a matrix from given input
    """

    def __init__(self, matrix_string: str):
        self.matrix = [[int(char) for char in line.split()] for line in matrix_string.splitlines()]

    def row(self, index: int) -> List[int]:
        """
        Get the row at given index

        :param:
        index: int

        :return:
        row: List[int]
        """
        return self.matrix[index - 1]

    def column(self, index: int) -> List[int]:
        """
        Get the column at given index

        :param
        index: int

        :return:
        column: List[int]
        """
        return [row[index - 1] for row in self.matrix]
