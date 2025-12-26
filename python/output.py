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

    output: list[str] = []

    for segment in path:

        start = galaxy_map.planets[segment.start]
        end = galaxy_map.planets[segment.end]
        speed = segment.speed

        output.append(f"{start.name}->{end.name}, speed={speed}")

        d = (start.pos - end.pos).magnitude()
        t  = d / speed

        cost_life = K_L * t
        cost_fuel = K_F * d * speed*speed

        food -= cost_life
        o2 -= cost_life
        fuel -= cost_fuel

        time += t

        if end.resupply is ps.ResupplyType.FOOD:
            food = MAX_FOOD_O2
        elif end.resupply is ps.ResupplyType.OXYGEN:
            o2 = MAX_FUEL

    print('\n'.join(output))
    print(f"Score = {time - (o2 + food + fuel)}\n")
