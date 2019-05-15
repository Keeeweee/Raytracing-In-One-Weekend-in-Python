from pyrr import vector3 as vec3


class Ray:
    def __init__(self, origin: vec3, direction: vec3):
        self._origin = origin
        self._direction = direction.normalized if direction.length > 0 else direction

    @property
    def origin(self) -> vec3:
        return self._origin

    @property
    def direction(self) -> vec3:
        return self._direction

    def pointAtParameter(self, t: float):
        return self.origin + t * self.direction

    def copyFrom(self, copy):
        self._origin = copy.origin
        self._direction = copy.direction.normalized if copy.direction.length > 0 else copy.direction
