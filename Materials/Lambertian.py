from Materials.Material import *
from Ray import Ray
from pyrr import Vector3 as vec3
from Utils import randomInUnitSphere


class Lambertian(Material):
    def __init__(self, albedo):
        self.albedo = albedo

    def scatter(self, ray: Ray, rec: HitRecord, attenuation: vec3, scattered: Ray) -> bool:
        target = rec.p + rec.normal + randomInUnitSphere()
        scattered.copyFrom(Ray(rec.p, target - rec.p))
        attenuation.x = self.albedo.x
        attenuation.y = self.albedo.y
        attenuation.z = self.albedo.z
        return True
