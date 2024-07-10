# z_{n+1} = z_{n}^2 + C


from PIL import Image

colors = [
    (24, 24, 37),     #rgb(24, 24, 37)     #0
    (137, 180, 250),  #rgb(137, 180, 250)  #1
    (137, 220, 235),  #rgb(137, 220, 235)  #2
    (24, 24, 37),     #rgb(24, 24, 37)     #3
    (24, 24, 37),     #rgb(24, 24, 37)     #4
    (24, 24, 37),     #rgb(24, 24, 37)     #5
    (44, 44, 57),     #rgb(44, 44, 57)     #6
    (108, 112, 134),  #rgb(108, 112, 134)  #7
    (166, 173, 200),  #rgb(166, 173, 200)  #8
    (166, 173, 200),  #rgb(166, 173, 200)  #9
    (186, 193, 220),  #rgb(186, 193, 220)  #10
    (186, 193, 220),  #rgb(186, 193, 220)  #11
    (137, 180, 250),  #rgb(137, 180, 250)  #12
    (116, 199, 236),  #rgb(116, 199, 236)  #13
    (137, 220, 235),  #rgb(137, 220, 235)  #14
    (166, 227, 161),  #rgb(166, 227, 161)  #15
    (249, 226, 175),  #rgb(249, 226, 175)  #16
    (250, 179, 135),  #rgb(250, 179, 135)  #17
    (245, 194, 231),  #rgb(245, 194, 231)  #18
    (243, 139, 168),  #rgb(243, 139, 168)  #19
    (203, 166, 247),  #rgb(203, 166, 247)  #20
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
    for i in range(20):
        z = z**2 + c
        if abs(z) > 10000:
            return i

    return 0


def main():
    X_DIMENSION = 3440
    Y_DIMENSION = 1504

    re_min, re_max = -5, 3.7

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


if __name__ == "__main__":
    main()
