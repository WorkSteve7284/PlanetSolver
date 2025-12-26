""" Generate random values """

import random

def planet_name() -> str:

    CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()-_=+[]{}\\/':;,<.>?\n\t\r "

    string = ''.join(random.choices(CHARS, k=20))

    return string

def pos(num: int) -> tuple[list[float], list[float]]:

    SCALE = 100

    return ([random.random() * SCALE for _ in range(num)], [random.random() * SCALE for _ in range(num)])

def case(string: str) -> str:
    out = ""
    for char in string:
        out += random.choice([str.upper, str.lower])(char) if char.isalpha() else char
    return out
