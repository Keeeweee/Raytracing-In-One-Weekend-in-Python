from pyrr import Vector3 as vec3
from Ray import Ray
from math import pi, tan


class Camera:
    def __init__(self, vFov: float, aspect: float):
        theta = vFov * pi / 180
        half_height = tan(theta / 2)
        half_width = aspect * half_height

        self.lowerLeftCorner = vec3([-half_width, -half_height, -1.0])
        self.horizontal = vec3([2.0 * half_width, 0.0, 0.0])
        self.vertical = vec3([0.0, 2.0 * half_height, 0.0])
        self.origin = vec3([0.0, 0.0, 0.0])

    def getRay(self, u: float, v: float) -> Ray:
        return Ray(self.origin, self.lowerLeftCorner + u * self.horizontal + v * self.vertical - self.origin)
