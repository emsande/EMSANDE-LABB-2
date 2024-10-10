"""Displays a Sierpinski Fractal."""
from tkinter import *
from random import randint


__author__ = "Marcus Dicander"
__copyright__ = "Copyright 2019-2024, Kth"
__license__ = "CC0"


"""The width and height of the image. Change these values to change the size of the image.
Make sure to use normalized coordinates for each function call to make sure the image scales
properly when the width and height are changed."""
WIDTH = 800
HEIGHT = 600


def normalized_to_pixel(n: float) -> int:
    """Converts a normalized value to a pixel value."""
    return int(n * WIDTH)


def pixel_to_normalized(p: int) -> float:
    """Converts a pixel value to a normalized value."""
    return p / WIDTH


def sierpinski(img, color="#ff00ff"):
    """Adds a Sierpinski Fractal to img and returns None."""
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if x & y == 0:
                img.put(color, (x, y))


def random_shape(img, upper_left: tuple[float, float], lower_right: tuple[float, float], color: str="#ffffff"):
    """Draws a random shape in img with the given color. The coordinates are normalized and given
    in the order (x, y) for the upper left and lower right corners of the shape.
    This implementation uses a random number generator to decide if a pixel should be colored or not.
    Your functions should have similar signatures to this one. Feed the image and the normalized
    coordinates to the function and make it draw the requested shape for each task. You may use
    the functions normalized to pixel and pixel to normalized to convert between the two coordinate
    systems."""
    for y in range(normalized_to_pixel(upper_left[1]), normalized_to_pixel(lower_right[1])):
        for x in range(normalized_to_pixel(upper_left[0]), normalized_to_pixel(lower_right[0])):
            if randint(0, 1) == 0:
                img.put(color, (x, y))


def main():
    """Create your image and call your functions from here"""
    window = Tk()
    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
    canvas.pack()
    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canvas.create_image((WIDTH / 2, HEIGHT / 2), image=img, state="normal")
    """Below this comment is where you should put your function calls to draw things
    in the Canvas. Do not change the code above this comment. Do not call mainloop 
    outside of this function."""
    import math
    def gran(ap: tuple[float, float], bp: tuple[float, float], cp: tuple[float, float]):

     def triarea (AX, BX, CX, AY, BY, CY):
        a = math.sqrt((AX-CX)**2 + (AY-CY)**2)
        b = math.sqrt((AX-BX)**2 + (AY-BY)**2)
        c = math.sqrt((BX-CX)**2 + (BY-CY)**2)
        s = (a + b + c)/2 + 0.000000001
        return math.sqrt(s*(s-a)*(s-b)*(s-c))
      
     for i in range (4):
        ax = normalized_to_pixel (ap[0]) 
        bx = normalized_to_pixel(bp[0] + i/20)
        cx = normalized_to_pixel(cp[0] - i/20)

        ay = normalized_to_pixel(ap[1]+i/10)
        by = normalized_to_pixel(bp[1]+i/10)
        cy = normalized_to_pixel(cp[1]+i/10)

        StoraX = max(ax, bx, cx)
        LillaX = min(ax, bx, cx)
        StoraY = max(ay, by, cy)
        LillaY = min(ay, by, cy)

        Area = triarea(ax, bx, cx, ay, by, cy)

        for y in range(LillaY, StoraY):
         for x in range(LillaX, StoraX):
            area1 = triarea(ax, x, cx, ay, y, cy)
            area2 = triarea(ax, bx, x, ay, by, y)
            area3 = triarea(x, bx, cx, y, by, cy)
            DeTreSmåAreorna = area1 + area2 + area3
            epsikon = 0.0001
            
            if abs(Area - DeTreSmåAreorna) < epsikon:
            
             img.put("#417d45", (x,y))

        for y in range (normalized_to_pixel(bp[1] + 3/10),normalized_to_pixel(bp [1] + 4/10)):
          for x in range (normalized_to_pixel(cp[0]),normalized_to_pixel(bp[0])):
           img.put("#7d4d41",(x, y))

    gran ((0.4, 0.009), (0.45,0.2), (0.35,0.2))
    """Do not change any code below this comment."""
    mainloop()


if __name__ == '__main__':
    main()