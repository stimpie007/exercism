"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0

    def __init__(self, x, y):
        Alien.total_aliens_created += 1
        self.x_coordinate = x
        self.y_coordinate = y
        self.health = 3
    
    def hit(self):
        self.health -= 1

    def is_alive(self):
        return True if self.health > 0 else False
    
    def teleport(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y

    def collision_detection(self, other_object):
        """
        TODO: Create collision detection
        """
        pass

    def total_aliens_created(self):
        return self.total_aliens_created
#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
