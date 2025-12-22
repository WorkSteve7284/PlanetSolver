""" The entrypoint for PlanetSolver """

import time
import sys
import pathlib

from python import parse_csv, planetsolver as ps, rendering, output, debug_output as debug


# Take in Command Line args

gui = True
valid_map = False
valid_target = False
valid_from = False
map_path = pathlib.Path("Map/ExampleMap.csv")
target_name = "Target"
from_name = "Earth"

for arg in sys.argv[1:]:
    match arg:
        case 'nogui':
            gui = False
    if arg.startswith("map="):
        map_path = pathlib.Path(arg[4:])
        valid_map = True
    if arg.startswith("target="):
        target_name = arg[7:]
        valid_target = True
    if arg.startswith("start="):
        from_name = arg[6:]
        valid_from = True

# Get the map from the user
while not valid_map:
    print("\nPath to map:")
    map_path = pathlib.Path(input("(Relative to main.py or absolute)\n"))
    if map_path.exists():
        valid_map = True
    else:
        print("File does not exist! Please try again.")

# Get the target from the user
while not valid_target:
    target_name = input("Target name: ")
    valid_target = True

while not valid_from:
    from_name = input("Starting planet name: ")
    valid_from = True

print()

start_time = time.perf_counter()

# Parse map
galaxy_map = parse_csv.parse(map_path)

# Find target
target = galaxy_map.index_from_name(target_name)
from_ = galaxy_map.index_from_name(from_name)

if target == -1:
    print("Target planet does not exist!")
    exit()

if from_ == -1:
    print("Starting planet does not exist!")
    exit()

# Run algorithm
path = ps.find_best_path(from_, target, galaxy_map)
#path = debug.list_to_path(['Persephone', 'Hestia', 'Aegis', 'Tethys'], galaxy_map)

# Print Results
print(f"Used map {map_path}")
output.print_path(path, galaxy_map, map_path.stem)

end_time = time.perf_counter()

print(f"Took {end_time - start_time}s")

# Draw galaxy & path
if gui:
    w, c = rendering.galaxy.draw_galaxy(galaxy_map)
    rendering.galaxy.draw_path(c, path, galaxy_map)
    w.mainloop()