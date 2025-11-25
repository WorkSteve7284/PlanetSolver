""" Find the fastest path to a planet """

import math

import galaxy
import ship

def find_path(galaxy_map: galaxy.Galaxy) -> ship.Ship | None:
    """ Returns best ship """

    # Find all possible paths

    # starting at earth, going to target planet

    # earth -> planet1 -> planet2 -> planet3 -> planet4, etc -> target
    # path of length (0,n], where n = number of planets + 1
    # Or, range(n + 1) with n = number of planets
    # So: (0, n+1]!


    possible_planets = len(galaxy_map.planets) - len(galaxy_map.hostile) - 1

    total = 0
    for n in range(possible_planets):
        total += math.factorial(n + 1)

    print(total)