from abc import ABC, abstractmethod
from Ray import Ray
from typing import List
from Shapes.Shape import HitRecord
from pyrr import Vector3 as vec3


class Material(ABC):
    @abstractmethod
    def scatter(self, ray: Ray, rec: List[HitRecord], attenuation: vec3, scattered: Ray) -> bool:
        pass