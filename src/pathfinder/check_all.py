""" Find the fastest path to a planet """

import math
import copy

from src import ship, galaxy, basic

def find_path(galaxy_map: galaxy.Galaxy) -> ship.Ship:
    """ Returns best ship """

    # Find number of possible paths

    possible_planets = len(galaxy_map.planets) - len(galaxy_map.hostile) - 1

    total = 0
    for n in range(possible_planets):
        total += math.factorial(n + 1)

    print(f"There are {total} total paths")

    traveling_ships: list[ship.Ship] = [ship.Ship()]
    successful_ships: list[ship.Ship] = []
    while traveling_ships:
        traveling_ships, successful = merge([send_to_all(s, galaxy_map) for s in traveling_ships])
        successful_ships.extend(successful)

    print(f"There are {len(successful_ships)} potentially possible paths")

    return ship.Ship()

def send_to_all(ship_to_move: ship.Ship, galaxy_map: galaxy.Galaxy) -> tuple[list[ship.Ship], list[ship.Ship]]:
    """ Sends a ship to all places it hasn't been before"""
    print("going")
    ships_out: list[ship.Ship] = []
    successful_ships: list[ship.Ship] = []

    past_places: set[str] = set(['Earth'])
    for path in ship_to_move.history:
        past_places.add(path.planets[0])
        past_places.add(path.planets[1])

    for name, planet in galaxy_map.planets.items():
        if not planet.is_hostile() and name not in past_places and planet.pos != ship_to_move.pos:
            temp_ship = copy.deepcopy(ship_to_move)
            if temp_ship.goto(galaxy_map, name) == basic.Status.SUCCESS:
                if name == basic.TARGET_PLANET_NAME:
                    successful_ships.append(temp_ship)
                    continue
                ships_out.append(temp_ship)


    return ships_out, successful_ships

def merge(to_merge: list[tuple[list[ship.Ship], list[ship.Ship]]]) -> tuple[list[ship.Ship], list[ship.Ship]]:
    """ Merge a list of tuples into a tuple of lists """
    if not to_merge:
        return ([], [])

    l1: list[ship.Ship] = []
    l2: list[ship.Ship] = []
    for t in to_merge:
        l1.extend(t[0])
        l2.extend(t[1])

    return (l1, l2)
