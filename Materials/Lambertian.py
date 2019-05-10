from Materials.Material import *
from Utils import randomInUnitSphere


class Lambertian(Material):
    def __init__(self, albedo: vec3):
        self.albedo = albedo

    def scatter(self, ray: Ray, rec: HitRecord, attenuation: vec3, scattered: Ray) -> bool:
        target = rec.p + rec.normal + randomInUnitSphere()
        scattered.copyFrom(Ray(rec.p, target - rec.p))
        attenuation.x = self.albedo.x
        attenuation.y = self.albedo.y
        attenuation.z = self.albedo.z
        return True
