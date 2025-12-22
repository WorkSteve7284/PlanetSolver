""" Draw the galaxy """

import tkinter as tk

from python import planetsolver as ps

from . import draw

def draw_galaxy(galaxy_map: ps.GalaxyMap) -> tuple[tk.Tk, draw.ResizingCanvas]:
    """ Create a tkinter window & canvas from a galaxy map """

    # Determine size of galaxy
    planet_x = [p.pos.x for p in galaxy_map.planets]
    planet_y = [p.pos.y for p in galaxy_map.planets]

    # Determine width & height
    width = max(planet_x) - min(planet_x)
    height = max(planet_y) - min(planet_y)

    # Apply padding
    width += 10
    height += 10

    # Scale up
    width *= 5
    height *= 5

    # Set draw constants
    draw.scale = 5
    draw.offset = ps.Vector2(-min(planet_x) + 5, -min(planet_y) + 5)
    draw.height = height

    # Initialize window
    window = tk.Tk()
    window.title("PlanetSolver Display")
    window.geometry(f"{int(width)}x{int(height)}")

    # Initialize canvas
    canvas = draw.ResizingCanvas(window, width=width, height=height, background="#000000", bd=0, highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=tk.YES)

    # Draw hostile radiuses
    for planet in galaxy_map.planets:
        if planet.is_hostile:
            draw.circle(canvas, draw.screen(planet.pos), 5 * planet.hostile_radius, color="#CC0000")

    # Draw planets
    for planet in galaxy_map.planets:

        color = "orange"
        # Draw regular planets
        match planet.resupply:
            case ps.ResupplyType.NONE:
                color = "green"
            case ps.ResupplyType.FOOD:
                color = "#964B00"
            case ps.ResupplyType.OXYGEN:
                color = "blue"

        draw.circle(canvas, draw.screen(planet.pos), 3, color=color)

        draw.text(canvas, draw.screen(planet.pos) - ps.Vector2(0, 12), planet.name)

    canvas.tag_raise("text")

    return window, canvas

def draw_path(canvas: tk.Canvas, path: list[ps.paths.Segment], galaxy_map: ps.GalaxyMap) -> None:
    for segment in path:
        draw.line(canvas, draw.screen(galaxy_map.planets[segment.start].pos), draw.screen(galaxy_map.planets[segment.end].pos), color="yellow", width=3)