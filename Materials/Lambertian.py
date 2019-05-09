from Materials.Material import Material
from Shapes.Shape import HitRecord
from Ray import Ray
from pyrr import Vector3 as vec3
from typing import List
from Utils import randomInUnitSphere

class Lambertian(Material):
    def __init__(self, albedo):
        self.albedo = albedo

    def scatter(self, ray: Ray, rec: List[HitRecord], attenuation: vec3, scattered: Ray) -> bool:
        target = rec[0].p + rec[0].normal + randomInUnitSphere()
        scattered = Ray(rec[0].p, target - rec[0].p)
        attenuation = self.albedo
        return True