from Shapes.Shape import *


class ShapeList(Shape):
    def __init__(self, shapeList: List[Shape] = None):
        if shapeList is None:
            shapeList = []
        self.shapeList = shapeList

    def append(self, shape: Shape):
        self.shapeList.append(shape)

    def hit(self, ray: Ray, t_min: float, t_max: float, rec: List[HitRecord]) -> bool:
        hitAnything = False
        tempRec = [HitRecord()]
        closestSoFar = t_max
        for shape in self.shapeList:
            if shape.hit(ray, t_min, closestSoFar, tempRec):
                hitAnything = True
                closestSoFar = tempRec[0].t
                rec[0] = tempRec[0]

        return hitAnything
