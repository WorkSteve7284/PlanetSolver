""" Testing script for PlanetSolver """
import pathlib

from src import render, galaxy, pathfinder, basic

test_galaxy = galaxy.Galaxy(pathlib.Path('Maps/ExampleMap.csv'))

ships = pathfinder.find_path(test_galaxy)

print("Finished finding paths")

window = render.galaxy.init_galaxy(test_galaxy)

canvas = render.galaxy.draw_galaxy(window, test_galaxy)

[render.galaxy.draw_path(canvas, test_galaxy, ship.history) for ship in ships]

segments: set[tuple[basic.Point, basic.Point]] = set()
for ship in ships:
    for segment in ship.history:
        segments.add((test_galaxy.planets[segment.planets[0]].pos, test_galaxy.planets[segment.planets[1]].pos))

print("Finished parsing segments")

for segment in segments:
    render.draw.line(canvas, render.draw.screen_pos(segment[0]), render.draw.screen_pos(segment[1]))

render.draw.draw_window(window)
