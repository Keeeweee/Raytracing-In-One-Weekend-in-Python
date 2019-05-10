from Materials.Material import *
from Utils import randomInUnitSphere

class Metal(Material):
    def __init__(self, albedo: vec3, f: float):
        self.albedo = albedo
        self.fuzz = f if f < 1 else 1

    def reflect(self, v: vec3, n: vec3) -> vec3:
        return v - 2 * v.dot(n) * n

    def scatter(self, ray: Ray, rec: HitRecord, attenuation: vec3, scattered: Ray) -> bool:
        reflected = self.reflect(ray.direction, rec.normal)
        scattered.copyFrom(Ray(rec.p, reflected + self.fuzz * randomInUnitSphere()))
        attenuation.x = self.albedo.x
        attenuation.y = self.albedo.y
        attenuation.z = self.albedo.z
        return scattered.direction.dot(rec.normal) > 0
