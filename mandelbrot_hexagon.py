# z_{n+1} = z_{n}^7 + C


from PIL import Image

colors = [
    (24, 24, 37),     #rgb(24, 24, 37)     #1
    (137, 180, 250),  #rgb(137, 180, 250)  #2
    (166, 173, 200),  #rgb(166, 173, 200)  #9
    (108, 112, 134),  #rgb(108, 112, 134)  #8
    (24, 24, 37),     #rgb(24, 24, 37)     #5
    (24, 24, 37),     #rgb(24, 24, 37)     #6
    (44, 44, 57),     #rgb(44, 44, 57)     #7
    (108, 112, 134),  #rgb(108, 112, 134)  #8
    (166, 173, 200),  #rgb(166, 173, 200)  #9
    (166, 173, 200),  #rgb(166, 173, 200)  #10
    (186, 193, 220),  #rgb(186, 193, 220)  #11
    (186, 193, 220),  #rgb(186, 193, 220)  #12
    (137, 180, 250),  #rgb(137, 180, 250)  #13
    (116, 199, 236),  #rgb(116, 199, 236)  #14
    (137, 220, 235),  #rgb(137, 220, 235)  #15
    (166, 227, 161),  #rgb(166, 227, 161)  #16
    (249, 226, 175),  #rgb(249, 226, 175)  #17
    (250, 179, 135),  #rgb(250, 179, 135)  #18
    (245, 194, 231),  #rgb(245, 194, 231)  #19
    (243, 139, 168),  #rgb(243, 139, 168)  #20
    (203, 166, 247),  #rgb(203, 166, 247)  #21
]

def linspace(min, max, density):
    step = (max - min) / density

    to_return = []

    i = min
    while i <= max:
        to_return.append(i)
        i += step

    return to_return


def complex_matrix(re_min, re_max, im_min, im_max, x_pixel_density, y_pixel_density):

    print("Generating Matrix...")
    res = linspace(re_min, re_max, x_pixel_density)
    ims = linspace(im_min, im_max, y_pixel_density)

    return res, ims


def is_crazy(c):
    z = 0
    i = 0
    while i < 20:
        z = z**7 + c
        i += 1
        if abs(z) > 10000:
            return i

    return 0


def main():
    X_DIMENSION = 3440
    Y_DIMENSION = 1504

    re_min, re_max = -5, 5

    im_range = (re_max - re_min) * (Y_DIMENSION / X_DIMENSION)
    im_min, im_max = -(im_range / 2), (im_range / 2)

    reals, imags = complex_matrix(
        re_min,
        re_max,
        im_min,
        im_max,
        x_pixel_density=X_DIMENSION,
        y_pixel_density=Y_DIMENSION,
    )

    image = Image.new("RGB", [X_DIMENSION, Y_DIMENSION])
    data = image.load()
    # reals = [number.real for number in matrix]
    # imags = [number.imag for number in matrix]
    print("Setting Image Data")
    for j in range(Y_DIMENSION):
        print(f"Row {j} out of {Y_DIMENSION}")
        for i in range(X_DIMENSION):
            data[i, j] = colors[is_crazy(complex(reals[i], imags[j]))]

    image.show()
    image.save("Assets/mandelbrot_hexagon.png")


if __name__ == "__main__":
    main()
