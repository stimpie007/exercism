MINE = '*'
EMPTY = " "


def investigate_index_for_mine(index: list, score: int, minefield: list):
    """
    Check for value in minefield

    :params:
    index: list
    score: int
    minefield: minefield
    """
    if index[0] < 0 or index[0] > len(minefield) - 1 or index[1] < 0 or index[1] > len(minefield[0]) - 1:
        return

    if minefield[index[0]][index[1]] == MINE:
        score[0] += 1
    elif minefield[index[0]][index[1]] == EMPTY:
        pass
    else:
        raise ValueError("Bad value in minefield")


def count_number_of_adj_mines(index: list, minefield: list) -> int:
    """
    Check for adjoining mines from index

    :params:
    index: list
    minefield: list

    :return:
    adjoining_mines: int
    """
    score = [0]

    investigate_index_for_mine([index[0] + 1, index[1]], score, minefield)
    investigate_index_for_mine([index[0] + 1, index[1] + 1], score, minefield)
    investigate_index_for_mine([index[0] + 1, index[1] - 1], score, minefield)
    investigate_index_for_mine([index[0], index[1] + 1], score, minefield)
    investigate_index_for_mine([index[0], index[1] - 1], score, minefield)
    investigate_index_for_mine([index[0] - 1, index[1] + 1], score, minefield)
    investigate_index_for_mine([index[0] - 1, index[1] - 1], score, minefield)
    investigate_index_for_mine([index[0] - 1, index[1]], score, minefield)

    return score[0]


def validate_minefield(minefield: list):
    """
    Validate if the minefield is in good format

    :param:
    minefield: list
    """
    row_len = len(minefield[0])
    for i in range(len(minefield)):
        if len(minefield[i]) != row_len:
            raise ValueError("Bad minefield. Number of columns is not consistent")


def annotate(minefield: list) -> list:
    """
    Annotate the given minefield in correct format

    :param
    minefield: list

    :return:
    minefield_annotation: list
    """
    if not minefield:
        return minefield
    validate_minefield(minefield)

    minefield_annotation = []
    for i in range(len(minefield)):
        minefield_annotation.append([])
        for j in range(len(minefield[0])):
            if minefield[i][j] != MINE:
                num_of_mines = count_number_of_adj_mines([i, j], minefield)
                if num_of_mines == 0:
                    minefield_annotation[i].append(EMPTY)
                else:
                    minefield_annotation[i].append(str(num_of_mines))

            else:
                minefield_annotation[i].append(MINE)
        minefield_annotation[i] = "".join(minefield_annotation[i])
    return minefield_annotation
