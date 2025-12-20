""" Report results in command line """

from . import planetsolver as ps

MAX_FOOD_O2 = 2000
MAX_FUEL = 3000

K_L = 0.3
K_F = 0.15

def print_path(path: list[ps.paths.Segment], galaxy_map: ps.GalaxyMap, map_name: str) -> None:

    food = MAX_FOOD_O2
    o2 = MAX_FOOD_O2
    fuel = MAX_FUEL
    time = 0
    for segment in path:
        print(f"{galaxy_map.planets[segment.start].name}->{galaxy_map.planets[segment.end].name}, speed={segment.speed}")

        d = (galaxy_map.planets[segment.start].pos - galaxy_map.planets[segment.end].pos).magnitude()
        t  = d / segment.speed

        cost_food = K_L * t
        cost_fuel = K_F * d * segment.speed**2

        food -= cost_food
        o2 -= cost_food
        fuel -= cost_fuel

        time += t

        match galaxy_map.planets[segment.end]:
            case ps.ResupplyType.FOOD:
                food = 2000
            case ps.ResupplyType.OXYGEN:
                o2 = 2000

    #print(f"\n{map_name}\n{resources}\nTime = {time}")
    print(f"Score = {time - (o2 + food + fuel)}\n")