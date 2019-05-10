from abc import ABC, abstractmethod
from Ray import Ray
from Shapes.HitRecord import HitRecord
from Materials.Material import Material


class Shape(ABC):
    @abstractmethod
    def hit(self, ray: Ray, t_min: float, t_max: float, rec: HitRecord) -> bool:
        pass
