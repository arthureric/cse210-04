class Point:
    """A distance from a relative origin (0, 0).

    The responsibility of Point is to hold and provide information about itself. Point has a few 
    convenience methods for adding, scaling, and comparing them.

    Attributes:
        _x (integer): The horizontal distance from the origin.
        _y (integer): The vertical distance from the origin.
    """
    
    def __init__(self, x, y):
        """Constructs a new Point using the specified x and y values.
        
        Args:
            x (int): The specified x value.
            y (int): The specified y value.
        """
        self._x = x
        self._y = y

    def add(self, other):
        """Gets a new point that is the sum of this and the given one.

        Args:
            other (Point): The Point to add.

        Returns:
            Point: A new Point that is the sum.
        """
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)

    def equals(self, other):
        """Whether or not this Point is equal to the given one.

        Args:
            other (Point): The Point to compare.

        Returns: 
            boolean: True if both x and y are equal; false if otherwise.
        """
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        """Gets the horizontal distance.
        
        Returns:
            integer: The horizontal distance.
        """
        return self._x

    def get_y(self):
        """Gets the vertical distance.
        
        Returns:
            integer: The vertical distance.
        """
        return self._y

    def scale(self, factor):
        """
        Scales the point by the provided factor.

        Args:
            factor (int): The amount to scale.
            
        Returns:
            Point: A new Point that is scaled.
        """
        return Point(self._x * factor, self._y * factor)

    def touches(self, other, cell_size):
        """Whether or not this Point touches other's position.

        Args:
            other (Point): The Point to compare.
            cell_size (int): the value that corresponds to the dimension of an Actor in pixels

        Returns: 
            boolean: True if both x and y are in the other's area; false if otherwise.
        """
        sx = self._x
        sy = self._y 
        ox = other.get_x() 
        oy = other.get_y()

        """
            I tested two versions of touch()
            1) the artifact needs to be in the same exact column as the robot
            2) the artifact has any part of it inside the area of the robot
                This is for the case where the robot could move freely in pixels.
 
        """
        # the artifact will be considered touched only if it lands directly on the robot.
        return (oy + cell_size >= sy) and (sx == ox)

        # if any part of the artifact is within the robot's area, the artifact is considered touched.
        # return (oy + cell_size >= sy) and ((sx <= ox + cell_size <= sx + cell_size) or (sx <= ox <= sx + cell_size))
