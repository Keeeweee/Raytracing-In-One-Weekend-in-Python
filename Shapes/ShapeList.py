from Shapes.Shape import *
from typing import List


class ShapeList(Shape):
    def __init__(self, shapeList: List[Shape] = None):
        if shapeList is None:
            shapeList = []
        self.shapeList = shapeList

    def append(self, shape: Shape):
        self.shapeList.append(shape)

    def hit(self, ray: Ray, t_min: float, t_max: float, rec: HitRecord) -> bool:
        hitAnything = False
        tempRec = HitRecord()
        closestSoFar = t_max
        for shape in self.shapeList:
            if shape.hit(ray, t_min, closestSoFar, tempRec):
                hitAnything = True
                closestSoFar = tempRec.t
                rec.copyFrom(tempRec)

        return hitAnything
