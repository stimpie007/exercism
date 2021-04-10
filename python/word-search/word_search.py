class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def search(self, word):
        width, height = len(self.puzzle[0]) - 1, len(self.puzzle) - 1
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1),  # → ← ↓ ↑
                      (-1, -1), (1, -1), (-1, 1), (1, 1))  # ↖ ↗ ↙ ↘
        # Storing co-ordinates of all the points in the puzzle that match first alphabet in the word to be searched
        points = [(x, y) for x in range(width + 1) for y in range(height + 1) if self.puzzle[y][x] == word[0]]
        # start iterating over all the matched first character of the target word
        for x, y in points:
            start_coordinates = Point(x, y)
            # search through all the possible directions for a given set of coordinates
            for direction in directions:
                line = []
                x2, y2 = x, y
                while 0 <= x2 <= width and 0 <= y2 <= height:
                    line.append(self.puzzle[y2][x2])
                    # if found match return the matched start and the end cordinates
                    if word == ''.join(line):
                        end_cordinates = Point(x2, y2)
                        return start_coordinates, end_cordinates
                    else:
                        x2 += direction[0]
                        y2 += direction[1]
        return None
