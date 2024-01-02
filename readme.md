# Images
If you want to edit any of these, you'll have to look through the code. This is just a hobby project for me to practice some parts of python that I don't usually get to mess with.

## The Mandelbrot Set
This is a basic generator for the mandelbrot set. The colors are based on how many iterations of the equation $z_{n+1} = z_{n}^{2} + C$ it takes to pass 10,000 for the complex value C.

It uses colors from the catpuccin-mocha theme.

![The Generated Image](https://github.com/Harrex/Python_Mathy_Image_Generators/blob/master/Assets/Mandelbrot.png)

## The Mandelbrot Set - Higher Powers
Changing the power in this equation causes multiple of the set, rotated evenly about the origin. This script (mandelbrot\_hexagon.py) uses a power of 7:
$z_{n+1} = z_{n}^{7} + C$

![The Generated Image](https://github.com/Harrex/Python_Mathy_Image_Generators/blob/master/Assets/mandelbrot-hexagon.png)
