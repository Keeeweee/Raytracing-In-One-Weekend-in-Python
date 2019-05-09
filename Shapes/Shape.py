from abc import ABC, abstractmethod
from Ray import Ray
from pyrr import Vector3 as vec3
from typing import List
import Materials.Material as Material


class HitRecord:
    def __init__(self, t: float = None, p: vec3 = None, normal: vec3 = None, material: Material = None):
        self.t = t
        self.p = p
        self.normal = normal
        self.material = material


class Shape(ABC):
    @abstractmethod
    def hit(self, ray: Ray, t_min: float, t_max: float, rec: List[HitRecord]) -> bool:
        pass
