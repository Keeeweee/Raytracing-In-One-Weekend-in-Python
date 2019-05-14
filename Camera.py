from pyrr import Vector3 as vec3
from Ray import Ray
from math import pi, tan


class Camera:
    def __init__(self, lookFrom: vec3, lookAt: vec3, vUp: vec3, vFov: float, aspect: float):
        theta = vFov * pi / 180
        half_height = tan(theta / 2)
        half_width = aspect * half_height

        self.origin = lookFrom

        w = (lookFrom - lookAt).normalized
        u = vUp.cross(w).normalized
        v = w.cross(u)

        self.lowerLeftCorner = self.origin - half_width * u - half_height * v - w
        self.horizontal = 2.0 * half_width * u
        self.vertical = 2.0 * half_height * v

    def getRay(self, u: float, v: float) -> Ray:
        return Ray(self.origin, self.lowerLeftCorner + u * self.horizontal + v * self.vertical - self.origin)
