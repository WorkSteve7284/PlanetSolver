""" Testing script for PlanetSolver """
import pathlib
import galaxy
import renderer
import pathfinder

test_galaxy = galaxy.Galaxy(pathlib.Path('ExampleMap.csv'))

pathfinder.find_path(test_galaxy)

window, canvas = renderer.draw_galaxy(test_galaxy)

#renderer.draw_line(canvas, renderer.screen_pos(basic.Point(0,0)), renderer.screen_pos(test_galaxy.planets["Target"].pos))

renderer.draw(window)
