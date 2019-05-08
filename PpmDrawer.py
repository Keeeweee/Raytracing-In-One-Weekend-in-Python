
class PpmDrawer:
    def __init__(self, fileName: str, nX: int, nY: int):
        self._filename = fileName
        self._nX = nX
        self._nY = nY

    def writePpm(self, points):
        with open(self._filename, "w+") as file:
            file.write("P3\n")
            file.write("{0} {1}\n".format(self._nX, self._nY))
            file.write("255\n")
            for point in points:
                file.write(" ".join([str(x) for x in point]) + "\n")
