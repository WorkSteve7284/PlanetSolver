""" Print various debug things to console """

from . import planetsolver as ps # type: ignore

def print_planet(planet: ps.Planet, galaxy_map: ps.GalaxyMap):
    print(planet.name)
    print(planet.position)
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

    final_path: list[ps.paths.Segment] = [ps.PathSegment()] * (len(path) - 1)
    for i in range(len(path) - 1):
        segment = ps.paths.Segment()
        segment.start = galaxy_map.name_to_index[path[i]]
        segment.end = galaxy_map.name_to_index[path[i + 1]]
        segment.speed = 40
        final_path[i] = segment
    return final_path