import math

def grid(w, h):
    out = ""
    y = 0
    while y < h:
        x = 0
        while x < w:
            out += "."
            x += 1
        y += 1
        out =+ "\n"
    return out

grid(10, 10)
