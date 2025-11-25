""" Render the Galaxy """

import tkinter as tk

from src import basic, galaxy
from . import draw

def init_galaxy(galaxy_map: galaxy.Galaxy) -> tk.Tk:
    """ Initialize the window to a given galaxy map """

    # Calculate the size of the screen
    planets_x = [n.pos.x for n in galaxy_map.planets.values()]
    planets_y = [n.pos.y for n in galaxy_map.planets.values()]

    window_size = basic.Point(max(planets_x) - min(planets_x), max(planets_y) - min(planets_y))

    draw.offset_factor = basic.Point(min(planets_x), min(planets_y))

    window_size += basic.Point(10, 10)
    window_size *= 10

    window_size = window_size.round()

    # Set settings
    window = tk.Tk()
    window.title("PlanetSolver")
    window.configure(bg="black")
    window.geometry(f"{window_size.x}x{window_size.y}")
    window.resizable(False, False)

    window.update_idletasks()

    return window

def draw_galaxy(window: tk.Tk, galaxy_map: galaxy.Galaxy) -> tk.Canvas:
    """ Draw a galaxy to the screen """

    print(window.winfo_height())

    canvas = tk.Canvas(
        window,
        width=window.winfo_width(),
        height=window.winfo_height(),
        bg="black",
        borderwidth=0,
        highlightthickness=0
    )

    canvas.pack()

    for hostile in galaxy_map.hostile:
        draw.circle(canvas, draw.screen_pos(hostile.pos), int(hostile.radius * 10), color="#500000")

    for planet in galaxy_map.planets.values():

        match planet.resupply:
            case basic.Resupply.NONE:
                color = "green"
            case basic.Resupply.FOOD:
                color = "#5C2E00"
            case basic.Resupply.OXYGEN:
                color = "blue"

        print(f"Drawing planet at {draw.screen_pos(planet.pos)}")
        draw.circle(canvas, draw.screen_pos(planet.pos), 6, color=color)

    return canvas



def draw_path(canvas: tk.Canvas, galaxy_map: galaxy.Galaxy, paths: list[basic.TravelPath]):
    """ Draws a path on the screen from """
    for path in paths:
        draw.line(canvas,
                  draw.screen_pos(galaxy_map.planets[path.planets[0]].pos),
                  draw.screen_pos(galaxy_map.planets[path.planets[1]].pos)
                 )
