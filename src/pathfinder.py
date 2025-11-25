""" Find the fastest path to a planet """

import math

import src.galaxy as galaxy
import src.ship as ship

def find_path(galaxy_map: galaxy.Galaxy) -> ship.Ship | None:
    """ Returns best ship """

    # Find number of possible paths

    possible_planets = len(galaxy_map.planets) - len(galaxy_map.hostile) - 1

    total = 0
    for n in range(possible_planets):
        total += math.factorial(n + 1)

    print(total)