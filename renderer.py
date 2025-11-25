""" Visualize the path of a ship """

import tkinter as tk
from typing import Callable

import basic
import galaxy

offset_factor = basic.Point(0, 0)

def screen_pos(og: basic.Point) -> basic.Point:
    return (og - offset_factor + basic.Point(5,5)) * 10

def draw_circle(canvas:tk.Canvas, pos: basic.Point, radius: int, width: int = 2, color: str = "green"):
    """ Draw a circle on a canvas """
    canvas.create_oval(pos.x - radius, pos.y - radius, pos.x + radius, pos.y + radius, width=width, fill=color)

def draw_galaxy(galaxy_map: galaxy.Galaxy) -> tuple[tk.Tk, tk.Canvas]:
    """ Draw a galaxy to the screen """

    # Calculate the size of the screen
    planets_x = [n.pos.x for n in galaxy_map.planets.values()]
    planets_y = [n.pos.y for n in galaxy_map.planets.values()]

    window_size = basic.Point(max(planets_x) - min(planets_x), max(planets_y) - min(planets_y))

    global offset_factor
    offset_factor = basic.Point(min(planets_x), min(planets_y))

    window_size += basic.Point(10, 10)
    window_size *= 10

    window_size = window_size.round()

    window = tk.Tk()
    window.title("PlanetSolver")
    window.configure(bg="black")
    window.geometry(f"{window_size.x}x{window_size.y}")
    window.resizable(False, False)

    canvas = tk.Canvas(window, width=window_size.x, height=window_size.y, bg="black")
    canvas.pack()

    for hostile in galaxy_map.hostile:
        draw_circle(canvas, screen_pos(hostile.pos), int(hostile.radius * 10), color="dark red")

    for planet in galaxy_map.planets.values():

        match planet.resupply:
            case basic.Resupply.NONE:
                color = "green"
            case basic.Resupply.FOOD:
                color = "#964B00"
            case basic.Resupply.OXYGEN:
                color = "blue"

        print(f"Drawing planet at {screen_pos(planet.pos)}")
        draw_circle(canvas, screen_pos(planet.pos), 6, color=color)

    return window, canvas

def draw(window: tk.Tk):
    """ Draw the canvas to screen\nNote: this is blocking (forever)! """
    window.mainloop()

def draw_line(canvas: tk.Canvas, p1: basic.Point, p2: basic.Point, fill: str = "yellow", width: int = 2):
    """ Draw a line """
    canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill=fill, width=width)

def draw_path(canvas: tk.Canvas, galaxy_map: galaxy.Galaxy, paths: list[basic.TravelPath]):
    """ Draws a path on the screen from """
    for path in paths:
        draw_line(canvas, screen_pos(galaxy_map.planets[path.planets[0]].pos), screen_pos(galaxy_map.planets[path.planets[1]].pos))
