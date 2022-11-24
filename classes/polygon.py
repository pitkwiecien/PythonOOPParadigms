import abc


class Polygon(abc.ABC):
    def __init__(self):
        self.dimensions = "2D"

    @property
    def dimensions(self):
        print("getting via getter")
        return self._dimensions

    @dimensions.setter
    def dimensions(self, value):
        print("changing via setter")
        self._dimensions = value

    @abc.abstractmethod
    def get_sides(self):
        pass

    def return_hello(self):
        return "hello"