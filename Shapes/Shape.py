from abc import ABC, abstractmethod
from Ray import Ray
from pyrr import Vector3 as vec3
from typing import List


class HitRecord:
    def __init__(self, t: float = None, p: vec3 = None, normal: vec3 = None):
        self.t = t
        self.p = p
        self.normal = normal


class Shape(ABC):
    @abstractmethod
    def hit(self, ray: Ray, t_min: float, t_max: float, rec: List[HitRecord]) -> bool:
        pass
