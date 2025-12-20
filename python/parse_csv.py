""" Parse CSV into a GalaxyMap """

import csv
import pathlib

from . import planetsolver as ps # type: ignore

def parse(csv_path: pathlib.Path) -> ps.GalaxyMap:

    with open(csv_path, mode='r', encoding='utf-8') as csv_file:

        reader = csv.reader(csv_file)

        rows = list(reader)
        galaxy_map = ps.GalaxyMap(len(rows))

        for i, row in enumerate(rows):
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

    return galaxy_map
