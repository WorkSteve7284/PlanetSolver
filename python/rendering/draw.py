""" Draw shapes """

import tkinter as tk

from python import planetsolver as ps

scale: int = 1
offset: ps.Vector2 = ps.Vector2()
height = 0

def screen(point: ps.Vector2) -> ps.Vector2:
    p = (point + offset) * scale
    return ps.Vector2(p.x, height - p.y)

def line(canvas: tk.Canvas, p1: ps.Vector2, p2: ps.Vector2, color="yellow", width=5) -> None:
    id = canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill=color, width=width)
    canvas.addtag("all", 'withtag', id)


def circle(canvas: tk.Canvas, center: ps.Vector2, radius: int | float, color="green") -> None:
    id = canvas.create_oval(center.x - radius, center.y - radius, center.x + radius, center.y + radius, fill=color, width=0)
    canvas.addtag("all", 'withtag', id)

def text(canvas: tk.Canvas, center: ps.Vector2, text: str, color="white", font={'Arial', 12, 'bold'}) -> None:
    id = canvas.create_text(center.x, center.y, text=text, fill=color, font=font)
    canvas.addtag("all", 'withtag', id)
    canvas.addtag("text", 'withtag', id)

class ResizingCanvas(tk.Canvas):
    def __init__(self, parent, **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self, event):
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height

        if wscale > hscale:
            self.width *= hscale
            self.height *= hscale
            self.config(width=self.width, height=self.height)
            self.scale("all", 0, 0, hscale, hscale)
        else:
            self.width *= wscale
            self.height *= wscale
            self.config(width=self.width, height=self.height)
            self.scale("all", 0, 0, wscale, wscale)
