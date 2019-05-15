from pyrr import Vector3 as vec3
from Ray import Ray
from math import pi, tan
from Utils import randomInUnitSphere


class Camera:
    def __init__(self, lookFrom: vec3, lookAt: vec3, vUp: vec3, vFov: float, aspect: float, aperture: float, focusDist: float):
        self.lensRadius = aperture / 2.0
        theta = vFov * pi / 180
        half_height = tan(theta / 2)
        half_width = aspect * half_height

        self.origin = lookFrom

        self.w = (lookFrom - lookAt).normalized
        self.u = vUp.cross(self.w).normalized
        self.v = self.w.cross(self.u)

        self.lowerLeftCorner = self.origin - focusDist * (half_width * self.u + half_height * self.v + self.w)
        self.horizontal = 2.0 * half_width * self.u * focusDist
        self.vertical = 2.0 * half_height * self.v * focusDist

    def getRay(self, s: float, t: float) -> Ray:
        rd = self.lensRadius * randomInUnitSphere()
        offset = self.u * rd.x + self.v * rd.y
        return Ray(self.origin + offset, self.lowerLeftCorner + s * self.horizontal + t * self.vertical - self.origin - offset)
