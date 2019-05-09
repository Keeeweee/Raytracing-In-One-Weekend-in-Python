
class PpmDrawer:
    def __init__(self, fileName: str, nX: int, nY: int, gamma: float = 2.0):
        self._filename = fileName
        self._nX = nX
        self._nY = nY
        self.gamma = gamma

    def writePpm(self, points):
        with open(self._filename, "w+") as file:
            file.write("P3\n")
            file.write("{0} {1}\n".format(self._nX, self._nY))
            file.write("255\n")
            for point in points:
                file.write(" ".join([str(pow(x, 1.0 / self.gamma)) for x in point]) + "\n")
