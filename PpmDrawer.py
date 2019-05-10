from typing import List

class PpmDrawer:
    def __init__(self, fileName: str, nX: int, nY: int, gamma: float = 2.0):
        self._filename = fileName
        self._nX = nX
        self._nY = nY
        self.gamma = gamma

    def scaleColor(self, colors: List[float]) -> List[int]:
        return [int(255.99 * pow(color, 1.0 / self.gamma)) for color in colors]

    def writePpm(self, points):
        with open(self._filename, "w+") as file:
            file.write("P3\n")
            file.write("{0} {1}\n".format(self._nX, self._nY))
            file.write("255\n")
            for point in points:
                file.write(" ".join([str(x) for x in self.scaleColor(point)]) + "\n")
