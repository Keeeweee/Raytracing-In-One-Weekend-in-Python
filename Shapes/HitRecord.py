from pyrr import Vector3 as vec3


class HitRecord:
    def __init__(self, t: float = None, p: vec3 = None, normal: vec3 = None, material=None):
        self.t = t
        self.p = p
        self.normal = normal
        self.material = material

    def copyFrom(self, copy):
        self.t = copy.t
        self.p = copy.p
        self.normal = copy.normal
        self.material = copy.material