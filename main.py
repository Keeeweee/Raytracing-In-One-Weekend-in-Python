from Shapes.Shape import Shape
from Shapes.HitRecord import HitRecord
from Shapes.ShapeList import ShapeList
from Shapes.Sphere import Sphere
from Materials.Lambertian import Lambertian
from Materials.Metal import Metal
from Materials.Dielectric import Dielectric
from pyrr import Vector3 as vec3
from PpmDrawer import PpmDrawer
from Ray import Ray
from Camera import Camera
from random import random

MAXFLOAT = 10000
nx = 200
ny = 100
ns = 100


def blueBlend(ray: Ray) -> vec3:
    t = 0.5 * (ray.direction.y + 1.0)
    return (1.0 - t) * vec3([1.0, 1.0, 1.0]) + t * vec3([0.5, 0.7, 1.0])


def colorRay(ray: Ray, world: Shape, depth: int) -> vec3:
    rec = HitRecord()
    if world.hit(ray, 0.001, MAXFLOAT, rec):
        scattered = Ray(vec3([0.0, 0.0, 0.0]), vec3([0.0, 0.0, 0.0]))
        attenuation = vec3()
        if depth < 50 and rec.material.scatter(ray, rec, attenuation, scattered):
            return attenuation * colorRay(scattered, world, depth + 1)
        else:
            return vec3([0.0, 0.0, 0.0])

    return blueBlend(ray)


def paintWorld():
    ppmDrawer = PpmDrawer("test.ppm", nx, ny)

    camera = Camera()

    points = []

    world = ShapeList()
    world.append(Sphere(vec3([0.0, 0.0, -1.0]),
                        0.5,
                        Lambertian(vec3([0.8, 0.3, 0.3]))))
    world.append(Sphere(vec3([0.0, -100.5, -1.0]),
                        100,
                        Lambertian(vec3([0.8, 0.8, 0.0]))))
    world.append(Sphere(vec3([1.0, 0.0, -1.0]),
                        0.5,
                        Metal(vec3([0.8, 0.6, 0.2]), 0.3)))
    world.append(Sphere(vec3([-1.0, 0.0, -1.0]),
                        0.5,
                        Dielectric(1.5)))

    count = 0
    last = 0

    for j in range(ny, 0, -1):
        for i in range(nx):

            new = int((count * 100) / (nx * ny))
            if last != new:
                print("Progress: " + str(last) + "%", end="\n")
                last = new
            count += 1

            col = vec3([0.0, 0.0, 0.0])
            for s in range(ns):
                u = (i + random()) / nx
                v = (j + random()) / ny

                ray = camera.getRay(u, v)
                col += colorRay(ray, world, 0)

            col = col / ns

            points.append(col)

    ppmDrawer.writePpm(points)


def main():
    paintWorld()


if __name__ == "__main__":
    main()
