def saddle_points(matrix: list) -> set:
    """
    Returns the list of all saddle points of the input matrix

    :param:
    matrix: list

    :return:
    saddle_points: list
    """
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("We need a regular matrix")

    row_maxs = [max(row) for row in matrix]
    col_mins = [min(col) for col in zip(*matrix)]

    saddle = [
        {"row": row, "column": column}
        for row, row_max in enumerate(row_maxs, start=1)
        for column, col_min in enumerate(col_mins, start=1)
        if row_max == col_min
    ]
    return saddle or [{}]
