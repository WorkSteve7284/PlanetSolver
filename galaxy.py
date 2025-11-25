""" Implement the galaxy & planets """

import pathlib
import csv
import dataclasses
import basic

@dataclasses.dataclass
class Planet:
    """ Store the data for a planet"""
    def __init__(
            self,
            pos: basic.Point,
            hostile_radius: int | float,
            resupply_type: basic.Resupply,
            name: str = "Undefined"
        ):

        self.pos = pos
        self.radius = hostile_radius
        self.resupply = resupply_type
        self.name = name

    def is_hostile(self):
        """ Check if a planet is hostile """
        return self.radius != 0

    def print(self):
        """ Print the details of this planet """

        print(f"Planet \"{self.name}\": Position=({self.pos.x},{self.pos.y}), Hostile Radius={self.radius}, Resupplies {self.resupply})")


class Galaxy:
    """ Store planets & their data """
    def __init__(self, csv_path: pathlib.Path):
        self.planets: dict[str, Planet] = {}# list of planets
        self.hostile: list[Planet] = [] # list of hostile planets

        # read CSV
        with open(csv_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for i, row in enumerate(reader):
                if i == 0 and (row[1] == 'x' or row[2] == 'X'):
                    continue

                match row[4]:
                    case 'oxygen':
                        resupply_type = basic.Resupply.OXYGEN
                    case 'food':
                        resupply_type = basic.Resupply.FOOD
                    case _:
                        resupply_type = basic.Resupply.NONE

                hostile_radius = float(row[5]) if row[3] == 'hostile' else 0

                self.planets[row[0]] = Planet(
                    basic.Point(float(row[1]),float(row[2])),
                    hostile_radius,
                    resupply_type,
                    name=row[0]
                )

                if hostile_radius != 0:
                    self.hostile.append(self.planets[row[0]])

                #print(row[0])


    def print(self):
        """ Print all planet stats """
        for _, planet in self.planets.items():
            planet.print()