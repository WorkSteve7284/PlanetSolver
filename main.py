""" Temporarily empty. Use test.py instead """

import sys

from python import help

# Parse arguments

target_planet = 'Target'

for arg in sys.argv[1:]: # Get >=2nd args (first is main.py)
    match arg:
        case '--help':
            print(help.help_str)
        case '--target':
            target_planet = sys.argv[sys.argv.index(arg) + 1]
        case _:
            continue

# Run code

