""" The entrypoint for PlanetSolver """

import time

import parse_csv
import debug_output

start_time = time.time()

# Take in Command Line args

map_location = '../../Maps/ExampleMap.csv'

# Run code

galaxy_map = parse_csv.parse(map_location)

print(type(galaxy_map))

debug_output.print_galaxy(galaxy_map)

end_time = time.time()

print(f"Took {end_time - start_time}s")