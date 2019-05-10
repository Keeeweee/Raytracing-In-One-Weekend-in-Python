from abc import ABC, abstractmethod
from Ray import Ray
from Shapes.HitRecord import HitRecord
from pyrr import Vector3 as vec3
from math import sqrt


class Material(ABC):
    @abstractmethod
    def scatter(self, ray: Ray, rec: HitRecord, attenuation: vec3, scattered: Ray) -> bool:
        pass

    @staticmethod
    def refract(v: vec3, n: vec3, ni_over_nt: float, refracted: vec3) -> bool:
        uv = v.normalized
        dt = uv.dot(n)
        discriminant = 1.0 - ni_over_nt**2 * (1.0 - dt**2)
        if discriminant > 0:
            new_refracted = ni_over_nt * (uv - n * dt) - n * sqrt(discriminant)
            refracted.x = new_refracted.x
            refracted.y = new_refracted.y
            refracted.z = new_refracted.z
            return True
        return False

    @staticmethod
    def reflect(v: vec3, n: vec3) -> vec3:
        return v - 2 * v.dot(n) * n

    @staticmethod
    def schlick(cosine: float, ref_idx: float):
        r0 = (1 - ref_idx) / (1 + ref_idx)
        r0 = r0**2
        return r0 + (1.0 - r0) * pow(1 - cosine, 5)
