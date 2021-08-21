BLACK = 'B'
WHITE = 'W'
NONE = ''
STONES = 'BW'
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # UP RIGHT DOWN LEFT


class Board:
    """Count territories of each player in a Go game
    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.board = board
        self.length = len(self.board)
        self.width = len(self.board[0])

    def valid(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.length

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board
        Args:
            x (int): Column on the board
            y (int): Row on the board
        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        if not self.valid(x, y):
            raise ValueError('Please enter a valid start coordinate.')

        set_stone, set_terr = self.move(x, y, [], [], [])

        if len(set_stone) == 1 and len(set_terr) == 1 and self.board[y][x] in STONES:
            return NONE, set()
        elif len(set_stone) == 1:
            return list(set_stone)[0], set_terr
        else:
            return NONE, set_terr

    def move(self, x, y, visited, terr, stones):

        if self.valid(x, y):
            visited.append((x, y))
            if self.board[y][x] in STONES:
                stones.append(self.board[y][x])
            elif self.board[y][x] == ' ':
                terr.append((x, y))

            for d in DIRECTIONS:
                if self.board[y][x] in STONES:
                    if len(visited) == 1:
                        terr.append((x, y))
                    break
                if self.valid(x + d[1], y + d[0]) and (x + d[1], y + d[0]) not in visited:
                    self.move(x + d[1], y + d[0], visited, terr, stones)

        return set(stones), set(terr)

    def territories(self):
        """Find the owners and the territories of the whole board
        Args:
            none
        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        table = {'B': set(), 'W': set(), '': set()}

        for x_c in range(self.length):
            for y_c in range(self.width):
                s, t = self.territory(y_c, x_c)
                if table[s] != set():
                    table[s].update(t)
                else:
                    table[s] = t

        return table