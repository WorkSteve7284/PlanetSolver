""" The entrypoint for PlanetSolver """

import time

import parse_csv

start_time = time.time()

# Take in Command Line args

map_location = '../../Maps/ExampleMap.csv'

# Run code

galaxy_map = parse_csv.parse(map_location)

end_time = time.time()

print(f"Took {end_time - start_time}s")