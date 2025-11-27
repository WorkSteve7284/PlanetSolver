""" Print various debug things to console """

import planetsolver_cxx as ps

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