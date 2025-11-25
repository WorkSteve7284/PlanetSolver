""" Testing script for PlanetSolver """
import pathlib

from src import render, galaxy, pathfinder

test_galaxy = galaxy.Galaxy(pathlib.Path('Maps/ExampleMap.csv'))

ship = pathfinder.find_path(test_galaxy)

window = render.galaxy.init_galaxy(test_galaxy)

canvas = render.galaxy.draw_galaxy(window, test_galaxy)

render.galaxy.draw_path(canvas, test_galaxy, ship.history)

render.draw.draw_window(window)
