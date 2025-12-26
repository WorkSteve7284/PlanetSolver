""" Parse CSV into a GalaxyMap """

import csv
import pathlib

from . import planetsolver as ps # type: ignore

RESUPPLY_MAP = {'oxygen': ps.ResupplyType.OXYGEN, 'food': ps.ResupplyType.FOOD}

def parse(csv_path: pathlib.Path) -> ps.GalaxyMap:

    with open(csv_path, mode='r', encoding='utf-8') as csv_file:

        reader = csv.reader(csv_file)

        next(reader, None)

        rows = list(reader)

    galaxy_map = ps.GalaxyMap(len(rows))

    for row in rows:

        name, x, y, _type, resupply, radius = row

        resupply_type = RESUPPLY_MAP.get(resupply.casefold(), ps.ResupplyType.NONE)

        hostile_radius = float(radius)

        galaxy_map.add_planet(
            ps.Planet(
                name,
                ps.Vector2(float(x), float(y)),
                resupply_type,
                hostile_radius,
                _type.casefold() == 'hostile'
            )
        )

    return galaxy_map
