from pyrr import Vector3 as vec3
from PpmDrawer import PpmDrawer
from Ray import Ray


def scaleColor(color) -> int:
    return int(255.99 * color)


def blueBlend(ray: Ray) -> vec3:
    t = 0.5 * (ray.direction.y + 1.0)

    return (1.0 - t) * vec3([1.0, 1.0, 1.0]) + t * vec3([0.5, 0.7, 1.0])


def paintBlueGradient():
    nx = 200
    ny = 100
    ppmDrawer = PpmDrawer("blue_gradient.ppm", nx, ny)

    lower_left_corner = vec3([-2.0, -1.0, -1.0])
    horizontal = vec3([4.0, 0.0, 0.0])
    vertical = vec3([0.0, 2.0, 0.0])
    origin = vec3([0.0, 0.0, 0.0])

    points = []

    for j in range(ny, 0, -1):
        for i in range(nx):

            u = i / nx
            v = j / ny

            ray = Ray(origin, lower_left_corner + u*horizontal + v*vertical)
            col = blueBlend(ray)

            ir = scaleColor(col[0])
            ig = scaleColor(col[1])
            ib = scaleColor(col[2])

            points.append([ir, ig, ib])

    ppmDrawer.writePpm(points)


def paintColorGradient():
    nx = 200
    ny = 100
    ppmDrawer = PpmDrawer("color_gradient.ppm", nx, ny)

    points = []

    for j in range(ny, 0, -1):
        for i in range(nx):
            r = i / nx
            g = j / ny
            b = 0.2
            ir = scaleColor(r)
            ig = scaleColor(g)
            ib = scaleColor(b)
            points.append([ir, ig, ib])

    ppmDrawer.writePpm(points)


def paintSphere():
    nx = 200
    ny = 100
    ppmDrawer = PpmDrawer("red_sphere.ppm", nx, ny)

    lower_left_corner = vec3([-2.0, -1.0, -1.0])
    horizontal = vec3([4.0, 0.0, 0.0])
    vertical = vec3([0.0, 2.0, 0.0])
    origin = vec3([0.0, 0.0, 0.0])

    points = []

    for j in range(ny, 0, -1):
        for i in range(nx):

            u = i / nx
            v = j / ny

            ray = Ray(origin, lower_left_corner + u*horizontal + v*vertical)
            col = colorRay(ray)

            ir = scaleColor(col[0])
            ig = scaleColor(col[1])
            ib = scaleColor(col[2])

            points.append([ir, ig, ib])

    ppmDrawer.writePpm(points)


def hitSphere(center: vec3, radius: float, ray: Ray) -> bool:
    oc = ray.origin - center
    a = ray.direction.dot(ray.direction)
    b = 2.0 * (oc.dot(ray.direction))
    c = oc.dot(oc) - (radius**2)
    discriminant = (b**2) - (4 * a * c)

    return discriminant > 0


def colorRay(ray: Ray) -> vec3:
    if hitSphere(vec3([0, 0, -1]), 0.5, ray):
        return vec3([1, 0, 0])

    return blueBlend(ray)


def main():
    paintSphere()


if __name__ == "__main__":
    main()
