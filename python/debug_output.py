""" Print various debug things to console """

from . import planetsolver as ps # type: ignore

def print_planet(planet: ps.Planet, galaxy_map: ps.GalaxyMap):
    print(planet.name)
    print(planet.pos)
    match planet.resupply:
        case ps.ResupplyType.FOOD:
            print("Resupplies food")
        case ps.ResupplyType.OXYGEN:
            print("Resupplies oxygen")
    if planet.is_hostile:
        print(f"Hostile, with radius {planet.hostile_radius}")

def print_galaxy(galaxy_map: ps.GalaxyMap):
    for planet in galaxy_map.planets:
        print_planet(planet, galaxy_map)
        print()

def list_to_path(path: list[str], galaxy_map: ps.GalaxyMap) -> list[ps.paths.Segment]:
    """ Convert a list of planets to a path """
    final_path: list[ps.paths.Segment] = []
    for i in range(len(path) - 1):
        segment = ps.paths.Segment(galaxy_map.index_from_name(path[i]), galaxy_map.index_from_name(path[i + 1]), 1.75)
        final_path.append(segment)
    return final_path