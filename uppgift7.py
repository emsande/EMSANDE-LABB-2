"""Displays a Sierpinski Fractal."""
from tkinter import *
from random import randint

__author__ = "Marcus Dicander"
__copyright__ = "Copyright 2019-2024, Kth"
__license__ = "CC0"


"""The width and height of the image. Change these values to change the size of the image.
Make sure to use normalized coordinates for each function call to make sure the image scales
properly when the width and height are changed."""
WIDTH = 400
HEIGHT = 300


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
 ## funktion för rektangel
    def rektkantigkant(ya, yb, xa, xb, färg): 

        for y in range(normalized_to_pixel(ya), normalized_to_pixel(yb)):
            for x in range(normalized_to_pixel(xa), normalized_to_pixel(xb)):
                img.put(färg,(x, y))

## funktion för triangel
    def triangeligang(ax, bx, cx, ay, by, cy, färg):
        ax = normalized_to_pixel(ax) 
        bx = normalized_to_pixel(bx)
        cx = normalized_to_pixel(cx)

        ay = normalized_to_pixel(ay)
        by = normalized_to_pixel(by)
        cy = normalized_to_pixel(cy)

        StoraX = max(ax, bx, cx)
        LillaX = min(ax, bx, cx)
        StoraY = max(ay, by, cy)
        LillaY = min(ay, by, cy)

        def triarea (AX, BX, CX, AY, BY, CY):
            import math
            a = math.sqrt((AX-CX)**2 + (AY-CY)**2)
            b = math.sqrt((AX-BX)**2 + (AY-BY)**2)
            c = math.sqrt((BX-CX)**2 + (BY-CY)**2)
            s = (a + b + c)/2 + 0.000000001
            return math.sqrt(s*(s-a)*(s-b)*(s-c))
            
        Area = triarea(ax, bx, cx, ay, by, cy)

        for y in range(LillaY, StoraY):
            for x in range(LillaX, StoraX): 
            
                area1 = triarea(ax, x, cx, ay, y, cy)
                area2 = triarea(ax, bx, x, ay, by, y)
                area3 = triarea(x, bx, cx, y, by, cy)

                DeTreSmåAreorna = area1 + area2 + area3
                epsikon = 0.01
                if abs(Area - DeTreSmåAreorna) < epsikon: 
                    img.put(färg, (x,y))

 ## lila bakgrund 
    rektkantigkant(0,0.9,0,1,'#3304b5' )

 ## random gran som flyter
    for i in range (4):
        ax = normalized_to_pixel(0.5) 
        bx = normalized_to_pixel(0.6 + i/50)
        cx = normalized_to_pixel(0.4 - i/50)
        ay = normalized_to_pixel(0.3+i/30)
        by = normalized_to_pixel(0.35+i/20)
        cy = normalized_to_pixel(0.35+i/20)

        StoraX = max(ax, bx, cx)
        LillaX = min(ax, bx, cx)
        StoraY = max(ay, by, cy)
        LillaY = min(ay, by, cy)
    
        def triarea (AX, BX, CX, AY, BY, CY):
            a = math.sqrt((AX-CX)**2 + (AY-CY)**2)
            b = math.sqrt((AX-BX)**2 + (AY-BY)**2)
            c = math.sqrt((BX-CX)**2 + (BY-CY)**2)
            s = (a + b + c)/2 + 0.000000001
            return math.sqrt(s*(s-a)*(s-b)*(s-c))
        area = triarea(ax, bx, cx, ay, by, cy)
        for y in range(LillaY, StoraY):
         for x in range(LillaX, StoraX):
       
            area1 = triarea(ax, x, cx, ay, y, cy)
            area2 = triarea(ax, bx, x, ay, by, y)
            area3 = triarea(x, bx, cx, y, by, cy)

            DeTreSmåAreorna = area1 + area2 + area3
            epsikon = 0.0001
            
            if abs(area - DeTreSmåAreorna) < epsikon:
            
             img.put("#8f07f0", (x,y))

    ## trädstam 
    rektkantigkant(0.35 + 3/20, 0.8, 0.5-0.02, 0.5+0.02,'#f007e0')

    ## svampen
    rektkantigkant(0.5, 0.65, 0.2, 0.3, '#f2db0a')
    ##cirkelfunktion 
    def cirkel (xc,yc,r,färg):
     xcent = normalized_to_pixel(xc) 
     ycent = normalized_to_pixel(yc)
     for y in range(normalized_to_pixel(0), normalized_to_pixel(0.9)):
      for x in range(normalized_to_pixel(0), normalized_to_pixel(1.0)):
       Area = (x-xcent)**2 + (y-ycent)**2 
       if Area <= r**2: 
         img.put(färg, (x,y))
    ## mun till bob
    cirkel (0.25, 0.56, normalized_to_pixel(0.03), '#030303')
    cirkel (0.25, 0.545, normalized_to_pixel(0.03375), '#f2db0a')
    ##tänder
    rektkantigkant(0.58, 0.585, 0.253, 0.261,'#fcfcfa')
    rektkantigkant(0.58, 0.585, 0.240, 0.248,'#fcfcfa')
    ##ögon till bob
    cirkel (0.235,0.55,normalized_to_pixel(0.01625), '#030303')
    cirkel (0.265,0.55,normalized_to_pixel(0.01625), '#030303' )

    cirkel (0.235,0.55,normalized_to_pixel(0.015), '#fcfcfa')
    cirkel (0.265,0.55,normalized_to_pixel(0.015), '#fcfcfa')
    
    cirkel (0.235,0.55,normalized_to_pixel(0.01125), '#03a5fc')
    cirkel (0.265,0.55,normalized_to_pixel(0.01125), '#03a5fc' )
    
    cirkel (0.235,0.55,normalized_to_pixel(0.0075), '#030303')
    cirkel (0.265,0.55,normalized_to_pixel(0.0075), '#030303' )
    ##byxor och skjorta
    rektkantigkant(0.6, 0.65, 0.2, 0.3, '#8f5a06')
    rektkantigkant(0.6, 0.67, 0.21, 0.23, '#8f5a06')
    rektkantigkant(0.6, 0.67, 0.27, 0.29, '#8f5a06')
    rektkantigkant(0.6, 0.62, 0.2, 0.3, '#fcfcfa')
    ##ben
    rektkantigkant(0.67, 0.7, 0.215, 0.225, '#f2db0a')
    rektkantigkant(0.67, 0.7, 0.275, 0.285, '#f2db0a')
    ##strumpor
    rektkantigkant(0.68, 0.7, 0.275, 0.285, '#fcfcfa')
    rektkantigkant(0.68, 0.7, 0.215, 0.225, '#fcfcfa')
    ##skor
    rektkantigkant(0.69, 0.7, 0.21, 0.225, '#030303')
    rektkantigkant(0.69, 0.7, 0.275, 0.29, '#030303')
    cirkel(0.21, 0.695, normalized_to_pixel(0.01),'#030303')
    cirkel(0.29, 0.695, normalized_to_pixel(0.01),'#030303')
    ##slips
    rektkantigkant(0.6, 0.62, 0.24, 0.26, '#ff0000')
    rektkantigkant(0.62, 0.63, 0.243, 0.258, '#ff0000')
    rektkantigkant(0.62, 0.64, 0.246, 0.254, '#ff0000')
     ##ögonfransar höger öga 
    rektkantigkant(0.525,0.538,0.256,0.259,'#030303')
    rektkantigkant(0.525,0.538,0.264,0.268,'#030303')
    rektkantigkant(0.525,0.538,0.272,0.275,'#030303')
    ##ögonfransar vänster öga
    rektkantigkant(0.525,0.538,0.225,0.229,'#030303')
    rektkantigkant(0.525,0.538,0.234,0.238,'#030303')
    rektkantigkant(0.525,0.538,0.242,0.245,'#030303')
    ##ärmar
    rektkantigkant(0.58, 0.6, 0.3, 0.32, '#fcfcfa')
    rektkantigkant(0.58, 0.6, 0.18, 0.2, '#fcfcfa')
    ##armar
    rektkantigkant(0.6, 0.65, 0.185, 0.195, '#f2db0a')
    rektkantigkant(0.6, 0.65, 0.305, 0.315, '#f2db0a')
    ##patrikssten
    cirkel(0.8, 0.65, normalized_to_pixel(0.1875),'#523334' )

    ##ram
    tjocklek = 3 ## antal pixlar
    
    for y in range(normalized_to_pixel(0.4325), normalized_to_pixel(0.4625)):
        for x in range(normalized_to_pixel(0.795), normalized_to_pixel(0.805)):
          if x < normalized_to_pixel (0.795 + tjocklek*1/WIDTH) or \
             x > normalized_to_pixel (0.805 - tjocklek*1/WIDTH - 1/WIDTH) or \
             y < normalized_to_pixel (0.4325 + tjocklek*1/WIDTH) or \
             y > normalized_to_pixel (0.4625 - tjocklek*1/WIDTH) - 1/WIDTH:
             img.put("#ffa500", (x,y))
    
    ##väder pil
    rektkantigkant (0.42, 0.4325, 0.75, 0.85, "#ffa500")
    triangeligang (0.85, 0.85, 0.9, 0.42625+0.03,0.42625-0.03 , 0.42625, "#ffa500")

    ## sand bakgrund
    rektkantigkant(0.7,0.9,0,1,'#f2910a')
    """Do not change any code below this comment."""
    mainloop()


if __name__ == '__main__':
    main()