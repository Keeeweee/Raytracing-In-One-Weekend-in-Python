from pyrr import vector3 as vec3


class Ray:
    def __init__(self, origin: vec3, direction: vec3):
        self._origin = origin
        self._direction = direction

    def origin(self) -> vec3:
        return self._origin

    def direction(self) -> vec3:
        return self._direction

    def point_at_parameter(self, t: float):
        return self.origin() + t * self.direction()
