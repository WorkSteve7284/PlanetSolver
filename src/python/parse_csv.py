""" Parse CSV into a GalaxyMap """

import csv

import planetsolver_cxx as ps

def parse(csv_path: str) -> ps.GalaxyMap:

    galaxy_map = ps.GalaxyMap()

    with open(csv_path, mode='r', encoding='utf-8') as csv_file:

        reader = csv.reader(csv_file)

        for i, row in enumerate(reader):
            if i == 0 and (row[1].casefold() == 'x' or row[2].casefold() == 'x'):
                continue

            match row[4].casefold():
                case 'oxygen':
                    resupply_type = ps.ResupplyType.OXYGEN
                case 'food':
                    resupply_type = ps.ResupplyType.FOOD
                case _:
                    resupply_type = ps.ResupplyType.NONE

            hostile_radius = float(row[5])

            galaxy_map.add_planet(
                ps.Planet(
                    row[0],
                    ps.Vector2(float(row[1]), float(row[2])),
                    resupply_type,
                    hostile_radius,
                    row[3].casefold() == 'hostile'
                )
            )
