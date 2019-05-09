from pyrr import Vector3 as vec3
from Ray import Ray


class Camera:
    def __init__(self):
        self.lowerLeftCorner = vec3([-2.0, -1.0, -1.0])
        self.horizontal = vec3([4.0, 0.0, 0.0])
        self.vertical = vec3([0.0, 2.0, 0.0])
        self.origin = vec3([0.0, 0.0, 0.0])

    def getRay(self, u: float, v: float) -> Ray:
        return Ray(self.origin, self.lowerLeftCorner + u * self.horizontal + v * self.vertical - self.origin)
