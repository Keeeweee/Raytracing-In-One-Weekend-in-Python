from pyrr import Vector3 as vec3
from random import random


def randomInUnitSphere():
    while True:
        p = 2.0 * vec3([random(), random(), random()]) - vec3([1.0, 1.0, 1.0])
        if p.squared_length >= 1.0:
            return p