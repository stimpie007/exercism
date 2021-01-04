# Globals for the directions
# Change the values as you see fit
EAST = 2
NORTH = 1
WEST = 0
SOUTH = 3


class Robot:
    """
    A robot that can move left, right and advance the position it is facing.
    """
    def __init__(self, direction=NORTH, x=0, y=0):
        """
        :param
        direction: [NORTH, EAST, SOUTH, WEST]
        x: int
        y: int
        """
        self._position_x = x
        self._position_y = y
        self.direction = direction

    @property
    def coordinates(self):
        """
        :return:
        coordinates: tuple
            (2, 3)
        """
        return tuple((self._position_x, self._position_y))

    def move(self, movement: str):
        """
        :param
        movement: str
            'A', 'R', 'L'
        """
        for direction in movement:
            if direction == 'R':
                self.direction = (self.direction + 1) % 4
            elif direction == 'L':
                self.direction = (self.direction - 1) % 4
            elif direction == 'A':
                if self.direction is NORTH:
                    self._position_y += 1
                elif self.direction is SOUTH:
                    self._position_y -= 1
                elif self.direction is EAST:
                    self._position_x += 1
                elif self.direction is WEST:
                    self._position_x -= 1
            else:
                raise ValueError("Wrong movement entered. Use R/A/L.")
