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
    def triangel(a: tuple[float, float], b: tuple[float, float], c: tuple[float, float], color: str="#ffffff"):
        
        (ax)=normalized_to_pixel(a[0])
        (bx)=normalized_to_pixel(b[0])
        (cx)=normalized_to_pixel(c[0])
        (ay)=normalized_to_pixel(a[1])
        (by)=normalized_to_pixel(b[1])
        (cy)=normalized_to_pixel(c[1])

        StoraX = max(ax, (bx), (cx))
        LillaX = min(ax, (bx), (cx))
        StoraY = max((ay), (by), (cy))
        LillaY = min((ay), (by), (cy))

        def triarea (AX, BX, CX, AY, BY, CY):
            A = math.sqrt(abs((AX-CX)**2 + (AY-CY)**2))
            B = math.sqrt(abs((AX-BX)**2 + (AY-BY)**2))
            C = math.sqrt(abs((BX-CX)**2 + (BY-CY)**2))
            s = (A + B + C)/2 + 0.00000000000001
            return math.sqrt(abs(s*(s-A)*(s-B)*(s-C)))
            
        Area = triarea((ax), (bx), (cx), (ay), (by), (cy))

        for y in range (LillaY, StoraY):
            for x in range(LillaX, StoraX): 
                
                area1 = triarea((ax), x, (cx), (ay), y, (cy))
                area2 = triarea((ax), (bx), x, (ay), (by), y)
                area3 = triarea(x, (bx), (cx), y, (by), (cy))
                print(area1,area2,area3,Area)
                DeTreSmåAreorna = area1 + area2 + area3
                epsikon = 0.001
                if abs(Area - DeTreSmåAreorna) < epsikon: 
                    img.put(color, (x,y))

    triangel((0.1,0.4), (0.9,0.7), (0.5,0.3), "#ff00ff")

    """Do not change any code below this comment."""
    mainloop()


if __name__ == '__main__':
    main()