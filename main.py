""" The entrypoint for PlanetSolver """

import time
import sys
import pathlib

from python import parse_csv, planetsolver as ps, rendering, output, debug_output as debug


# Take in Command Line args

gui = True
valid_map = False
valid_target = False
target_name = "Target"
map_path = pathlib.Path("Map/ExampleMap.csv")

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


# Get the map from the user

while not valid_map:
    print("\nPath to map:")
    map_path = pathlib.Path(input("(Relative to main.py or absolute)\n"))
    if map_path.exists():
        valid_map = True
    else:
        print("File does not exist! Please try again.")

while not valid_target:
    target_name = input("Target name: ")
    valid_target = True

start_time = time.time()


# Parse map
galaxy_map = parse_csv.parse(map_path)

# Find target
target = galaxy_map.index_from_name(target_name)

if target == -1:
    print("Target planet does not exist!")
    exit()

# Run algorithm
path = ps.find_best_path(0, target, galaxy_map)

# Print Results
output.print_path(path, galaxy_map, map_path.stem)

end_time = time.time()

print(f"Took {end_time - start_time}s")

# Draw galaxy & path
if gui:
    w, c = rendering.galaxy.draw_galaxy(galaxy_map)
    rendering.galaxy.draw_path(c, path, galaxy_map)
    w.mainloop()