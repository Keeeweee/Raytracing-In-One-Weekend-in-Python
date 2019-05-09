from Shapes.Shape import HitRecord, Shape
from Shapes.ShapeList import ShapeList
from Shapes.Sphere import Sphere
from pyrr import Vector3 as vec3
from PpmDrawer import PpmDrawer
from Ray import Ray
from Camera import Camera
from random import random
from Utils import randomInUnitSphere
import multiprocessing as mp


def scaleColor(color) -> int:
    return int(255.99 * color)


def blueBlend(ray: Ray) -> vec3:
    t = 0.5 * (ray.direction.y + 1.0)
    return (1.0 - t) * vec3([1.0, 1.0, 1.0]) + t * vec3([0.5, 0.7, 1.0])


def colorRay(ray: Ray, world: Shape) -> vec3:
    rec = [HitRecord()]
    if world.hit(ray, 0, 10000, rec):
        target = rec[0].p + rec[0].normal + randomInUnitSphere()
        return 0.5 * colorRay(Ray(rec[0].p, target - rec[0].p), world)

    return blueBlend(ray)


nx = 200
ny = 100
ns = 100
camera = Camera()

points = []

world = ShapeList()
world.append(Sphere(vec3([0.0, 0.0, -1.0]), 0.5))
world.append(Sphere(vec3([0.0, -100.5, -1.0]), 100))
count = 0
last = 0.0

def run(j: int):
    global count
    global last
    for i in range(nx):

        new = int((count * 100) / (nx * ny))
        if last != new:
            print("Progress: " + str(last) + "% with j= " + str(j), end="\n")
            last = new
        count += 1

        col = vec3([0.0, 0.0, 0.0])
        for s in range(ns):
            u = (i + random()) / nx
            v = (j + random()) / ny

            ray = camera.getRay(u, v)
            col += colorRay(ray, world)

        col = col / ns
        ir = scaleColor(col[0])
        ig = scaleColor(col[1])
        ib = scaleColor(col[2])

        points.append([ir, ig, ib])


def paintWorld():
    ppmDrawer = PpmDrawer("08_parallel.ppm", nx, ny)

    N = mp.cpu_count()
    with mp.Pool(processes= int(N)) as p:
        p.map(run, [j for j in range(ny, 0, -1)])

    ppmDrawer.writePpm(points)


def main():
    paintWorld()


if __name__ == "__main__":
    main()
