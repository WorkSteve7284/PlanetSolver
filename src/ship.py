""" Implement the Ship class"""

import dataclasses
import math

from src.basic import *
from src import galaxy

MAX_FOOD = 2000
MAX_O2 = 2000
MAX_FUEL = 3000

K_F = 0.3
K_L = 0.15

MAX_DEPTH = 100

@dataclasses.dataclass
class Resources:
    """ Store the maximum possible resources available to a ship """
    max_food: float = MAX_FOOD
    max_o2: float = MAX_O2
    max_fuel: float = MAX_FUEL

    def __str__(self):
        return f"Food: {self.max_food}, O2: {self.max_o2}, Fuel: {self.max_fuel}"

class Ship:
    """ Represent a ship traveling through space! """

    def __init__(self):
        self.resources = Resources()
        self.pos = Point(0, 0)
        self.history: list[TravelPath] = []
        self.depth = 0
        self.current_planet = 'Earth'

    def goto(self, galaxy_map: galaxy.Galaxy, target: str) -> Status:
        """ Move to a target planet. Returns success status """
        # calculate distance
        vec: Point = galaxy_map.planets[target].pos - self.pos # From here to target
        dist: float = vec.magnitude()

        # check if it goes through a hostile zone

        # convert vec to point-slope form ((0, 0) and vec)
        # y - y1 = m (x - x1)
        slope = vec.y / vec.x

        # convert point-slope to not-quite-standard form

        # y = mx + (y1 - m(x1))
        # y - mx - (y1 - m(x1)) = 0

        c = -1 * slope * vec.x

        # Check if it passes through any hostile radii
        # Use formula |ax + by + c| / sqrt(a^2 + b^2) > radius

        denom = math.sqrt(slope**2 + 1)

        # List comprehension for that
        if not [0 for p in galaxy_map.hostile if abs(-1 * slope * p.pos.x + p.pos.y + c) / denom > p.radius]:
            #print("Intersected with a hostile zone")
            return Status.FAIL


        # calculate min speed (to not run out of food & o2)

        # Formula:
        # Example using food. Note that the formula for water is the same.
        # Also note that all variables must be positive.
        # distance * K_L / speed = food consumption
        # food consumption < current food
        # distance * K_L / speed < current food
        # distance * K_L < current food * speed
        # distance * K_L / current food < speed

        min_speed = min([dist * K_L / n for n in [self.resources.max_food, self.resources.max_o2]])

        # calculate max speed (to not run out of fuel)

        # Formula:
        # Again, all variables must be positive.
        # distance * K_F * speed^2 = fuel consumption
        # fuel consumption < current fuel
        # distance * K_F * speed^2 < current fuel
        # speed^2 < current fuel / (distance * K_F)
        # speed < sqrt( current fuel / (distance * K_F) )

        max_speed = math.sqrt(self.resources.max_fuel / (dist * K_F)) if dist != 0 else 0

        if min_speed > max_speed:
            #print("Resource Failure")
            return Status.FAIL

        self.pos = galaxy_map.planets[target].pos

        # Set resource values to their best-case scenario values
        self.resources.max_food -= dist * K_L / max_speed
        self.resources.max_o2 -= dist * K_L / max_speed
        self.resources.max_fuel -= dist * K_F * min_speed**2

        # If this is a resupply planet, resupply
        match galaxy_map.planets[target].resupply:
            case Resupply.FOOD:
                self.resources.max_food = MAX_FOOD
            case Resupply.OXYGEN:
                self.resources.max_o2 = MAX_O2

        # Iterate depth counter
        self.depth += 1

        if self.depth > MAX_DEPTH:
            return Status.FAIL

        self.history.append(TravelPath((self.current_planet, target), dist, min_speed, max_speed))
        self.current_planet = target

        return Status.SUCCESS
