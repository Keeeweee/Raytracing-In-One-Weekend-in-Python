from pyrr import Vector3 as vec3
from PpmDrawer import PpmDrawer


def scaleColor(color) -> int:
    return int(255.99 * color)


def paintColorGradient():
    nx = 200
    ny = 100
    ppmDrawer = PpmDrawer("color_gradient.ppm", nx, ny)

    points = []

    for j in range(ny, 0, -1):
        for i in range (nx):
            r = i / nx
            g = j / ny
            b = 0.2
            ir = scaleColor(r)
            ig = scaleColor(g)
            ib = scaleColor(b)
            points.append([ir, ig, ib])

    ppmDrawer.writePpm(points)


def main():
    nx = 200
    ny = 100
    ppmDrawer = PpmDrawer("color_gradient.ppm", nx, ny)

    points = []

    for j in range(ny, 0, -1):
        for i in range (nx):
            r = i / nx
            g = j / ny
            b = 0.2
            ir = scaleColor(r)
            ig = scaleColor(g)
            ib = scaleColor(b)
            points.append([ir, ig, ib])

    ppmDrawer.writePpm(points)


if __name__ == "__main__":
    main()
