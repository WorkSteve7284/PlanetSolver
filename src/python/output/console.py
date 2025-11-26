""" Write output to console """

from src import basic, galaxy, ship

def print_path(path: basic.FinalPath, galaxy_map: galaxy.Galaxy):
    """ Print a given path to the console """

    # Earth -> Luna @ speed = 15 AU/t
    # Luna -> Mars

    resources = ship.Resources()
    time: float = 0

    for segment in path.segments:
        print(f"{segment.planets[0]} -> {segment.planets[1]}, speed = {segment.speed}")

        d = (galaxy_map.planets[segment.planets[0]].pos - galaxy_map.planets[segment.planets[1]].pos).magnitude()

        cost_food = d * ship.K_L / segment.speed
        cost_fuel = d * ship.K_F * segment.speed**2

        resources.max_food -= cost_food
        resources.max_o2 -= cost_food
        resources.max_fuel -= cost_fuel

        match galaxy_map.planets[segment.planets[1]].resupply:
            case basic.Resupply.FOOD:
                resources.max_food = ship.MAX_FOOD
            case basic.Resupply.OXYGEN:
                resources.max_food = ship.MAX_O2

        time += d / segment.speed

    print(f"Score: {time - (resources.max_food + resources.max_fuel + resources.max_o2)}")