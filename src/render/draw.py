import tkinter as tk

from src import basic

offset_factor = basic.Point(0, 0)
def screen_pos(og: basic.Point) -> basic.Point:
    """ Convert Point to screen space """
    return (og - offset_factor + basic.Point(5,5)) * 10

def circle(canvas:tk.Canvas, pos: basic.Point, radius: int, width: int = 2, color: str = "green"):
    """ Draw a circle on a canvas """
    canvas.create_oval(
        pos.x - radius, pos.y - radius,
        pos.x + radius, pos.y + radius,
        width=width,
        fill=color
    )

def line(canvas: tk.Canvas, p1: basic.Point, p2: basic.Point, fill: str = "yellow", width: int = 2):
    """ Draw a line """
    canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill=fill, width=width)

def draw_window(window: tk.Tk):
    """ Draw the canvas to screen\nNote: this is blocking (forever)! """
    window.mainloop()
