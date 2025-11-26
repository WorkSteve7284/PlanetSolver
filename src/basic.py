""" Basic classes & methods for PlanetSolver """

import dataclasses
import enum
import math

TARGET_PLANET_NAME: str = "Target"

@dataclasses.dataclass
class Point:
    """ Store a point in 2D space """
    def __init__(self, x: float | int, y: float | int):
        self.x = x
        self.y = y

    def __add__(self, other: 'Point'):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float | int):
        return Point(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float | int):
        return self * scalar

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other


    def magnitude(self):
        """ Return the length of this vector """
        return math.sqrt(self.x**2 + self.y**2)

    def round(self):
        """ Round this to int """
        return Point(int(round(self.x)), int(round(self.y)))

class Status(enum.Enum):
    """ Return values from a ship's travel """
    FAIL = 0
    SUCCESS = 1

    def __str__(self):
        match self:
            case Status.FAIL:
                return 'fail'
            case Status.SUCCESS:
                return 'success'

class Resupply(enum.Enum):
    """ Store type of a planet """
    NONE = 0
    FOOD = 1
    OXYGEN = 2

    def __str__(self):
        match self:
            case Resupply.NONE:
                return 'none'
            case Resupply.FOOD:
                return 'food'
            case Resupply.OXYGEN:
                return 'oxygen'

@dataclasses.dataclass
class TravelPath:
    """ Store the path of a ship from one planet to the next"""
    planets: tuple[str, str] # from, to
    distance: float

    # Min/max to not die
    min_speed: float
    max_speed: float