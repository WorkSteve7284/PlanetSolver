""" Test the speed of stuff """

import time
import pathlib

from src import render, galaxy, pathfinder

test_galaxy = galaxy.Galaxy(pathlib.Path('Maps/ExampleMap.csv'))

start = time.time()
pathfinder.find_path(test_galaxy)
end = time.time()

print(f"Took {end - start}s")