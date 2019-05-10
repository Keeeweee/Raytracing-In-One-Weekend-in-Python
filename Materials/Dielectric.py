from Materials.Material import *
from random import random

class Dielectric(Material):
    def __init__(self, ri: float):
        self.ref_idx = ri

    def scatter(self, ray: Ray, rec: HitRecord, attenuation: vec3, scattered: Ray) -> bool:
        reflected = self.reflect(ray.direction, rec.normal)
        attenuation.x = 1.0
        attenuation.y = 1.0
        attenuation.x = 1.0
        refracted = vec3([0.0, 0.0, 0.0])
        if ray.direction.dot(rec.normal) > 0:
            outward_normal = -rec.normal
            ni_over_nt = self.ref_idx
            cosine = self.ref_idx * ray.direction.dot(rec.normal) / ray.direction.length
        else:
            outward_normal = rec.normal
            ni_over_nt = 1.0 / self.ref_idx
            cosine = -ray.direction.dot(rec.normal) / ray.direction.length

        if self.refract(ray.direction, outward_normal, ni_over_nt, refracted):
            reflect_prob = self.schlick(cosine, self.ref_idx)
        else:
            reflect_prob = 1.0

        if random() < reflect_prob:
            scattered.copyFrom(Ray(rec.p, reflected))
        else:
            scattered.copyFrom(Ray(rec.p, refracted))

        return True
